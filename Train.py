#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:11:25 2017

@author: alexanderwahl
"""

from sklearn.externals import joblib

from Preprocessing import DataStoreManager
from Preprocessing import DataGrouper
from Preprocessing import DataPreprocessor
from LogRegr import Model


class Trainer(object):
    
    """
    This class is used to train the main and clerical models. Its __init__ method
    runs several scripts from the Preprocessing module to get the data in order.
    """
    
    def __init__(self):
        
        self.data_store_manager = DataStoreManager()
        self.data_store_manager.load_data()
        
        self.data_grouper = DataGrouper()
        for name,main_type in self.data_store_manager:
            if main_type=="clinical":
                self.data_grouper.add_clinical(self.data_store_manager.get_data(name), name)
            elif main_type=="clerical":
                self.data_grouper.add_clerical(self.data_store_manager.get_data(name), name)
            elif main_type=="other":
                self.data_grouper.add_other(self.data_store_manager.get_data(name), name)
        
        self.data_preprocessor = DataPreprocessor(self.data_grouper)
        self.data_preprocessor.process_for_training()
        self.word2vec = self.data_preprocessor.word2vec
        self.model_manager = Model()
        self.model_manager.set_data(self.data_preprocessor)
    
    def train_main(self):
        
        """
        Trains the main model. Creates a main_accuracy attribute that gives
        accuracy evaluated on a test set.
        """
    
        self.model_manager.toplevel_logistic_regr(include_other=True)
        self.model_manager.set_accuracy(self.model_manager.toplevel_test_x,
                                        self.model_manager.toplevel_test_y,
                                        self.model_manager.model_main)
        self.main_accuracy = self.model_manager.accuracy
        self.model_main = self.model_manager.model_main
    
    def train_cler(self):
        
        """
        Trains the clerical model. Creates a cler_accuracy attribute that gives
        accuracy evaluated on a test set.
        """
        
        self.model_manager.clerical_logistic_regr()
        self.model_manager.set_accuracy(self.model_manager.cler_test_x,
                                        self.model_manager.cler_test_y,
                                        self.model_manager.model_cler)
        self.cler_accuracy = self.model_manager.accuracy
        self.model_cler = self.model_manager.model_cler
        
    def save_main(self, model_main_path="main_model.pkl"):
        
        """
        save the main model to disk as a pickle-like object
        
        Params:
            model_main_path: the file path at which to save the model
        """
        
        joblib.dump(self.model_manager.model_main, model_main_path)
        
    def save_cler(self, cler_model_path="cler_model.pkl"):
        
        """
        save the clerical model to disk as a pickle-like object
        
        Params:
            cler_model_path: the file path at which to save the model
        """
        
        joblib.dump(self.model_manager.model_cler, cler_model_path)