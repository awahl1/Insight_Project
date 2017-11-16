#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:59:09 2017

@author: alexanderwahl
"""
from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex


class WhatIsYourRefundPolicy(Template):
    
    def __init__(self):
        
        self.sequence = [lx.WhatIsThe(), lx.ReturnPolicy()]
        
class DoYouAllowReturns(Template):
    
    def __init__(self):
        
        self.sequence = [lx.AuxNonthird(), lx.You(), lx.AllowPermit(), lx.ReturnsRefunds()]
        
class AreReturnsPermitted(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Are(), lx.ReturnsRefunds(), lx.AllowedPermitted()]

class HowDoIReturnMyProducts(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.AuxNonthird(), lx.SubjNonthird(), lx.Return(), lx.PossessivesNonthird(), ex.ProductsExpander()]
        
class HowCanIReturnMyProducts2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Modals(), lx.SubjNonthird(), lx.Return(), lx.PossessivesNonthird(), ex.ProductsExpander()]

class HowDoesMySonReturnHisProducts(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.AuxThird(), lx.PossessedNouns(), lx.Return(), lx.PossessivesThird(), ex.ProductsExpander()]
        
class HowDoesMySonReturnHisProducts2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Modals(), lx.PossessedNouns(), lx.Return(), lx.PossessivesThird(), ex.ProductsExpander()]
    
class HowDoIGetARefund(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.DoCan(), lx.SubjNonthird(), lx.ReceiveGet(), lx.Refund()]
        
class HowDoIGetARefund2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Modals(), lx.SubjNonthird(), lx.ReceiveGet(), lx.Refund()]
    
class HowDoesMySonGetARefund(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.DoesCan(), lx.PossessedNouns(), lx.ReceiveGet(), lx.Refund()]

class HowDoesMySonGetARefund2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Modals(), lx.PossessedNouns(), lx.ReceiveGet(), lx.Refund()]
        
class HowDoIGetARefundForMyProducts(Template):
    
    def __init__(self):
            
        self.sequence = [lx.How(), lx.DoCan(), lx.SubjNonthird(), lx.ReceiveGet(), lx.Refund(), lx.For(), lx.PossessivesNonthird(),
                             ex.ProductsExpander()]
        
class HowDoIGetARefundForMyProducts2(Template):
    
    def __init__(self):
            
        self.sequence = [lx.How(), lx.Modals(), lx.SubjNonthird(), lx.ReceiveGet(), lx.Refund(), lx.For(), lx.PossessivesNonthird(),
                             ex.ProductsExpander()]
    
class HowDoesMySonGetARefundForHisProducts(Template):
    
    def __init__(self):
            
        self.sequence = [lx.How(), lx.DoesCan(), lx.PossessedNouns(), lx.ReceiveGet(), lx.Refund(), lx.For(), lx.PossessivesThird(),
                             ex.ProductsExpander()]
        
class HowDoesMySonGetARefundForHisProducts2(Template):
    
    def __init__(self):
            
        self.sequence = [lx.How(), lx.Modals(), lx.PossessedNouns(), lx.ReceiveGet(), lx.Refund(), lx.For(), lx.PossessivesThird(),
                             ex.ProductsExpander()]
    
class IsItPossibleToGetARefund(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsItPossible(), lx.To(), lx.Get(), lx.Refund()]
    
class IsItPossibleToGetARefundForProducts(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsItPossible(), lx.To(), lx.Get(), lx.Refund(), lx.For(), ex.ProductsExpander()]
    
class IsItPossibleToReturnProducts(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsItPossible(), lx.To(), lx.Return(), ex.ProductsExpander()]
    
class CanIGetARefund(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.SubjNonthird(), lx.Get(), lx.Refund()]
        
class CanIGetARefund2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.SubjNonthird(), lx.Get(), lx.Refund(), lx.For(), ex.ProductsExpander()]
    
class CanMySonGetARefund(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.PossessedNouns(), lx.Get(), lx.Refund()]
        
class CanMySonGetARefund2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.PossessedNouns(), lx.Get(), lx.Refund(), lx.For(), ex.ProductsExpander()]
    
class CanIReturnMyProduct(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.SubjNonthird(), lx.Return(), lx.PossessivesNonthird(), ex.ProductsExpander()]

class CanMySonReturnHisProduct(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Can(), lx.PossessedNouns(), lx.Return(), lx.PossessivesThird(), ex.ProductsExpander()]
        
class IAmNotSatisfiedWithMyProduct(Template):
    
    def __init__(self):
        
        self.sequence = [lx.FirstPersonToBe(), lx.NotSatisfiedWith(), lx.PossessivesNonthird(), ex.ProductsExpander()]
    
class MySonIsNotSatisfiedWithHisProduct(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.Is(), lx.NotSatisfiedWith(), lx.PossessivesThird(), ex.ProductsExpander()]