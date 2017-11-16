#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:32:37 2017

@author: alexanderwahl
"""

from Baseclasses import Expander
import WhenWillIGetMyMedicine as mdcn
import HowLongToReviewMyCase as rvw
import HearFromDoctor as hear
import HowMuchDoesShippingCost as cost
import WhatIsTheRefundPolicy as rfnd
import CallMeAtThisNumber as call
import MoreInfoAboutDoctors as info
import ShouldIStopTaking as stop
import WillCauseAcne as acne


class WhenWillIGetMyMedicineToplevel(Expander):

    def __init__(self):
        
        self.all_templates = [mdcn.WhenWillIGetMyMedicine1(), mdcn.WhenWillIGetMyMedicine2(), mdcn.WhenWillIGetMyMedicine3(), mdcn.WhenWillIGetMyMedicine4(), mdcn.WhenWillMyMedicineArrive1(),
                              mdcn.WhenWillMyMedicineArrive2(), mdcn.WhenCanIExpectMyMedicineToArrive1(), mdcn.WhenCanIExpectMyMedicineToArrive2(), mdcn.WhenCanIExpectToGetMyMedicine1(),
                              mdcn.WhenCanIExpectToGetMyMedicine2(), mdcn.HowLongUntilMyMedicineArrives1(), mdcn.HowLongUntilMyMedicineArrives2(), mdcn.HowLongUntilMyMedicineComes1(),
                              mdcn.HowLongUntilMyMedicineComes2(), mdcn.HowLongUntilMyMedicineGetsToMyApartment1(), mdcn.HowLongUntilMyMedicineGetsToMyApartment2(),
                              mdcn.HowLongUntilIReceiveMyMedicine1(), mdcn.HowLongUntilIReceiveMyMedicine2(), mdcn.HowLongDoesItTakeForMyMedicineToArrive1(),
                              mdcn.HowLongDoesItTakeForMyMedicineToArrive2(), mdcn.HowLongWillIHaveToWaitForMyMedicineToArrive1(),
                              mdcn.HowLongWillIHaveToWaitForMyMedicineToArrive2(), mdcn.WhatIsTheTimeItWillTakeForMyMedicineToArrive1(),
                              mdcn.WhatIsTheTimeItWillTakeForMyMedicineToArrive2(), mdcn.WhatIsTheShippingTimeForMyMedicine1(), mdcn.WhatIsTheShippingTimeForMyMedicine2()]
        

class HowLongToReviewMyCaseTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [rvw.HowLongDoesItTakeToReview1(), rvw.HowLongDoesItTakeToReview2(), rvw.WhenWillTheDoctorFinish1(), 
                              rvw.WhenWillTheDoctorFinish3(), rvw.WhenWillTheDoctorFinish3(), rvw.WhenWillIHear(), rvw.WhenWillHeHear(), 
                              rvw.HowLongDoIHaveToWaitForReview1(), rvw.HowLongDoIHaveToWaitForReview2()]
        
        
        
        
class HearFromDoctorTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [hear.WhenWillIHearFromMyDoctor(), hear.WhenWillHeHearFromMyDoctor(), hear.WhenWillTheDoctorContactMe(), 
                              hear.WhenWillTheDoctorContactHim(),hear.HowLongDoesItTakeToHearFromMyDoctor(), hear.HowLongDoesItTakeToHearFromMyDoctor2(), 
                              hear.HowLongDoesItTakeToHearFromMyDoctor3(), hear.HowLongDoIHaveToWaitToHearFromTheDoctor(), 
                              hear.HowLongDoIHaveToWaitToHearFromTheDoctor2()]
        
        
        
class HowMuchDoesShippingCostTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [cost.HowMuchDoesShippingCost(), cost.HowMuchDoesShippingCost2(), cost.HowMuchDoesItCostToShip(), 
                              cost.HowExpensiveIsItToMail(), cost.HowExpensiveIsShipping(), cost.HowExpensiveIsShippingProducts()]


class WhatIsTheRefundPolicyTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [rfnd.WhatIsYourRefundPolicy(),rfnd.DoYouAllowReturns(),rfnd.AreReturnsPermitted(),rfnd.AreReturnsPermitted(),rfnd.HowDoIReturnMyProducts(),
                              rfnd.HowCanIReturnMyProducts2(),rfnd.HowDoesMySonReturnHisProducts(),rfnd.HowDoesMySonReturnHisProducts2(),rfnd.HowDoIGetARefund(),
                              rfnd.HowDoIGetARefund2(),rfnd.HowDoesMySonGetARefund(),rfnd.HowDoesMySonGetARefund2(),rfnd.HowDoIGetARefundForMyProducts(),
                              rfnd.HowDoIGetARefundForMyProducts2(),rfnd.HowDoesMySonGetARefundForHisProducts(),rfnd.HowDoesMySonGetARefundForHisProducts2(),
                              rfnd.IsItPossibleToGetARefund(),rfnd.IsItPossibleToGetARefundForProducts(),rfnd.IsItPossibleToReturnProducts(),rfnd.CanIGetARefund(),
                              rfnd.CanIGetARefund2(),rfnd.CanMySonGetARefund(),rfnd.CanMySonGetARefund2(),rfnd.CanIReturnMyProduct(),rfnd.CanMySonReturnHisProduct(),
                              rfnd.IAmNotSatisfiedWithMyProduct(), rfnd.MySonIsNotSatisfiedWithHisProduct()]
        
        
class CallMeAtThisNumberTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [call.ContactMeAtThisNumber(), call.ContactMeAtThisNumber2(), call.ContactHimAtThisNumber(), 
                              call.ContactHimAtThisNumber2(), call.IWantToSpeakToADoctor(), call.MySonWantToSpeakToADoctor(), 
                              call.CanISpeakToADoctor(), call.CanMySonSpeakToADoctor(), call.IsItPossibleToSpeakToADoctor(),
                              call.CanTheDoctorCallMe()]

class MoreInfoAboutDoctorsTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [info.CanYouTellMeAboutTheDoctors(), info.WhoWillBeReviewingMyCase(), info.WhoWillBeReviewingMySonsCase(), 
                              info.IdLikeToKnowMoreAboutTheDoctors(), info.HowDoIGetMoreInfoAboutTheDoctors()]
        
class ShouldIStopTakingTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [stop.QuestionProblem(),stop.QuestionTimeProblem(),stop.QuestionProblemTime(),
                              stop.ProblemQuestion(),stop.TimeProblemQuestion(),stop.ProblemTimeQuestion()]
        
class WillCauseMeAcneTopLevel(Expander):
    
    def __init__(self):
        
        self.all_templates = [acne.WillXMakeAcneWorse(), acne.WillXMakeAcneGetWorse(), acne.WillXCauseBreakOut(), acne.WillAcneGetWorse(), acne.WillAcneGetWorse2(), acne.WillIBreakOut(),
                             acne.WillMySonBreakOut(), acne.IWasPrescribed(), acne.MySonWasPrescribed(), acne.TheDoctorPrescribed(), acne.ITakeWillGetWorse(), acne.MySonTakesGetWorse(),
                             acne.IWasPrescribedBreakOut(),acne.MySonWasPrescribedBreakOut(),acne.TheDoctorPrescribedBreakOut(),acne.ITakeWillGetWorseBreakOut(),
                             acne.MySonTakesGetWorseBreakOut()]