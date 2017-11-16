#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:16:06 2017

@author: alexanderwahl
"""

from Baseclasses import Lexicalizer

class BlankLex(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = []
        
class Weeks(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["weeks"]
        
class SinceTimeLex(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["since last week","since last month","since yesterday"]
        
class Ago(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["ago"]
        
class Days(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["days"]

class OneTwoThreeFour(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["one","two","three","four"]
        
class OneThroughTen(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["one","two","three","four","five","six","seven","eight","nine","ten"]

class CanShouldShall(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["can","should","shall"]
        
class ToBe(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["to be"]
        
class ObjectNonthird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["me","us"]
        
class Was(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["was"]
        
class ShouldNeedWant(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["should","need to","want to"]
        
class WantNeed(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["want","need"]
        
class StartedBeganIs(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["started","began","is","has been"]
        
class BreakOut(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["break out"]
        
class StartedBeganHaveBeen(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["started","began","have been"]
        
class SafeDangerous(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["safe","dangerous","a problem","risky"]
        
class IsIt(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Is it"]
        
class ItIs(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["it is"]

class The(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["the"]
        
class DoctorNurse(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["doctor","nurse"]
        
class Do(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["do"]
        
class Does(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Does"]

class Think(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["think"]
        
class RecordHistory(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["record", "history", "background", "credentials"]
        
class Of(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["of"]

class PracticingMedicine(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["when did they start practicing medicine", "how long have they been practicing medicine",
                          "how long have they been a doctor", "when did they become a doctor",
                          "when did they get their license","how long have they had their license"]
        
class Thinks(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["thinks"]
        
class What(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["What"]
        
class How(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["How"]
        
class Proceed(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["proceed"]
        
class IfWhether(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["if","whether"]
        
class WonderingWorried(Lexicalizer):
    
    def __init__(self):
        
        self.all_words= ["wondering","worried","concerned","curious","considering"]
        
class IsMakingIsCausing(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["is making","is causing","causes","makes","caused","made","has caused","has made"]
        
class MakeCause(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["make","cause"]
        
class IamWeare(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["I am","We are"]
        
class ContinueStopGerund(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["continue", "discontinue", "keep", "stop", "go on"]
        
class StopDiscontinue(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["stop", "discontinue"]
        
class TakingApplyingUsing(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["taking","applying","using"]
        
class TakeApplyUse(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["take","apply","use"]
        
class Skin(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["skin"]
        
class ItchIrritated(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["itch","itchy","scratch","scratchy","irritated","swollen","red","sensitive","inflamed","painful",
                          "swell","dry","peel","a rash"]
        
        

class IdLikeToKnowMore(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["I", "would", "like", "to","know","more"]

class More(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["more"]
        
class MeMySonLex(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["me", "us", "my son","my daughter","my mom","my dad","my mother","my daughter",
                          "my grandmother","my grandfather","my grandson","my granddaughter","my aunt","my uncle",
                          "my neice","my nephew","my cousin","my husband","my wife","my partner","girlfriend",
                          "my boyfriend","my child","my kid","my friend","my spouse","our son","our daughter",
                          "our mom","our dad","our mother","our daughter", "our grandmother","our grandfather",
                          "our grandson","our granddaughter","our aunt","our uncle",
                          "our neice","our nephew","our cousin","our child","our kid","our friend"]
        
class Info(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["info","details","information","background"]
        
        
class SpeakTalk(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["speak", "talk"]
        

class PolitePreface(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Please","I want you to","I'd like you to","I would like for you to","Can you","Could you","Would you please",
                         "Would you mind"]
        
class CanCouldWould(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Can","Could","Would"]
        
class ByPhone(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["by phone","by cell"]
        
class ByTheDoctor(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["by the doctor","by the nurse"]
        
class Numbers(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["home number","number","cell number"]
        
class AboutCase(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["about a case"]
        
class Your(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["your"]
        
class You(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["you"]
        
class ReturnPolicy(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["return policy","refund policy","policy on returns","policy on refunds"]
        
class ReturnsRefunds(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["returns","refunds"]
        
class Return(Lexicalizer):

    def __init__(self):
        
        self.all_words = ["return"]
        
class Refund(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["refund"]
        
class Back(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["back"]
        
class AllowPermit(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["allow","permit"]
        
class AllowedPermitted(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["allowed","permitted"]
        
class HowMuch(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["How much"]

class Shipping(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["shipping","shipment","delivery","mailing"]
        
class Mail(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["mail","ship","send","deliver"]

class Cost(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["cost"]
        
class Expensive(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["expensive","pricy","cheap","reasonably priced"]
        
class To(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["to"]
        

        
class ComeGethere(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["come", "get here"]
        
class ComesGetshere(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["comes","gets here"]
        
class Get(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["get"]

        
class Gets(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["gets"]
        
class Arrive(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["arrive"]
        
class Arrives(Lexicalizer):
    
    def __init__(self):
        
        self.all_words= ["arrives"]
        
class Contact(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["contact","call","email"]
        
class ContactCallPhone(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["contact","call","phone"]
        
class ObjNonthird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["me","us"]
        
class Hear(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["hear"]
        
class Expect(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["expect"]
        
class IsItPossible(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Is it possible"]
        
class FirstPersonToBeInversion(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["am I","are we"]
        
class FirstPersonToBe(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["I am","we are"]

class Modals(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["can","could","would","should","shall"]

class Worse(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["worse", "bad", "flare up"]
        
class Is(Lexicalizer):
    
    def __init__(self):

        self.all_words = ["is"]
        
class GoingtoGonna(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["going to", "gonna"]

        
class WantsNeeds(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["wants","needs"]
        
class SubjThird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["he","she"]
        
class If(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["if"]


class PossessivesNonthird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["my","our"]
        
class PossessivesThird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["his","her","their"]
        
class PossessivesThirdAll(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["his","her","their","my son's","my daughter's","my mom's","my dad's","my mother's","my daughter's",
                          "my grandmother's","my grandfather's","my grandson's","my granddaughter's","my aunt's","my uncle's",
                          "my neice's","my nephew's","my cousin's","my husband's","my wife's","my partner's","girlfriend's",
                          "my boyfriend's","my child's","my kid's","my friend's","my spouse's","our son's","our daughter's",
                          "our mom's","our dad's","our mother's","our daughter's", "our grandmother's","our grandfather's",
                          "our grandson's","our granddaughter's","our aunt's","our uncle's",
                          "our neice's","our nephew's","our cousin's","our child's","our kid's","our friend's",
                          "my parents'","my children's","my grandchildren's","my grandparents'","my friends'",
                          "our parents'","our children's","our grandchildren's","our grandparents'","our friends'"]

class PossessedNouns(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["my son","my daughter","my mom","my dad","my mother","my daughter",
                          "my grandmother","my grandfather","my grandson","my granddaughter","my aunt","my uncle",
                          "my neice","my nephew","my cousin","my husband","my wife","my partner","girlfriend",
                          "my boyfriend","my child","my kid","my friend","my spouse","our son","our daughter",
                          "our mom","our dad","our mother","our daughter", "our grandmother","our grandfather",
                          "our grandson","our granddaughter","our aunt","our uncle",
                          "our neice","our nephew","our cousin","our child","our kid","our friend"]
        
class When(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["When", "Which day", "On what day"]
        
class HowLongUntil(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["How long until"]
        
class HowLong(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["How long","How much time"]
        
class Tell(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["tell"]
        
class DoesItTakeFor(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["does it take for","will it take for","is it going to take for","is it gonna take for"]
        
class HaveToWaitFor(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["have to wait for"]
        
class WhatIsThe(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["What is the"]
        
class Who(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["who"]
        
class TimeAmountOfTime(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["time","amount of time"]
        
class TakesWillTake(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["takes","will take","is going to take","is gonna take"]

class WillIsGonna(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Will", "Is going to", "Is gonna", "Could", "Can"]
        
class It(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["it"]
        
class For(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["for"]
        
class Are(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Are"]
        
class AuxNonthird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["will","do"]
        
class DoCan(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["do","can"]
        
class Can(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Can"]
        
class DoesCan(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["does","can"]
        
class AuxThird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words= ["will","does"]
        
class Will(Lexicalizer):
    
    def __init__(self):
        
        self.all_words= ["will"]

class WillCap(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["Will"]
        
class SubjNonthird(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["I","we"]
        
        
class SinglePeople(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["mom","dad","son","daughter","spouse","child","grandson","granddaughter",
                          "parent","aunt","uncle","cousin","girlfriend","boyfriend","husband","wife",
                          "grandmother","grandfather","friend","mother","father","neice","nephew","partner","kid"]
        
class PluralPeople(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["parents","children","grandchildren","grandparents","friends"]


class AllPeople(Lexicalizer):
    
    def __init__(self):
        
            self.all_words = ["mom","dad","son","daughter","spouse","child","grandson","granddaughter",
                          "parent","aunt","uncle","cousin","girlfriend","boyfriend","husband","wife",
                          "grandmother","grandfather","friend","mother","father","neice","nephew","partner","kid",
                          "parents","children","grandchildren","grandparents","friends"]

class ReceiveGet(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["receive","get"]
        
class ReceivesGets(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["receives","gets"]
        
class ProductsBasic(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["medicine","prescription","medication"]
        
class Prescribed(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["prescribed", "given"]
        

        
class Products(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["medicine","acne cream","shipment","prescription","betamethasone","Kenalog-10","Betnovate","triamcinolone",
                          "betamethasone","Celestone","hydroquinone","Analpram-HC","Diprosone","urea","Hydroquinone and Sunscreen","salicylic acid",
                          "Diprolene","Bensal HP","Luxiq","Dermarest Psoriasis Skin Treatment","hydrocortisone","pramoxine",
                          "Valisone","X-Viate","benzoic acid","salicylic acid","Beta-Val","clobetasol","Aclaro","Pramosone",
                          "Celestone Soluspan","Bionect","Lustra","Diprolene AF","Salex","Aluvea","Proctofoam HC","silver",
                          "Carmol 20","Epifoam","Resinol","Carmol","Eldoquin","Keralac","Melquin HP","Acnex","Durasal","Alera",
                          "Alphatrex","Atrac-Tain","Betacort","Betamethacot","Kerol","Latrix","Novacort","Olux","sodium hyaluronate",
                          "Clobevate","Clobex","Clodan","Cormax","Cormax Scalp","Del-Beta","Dermovate","DHS Salicylic Acid 3%","Embeline",
                          "Embeline E","Kerafoam","KeralytGel","Nuquin HP","Obagi C Rx System C Clarifying Serum","Olux-E",
                          "Olux","Olux-E Kit","resorcinol","Salvax","Scalpicin Scalp Relief","Skin Lightening Complex","Temovate","Temovate E",
                          "Ureacin-10","Urealac","Aliclen","Analpram E","boric acid","Cerovel","Clear Away Wart Removal System",
                          "Eldopaque","EpiQuin Micro","Gordons Urea","Gormel","Hydro 35","Ionil Plus","Kera-42","Keralyt Shapoo","Kerol AD",
                          "RadiaPlexRx","Salacyn","Salicylic Acid Cleansing Bar","Salkera","Stri-Dex","U40","Umecta","Umecta Mousse",
                          "Umecta PD","Uramaxin","Xclair","Aclaro PD","Acnomel Acne Mask","Adazin","Akurza","Alphaquin HP","AMBI Fade",
                          "Aqua Care","Aquaphilic with Urea","Blanche","Carb-O-Philic 10","CEM-Urea","Complex HQ Plus","DermalZone",
                          "Dermasorb XM","Dr Scholl's Callus Removers","Dr Scholl's Corn Removers","Dr Scholl's Zino Soft Corn Remover","Epimide 50","Esoterica",
                          "Esoterica Daytime","Esoterica Nighttime","Esoterica Sensitive Skin","Exuviance Intense Lightening Complex","Fostex",
                          "Freezeone One Step","Freezone","Freezone Corn Remover","Glytone Clarifying","HC Pram","Hydrisalic","Hydro-Q",
                          "Hydro 40 Foam","Hylafem","Hylase Wound Gel","Hylira","IPM Wound","Keralyt Scalp","Kera Nail","Keratol 45","Lustra-AF",
                          "Lustra-Ultra","Melamin","Melamin-C","Melamix","Melpaque HP","Melquin-3","Mosco Corn and Callus Remover","NeoCeuticals Post-Acne Fade",
                          "NeoStrata HQ Skin Lightening","Neova Complex HQ Plus","Neutrogena Healthy Scalp","Nutraplus","Obagi-C Rx System C-Therapy Night Cream",
                          "Obagi Condition and Enhance","Obagi Skin Lightening Complex","Oxy Face Scrub","P & S","Palmers Skin Success Eventone Fade",
                          "Pramosone E","Propa pH Acne Med Cleansing","R A Acne","RE-U40","Rea Lo 39","Rea Lo 40","Recover Lightening Complex",
                          "Remergent HQ","Remeven","Rinnovi Nail System","Salac","Salitop","Skinprint Cleartone","Stridex Body Focus",
                          "Stridex Maximum Strength","SunVanish Cream","Thera-Sal","U-Kera","Umecta Nail Film","Uramaxin GT","Uramaxin TS	",
                          "URE-K","Urea Nail","Urevaz","Utopic",]

class Conditions(Lexicalizer):

    def __init__(self):
        
        self.all_words = ["Acanthosis Nigricans","Acne","Alopecia","Cutaneous Mastocytosis",
                          "Dermal Necrosis","Dermal Ulcer","Dermatitis","Dermatographism","Dermatologic Lesion",
                          "Dry Skin","Eosinophilic Folliculitis","Facial Wrinkles","Granuloma Annulare","Hemangioma",
                          "Hidradenitis Suppurativa","Hirsutism","Hyperhidrosis","Ichthyosis","Impetigo","Insect Bites",
                          "Intertrigo","Lichen Planus","Lichen Sclerosus","Lichen Simplex Chronicus","Linear IgA Disease",
                          "Manscaping Pain","Melasma","Minor Skin Conditions","Molluscum Contagiosum","Nail Dystrophy",
                          "Necrobiosis Lipoidica Diabeticorum","Paronychia","Pemphigus","Photoaging of the Skin",
                          "Pityriasis rubra pilaris","Pruritus","Psoriasis","Pyoderma Gangrenosum","Seborrheic Dermatitis",
                          "Sjogren-Larsson Syndrome","Skin or Soft Tissue Infection","Skin Rash","Submental Fullness",
                          "Toxic Epidermal Necrolysis","Urticaria","Vitiligo","Warts"]
        
class InTheMailLex(Lexicalizer):
    
    def __init__(self):

        self.all_words = ["in the mail"]
        
class Locations(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["home","house","apartment","condo","office"]
        
class At(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["at"]
        
class ShippingTime(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["shipping time","shipment time","delivery time","mailing time"]
        

class Review(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["review","look over","analyze"]
        
class HearFindOut(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["hear", "find out"]
        
class LearnGetFindOut(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["learn","get","find out"]
        
class Finish(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["finish"]
        
class From(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["from"]
        
class About(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["about"]
        
class Case(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["case","record","file"]
        
class NotSatisfiedWith(Lexicalizer):
    
    def __init__(self):
        
        self.all_words = ["not satisfied with"]