#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:35:48 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class WhenWillIGetMyMedicine1(Template):
    
    """When will I get my medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxNonthird(), lx.SubjNonthird(), lx.ReceiveGet(), lx.PossessivesNonthird(), ex.ProductsExpander(), 
                         ex.OptionalObliquesNonthird()]
        
class WhenWillIGetMyMedicine2(Template):
    
    """When will my son get his medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.PossessedNouns(), lx.ReceiveGet(), lx.PossessivesThird(), ex.ProductsExpander(), 
                         ex.OptionalObliquesThird()]
        
class WhenWillIGetMyMedicine3(Template):
    
    """When am I gonna get my medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.FirstPersonToBeInversion(), lx.GoingtoGonna(), lx.ReceiveGet(), lx.PossessivesNonthird(), ex.ProductsExpander(), 
                         ex.OptionalObliquesNonthird()]
        
class WhenWillIGetMyMedicine4(Template):
    
    """When is my son gonna get his medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.Is(), lx.PossessedNouns(), lx.GoingtoGonna(), lx.ReceiveGet(), lx.PossessivesThird(), ex.ProductsExpander(), 
                         ex.OptionalObliquesThird()]
        
        
class WhenWillMyMedicineArrive1(Template):
    
    """When will my medicine arrive at my house"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.PossessivesThirdAll(), ex.ProductsExpander(), ex.ArrivalPhraseThird()]

class WhenWillMyMedicineArrive2(Template):
    
    """When will my son's medicine arrive at his house"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.AuxThird(), lx.PossessivesNonthird(), ex.ProductsExpander(), ex.ArrivalPhraseNonthird()]
        
class WhenCanIExpectMyMedicineToArrive1(Template):
    
    """When can I expect my medicine to arrive at my house"""

    def __init__(self):

        self.sequence = [lx.When(), lx.Modals(), lx.SubjNonthird(), lx.Expect(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.To(), ex.ArrivalPhraseNonthird()]        

class WhenCanIExpectMyMedicineToArrive2(Template):
    
    """When can my son expect his medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.When(), lx.Modals(), lx.PossessedNouns(), lx.Expect(), lx.PossessivesThird(), ex.ProductsExpander(), lx.To(), ex.ArrivalPhraseThird()]      

class WhenCanIExpectToGetMyMedicine1(Template):
    
    """When can I expect to get my medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.Modals(), lx.SubjNonthird(), lx.Expect(), lx.To(), lx.ReceiveGet(), lx.PossessivesNonthird(), ex.ProductsExpander(),
                         ex.OptionalObliquesNonthird()]
        
class WhenCanIExpectToGetMyMedicine2(Template):
    
    """When can my son expect to get his medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.When(), lx.Modals(), lx.PossessedNouns(), lx.Expect(), lx.To(), lx.ReceiveGet(), lx.PossessivesThird(), ex.ProductsExpander(),
                         ex.OptionalObliquesThird()]


class HowLongUntilMyMedicineArrives1(Template):
    
    """How long until my medicine arrives in the mail"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.Arrives(), ex.OptionalObliquesNonthird()]        

class HowLongUntilMyMedicineArrives2(Template):
    
    """How long until my son's medicine arrives in the mail"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesThirdAll(), ex.ProductsExpander(), lx.Arrives(), ex.OptionalObliquesThird()]      
        
class HowLongUntilMyMedicineComes1(Template):
    
    """How long until my medicine comes"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.ComesGetshere(), ex.OptionalObliquesNonthirdTo()]        

class HowLongUntilMyMedicineComes2(Template):
    
    """How long until my son's medicine comes"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesThirdAll(), ex.ProductsExpander(), lx.ComesGetshere(), ex.OptionalObliquesThirdTo()]     
        
class HowLongUntilMyMedicineGetsToMyApartment1(Template):
    
    """How long until my medicine gets to my apartment"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.Gets(), ex.GetComplementNonthird()]        

class HowLongUntilMyMedicineGetsToMyApartment2(Template):
    
    """How long until my son's medicine gets to his apartment"""

    def __init__(self):

        self.sequence = [lx.HowLongUntil(), lx.PossessivesThirdAll(), ex.ProductsExpander(), lx.Gets(), ex.GetComplementThird()]     

class HowLongUntilIReceiveMyMedicine1(Template):
    
    """How long until I receive my medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.HowLongUntil(), lx.SubjNonthird(), lx.ReceiveGet(), lx.PossessivesNonthird(), ex.ProductsExpander(),
                         ex.OptionalObliquesNonthird()]
        
class HowLongUntilIReceiveMyMedicine2(Template):
    
    """How long until my son receives his medicine in the mail"""
    
    def __init__(self):
        
        self.sequence = [lx.HowLongUntil(), lx.PossessedNouns(), lx.ReceivesGets(), lx.PossessivesThird(), ex.ProductsExpander(),
                         ex.OptionalObliquesThird()]
        
class HowLongDoesItTakeForMyMedicineToArrive1(Template):
    
    """How long does it take for my medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.HowLong(), lx.DoesItTakeFor(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.To(), ex.ArrivalPhraseNonthird()]        

class HowLongDoesItTakeForMyMedicineToArrive2(Template):
    
    """How long long does it for my son's medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.HowLong(), lx.DoesItTakeFor(), lx.PossessivesThirdAll(), ex.ProductsExpander(), lx.To(), ex.ArrivalPhraseThird()]      

class HowLongWillIHaveToWaitForMyMedicineToArrive1(Template):
    
    """How long will I have to wait for my medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.HowLong(), lx.AuxNonthird(), lx.SubjNonthird(), lx.HaveToWaitFor(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.To(),
                         ex.ArrivalPhraseNonthird()]        

class HowLongWillIHaveToWaitForMyMedicineToArrive2(Template):
    
    """How long will my son have to wait for his medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.HowLong(), lx.AuxThird(), lx.PossessedNouns(), lx.HaveToWaitFor(), lx.PossessivesThird(), ex.ProductsExpander(), lx.To(), 
                         ex.ArrivalPhraseThird()]


class WhatIsTheTimeItWillTakeForMyMedicineToArrive1(Template):
    
    """What is the time it will take for my medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.WhatIsThe(), lx.TimeAmountOfTime(), lx.It(), lx.TakesWillTake(), lx.For(), lx.PossessivesNonthird(), ex.ProductsExpander(), lx.To(),
                         ex.ArrivalPhraseNonthird()]        

class WhatIsTheTimeItWillTakeForMyMedicineToArrive2(Template):
    
    """What is the time it willt ake for my son's medicine to arrive"""

    def __init__(self):

        self.sequence = [lx.WhatIsThe(), lx.TimeAmountOfTime(), lx.It(), lx.TakesWillTake(), lx.For(), lx.PossessivesThird(), ex.ProductsExpander(), lx.To(), 
                         ex.ArrivalPhraseThird()]      

class WhatIsTheShippingTimeForMyMedicine1(Template):
    
    """What is the shipping time for my medicine"""
    
    def __init__(self):
        
        self.sequence = [lx.WhatIsThe(), lx.ShippingTime(), lx.For(), lx.PossessivesNonthird(), ex.ProductsExpander()]

class WhatIsTheShippingTimeForMyMedicine2(Template):
    
    """What is the shipping time for my son's medicine"""
    
    def __init__(self):
        
        self.sequence = [lx.WhatIsThe(), lx.ShippingTime(), lx.For(), lx.PossessivesThirdAll(), ex.ProductsExpander()]
        
