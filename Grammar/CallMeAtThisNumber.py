#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:04:46 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex


class ContactMeAtThisNumber(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PolitePreface(), lx.ContactCallPhone(), lx.ObjNonthird(), lx.ByPhone()]
        
class ContactMeAtThisNumber2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PolitePreface(), lx.ContactCallPhone(), lx.ObjNonthird(), lx.At(), lx.PossessivesNonthird(), lx.ByPhone()]
        
class ContactHimAtThisNumber(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PolitePreface(), lx.ContactCallPhone(), lx.PossessedNouns(), lx.ByPhone()]
        
class ContactHimAtThisNumber2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PolitePreface(), lx.ContactCallPhone(), lx.PossessedNouns(), lx.At(), lx.PossessivesThird(), lx.ByPhone()]
        
class IWantToSpeakToADoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.WantNeed(), lx.To(), lx.SpeakTalk(), lx.To(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ByPhone(), ex.OptionalAboutPhrase()]
        
class MySonWantToSpeakToADoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.WantsNeeds(), lx.To(), lx.SpeakTalk(), lx.To(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ByPhone(), ex.OptionalAboutPhrase()]
        
class CanISpeakToADoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.SubjNonthird(), lx.SpeakTalk(), lx.To(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ByPhone(), ex.OptionalAboutPhrase()]
        
class CanMySonSpeakToADoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.PossessedNouns(), lx.SpeakTalk(), lx.To(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ByPhone(), ex.OptionalAboutPhrase()]
        
class IsItPossibleToSpeakToADoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsItPossible(), lx.To(), lx.SpeakTalk(), lx.To(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ByPhone(), ex.OptionalAboutPhrase()]

class CanTheDoctorCallMe(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.DoctorNurse(), ex.OptionalWhoPhrase(), lx.ContactCallPhone(), ex.MeMySon()]
