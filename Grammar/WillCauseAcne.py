#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:11:22 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class WillXMakeAcneWorse(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.MakeCause(), lx.Conditions(), lx.Worse()]
        
class WillXMakeAcneGetWorse(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.MakeCause(), lx.Conditions(), lx.To(), lx.Get(), lx.Worse()]
        
class WillXCauseBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.MakeCause(), lx.BreakOut()]
        
class WillAcneGetWorse(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.Conditions(), lx.Get(), lx.Worse(), lx.If(), lx.SubjNonthird(), lx.TakeApplyUse(), ex.ProductsExpander()]
        
class WillAcneGetWorse2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.Conditions(), lx.Get(), lx.Worse(), lx.If(), lx.PossessedNouns(), lx.TakeApplyUse(), ex.ProductsExpander()]

class WillIBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.SubjNonthird(), lx.BreakOut(), lx.If(), lx.PossessivesNonthird(), lx.TakeApplyUse(), ex.ProductsExpander()]

class WillMySonBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WillIsGonna(), lx.PossessedNouns(), lx.BreakOut(), lx.If(), lx.SubjThird(), lx.TakeApplyUse(), ex.ProductsExpander()]
        
class IWasPrescribed(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.Was(), lx.Prescribed(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(), lx.Conditions(),
                          lx.Get(), lx.Worse()]
        
class MySonWasPrescribed(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.Was(), lx.Prescribed(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(), lx.Conditions(),
                          lx.Get(), lx.Worse()]
        
class TheDoctorPrescribed(Template):
    
    def __init__(self):
        
        self.sequence = [lx.DoctorNurse(), lx.Prescribed(), ex.ProductsExpander(), lx.WillIsGonna(), lx.Conditions(),
                          lx.Get(), lx.Worse()]
        
class ITakeWillGetWorse(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.TakeApplyUse(), ex.ProductsExpander(), lx.WillIsGonna(), lx.Conditions(),
                          lx.Get(), lx.Worse()]
        
class MySonTakesGetWorse(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.TakeApplyUse(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(), lx.Conditions(),
                          lx.Get(), lx.Worse()]      

class IWasPrescribedBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.Was(), lx.Prescribed(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(), lx.BreakOut()]
        
class MySonWasPrescribedBreakOut(Template):
    
    def __init__(self):

        self.sequence = [lx.PossessedNouns(), lx.Was(), lx.Prescribed(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(), lx.BreakOut()]
        
class TheDoctorPrescribedBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.DoctorNurse(), lx.Prescribed(), ex.ProductsExpander(), lx.WillIsGonna(), lx.BreakOut()]
        
class ITakeWillGetWorseBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.TakeApplyUse(), ex.ProductsExpander(), lx.WillIsGonna(), lx.BreakOut()]
        
class MySonTakesGetWorseBreakOut(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.TakeApplyUse(), ex.ProductsExpander(), lx.ByTheDoctor(), lx.WillIsGonna(),lx.BreakOut()]  