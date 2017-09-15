#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:21:49 2017

@author: alexanderwahl
"""

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import pandas as pd
import numpy as np

from Preprocessing import Data


class Model(object):
    
    def set_data(self, data_path="/Users/alexanderwahl/Documents/Insight/Project/medscape_data_cleaned.json",
                       dev=10, 
                       test=10):
        
        self.data = Data(data_path, dev, test)
        self.data.set_data_for_log_reg()
        self.training_x = self.data.training_x
        self.training_y = self.data.training_y
        self.dev_x = self.data.dev_x
        self.dev_y = self.data.dev_y
        self.test_x = self.data.test_x
        self.test_y = self.data.test_y
        
    def run_log_regr_model(self, C=1.0):
        
        self.model = LogisticRegression(C=C)
        self.model.fit(self.data.training_x, self.data.training_y)
        
    def run_svm_model(self, C=1.0):
        
        self.model = SVC(C=C)
        self.model.fit(self.data.training_x, self.data.training_y)
    
    def set_accuracy(self, combine_dev_test=True):
        
        if combine_dev_test:
            self.current_test_x,self.current_test_y = self.combine_dev_test()
        else:
            self.current_test_x,self.current_test_y = self.test_x,self.test_y
        
        self.accuracy = self.model.score(self.current_test_x, self.current_test_y)
    
    def set_precision_recall(self, combine_dev_test=True):
        
        if combine_dev_test:
            self.current_test_x,self.current_test_y = self.combine_dev_test()
        else:
            self.current_test_x,self.current_test_y = self.test_x,self.test_y
        
        self.predicted_y = self.model.predict(self.current_test_x)
        self.precision = precision_score(self.current_test_y, self.predicted_y)
        self.recall = recall_score(self.current_test_y, self.predicted_y)
            
    def combine_dev_test(self):
        
        devtest_x = np.append(self.test_x, self.dev_x, axis=0)
        devtest_y = np.append(self.test_y, self.dev_y)
        return devtest_x,devtest_y
    



#Recall with 80/20 split and C=7.5
#0.79729729729729726

#Recall with 80/20 split and C=7.5
#0.50643776824034337





#
#####subsampling the clinical data
#
##get indices of all clinical labels
#all_clin_inds = np.where(i.labels=="clinical")[0]
#
#
##for x in range(50):
#for x in range(21):
#    #sample 2400 of those indices
#    random.seed(x)
#    #downsample_clin_inds = np.array(random.sample(all_clin_inds,2400))
#    downsample_clin_inds = all_clin_inds[x*2400:(x+1)*2400]
#    
#    #get the ~2400 clerical indices
#    all_cler_inds = np.where(i.labels=="clerical")[0]
#    
#    #join the 2400 random clinical indices with the ~2400 clerical indices
#    downsample_all_inds = np.append(downsample_clin_inds,all_cler_inds)
#    
#    #shuffle the combined index array
#    random.shuffle(downsample_all_inds)
#    
#    #take the first 3800 indices for training
#    downsample_training_inds = downsample_all_inds[:3800]
#    
#    #take the last 3800 indices for test
#    downsample_test_inds = downsample_all_inds[3800:]
#    
#    #get the x's and y's for training using the training index array
#    downsample_training_x = i.inputs[downsample_training_inds]
#    downsample_training_y = i.labels[downsample_training_inds]
#    
#    #get the x's and y's for test using the test index array
#    downsample_test_x = i.inputs[downsample_test_inds]
#    downsample_test_y = i.labels[downsample_test_inds]
#    
#    #lrm_downsample = LogisticRegression()
#    lrm_downsample = svm.SVC(C=4000)
#    lrm_downsample.fit(downsample_training_x, downsample_training_y)
#    score = lrm_downsample.score(downsample_test_x, downsample_test_y)
#    print "accuracy:",score
#
#    predicted_y = lrm.predict(downsample_test_x)
#    predicted_y_binary = np.zeros(len(predicted_y), dtype=int)
#    predicted_y_binary[np.where(predicted_y=="clerical")[0]] = 1
#
#    test_y_binary = np.zeros(len(predicted_y), dtype=int)
#    test_y_binary[np.where(downsample_test_y=="clerical")[0]] = 1
#
#    precision = sklearn.metrics.precision_score(test_y_binary, predicted_y_binary)
#    print "precision:", precision
#
#    recall = sklearn.metrics.recall_score(test_y_binary, predicted_y_binary)
#    print "recall:",recall
#
#    print "-----------------------------------------"









