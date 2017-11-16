#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:07:16 2017

@author: alexanderwahl
"""

from Baseclasses import Template
from Baseclasses import Expander
import Lexicalizers as lx
import MinorTemplatesExpanders as ex

###Macro Expanders

class QuestionProblem(Template):
    
    def __init__(self):
        
        self.sequence = [QuestionFirst(),ProblemLater()]
        
class QuestionTimeProblem(Template):
    
    def __init__(self):
        
        self.sequence = [QuestionFirst(),TimeLater(),ProblemLater()]
        
class QuestionProblemTime(Template):
    
    def __init__(self):
        
        self.sequence = [QuestionFirst(),ProblemLater(),TimeLater()]
        
class ProblemQuestion(Template):
    
    def __init__(self):
        
        self.sequence = [ProblemFirst(), QuestionLater()]
        

class TimeProblemQuestion(Template):
    
    def __init__(self):
        
        self.sequence = [TimeFirst(), ProblemLater(), QuestionLater()]
        
class ProblemTimeQuestion(Template):
    
    def __init__(self):
        
        self.sequence = [ProblemFirst(), TimeLater(), QuestionLater()]
        



class QuestionFirst(Expander):
    
    def __init__(self):
        
        self.all_templates = [ShouldIKeepTakingMyMedication(),ShouldIKeepTakingMyMedication2(),ShouldMySonKeepTakingHisMedication(),
                             WonderingIfIShouldKeepTakingMyMedication1(),WonderingIfIShouldKeepTakingMyMedication2(),WonderingIfMySonShouldKeepTakingHisMedication1(),
                             WonderingIfMySonShouldKeepTakingHisMedication2(),WhatCanIDo(),WhatCanMySonDo(),HowShallIProceed(),IsItSafeToKeepUsingThis1(),
                             IsItSafeToKeepUsingThis2(),WonderingIfItIsSafeToContinue1(),WonderingIfItIsSafeToContinue2(),WonderingIfItIsSafeToContinue4(),
                             IWantToStop1(), IWantToStop2(), IWantToStop4(), IThinkIShouldStop1(),IThinkIShouldStop2(),IThinkIShouldStop4(),
                             DoesTheDoctorThinkIShouldStop1(),DoesTheDoctorThinkIShouldStop3()]
        
class ProblemFirst(Expander):
    
    def __init__(self):
        
        self.all_templates = [ThisMedicationIsMakingMySkinItch1(),ThisMedicationIsMakingMySkinItch1(),ThisMedicationIsMakingMySkinItch3(),MySkinStartedPeeling1(),
                              MySkinStartedPeeling3()]
        
class TimeFirst(Expander):
    
    def __init__(self):
        
        self.all_templates = [IStartedTakingThisMedicationFor(),IStartedTakingThisMedicationFor1(),MySonStartedTakingThisMedicationFor1()]
    
class QuestionLater(Expander):
    
    def __init__(self):
        
        self.all_templates = [ShouldHeKeepTakingHisMedication2(),WonderingIfHeShouldKeepTakingMyMedication1(),
                             WhatCanHeDo(),HowShallHeProceed(),IsItSafeToKeepUsingThis4(),WonderingIfItIsSafeToContinue3(),
                             IWantToStop3(),IThinkIShouldStop3(),DoesTheDoctorThinkIShouldStop2(),ShouldIKeepTakingMyMedication2(),
                             WonderingIfIShouldKeepTakingMyMedication2(),WhatCanIDo(),HowShallIProceed(),
                             WonderingIfItIsSafeToContinue2(), IWantToStop2(),IThinkIShouldStop2()]
        
class ProblemLater(Expander):
    
    def __init__(self):
        
        self.all_templates = [ThisMedicationIsMakingMySkinItch1(),ThisMedicationIsMakingMySkinItch2(), MySkinStartedPeeling1(), MySkinStartedPeeling2(),ThisMedicationIsMakingMySkinItch1()]
        
class TimeLater(Expander):
    
    def __init__(self):
        
        self.all_templates = [IStartedTakingThisMedicationFor3(),MySonStartedTakingThisMedicationFor2()]




###Templates

class ShouldIKeepTakingMyMedication(Template):
    
    def __init__(self):
    
        self.sequence = [lx.CanShouldShall(), lx.SubjNonthird(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class ShouldIKeepTakingMyMedication2(Template):
    
    def __init__(self):
    
        self.sequence = [lx.CanShouldShall(), lx.SubjNonthird(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     lx.ProductsBasic()]
        
class ShouldHeKeepTakingHisMedication(Template):
    
    def __init__(self):
    
        self.sequence = [lx.CanShouldShall(), lx.SubjThird(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     ex.ProductsExpander(), ex.OptionalForHisSkin()]
        
class ShouldHeKeepTakingHisMedication2(Template):
    
    def __init__(self):
    
        self.sequence = [lx.CanShouldShall(), lx.SubjThird(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     lx.ProductsBasic()]
        

class ShouldMySonKeepTakingHisMedication(Template):
    
    def __init__(self):
    
        self.sequence = [lx.CanShouldShall(), lx.PossessedNouns(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     ex.ProductsExpander(), ex.OptionalForHisSkin()]
        
class WonderingIfIShouldKeepTakingMyMedication1(Template):
    
    def __init__(self):
    
        self.sequence = [lx.IamWeare(), lx.WonderingWorried(), lx.IfWhether(), lx.SubjNonthird(), lx.CanShouldShall(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class WonderingIfIShouldKeepTakingMyMedication2(Template):
    
    def __init__(self):
    
        self.sequence = [lx.IamWeare(), lx.WonderingWorried(), lx.IfWhether(), lx.SubjNonthird(), lx.CanShouldShall(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     lx.ProductsBasic()]

class WonderingIfHeShouldKeepTakingMyMedication1(Template):
    
    def __init__(self):
    
        self.sequence = [lx.SubjThird(), lx.Is(), lx.WonderingWorried(), lx.IfWhether(), lx.SubjNonthird(), lx.CanShouldShall(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     lx.ProductsBasic()]

class WonderingIfMySonShouldKeepTakingHisMedication1(Template):
    
    def __init__(self):
    
        self.sequence = [lx.PossessedNouns(), lx.Is(), lx.WonderingWorried(), lx.IfWhether(), lx.SubjThird(), lx.CanShouldShall(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class WonderingIfMySonShouldKeepTakingHisMedication2(Template):
    
    def __init__(self):
    
        self.sequence = [lx.PossessedNouns(), lx.Is(), lx.WonderingWorried(), lx.IfWhether(), lx.SubjThird(), lx.CanShouldShall(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     lx.ProductsBasic()] 
        
class WhatCanIDo(Template):

    def __init__(self):
        
        self.sequence = [lx.What(), lx.CanShouldShall(), lx.SubjNonthird(), lx.Do()]
    
class WhatCanHeDo(Template):
    
    def __init__(self):
        
        self.sequence = [lx.What(), lx.CanShouldShall(), lx.SubjThird(), lx.Do()]
    

class WhatCanMySonDo(Template):
        
   def __init__(self):
        
        self.sequence = [lx.What(), lx.CanShouldShall(), lx.PossessedNouns(), lx.Do()]
        
class HowShallIProceed(Template):

    def __init__(self):
        
        self.sequence = [lx.How(), lx.CanShouldShall(), lx.SubjNonthird(), lx.Proceed()]
    
class HowShallHeProceed(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How(), lx.CanShouldShall(), lx.SubjThird(), lx.Proceed()]
    
    
class HowShallMySonProceed(Template):
        
   def __init__(self):
        
        self.sequence = [lx.How(), lx.PossessedNouns(), lx.SubjThird(), lx.Proceed()]
        
class IsItSafeToKeepUsingThis1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsIt(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(),
                         ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class IsItSafeToKeepUsingThis2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsIt(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(),
                         lx.ProductsBasic()]

class IsItSafeToKeepUsingThis3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsIt(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(),
                         ex.ProductsExpander(), ex.OptionalForHisSkin()]
        
class IsItSafeToKeepUsingThis4(Template):
    
    def __init__(self):
        
        self.sequence = [lx.IsIt(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(),
                         lx.ProductsBasic()]

class WonderingIfItIsSafeToContinue1(Template):
    
    def __init__(self):
    
        self.sequence = [lx.IamWeare(), lx.WonderingWorried(), lx.IfWhether(), lx.ItIs(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class WonderingIfItIsSafeToContinue2(Template):
    
    def __init__(self):
    
        self.sequence = [lx.IamWeare(), lx.WonderingWorried(), lx.IfWhether(), lx.ItIs(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                     lx.ProductsBasic()]
        
class WonderingIfItIsSafeToContinue3(Template):
    
    def __init__(self):
    
        self.sequence = [lx.SubjThird(), lx.Is(), lx.WonderingWorried(), lx.IfWhether(), lx.ItIs(), lx.SafeDangerous(), lx.To(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     lx.ProductsBasic()]
        
class WonderingIfItIsSafeToContinue4(Template):
    
    def __init__(self):
    
        self.sequence = [lx.PossessedNouns(), lx.Is(), lx.WonderingWorried(), lx.IfWhether(), lx.ItIs(), lx.SafeDangerous(), lx.ContinueStopGerund(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                     ex.ProductsExpander(), ex.OptionalForHisSkin()] 

class IWantToStop1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.WantNeed(), lx.To(), lx.StopDiscontinue(), lx.PossessivesNonthird(), lx.TakingApplyingUsing(),
                         ex.ProductsExpander(), ex.OptionalForMySkin()]
    
class IWantToStop2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.WantNeed(), lx.To(), lx.StopDiscontinue(), lx.PossessivesNonthird(), lx.TakingApplyingUsing(),
                         lx.ProductsBasic()]
        
class IWantToStop3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjThird(), lx.WantNeed(), lx.To(), lx.StopDiscontinue(), lx.PossessivesThird(), lx.TakingApplyingUsing(),
                         lx.ProductsBasic()]       

class IWantToStop4(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.WantNeed(), lx.To(), lx.StopDiscontinue(), lx.PossessivesThird(), lx.TakingApplyingUsing(),
                         ex.ProductsExpander(), ex.OptionalForHisSkin()] 

class IThinkIShouldStop1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.Think(), lx.SubjNonthird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), lx.TakingApplyingUsing(),
                         ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class IThinkIShouldStop2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.Think(), lx.SubjNonthird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), lx.TakingApplyingUsing(),
                         lx.ProductsBasic()]
        
class IThinkIShouldStop3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjThird(), lx.Thinks(), lx.SubjThird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), lx.TakingApplyingUsing(),
                         lx.ProductsBasic()]       

class IThinkIShouldStop4(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.Thinks(), lx.SubjThird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), 
                         lx.TakingApplyingUsing(), ex.ProductsExpander(), ex.OptionalForHisSkin()]

class DoesTheDoctorThinkIShouldStop1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Does(), lx.The(), lx.DoctorNurse(), lx.Think(), lx.SubjNonthird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), lx.TakingApplyingUsing(),
                         ex.ProductsExpander(), ex.OptionalForMySkin()]
        
class DoesTheDoctorThinkIShouldStop2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Does(), lx.The(), lx.DoctorNurse(), lx.Think(), lx.SubjThird(), lx.ShouldNeedWant(), lx.StopDiscontinue(), lx.TakingApplyingUsing(),
                         lx.ProductsBasic()]       

class DoesTheDoctorThinkIShouldStop3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Does(), lx.The(), lx.DoctorNurse(), lx.Think(), lx.PossessedNouns(), lx.ShouldNeedWant(), lx.StopDiscontinue(), 
                         lx.TakingApplyingUsing(), ex.ProductsExpander(), ex.OptionalForHisSkin()]
        

class ThisMedicationIsMakingMySkinItch1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesNonthird(), ex.ProductsExpander(), lx.IsMakingIsCausing(), lx.PossessivesNonthird(), lx.Skin(),
                          lx.ItchIrritated()]

class ThisMedicationIsMakingMySkinItch2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesThird(), lx.ProductsBasic(), lx.IsMakingIsCausing(), lx.PossessivesThird(), lx.Skin(),
                          lx.ItchIrritated()]

class ThisMedicationIsMakingMySkinItch3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesThirdAll(), ex.ProductsExpander(), lx.IsMakingIsCausing(), lx.PossessivesThird(), lx.Skin(),
                          lx.ItchIrritated()]
        
class MySkinStartedPeeling1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesNonthird(), lx.Skin(), lx.StartedBeganIs(), lx.ToBe(), lx.ItchIrritated()]

class MySkinStartedPeeling2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesThird(), lx.Skin(), lx.StartedBeganIs(), lx.ToBe(), lx.ItchIrritated()]

class MySkinStartedPeeling3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessivesThirdAll(), lx.Skin(), lx.StartedBeganIs(), lx.ToBe(), lx.ItchIrritated()]
        

class IStartedTakingThisMedicationFor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.StartedBeganHaveBeen(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                          ex.ProductsExpander(), ex.TimeExpander()]

class IStartedTakingThisMedicationFor1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.StartedBeganHaveBeen(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                          lx.ProductsBasic(), ex.TimeExpander()]
        
class IStartedTakingThisMedicationFor3(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SubjNonthird(), lx.StartedBeganHaveBeen(), lx.TakingApplyingUsing(), lx.PossessivesNonthird(), 
                          lx.ProductsBasic()]

class MySonStartedTakingThisMedicationFor1(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.StartedBeganHaveBeen(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                          ex.ProductsExpander(), ex.TimeExpander()]

class MySonStartedTakingThisMedicationFor2(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PossessedNouns(), lx.StartedBeganHaveBeen(), lx.TakingApplyingUsing(), lx.PossessivesThird(), 
                          lx.ProductsBasic()]