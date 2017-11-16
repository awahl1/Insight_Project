#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:30:59 2017

@author: alexanderwahl
"""

from TopLevelExpanders import (WhenWillIGetMyMedicineToplevel,HowLongToReviewMyCaseTopLevel,HearFromDoctorTopLevel,
                               HowMuchDoesShippingCostTopLevel,WhatIsTheRefundPolicyTopLevel,CallMeAtThisNumberTopLevel,
                               MoreInfoAboutDoctorsTopLevel,ShouldIStopTakingTopLevel,WillCauseMeAcneTopLevel)


"""
The functions is this module can be used to generate alternate forms of asking the clerical and clinical questions
specified in the name of each function.

Each function takes a single arugument specifying the number of samples to return.
"""

###Private
def _QuestionGenerator(number_of_iterations, toplevel_expander=None):
        
        top = toplevel_expander()
        results = []
        for i in range(number_of_iterations):
            result = top.expand()
            results.append(" ".join(result))
        return results

 
###Clerical
        
def WhenWillIGetMyMedicineGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, WhenWillIGetMyMedicineToplevel)
        
def HowLongToReviewMyCaseGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, HowLongToReviewMyCaseTopLevel)
        
def HearFromDoctorGenerator(number_of_iterations):

    return _QuestionGenerator(number_of_iterations, HearFromDoctorTopLevel)
          
def HowMuchDoesShippingCostGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, HowMuchDoesShippingCostTopLevel)

def WhatIsTheRefundPolicyGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, WhatIsTheRefundPolicyTopLevel)
    
def CallMeAtThisNumberGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, CallMeAtThisNumberTopLevel)
    
def MoreInfoAboutDoctorsGenerator(number_of_iterations):

    return _QuestionGenerator(number_of_iterations, MoreInfoAboutDoctorsTopLevel)



#####Clinical

def ShouldIStopTakingGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, ShouldIStopTakingTopLevel)

def WillCauseMeAcneGenerator(number_of_iterations):
    
    return _QuestionGenerator(number_of_iterations, WillCauseMeAcneTopLevel)