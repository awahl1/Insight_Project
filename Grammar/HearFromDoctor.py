#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:54:39 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class WhenWillIHearFromMyDoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxNonthird(), lx.SubjNonthird(), lx.HearFindOut(), lx.From(), lx.PossessivesNonthird(), lx.DoctorNurse(), ex.OptionalWhoPhrase()]
        
class WhenWillHeHearFromMyDoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.PossessedNouns(), lx.Hear(), lx.From(), lx.PossessivesThird(), lx.DoctorNurse(), ex.OptionalWhoPhrase()]
        
class WhenWillTheDoctorContactMe(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.Contact(), lx.ObjNonthird()]
        
class WhenWillTheDoctorContactHim(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.Contact(), lx.PossessedNouns()]
        
class HowLongDoesItTakeToHearFromMyDoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.DoesItTakeFor(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.To(), lx.Contact(), lx.ObjNonthird()]
        
class HowLongDoesItTakeToHearFromMyDoctor2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.DoesItTakeFor(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.To(), lx.Contact(), lx.PossessedNouns()]
        
class HowLongDoesItTakeToHearFromMyDoctor3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.DoesItTakeFor(), lx.Hear(), lx.From(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase()]
        
class HowLongDoIHaveToWaitToHearFromTheDoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.AuxNonthird(), lx.SubjNonthird(), lx.HaveToWaitFor(), lx.Hear(), lx.From(), lx.DoctorNurse(), ex.OptionalWhoPhrase()]
        
class HowLongDoIHaveToWaitToHearFromTheDoctor2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowLong(), lx.AuxThird(), lx.PossessedNouns(), lx.HaveToWaitFor(), lx.Hear(), lx.From(), lx.DoctorNurse(), ex.OptionalWhoPhrase()]

class WillTheDoctorContactMe(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillCap(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.Contact(), lx.ObjNonthird()]
        
class WillTheDoctorContactHim(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillCap(), lx.The(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.Contact(), lx.PossessedNouns()]