#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:05:43 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class CanYouTellMeAboutTheDoctors(Template):
    
    def __init__(self):
        
        self.sequence = [lx.CanCouldWould(), lx.Tell(), lx.ObjNonthird(), lx.About(), ex.OptionalTheRecordOf(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), ex.OptionalPracticingMedicine()]

    
class WhoWillBeReviewingMyCase(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Who(), lx.Will(), lx.Review(), lx.PossessivesNonthird(), lx.Case(), ex.OptionalPracticingMedicine()]
    

class WhoWillBeReviewingMySonsCase(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Who(), lx.Will(), lx.Review(), lx.PossessivesThirdAll(), lx.Case(), ex.OptionalPracticingMedicine()]
    

class IdLikeToKnowMoreAboutTheDoctors(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IdLikeToKnowMore(), lx.About(), ex.OptionalTheRecordOf(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), ex.OptionalPracticingMedicine()]
    

class HowDoIGetMoreInfoAboutTheDoctors(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.AuxNonthird(), lx.LearnGetFindOut(), lx.More(), lx.Info(), lx.About(), ex.OptionalTheRecordOf(), lx.DoctorNurse(), 
                         ex.OptionalWhoPhrase()]