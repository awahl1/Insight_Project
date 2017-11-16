#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:46:52 2017

@author: alexanderwahl
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:14:18 2017

@author: alexanderwahl
"""

from Baseclasses import Template
from Baseclasses import Expander

import Lexicalizers as lx

####Minor Templates

class ForXWeeks(Template):
    
    def __init__(self):
        
        self.sequence = [lx.For(), lx.OneTwoThreeFour(), lx.Weeks()]
        
class ForXDays(Template):
    
    def __init__(self):
        
        self.sequence = [lx.For(), lx.OneThroughTen(), lx.Days()]
        
class SinceTime(Template):
    
    def __init__(self):
        
        self.sequence = [lx.SinceTimeLex()]
        
class WhenTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.When()]
        
class TheRecordOf(Template):
    
    def __init__(self):
        
        self.sequence = [lx.The(), lx.RecordHistory(), lx.Of()]
        
class XDaysAgo(Template):
    
    def __init__(self):
        
        self.sequence = [lx.OneThroughTen(), lx.Days(), lx.Ago()]
        
class XWeeksAgo(Template):
    
    def __init__(self):
        
        self.sequence = [lx.OneTwoThreeFour(), lx.Weeks(), lx.Ago()]



class ForMySkinTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.For(), lx.PossessivesNonthird(), lx.Skin()]
        
class ForHisSkinTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.For(), lx.PossessivesThird(), lx.Skin()]

class DoesItTakeForTheDoctor(Template):
    
    def __init__(self):
        
        self.sequence = [lx.DoesItTakeFor(), lx.The(), lx.DoctorNurse(), lx.Review()]
        
class DoesItTakeToReview(Template):
    
    def __init__(self):
        
        self.sequence = [lx.DoesItTakeFor(), lx.Review()]
        
class DoesTheDoctorNeed(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Does(), lx.The(), lx.DoctorNurse(), lx.WantNeed(), lx.To(), lx.Review()]

class ArriveNonthirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Arrive(), OptionalObliquesNonthird()]

class ArriveThirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Arrive(), OptionalObliquesThird()]
        
class ComeGethereNonthirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.ComeGethere(), OptionalObliquesNonthirdTo()]

class ComeGethereThirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.ComeGethere(), OptionalObliquesThirdTo()]
        
class GetToMyApartmentNonthirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Get(), GetComplementNonthird()]

class GetToMyApartmentThirdTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Get(), GetComplementThird()]



class InTheMailTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.InTheMailLex()]

class AtLocativesNonthird(Template):
    
    def __init__(self):
        
        self.sequence = [lx.At(), lx.PossessivesNonthird(), lx.Locations()]
        
class AtLocativesThird(Template):
    
    def __init__(self):
        
        self.sequence = [lx.At(), lx.PossessivesThirdAll(), lx.Locations()]
        
class ToLocativesNonthird(Template):
    
    def __init__(self):
        
        self.sequence = [lx.To(), lx.PossessivesNonthird(), lx.Locations()]
        
class ToLocativesThird(Template):
    
    def __init__(self):
        
        self.sequence = [lx.To(), lx.PossessivesThirdAll(), lx.Locations()]
        
class ProductsSingleTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Products()]
        
class ProductsMWETemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.ProductsBasic(), lx.For(), lx.Conditions()]
        
class MeMySonTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.MeMySonLex()]

class BlankTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.BlankLex()]

class HowTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.How()]
        
class AboutProductsTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.About(), lx.Products()]
        
class AboutConditionsTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.About(), lx.Conditions()]
        
class AboutACaseTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.AboutCase()]
        
class WhoPhraseTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.Who(), lx.Will(), lx.Review(), lx.Case()]
        
class ByTheDoctorTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.ByTheDoctor()]
        
class PracticingMedicineTemplate(Template):
    
    def __init__(self):
        
        self.sequence = [lx.PracticingMedicine()]
        


###Minor Expanders
        
class OptionalObliquesNonthird(Expander):
    
    def __init__(self):
        
        self.all_templates = [InTheMailTemplate(), AtLocativesNonthird(), BlankTemplate()]
        
class OptionalObliquesThird(Expander):
    
    def __init__(self):
        
        self.all_templates = [InTheMailTemplate(), AtLocativesThird(), BlankTemplate()]
        
class OptionalObliquesNonthirdTo(Expander):
    
    def __init__(self):
        
        self.all_templates = [InTheMailTemplate(), ToLocativesNonthird(), BlankTemplate()]
        
class OptionalObliquesThirdTo(Expander):
    
    def __init__(self):
        
        self.all_templates = [InTheMailTemplate(), ToLocativesThird(), BlankTemplate()]
        
class OptionalHow(Expander):
    
    def __init__(self):
        
        self.all_templates = [HowTemplate(), BlankTemplate()]
        
class OptionalAboutPhrase(Expander):
    
    def __init__(self):
        
        self.all_templates = [AboutProductsTemplate(), AboutConditionsTemplate(), AboutACaseTemplate(), BlankTemplate()]

class OptionalTheRecordOf(Expander):
    
    def __init__(self):
        
        self.all_templates = [TheRecordOf(), BlankTemplate()]

class ArrivalPhraseThird(Expander):
    
    def __init__(self):
    
        self.all_templates = [ArriveThirdTemplate(), ComeGethereThirdTemplate(), GetToMyApartmentThirdTemplate()]
    
class ArrivalPhraseNonthird(Expander):
    
    def __init__(self):
    
        self.all_templates = [ArriveNonthirdTemplate(), ComeGethereNonthirdTemplate(), GetToMyApartmentNonthirdTemplate()]
        
class GetComplementNonthird(Expander):
    
    def __init__(self):
        
        self.all_templates = [ToLocativesNonthird()]
        
class GetComplementThird(Expander):
    
    def __init__(self):
        
        self.all_templates = [ToLocativesThird()]
        
class ProductsExpander(Expander):
    
    def __init__(self):
        
        self.all_templates = [ProductsSingleTemplate(), ProductsMWETemplate()]
        
class HowLongReview(Expander):
    
    def __init__(self):
        
        self.all_templates = [DoesItTakeForTheDoctor(), DoesItTakeToReview(), DoesTheDoctorNeed()]
        
class OptionalWhoPhrase(Expander):
    
    def __init__(self):
        
        self.all_templates = [WhoPhraseTemplate(), BlankTemplate()]
        
class OptionalForMySkin(Expander):
    
    def __init__(self):
        
        self.all_templates = [ForMySkinTemplate(), BlankTemplate()]
        
class MeMySon(Expander):
    
    def __init__(self):
        
        self.all_templates = [MeMySonTemplate()]
        
class OptionalForHisSkin(Expander):
    
    def __init__(self):
        
        self.all_templates = [ForHisSkinTemplate(), BlankTemplate()]
        
class OptionalPracticingMedicine(Expander):
    
    def __init__(self):
        
        self.all_templates = [PracticingMedicineTemplate(), BlankTemplate()]
        
class OptionalWhen(Expander):
    
    def __init__(self):
        
        self.all_templates = [WhenTemplate(), BlankTemplate()]
        
class TimeExpander(Expander):
    
    def __init__(self):
        
        self.all_templates = [ForXWeeks(), ForXDays(), SinceTime(), XDaysAgo(), XWeeksAgo()]
        
class OptionalByTheDoctor(Expander):
    
    def __init__(self):
        
        self.all_templates = [ByTheDoctorTemplate(), BlankTemplate()]