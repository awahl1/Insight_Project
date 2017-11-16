#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:38:41 2017

@author: alexanderwahl
"""

import random


class Template(object):
    
    def __init__(self):
        
        self.sequence = []
        
    def generate(self):
        
        self.lexicalized_sequence = []
        
        for element in self.sequence:
            if issubclass(type(element), Lexicalizer):
                self.lexicalized_sequence.extend(element.lexicalize())
            elif issubclass(type(element), Expander):
                self.lexicalized_sequence.extend(element.expand())

        return self.lexicalized_sequence


class Lexicalizer(object):
    
    def __init__(self):
        
        self.all_words = []
        
    def lexicalize(self):
        
        if self.all_words:
            return random.sample(self.all_words,1)
        else:
            return []


class Expander(object):
    
    def __init__(self):
        
        self.all_templates = []
        
    def expand(self):
        
        self.curr_template = random.sample(self.all_templates,1)[0]
        return self.curr_template.generate()