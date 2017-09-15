#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:12:31 2017

@author: alexanderwahl
"""

import random
import math

import numpy as np
import json
import gensim
#from scipy.sparse import csr_matrix
#from nltk.corpus import stopwords




class Data(object):
    
    """
    This class loads and preprocesses the data for the Clarity Medical query classifiers
    """
    def __init__(self, sentence_path="/Users/alexanderwahl/Documents/Insight/Project/cleaned_sentences.json",
                       label_path="/Users/alexanderwahl/Documents/Insight/Project/cleaned_labels.json",
                       term_locs_path="/Users/alexanderwahl/Documents/Insight/Project/term_locations.json",
                       term_freqs_path="/Users/alexanderwahl/Documents/Insight/Project/term_frequencies.json",
                       dev=.1,
                       test=.1):
        
        with open(sentence_path,"r") as f:
            self.sentences = json.load(f)
        self.corpus_len = len(self.sentences)
            
        with open(label_path,"r") as f:
            self.labels = np.array(json.load(f))
            
        with open(term_locs_path,"r") as f:
            self.term_locs = json.load(f)
            
        with open(term_freqs_path,"r") as f:
            self.term_freqs = json.load(f)
                
        if dev + test > .5:
            raise ValueError("dev and test sizes must sum to less than .5")
        else:
            self.dev = dev
            self.test = test
            self.training = 1 - self.dev - self.test
        
    def set_data_for_log_regr(self):
        
        """
        training:
        clerical: 1908 sentences
        clinical: 40853 sentences
        """
        
        self._set_sentence_embeddings()
        self._set_segmentation_inds()
        self._set_segmentations()
              
    def _set_sentence_embeddings(self):
        
        self.word2vec = gensim.models.KeyedVectors.load_word2vec_format('/Users/alexanderwahl/Documents/Insight/Project/GoogleNews-vectors-negative300.bin', binary=True)
        self.embeddings = []
        for i,s in enumerate(self.sentences):
            self.i = i
            print i
            self.s = s
            self.weighted_vecs = []
            for w in s:
                self.w = w
                self.curr_vec = self.word2vec.word_vec(self.w)
                self._set_tf_idf()
                self.weighted_vecs.append(self.curr_vec * self.tf_idf)
            self.embeddings.append(np.mean(self.weighted_vecs, axis=0))
        self.inputs = np.asarray(self.embeddings)
            
    def _set_tf_idf(self):
        
        self.tf = self.term_freqs[self.i][self.w]
        self.idf = math.log10(self.corpus_len) / self.term_locs[self.w]
        self.tf_idf = self.tf * self.idf
    
#    def _downsample(self):
#        
#        if self.num_clinical:
#            clin_indices = random.sample(range(len(self.clinical_data)), self.num_clinical)
#            self.clinical_data = self.clinical_data[clin_indices]
#        
#        if self.num_clerical:
#            cler_indices = random.sample(range(len(self.clerical_data)), self.num_clerical)
#            self.clerical_data = self.clerical_data[cler_indices]
#            
#    def _set_labels(self):
#        
#        self.all_utts = np.append(self.clinical_data, self.clerical_data)
#        self.all_labs = np.array(["clinical"]*len(self.clinical_data) + ["clerical"]*len(self.clerical_data))
#            
#    def _set_word_types(self):
#        
#        self.word_types = dict()
#        self.counter = 0
#        for utt_ind,utt in enumerate(self.all_utts):
#            for w in utt:
#                if w not in self.word_types:
#                    self.word_types[w] = self.counter
#                    self.counter += 1
#    
#    def _set_count_vectors(self):
#        
#        self.count_vectors = csr_matrix((len(self.all_utts),len(self.word_types)), dtype=np.int8).toarray()
#        for utt_ind,utt in enumerate(self.all_utts):
#            for w in utt:
#                self.count_vectors[utt_ind][self.word_types[w]] += 1
                
    def _set_segmentation_inds(self):
        
        self.rndmzd_inds = range(self.corpus_len)
        random.seed(10)
        random.shuffle(self.rndmzd_inds)
        self.training_inds = self.rndmzd_inds[:int(round(self.training*self.corpus_len))]
        self.dev_inds = self.rndmzd_inds[int(round(self.training*self.corpus_len)):int(round((self.training+self.dev)*self.corpus_len))]
        self.test_inds = self.rndmzd_inds[int(round((self.training+self.dev)*self.corpus_len)):]
    
    def _set_segmentations(self):
        
        self.training_x = self.inputs[self.training_inds, :]
        self.training_y = self.labels[self.training_inds]
        self.dev_x = self.inputs[self.dev_inds, :]
        self.dev_y = self.labels[self.dev_inds]
        self.test_x = self.inputs[self.test_inds, :]
        self.test_y = self.labels[self.test_inds]
            
    

            
        