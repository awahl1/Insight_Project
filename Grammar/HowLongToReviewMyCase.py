#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:50:55 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class HowLongDoesItTakeToReview1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), ex.HowLongReview, lx.PossessivesNonthird(), lx.Case()]
        
class HowLongDoesItTakeToReview2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), ex.HowLongReview(), lx.PossessivesThirdAll(), lx.Case()]  
        
class WhenWillTheDoctorFinish1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxNonthird(), lx.The(), lx.DoctorNurse(), lx.Finish(), lx.Review(), lx.PossessivesNonthird(), lx.Case()]
        
class WhenWillTheDoctorFinish3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.The(), lx.DoctorNurse(), lx.Finish(), lx.Review(), lx.PossessivesThirdAll(), lx.Case()]
        
class WhenWillIHear(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxNonthird(), lx.SubjNonthird(), lx.HearFindOut(), lx.From(), lx.The(), lx.DoctorNurse(), lx.About(), 
                         lx.PossessivesNonthird(), lx.Case()]
        
class WhenWillHeHear(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.PossessedNouns(), lx.HearFindOut(), lx.From(), lx.The(), lx.DoctorNurse(), lx.About(), 
                         lx.PossessivesThird(), lx.Case()]

class HowLongDoIHaveToWaitForReview1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.AuxNonthird(), lx.SubjNonthird(), lx.HaveToWaitFor(), lx.HearFindOut(), lx.About(), 
                         lx.PossessivesNonthird(), lx.Case()]
        
class HowLongDoIHaveToWaitForReview2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.AuxThird(), lx.PossessedNouns(), lx.HaveToWaitFor(), lx.HearFindOut(), lx.About(), 
                         lx.PossessivesThirdAll(), lx.Case()] 