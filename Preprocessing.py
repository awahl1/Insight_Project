#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:12:31 2017

@author: alexanderwahl
"""

import random
import os

import numpy as np
import pandas as pd
import json
import gensim
from nltk import word_tokenize

from Tests import (ensure_in_df_index,ensure_string_argument,ensure_boolean_argument,ensure_main_type,ensure_data_size)


class DataStoreManager(object):
    
    """
    Used for loading, editing, and saving the file "data_store_df.csv," which records the different sources
    of available data and relevant details about these sources. The file is loaded in as a Pandas df.
    """
    
    def __init__(self):
        
        self.data_store_df = pd.read_csv("data_store_df.csv", index_col="NAME", sep=",")
        
    def data_sources(self, NAME=None):
        
        """
        prints the data frame to the screen. 
        
        Params:
            NAME: Optionally specify a particular data source to print the details of.
        """
        
        if NAME:
            ensure_in_df_index(NAME, self.data_store_df, "Data Store")
            print(self.data_store_df.loc[NAME])
        else:
            print(self.data_store_df)
        
    def add_data_source(self, NAME=None, PATH=None, MAIN_TYPE=None, SUBTYPE=None, USE_UNIQUE=None, RANDOM=None):
        
        """
        Add a new row (data source). Make sure the file exists specified by PATH. Automatically calculates NUM_SENTENCES,
        UNIQUE_SENTENCES, AND SAMPLE_SIZE. SAMPLE_SIZE is set to UNIQUE_SENTENCES by default.
        
        Params:
            Must specify all of NAME, PATH, MAIN_TYPE, SUBTYPE, USE_UNIQUE, RANDOM (see description of spreadsheet in
            README for details on these columns)
        """
        
        ensure_string_argument(NAME, "NAME")
        ensure_string_argument(PATH, "PATH")
        ensure_main_type(MAIN_TYPE)
        ensure_string_argument(SUBTYPE, "SUBTYPE")
        ensure_boolean_argument(USE_UNIQUE, "USE_UNIQUE")
        ensure_boolean_argument(RANDOM, "RANDOM")

        with open(os.getcwd()+PATH, "r") as f:
            self.curr_data = json.load(f)
        NUM_SENTENCES = len(self.curr_data)
        UNIQUE_SENTENCES = len(set(self.curr_data))
        SAMPLE_SIZE = UNIQUE_SENTENCES
        
        self.new_row = pd.DataFrame({"PATH":PATH, "MAIN_TYPE":MAIN_TYPE, "SUBTYPE":SUBTYPE, "NUM_SENTENCES":NUM_SENTENCES,
                      "UNIQUE_SENTENCES":UNIQUE_SENTENCES, "USE_UNIQUE":USE_UNIQUE, "SAMPLE_SIZE":SAMPLE_SIZE, "RANDOM":RANDOM}, index=[NAME])
    
        self.data_store_df = self.data_store_df.append(self.new_row)
        
    def save_data_sources(self, path="data_store_df.csv"):
        
        """
        save the data frame.
        
        Params:
            path: the path of where to save the data_store_df.csv file
        """
        
        self.data_store_df.to_csv(path, sep=",", index_label="NAME")
        
    def remove_data_source(self, NAME=None):
        
        """
        remove a row (data source)
        
        Params:
            NAME: the name of the data source to delete
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        self.data_store_df = self.data_store_df.drop(NAME)
        
    def change_sample_size(self, NAME=None, SAMPLE_SIZE=None):
        
        """
        change the number of sentences from a data source to use.
        
        Params:
            NAME: the name of the data source whose sample size is to be changed
            SAMPLE_SIZE: the new sample size
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        self.data_store_df["SAMPLE_SIZE"].loc[NAME] = SAMPLE_SIZE
        
    def change_path(self, NAME=None, PATH=None):
        
        """
        change the location of a data source
        
        Params:
            NAME: the name of the data source whose path is to be changed
            PATH: the new file path
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        ensure_string_argument(PATH, "PATH")
        self.data_store_df["PATH"].loc[NAME] = PATH
        
    def toggle_use_unique(self, NAME=None):
        
        """
        switch whether to use only unique sentences from data source, or allow repetitions.
        
        Params:
            NAME: the name of the data source whose USE_UNIQUE value is to be toggled
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        self.data_store_df["USE_UNIQUE"].loc[NAME] = not self.data_store_df["USE_UNIQUE"].loc[NAME]
        
    def toggle_random(self, NAME=None):
        
        """
        switch whether to randomly select the sample sentences from a data source, or take the sample starting
        from sentence index 0 until sentence index = sample size.
        
        Params:
            NAME: the name of the data set whos RANDOM value is to be toggled
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        self.data_store_df["RANDOM"].loc[NAME] = not self.data_store_df["RANDOM"].loc[NAME]

    def load_data(self):
        
        """
        load all the data files corresponding to the different data sources. To prevent a file from being loaded,
        set its sample size to 0. Note that NUM_SENTENCES and UNIQUE_SENTENCES cells will be automatically
        updated. If USE_UNIQUE is true, the sample sentences will be sampled from the unique set of all sentences.
        If the SAMPLE_SIZE is greater than the number of available sentences, sentences will be repeated in the sample
        until the SAMPLE_SIZE is surpassed, even if USE_UNIQUE is true.
        """
        
        self.all_data = {}
        for index,row in self.data_store_df.iterrows():
            self.name = index
            self.row = row
            if self.row["SAMPLE_SIZE"] > 0:
                with open(os.getcwd()+self.row["PATH"],"r") as f:
                    self.current_data = json.load(f)
                random.shuffle(self.current_data)
                self._update_cells()
                self._align_data_to_sample_size()
                self.all_data[self.name] = self.current_data
                setattr(self, self.name, self.current_data)
    
    def _update_cells(self):
        
        self.data_store_df.loc[self.name,"NUM_SENTENCES"] = len(self.current_data)
        self.data_store_df.loc[self.name,"UNIQUE_SENTENCES"] = len(set(self.current_data))
        
    def _align_data_to_sample_size(self):
        
        if self.row["USE_UNIQUE"]==True:
            
            if self.row["SAMPLE_SIZE"] > self.row["UNIQUE_SENTENCES"]:
                self.current_data = self._augment_data(list(set(self.current_data)))
            elif self.row["SAMPLE_SIZE"] < self.row["UNIQUE_SENTENCES"]:
                self.current_data = self._trim_data(list(set(self.current_data)))
            else:
                self.current_data = list(set(self.current_data))
                
        else:
            
            if self.row["SAMPLE_SIZE"] > self.row["NUM_SENTENCES"]:
                self.current_data = self._augment_data(self.current_data)
            elif self.row["SAMPLE_SIZE"] < self.row["NUM_SENTENCES"]:
                self.current_data = self._trim_data(self.current_data)
                
                
    def _augment_data(self, data):
        
        self.augmented_data = []
        while len(self.augmented_data) < self.row["SAMPLE_SIZE"]:
            self.augmented_data.extend(data)
        return self.augmented_data[0:self.row["SAMPLE_SIZE"]]
        
    def _trim_data(self, data):
        
        if self.row["RANDOM"]==True:
            return random.sample(data, self.row["SAMPLE_SIZE"])
        else:
            return data[0:self.row["SAMPLE_SIZE"]]
            
    def __iter__(self):
        
        for name,row in self.data_store_df.iterrows():
            yield name,row["MAIN_TYPE"]
            
    def get_data(self, NAME=None):
        
        """
        return the details of one data source.
        """
        
        ensure_in_df_index(NAME, self.data_store_df, "Data Store")
        return self.all_data[NAME]
                
        




                

class DataGrouper(object):
    
    def __init__(self, clinical=None, clinicalnames=None, clerical=None, clericalnames=None,
                 other=None, othernames=None):
        
        if clinical:
            self.clinical = clinical
            self.clinicalnames = [clinicalnames]*len(clinical)
        else:
            self.clinical = []
            self.clinicalnames = []
        if clerical:
            self.clerical = clerical
            self.clericalnames = [clericalnames]*len(clerical)
        else:
            self.clerical = []
            self.clericalnames = []
        if other:
            self.other = other
            self.othernames = [othernames]*len(other)
        else:
            self.other = []
            self.othernames = []
        
    def add_clinical(self, data, name):
        
        self.clinical.extend(data)
        self.clinicalnames.extend([name]*len(data))
        
    def add_clerical(self, data, name):
        
        self.clerical.extend(data)
        self.clericalnames.extend([name]*len(data))
        
    def add_other(self, data, name):
        
        self.other.extend(data)
        self.othernames.extend([name]*len(data))


class DataPreprocessor(object):
    
    """
    This class preprocesses the data after it has been loaded by DataStoreManager and
    grouped into clinical, clerical, and other lists by DataGrouper.
    """
    def __init__(self, data_grouper, test=.2):
        
        self.clinical = np.array(data_grouper.clinical)
        self.clinicalnames = np.array(data_grouper.clinicalnames)
        self.clerical = np.array(data_grouper.clerical)
        self.clericalnames = np.array(data_grouper.clericalnames)
        self.other = np.array(data_grouper.other)
        self.othernames = np.array(data_grouper.othernames)
        ensure_data_size(self.clinical, self.clerical, self.other)

        if test > .5:
            raise ValueError("test size must be less than .5")
        else:
            self.test = test
            self.training = 1 - self.test
            
    def process_for_training(self):
        
        self.set_word2vec()
        self.tokenize()
        self.set_sentence_embeddings()
        self.set_toplevel_segmentations()
        self.set_labels()
        self.set_segmentations_clerical_subtype()
            
    def downsample_group(self, group="clinical", newsize=None):
        
        if group=="clinical":
            newindices_clinical = random.sample(range(self.get_size("clinical")), newsize)
            self.clinical = self.clinical[newindices_clinical]
            self.clinicalnames = self.clinicalnames[newindices_clinical]
        elif group=="clerical":
            newindices_clerical = random.sample(range(self.get_size("clerical")), newsize)
            self.clerical = self.clerical[newindices_clerical]
            self.clericalnames = self.clericalnames[newindices_clerical]
        else:
            newindices_other = random.sample(range(self.get_size("other")), newsize)
            self.other = self.other[newindices_other]
            self.other = self.othernames[newindices_other]            
            
            
    def get_size(self, group="clinical"):
        
        if group=="clinical":
            return len(self.clinical)
        if group=="clerical":
            return len(self.clerical)
        if group=="other":
            return len(self.other)
        
    def set_word2vec(self, model=None):
        
        if model:
            self.word2vec = model
        else:
            self.word2vec = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
        
    def tokenize(self):
        
        self.clinical,self.clinicalnames,self.clinicalmissing = self._tokenize_group(self.clinical,self.clinicalnames)
        self.clerical,self.clericalnames,self.clericalmissing = self._tokenize_group(self.clerical,self.clericalnames)
        self.other,self.othernames,self.othermissing = self._tokenize_group(self.other,self.othernames)
        
    def _tokenize_group(self, group_sentences, group_names):
        
        self.group_sentences = group_sentences
        self.group_names = group_names
        self.cleaned_sentences = []
        self.cleaned_names = []
        self.missing_words = set()
        for index,sentence in enumerate(self.group_sentences):
            self.curr_tokenized_sentence = []
            for word in word_tokenize(sentence):
                if word in self.word2vec:
                    self.curr_tokenized_sentence.append(word)
                else:
                    self.missing_words.add(word)
            if self.curr_tokenized_sentence:
                self.cleaned_sentences.append(self.curr_tokenized_sentence)
                self.cleaned_names.append(self.group_names[index])
        return self.cleaned_sentences,self.cleaned_names,self.missing_words
    
    def set_sentence_embeddings(self):
        
        self.clinical_inputs = self._set_sentence_embeddings_for_group(self.clinical)
        self.clerical_inputs = self._set_sentence_embeddings_for_group(self.clerical)
        self.other_inputs = self._set_sentence_embeddings_for_group(self.other)
        
    def _set_sentence_embeddings_for_group(self, group_sentences):
        
        self.group_sentences = group_sentences
        self.sentence_vectors = []
        for sentence in self.group_sentences:
            self.curr_word_vectors = [self.word2vec.word_vec(w) for w in sentence]
            self.sentence_vectors.append(np.mean(self.curr_word_vectors, axis=0))
        self.inputs = np.asarray(self.sentence_vectors)   
        return self.inputs
        
    def set_toplevel_segmentations(self):
        
        self.clinical_segmentations = self._set_segmentation_indices_for_dataset(self.clinical)
        self.clerical_segmentations = self._set_segmentation_indices_for_dataset(self.clerical)
        self.other_segmentations = self._set_segmentation_indices_for_dataset(self.other)

    def _set_segmentation_indices_for_dataset(self, dataset):
        
        self.dataset = dataset
        self.len_dataset = len(dataset)
        self.segmentation_column = np.zeros(self.len_dataset, dtype=str)
        self.rndmzd_inds = range(len(self.dataset))
        random.seed(10)
        random.shuffle(self.rndmzd_inds)
        
        training_inds = self.rndmzd_inds[:int(round(self.training*self.len_dataset))]
        self.segmentation_column[training_inds] = "R"
        
        test_inds = self.rndmzd_inds[int(round(self.training*self.len_dataset)):]
        self.segmentation_column[test_inds] = "T"
        
        return self.segmentation_column
    
    def set_labels(self):
        
        self.all_sentences = np.concatenate((self.clinical,self.clerical,self.other))
        self.all_inputs = np.concatenate((self.clinical_inputs, self.clerical_inputs, self.other_inputs), axis=0)
        self.all_labels = np.array(["clinical"]*len(self.clinical) + ["clerical"]*len(self.clerical) + ["other"]*len(self.other))
        self.all_names = np.concatenate((self.clinicalnames,self.clericalnames,self.othernames))
        self.all_segmentations = np.concatenate((self.clinical_segmentations,self.clerical_segmentations,self.other_segmentations))
        self.all_info = pd.DataFrame({"Sentences":self.all_sentences, "Labels":self.all_labels,
                                      "Names":self.all_names, "Segmentations":self.all_segmentations})
        
        self.corpus_len = len(self.all_sentences)
        
    def set_segmentations_clerical_subtype(self):
        
        self.clerical_info = self.all_info.iloc[np.where(self.all_info["Labels"]=="clerical")[0]]
        self.clerical_inputs = self.all_inputs[np.where(self.all_info["Labels"]=="clerical")[0]]
        self.clerical_names_set = set(self.clerical_info["Names"])
        self.clerical_subtype_segmentations = np.zeros(len(self.clerical_info), dtype=str)
        for name in self.clerical_names_set:
            
            self.current_indices = np.where(self.clerical_info["Names"]==name)[0]
            self.len_current_indices = len(self.current_indices)
            random.shuffle(self.current_indices)
            
            training_inds = self.current_indices[:int(round(self.training*self.len_current_indices))]
            self.clerical_subtype_segmentations[training_inds] = "R"
            
            test_inds = self.current_indices[int(round(self.training*self.len_current_indices)):]
            self.clerical_subtype_segmentations[test_inds] = "T"
            
        self.clerical_info.loc[self.clerical_info.index]["Segmentations"] = self.clerical_subtype_segmentations
        

        

    

            
        