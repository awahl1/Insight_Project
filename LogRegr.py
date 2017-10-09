#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:21:49 2017

@author: alexanderwahl
"""
import re
import random
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from nltk import word_tokenize
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from lime.lime_text import LimeTextExplainer




class Model(object):
    
    def set_data(self, data_instance):
        
        self.data = data_instance
        self.all_info = data_instance.all_info
        self.all_inputs = data_instance.all_inputs
        
        self.clerical_info = data_instance.clerical_info
        self.clerical_inputs = data_instance.clerical_inputs
        
    def toplevel_logistic_regr(self, C=1.0, include_other=True):
        
        if include_other:
            self.current_info = self.all_info
            self.current_inputs = self.all_inputs
        else:
            self.current_info = self.all_info.iloc[np.where(self.all_info["Labels"]!="other")[0]]
            self.current_inputs = self.all_inputs[np.where(self.all_info["Labels"]!="other")[0]]
        
        self.toplevel_training_x,self.toplevel_training_y,self.toplevel_training_sentences,self.toplevel_test_x,self.toplevel_test_y,self.toplevel_test_sentences= self.set_training_test_sets(self.current_info, 
                                                                                                                                                                  self.current_inputs,
                                                                                                                                                                  "Labels")
        self.model_main = LogisticRegression(C=C)
        self.model_main.fit(self.toplevel_training_x, self.toplevel_training_y)
        
    def set_training_test_sets(self, info_df, inputs, label_col):
        
        self.training_indices = np.where(info_df["Segmentations"]=="R")[0]
        self.test_indices = np.where(info_df["Segmentations"]=="T")[0]
        
        self.training_x = inputs[self.training_indices]
        self.training_y = info_df[label_col].iloc[self.training_indices]
        self.training_sents = info_df["Sentences"].iloc[self.training_indices]

        self.test_x = inputs[self.test_indices]
        self.test_y = info_df[label_col].iloc[self.test_indices]
        self.test_sents = info_df["Sentences"].iloc[self.test_indices]
        
        return self.training_x,self.training_y,self.training_sents,self.test_x,self.test_y,self.test_sents
    
    def set_accuracy(self, test_x, test_y, curr_model):
        
        self.accuracy = curr_model.score(test_x, test_y)
        
    def clerical_logistic_regr(self, C=1.0):
        
        self.cler_training_x,self.cler_training_y,self.cler_training_sentences,self.cler_test_x,self.cler_test_y,self.cler_test_sentences = self.set_training_test_sets(self.clerical_info,
                                                                                                                                              self.clerical_inputs,
                                                                                                                                              "Names")
        self.model_cler = LogisticRegression(C=C)
        self.model_cler.fit(self.cler_training_x, self.cler_training_y)

    
    def set_PCA(self, test_data, test_labels, savepath="PCA_demo.csv", plot=True):
        
        self.pca = PCA(n_components=4)
        self.pca.fit(test_data)
        self.pca_scores = self.pca.transform(test_data)
        self.color_mapper = {label:idx for idx,label in enumerate(set(test_labels))}
        self.color_column = [self.color_mapper[label] for label in test_labels]
        if savepath:
            pca_df = pd.DataFrame({"PC1":self.pca_scores[:,0], "PC2":self.pca_scores[:,1], "PC3":self.pca_scores[:,2],
                                   "PC4":self.pca_scores[:,3], "Labels":test_labels})
            pca_df.to_csv(savepath,sep=",")
        if plot:
            plt.scatter(self.pca_scores[:,0], self.pca_scores[:,1], s=1, c=self.color_column)


    def set_LIME(self, samplesize, testsentences, curr_model, split_expression=r'\W+', binary=True):
        
        self.samplesize = 30
        self.testsentences = testsentences
        self.curr_model = curr_model
        self.split_expression = split_expression
        self.non_word = re.compile(r'(%s)|$' % self.split_expression).match
        self.sample_sents = random.sample(testsentences, samplesize)
        
        self.explainer = LimeTextExplainer()
        self.contributors = defaultdict(dict)
        self.labels_sents = defaultdict(list)
        for i,sent in enumerate(self.sample_sents):
            print(i)
            self.sent = " ".join(sent)
            self.probs = self.LIMEPredictLabel([self.sent])
            #self.curr_label = self.curr_model.classes_[self.probs[0].argmax()]
            self.curr_label = self.probs[0].argmax()
            self.labels_sents[self.curr_label].append(self.sent)
            if binary:
                self.exp = self.explainer.explain_instance(self.sent + " @@", self.LIMEPredictLabel, num_features=6)
                self.listed_explanation = self.exp.as_list()
            else:
                self.exp = self.explainer.explain_instance(self.sent + " @@", self.LIMEPredictLabel, num_features=6, labels=[self.curr_label])
                self.listed_explanation = self.exp.as_list(label=self.curr_label)
            for word,contributing_weight in self.listed_explanation:
                if word in self.contributors[self.curr_label]:
                    self.contributors[self.curr_label][word].append(contributing_weight)
                else:
                    self.contributors[self.curr_label][word] = [contributing_weight]
            
        self.average_contributions = {}
        self.sorted_contributions = {}
        for label,lexica in self.contributors.iteritems():
            self.curr_label = label
            self.curr_lexica = lexica
            self.average_contributions[self.curr_label] = pd.Series(index=self.curr_lexica.keys())
            for word,scores in self.curr_lexica.iteritems():
                self.average_contributions[self.curr_label].loc[word] = np.sum(np.array(scores))/self.samplesize
            detractors = self.average_contributions[self.curr_label].sort_values()
            supporters = self.average_contributions[self.curr_label].sort_values(ascending=False)
            self.sorted_contributions[self.curr_label] = (detractors,supporters)

    def LIMEPredictLabel(self, sentences):
        self.sentences = sentences
        self.list_of_features = []
        for sentence in self.sentences:
            self.tokenized_sample = word_tokenize(sentence)
            self.list_of_features.append(np.mean([self.data.word2vec.word_vec(w) for w in self.tokenized_sample if w in self.data.word2vec],axis=0))
        return self.curr_model.predict_proba(self.list_of_features)










