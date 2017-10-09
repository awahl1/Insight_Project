#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:44:38 2017

@author: alexanderwahl
"""


def ensure_in_df_index(rowname, df, name_df):
    
    if rowname not in df.index:
        raise KeyError("The named data source is not present in " + name_df)
        
def ensure_string_argument(datastructure, name_datastructure):
    
    if type(datastructure)!=str:
        raise TypeError(name_datastructure + " argument must be a string")
        
def ensure_boolean_argument(datastructure, name_datastructure):
    
    if type(datastructure)!=bool:
        raise TypeError(name_datastructure + " argument must be true or false")
        
def ensure_main_type(MAIN_TYPE):
    
    if MAIN_TYPE not in ["clinical", "clerical", "other"]:
        raise TypeError("MAIN_TYPE argument must be either 'clinical', 'clerical', or 'other'")
        
def ensure_data_size(clinical, clerical, other):
    
    if len(clinical)==0 or len(clerical)==0 or len(other)==0:
        raise TypeError("The clinical, clerical, or other list of data passed from DataGrouper is empty.")