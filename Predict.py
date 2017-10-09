#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:11:55 2017

@author: alexanderwahl
"""
import re

import numpy as np
from nltk import word_tokenize
import gensim
from sklearn.externals import joblib


def LoadSavedModels(main_model_path="main_model.pkl", 
                    cler_model_path="cler_model.pkl", 
                    word2vec_path='GoogleNews-vectors-negative300.bin'):
    
    """
    Used for loading in model and word2vec files from disk.
    Returns their objects.
    """
    
    model_main = joblib.load(main_model_path)
    model_cler = joblib.load(cler_model_path)
    word2vec = gensim.models.KeyedVectors.load_word2vec_format(word2vec_path, binary=True)

    return model_main,model_cler,word2vec    
    




def PredictLabel(sentence, model_main, word2vec, boundary=0.5):
    
    """
    Predict a label using the main model (clinical, clerical or other).
    Input is a sentence, along w/ model object and word2vec object.
    These objects can either be loaded from disk using the LoadSavedModels
    function, or, if you have just completed training, they can be passed in
    from the Train.Trainer class.
    
    May also adjust the probability threshold above which a clerical decision
    is made (good for reducing false positives). 0.98 makes for very few
    false positives!
    """
    
    tokenized_sample = word_tokenize(re.sub("-"," ",sentence))
    features = np.mean([word2vec.word_vec(w) for w in tokenized_sample if w in word2vec],axis=0)
    prediction = model_main.predict_proba(features.reshape(1,-1))[0]
    if model_main.classes_[prediction.argmax()]!="clerical":
        return model_main.classes_[prediction.argmax()]
    else:
        if np.max(prediction)>boundary:
            return "clerical"
        else:
            ranger = range(len(prediction))
            del ranger[prediction.argmax()]
            return model_main.classes_[ranger][prediction[ranger].argmax()]


def PredictClerLabel(sentence, model_cler, word2vec): 
    
    """
    Predict a label use the clerical model. Input is a sentence, along w/ model
    object and word2vec object. These objects can either be loaded from disk 
    using the LoadSavedModels function, or, if you have just completed training, 
    they can be passed in from the Train.Trainer class.
    """
    
    tokenized_sample = word_tokenize(re.sub("-"," ",sentence))
    features = np.mean([word2vec.word_vec(w) for w in tokenized_sample if w in word2vec],axis=0)
    prediction = model_cler.predict_proba(features.reshape(1,-1))[0]
    return model_cler.classes_[prediction.argmax()]


      
if __name__=="__main__":
    flag = True
    model_main,model_cler,word2vec = LoadSavedModels()
    while flag:
        sentence = raw_input("Type your question or q to quit:")
        if sentence=="q":
            flag = False
        else:
            toplevel_prediction = PredictLabel(sentence, model_main, word2vec)
            print("toplevel prediction: " + toplevel_prediction)
            if toplevel_prediction=="clerical":
                clerical_prediction = PredictClerLabel(sentence, model_cler, word2vec)
                print("clerical prediction: " + clerical_prediction)
            print("--------------------------------------------")