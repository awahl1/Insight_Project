#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:55:50 2017

@author: alexanderwahl
"""

from Baseclasses import Template
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

class HowMuchDoesShippingCost(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowMuch(), lx.Does(), lx.Shipping(), lx.Cost()]

class HowMuchDoesShippingCost2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowMuch(), lx.Does(), lx.Shipping(), ex.ProductsExpander(), lx.Cost()]
        
class HowMuchDoesItCostToShip(Template):
    
    def __init__(self):
        
        self.sequence = [lx.HowMuch(), lx.Does(), lx.It(), lx.Cost(), lx.To(), lx.Mail(), ex.ProductsExpander()]
        
class HowExpensiveIsItToMail(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Expensive(), lx.Is(), lx.It(), lx.To(), lx.Mail(), ex.ProductsExpander()]
        
class HowExpensiveIsShipping(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Expensive(), lx.Is(), lx.Shipping()]
        
class HowExpensiveIsShippingProducts(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.Expensive(), lx.Is(), lx.Shipping(), ex.ProductsExpander()]