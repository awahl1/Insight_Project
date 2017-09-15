#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:25:53 2017

@author: alexanderwahl
"""

import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import FreqDist
import gensim
from bs4 import BeautifulSoup
import urllib
import pandas as pd
import re
import os
import json
from collections import Counter
from collections import defaultdict




#############Processing html from wiki
clerical_wiki_urls = pd.read_csv('/Users/alexanderwahl/Documents/Insight/Project/clerical_wiki_urls.csv', header=0)

def scrape_wiki_pages(urls=clerical_wiki_urls):
    for i,row in urls.iterrows():
        curr_url = row["URLs"]
        name = re.sub("^.*/wiki/", "", curr_url)
        fn = name + ".txt"
        r = urllib.urlopen(curr_url)
        soup = BeautifulSoup(r)
        try:
            with open(fn, "w") as f:
                f.write(soup.get_text().encode('utf-8'))
        except:
            print curr_url
        
        
        

medscape_dermatology_urls = pd.read_csv('/Users/alexanderwahl/Documents/Insight/Project/medscape_dermatology_urls.csv')

def scrape_medscape_pages(urls=medscape_dermatology_urls):
    for i,row in urls.iterrows():
        curr_txt = row["Data"]
        if curr_txt.startswith("<li>"):
            deprefixed = re.sub("^.*href=\"", "", curr_txt)
            curr_url = "http://emedicine.medscape.com" + re.sub("\">.*$", "", deprefixed)
            desuffixed = re.sub("<.*$","",deprefixed)
            curr_name = re.sub("^.*>","",desuffixed)
            fn = re.sub(" ", "_", curr_name)
            r = urllib.urlopen(curr_url)
            soup = BeautifulSoup(r)
            raw_text = "\n".join([x.text for x in soup.findAll('p')])
            try:
                with open(fn, "w") as f:
                    f.write(raw_text.encode('utf-8'))
            except:
                print curr_url
        
        
        
        

class Cleanup(object):
    
    def __init__(self):
        
        #Load in word2vec
        self.w2v = gensim.models.KeyedVectors.load_word2vec_format('/Users/alexanderwahl/Documents/Insight/Project/GoogleNews-vectors-negative300.bin', binary=True)


    ####################Dataset-specific scripts
    
    def clean_wiki_data(self, filepath='/Users/alexanderwahl/Documents/Insight/Project/wiki_articles/'):

        self.wiki_data = self.load_data(filepath)
        self.fdist_wiki = self.get_sentence_freqs(self.wiki_data)
        self.wiki_data_clean1 = self.exclude_suspiciously_frequent(self.wiki_data, self.fdist_wiki, max_threshold=9)
        self.wiki_data_clean2 = self.tokenize(self.wiki_data_clean1)
        self.wiki_data_clean3,self.wiki_missing_words = self.excl_wrds_not_in_word2vec(self.wiki_data_clean2)
        self.wiki_data_clean4,self.wiki_short_sent_count = self.excl_short_sentences(self.wiki_data_clean3, min_threshold=3)
        self.wiki_word_count = self.get_word_count(self.wiki_data_clean4)
        
    def clean_medscape_data(self, filepath='/Users/alexanderwahl/Documents/Insight/Project/medscape/'):
        
        self.medscape_data = self.load_data(filepath)
        self.fdist_medscape = self.get_sentence_freqs(self.medscape_data)
        self.medscape_data_clean1 = self.exclude_suspiciously_frequent(self.medscape_data, self.fdist_medscape, max_threshold=1)
        self.medscape_data_clean2 = self.tokenize(self.medscape_data_clean1)
        self.medscape_data_clean3,self.medscape_missing_words = self.excl_wrds_not_in_word2vec(self.medscape_data_clean2)
        self.medscape_data_clean4,self.medscape_short_sent_count = self.excl_short_sentences(self.medscape_data_clean3, min_threshold=3)
        self.medscape_word_count = self.get_word_count(self.medscape_data_clean4)
        
        
    ##################################Individual methods
        
    def load_data(self, filepath=None):
        data = []
        for fn in os.listdir(filepath):
            with open(filepath+fn,"r") as f:
                data.extend(f.read().decode('utf-8').splitlines())
        return data
        
    def get_sentence_freqs(self, data):
        return FreqDist(data)
    
    def exclude_suspiciously_frequent(self, data, fdist, max_threshold=None):
        return [sentence for sentence in data if fdist[sentence] <= max_threshold]
    
    def tokenize(self, data):
        cleaned_data=[]
        for sentence in data:
            if "-" in sentence:
                cleaned_data.append(word_tokenize(re.sub("-", " ", sentence)))
            else:
                cleaned_data.append(word_tokenize(sentence))
        return cleaned_data

    def excl_wrds_not_in_word2vec(self, data):
        cleaned_data = []
        missing_words = set()
        for sentence in data:
            cleaned_sentence = []
            for word in sentence:
                word_utf = word.encode('utf-8')
                if word_utf in self.w2v:
                    cleaned_sentence.append(word_utf)
                else:
                    missing_words.add(word_utf)
            cleaned_data.append(cleaned_sentence)
        return cleaned_data,missing_words
    
    def excl_short_sentences(self, data, min_threshold=None):
        short_sentence_counter = 0
        cleaned_data = []
        for sentence in data:
            if len(sentence) >= min_threshold:
                cleaned_data.append(sentence)
            else:
                short_sentence_counter += 1
        return cleaned_data,short_sentence_counter
    
    def get_word_count(self, data):
        counter = 0
        for sentence in data:
            counter += len(sentence)
        return counter



####Consolidate data into single lists
    
with open("wikipedia_data_cleaned.json","r") as f:
    cleaned_wiki_final = json.load(f)
    
with open("medscape_data_cleaned.json","r") as f:
    cleaned_medscape_final = json.load(f)



class Dataset_Combiner(object):
    
    def __init__(self, clinical_data=None, clerical_data=None):
        
        self.sentences = clerical_data + clinical_data
        self.labels = [1]*len(clerical_data) + [0]*len(clinical_data)

    def save_combined(self, sentence_file_name="cleaned_sentences.json", label_file_name="cleaned_labels.json"):
        
        with open(sentence_file_name,"w") as f:
            json.dump(self.sentences,f)
            
        with open(label_file_name,"w") as f:
            json.dump(self.labels,f)
    
    def set_structures_for_tf_idf(self):
        
        self.term_freqs = []
        self.term_locs = defaultdict(set)
        for index,sentence in enumerate(self.sentences):
            curr_counter = Counter()
            for word in sentence:
                curr_counter[word] += 1
                self.term_locs[word].add(index)
            self.term_freqs.append(curr_counter)
    
        self.term_locs_cleaned = {w:len(locs) for w,locs in self.term_locs.iteritems()}

    def save_structures_for_tf_idf(self, term_freqs_file="term_frequencies.json", term_locs_file="term_locations_w_cler.json"):
        
        with open(term_freqs_file,"w") as f:
            json.dump(self.term_freqs,f)
        
        with open(term_locs_file,"w") as f:
            json.dump(self.term_locs_cleaned,f)
    
    
    
    









    
    
    