#!/usr/bin/env python
# coding: utf-8

# In[528]:


import random
import copy
import json as js
#from prettytable import PrettyTable
occupied_teacher=[]
occupied_rooms=[]
occupied_labs=[]
occupied_tutorials=[]

import csv
import ast

# open the file in universal line ending mode 
with open('rooms.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  rooms = {}
  for row in reader:
    for header, value in row.items():
      try:
        rooms[header].append(value)
      except KeyError:
        rooms[header] = [value]
        
for i,j in rooms.items():
    for k in j:
        if k=='':
            j.remove('')
            
remaining_rooms=copy.deepcopy(rooms)

# open the file in universal line ending mode 
with open('depts.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  depts = {}
  for row in reader:
    for header, value in row.items():
      try:
        depts[header].append(value)
      except KeyError:
        depts[header] = [value]

for i,j in depts.items():
    l=[]
    for k in j:
        #print(k)
        l.append(ast.literal_eval(k))
        #j.remove(k)
    #print(l)
    j=copy.deepcopy(l)
    #print(j)
    depts[i]=j
        
remaining_tutorials=copy.deepcopy(depts)


# open the file in universal line ending mode 
with open('teacher_code.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  teacher_code = {}
  for row in reader:
    for header, value in row.items():
      try:
        teacher_code[header].append(value)
      except KeyError:
        teacher_code[header] = [value]
        
for i in range(5):
    for i,j in teacher_code.items():
        for k in j:
            if k=='':
                j.remove('')
        
        
remaining_teacher=[]
for i in teacher_code.keys():
    remaining_teacher.append(i)

# open the file in universal line ending mode 
with open('lab_code.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  lab_code = {}
  for row in reader:
    for header, value in row.items():
      try:
        lab_code[header].append(value)
      except KeyError:
        lab_code[header] = [value]
        
for i in range(5):
    for i,j in lab_code.items():
        for k in j:
            if k=='':
                j.remove('')
        
remaining_labs=[]
for i in lab_code.keys():
    remaining_labs.append(i)

"""
dp = open("lab_code.db","r")
lab_code=js.load(dp)
    #print(data)
dp.close()
lab_code={'MP':['MED217'],'MM':['MED218'],'FM':['MED219'],'EM':['MED216','EED317'],'HY':['CED210'],'EG':['CED219']          ,'SA':['CED217'],'SU':['CED218'],'DE':['CSD219','ECD218','EED218','CSDD219','ECDD218'],'CC2':['CSD217','CSD216','CSDD217','CSDD216']          ,'mP':['CSD218','ECD319','CSDD218','ECDD319'],'ESTOP1':['ECD219','ECD210','ECDD219','ECDD210'],'AE':['ECD217','ECDD217'],'MS':['MSD218','MSD219']          ,'NA':['EED217'],'EE':['EED219','EED210'],'IIIT':['CSD216','CSD217','CSDD216','CSDD217'],'CHF':['CHD217'],'MUO':['CHD218']          ,'CHC':['CHD219','CHD416'],'HT':['MED317'],'Mac':['MED318'],'DM':['MED319'],'RS':['CED317']          ,'MED':['CED319','CHD319'],'GE':['CED318'],'RECS':['CSD317','CSD318','CSDD317','CSDD318']          ,'CSTOP1':['CSD319','CSD415','CSDD319','CSDD415']          ,'ED':['ECD318','ECDD318'],'DC':['ECD317','ECDD317'],'Htr':['MSD319'],'NM':['MSD318'],'PS':['EED318'],'Tra':['EED319']          ,'CHE':['CHD317'],'PDC':['CHD318']          ,'RAC':['MED417'],'TM':['MED418'],'DRG':['CED416','EED417'],'EE':['CED417'],'CSTOP2':['CSD416','CSDD416']          ,'OC':['ECD417','ECDD417'],'IE':['ECD418','ECDD418'],'ECSEM':['ECD419','ECDD419'],'Sim':['EED418'],'CHed':['CHD417'],'CH418':['CHD419']}
dp = open("teacher_code.db","r")
teacher_code=js.load(dp)
    #print(data)
dp.close()
teacher_code={'PVY':['MED213'],'RJS':['MED214'],'CHA':['MED212'],'YDS':['MES211'],'PSI':['MED217'],              'SID':['MED218','MED311'],'ANO':['MED219','MED215'],'RJN':['MED216'],'SUK':['CES211'],              'UKP':['CED212','CED217'],'ASA':['CED213','CED218'],'RSB':['CED214','CED219'],'JTR':['CED215'],              'RPA':['CED216'],'AMK':['CED210','ECD214','ECD217','CED314','CED318']              ,'RAJ':['CSD211','CSDD211'],'JYO':['CSD212','CSD216','CSDD212','CSDD216']              ,'NAV':['CSD213','CSD217','CSDD213','CSDD217'],'VIK':['CSD214','CSD218','CSDD214','CSDD218'],              'GKH':['CSD215','ECD218','CSDD215','ECDD218'],'BUM':['CSD217','CS713','CSDD217']              ,'SML':['CSD218','CSD214','CS600','CSDD218','CSDD214'],              'MRB':['CSD219','ECD215','CSDD219','ECDD215'],'PKS':['ECS211','ECSD211']              ,'RHD':['ECD212','ECD217','ECDD212','ECDD217'],'VKS':['ECD213','ECD219','ECDD213','ECDD219'],              'CSP':['ECD214','ECD313','ECDD214','ECDD313'],'RAK':['ECD215','EC609','ECDD215','ECD609'],'NGU':['ECD216','ECD210','ECDD216','ECDD210'],              'PUN':['ECD218','CSD215','ECD311','CSDD215','ECDD218','ECDD311']              ,'MA2':['MSS211'],'MS2':['MSD212','MSD218','MSD315'],'RMA':['MSD213','MSD219'],'MS3':['MSD214','MSD216'],              'MS4':['MSD215','MSD219','MSD311','MSO317'],'MS5':['MSD216'],'PKK':['MSD217','MSD312'],              'MA1':['EES211'],'AYA':['EED212','EED217','CHD211'],'ABA':['EED213','EEO316','EED319'],'RNS':['EED214'],              'MSH':['EED215','EED219','EED314'],'EE2':['EED216','EED317','EED417'],'SKU':['EED218','ECE414a','EC675','ECED414a','ECD675'],              'TGA':['CSS210','CSSD210'],'TCH':['CSD219','ECD213','CSDD219','ECDD213']              ,'ASI':['ECS211','ECSD211'],'MSA':['ECD212','ECD419','ECDD212','ECDD419']              ,'PTK':['ECD219','ECD311','ECD418','ECDD219','ECDD311','ECDD418'],'SHI':['ECD210','ECDD210'],              'RAD':['CHD212','CHD217','CHD412'],'KAT':['CHD213','CHD317'],'SMA':['CHD214','CHD314'],'MS1':['CHD215'],              'AKG':['CHD216','CHE415a','CHD416','CHD419'],'LEE':['CHD218','CHD311','CHE414a'],              'TCK':['CHD219','CHD411','CHO316'],'VAR':['MED312','MED317'],'MKS':['MED313','MEE414b'],              'SND':['MED314','MED319'],'RIV':['MED315','MEE415a'],'DAK':['MED318','MEE415b']              ,'NRA':['CED311'],'CPR':['CED312','CED317'],'RAV':['CED313'],'VKB':['CED315'],'AKR':['CED319','CED411'],              'DPM':['CSD311','CSD317','CSDD311','CSDD317'],'JCH':['CSD312','CSDD312']              ,'NCH':['CSD313','CSD318','CSDD313','CSDD318'],'NPS':['CSD314','CSD319','CSDD314','CSDD319'],              'KKU':['CSD315','CSDD315'],'ASH':['ECD312','ECD317','ECDD312','ECDD317'],'ASO':['ECD313','ECDD313']              ,'ARA':['ECD314','ECD318','ECDD314','ECDD318'],'HHA':['ECD315','ECDD315'],              'GAG':['ECD319','EED313','ECDD319']              ,'MS6':['MSD314'],'VVE':['MSD313'],'RVK':['MSD318'],'OPR':['EED311'],'ZHU':['EED312'],'AKA':['EED313']              ,'JKA':['EED318'],'VEE':['EED319','ECD315'],'SCH':['CSD313','CSDD318','CSD313','CSDD318']              ,'PUS':['CSD315','CSDD315'],'TAB':['CSD317','CSDD317'],              'PUK':['CSD319','CSD413','CSDD319','CSDD413'],'DSY':['ECD312','ECD317','ECDD312','ECDD317'],'RCH':['ECD314','ECD318','ECDD314','ECDD318']              ,'TPA':['CHD312','CHD413','CHD417'],'AGA':['CHD313','CHD318','CHE414c'],'SSA':['CHD315','CHD319'],              'PKU':['MED411'],'SSH':['MED413'],'DSH':['MED412','MED418'],'AKC':['MEE414a'],'DDA':['MED417'],              'DHA':['CED412'],'VSD':['CED413'],'SBI':['CEE414a'],'RKD':['CEE415b'],'SNL':['CED417'],              'KNS':['CED416'],'ACF':['CED418']              ,'PSH':['CSD411','CSDD411'],'RKR':['CSD412','CSDD412'],'PCH':['CSD414','CSD416','CSDD414','CSDD416']              ,'LKC':['CSD415','CSD410','CSDD415','CSDD410'],              'NTR':['CSD416','CSD412','CSDD416','CSDD412'],'BSU':['CSD417','CSDD417'],'YGU':['ECH411','ECHD411'],'NVE':['ECD412','ECD417','ECDD412','ECDD417'],              'VKA':['ECD413','ECD418','ECDD413','ECDD418'],'VPS':['ECE415a','ECD417','ECED415a','ECDD417'],'RKJ':['EED411'],'BBS':['EED412'],'ACH':['EED413'],              'YRS':['EEE414'],'RAN':['EEE415']              ,'NDO':['EED418'],'DYA':['CS716'],'APU':['CSD411'],'IVA':['CSD415'],'ADW':['EC677','ECO316a','ECD677'],              'MAN':['ECH411','ECHD411'],'RAM':['ECD419','ECDD419'],'T1':['CES111','ECS111','ECSD111','MES111','MSS111','CHS111','CSS111'],              'T2':['CES112','MES112','MES116','MSS113','CHS112','CHS116'],              'T3':['CEH113','CEH117','MEH113','MEH117','CHH113','CHH117'],'T4':['CED114','CED118'],              'T5':['CED115','MED114','CHD115'],'T6':['ECS112','ECS116','MSS112','MSS117','CSS112','CSD117','ECSD112','ECSD116'],              'T7':['ECS113','ECSD113'],'T8':['ECD114','ECD117','ECDD114','ECDD117'],'T9':['ECD115','MED115','ECDD115'],'T10':['ECD118','ECDD118']              ,'T11':['MED118'],'T12':['MSD114','MSD118','CSD113','CSD118','CSDD113','CSDD118'],'T13':['MSH116','CSH116'],'T14':['MSH119'],              'T15':['CHD114'],'T16':['EED113'],'T17':[],'T18':[],'T19':[],'T20':[],'T21':[],'T22':[],'T23':[],              'T24':['CSD114','CSDD114'],'T25':['CSD115','CSD119','CSDD115','CSDD119'],'SRC':['MEO316a']              ,'SKG':['MEO316b'],'SMJ':['CEO316'],'SUS':['EEO316']}
#optional_courses3=[]
dp = open("remaining_labs.db","r")
remaining_labs=js.load(dp)
    #print(data)
dp.close()
dp = open("remaining_tutorials.db","r")
remaining_tutorials=js.load(dp)
    #print(data)
dp.close()

remaining_labs=['MP','MM','FM','EM','HY','EG','SA','SU','DE','CC2','mP','ESTOP1','AE','MS','NA','EE','IIIT','CHF','MUO'               ,'CHC','HT','Mac','DM','RS','MED','GE','RECS','CSTOP1','ED','DC','Htr','NM','PS','Tra','CHE','PDC'               ,'RAC','TM','DRG','EE','CSTOP2','OC','IE','ECSEM','Sim','CHed','CH418']
remaining_tutorials={'CS1':[['CSS111','CSS112','CSD113','CSD114','CSD115','CSH116'],['CSD117','CSD118','CSD119']]       ,'EE1':[['EED111','EED112','EED113','EED114','EED115','EED116'],['EED118','EED117']]      ,'CH1':[['CHS111','CHS112','CHH113','CHD114','CHD115'],['CHS116','CHH117']]      ,'MS1':[['MSS111','MSS112','MSS113','MSD114','MSD115','MSH116','MSH119'],['MSS117','MSD118']]      ,'ME1':[['MES111','MES112','MEH113','MED114','MED115'],['MES116','MEH117','MED118']]      ,'EC1':[['ECS111','ECS112','ECS113','ECD114','ECD115'],['ECS116','ECD117','ECD118']]      ,'CE1':[['CES111','CES112','CEH113','CED114','CED115'],['CEH117','CED118']]      ,'ME2':[['MES211','MED212','MED213','MED214','MED215'],['MED216','MED217','MED218','MED219']]      ,'CE2':[['CES211','CED212','CED213','CED214','CED215','CED216'],['CED210','CED217','CED218','CED219']]      ,'CS2':[['CSD211','CSD212','CSD213','CSD214','CSD215'],['CSD216','CSD217','CSD218','CSD219']]      ,'EC2':[['ECS211','ECD212','ECD213','ECD214','ECD215','ECD216'],['ECD217','ECD218','ECD219','ECD210']]      ,'MS2':[['MSS211','MSD212','MSD213','MSD214','MSD215','MSD216','MSD217'],['MSD218','MSD219']]      ,'EE2':[['EES211','EED212','EED213','EED214','EED215','EED216'],['EED217','EED218','EED219','EED210']]      ,'CD2':[['CSSD210','CSDD211','CSDD212','CSDD213','CSDD214','CSDD215'],['CSDD216','CSDD217','CSDD218','CSDD219']]      ,'ED2':[['ECSD211','ECDD212','ECDD213','ECDD214','ECDD215','ECDD216'],['ECDD217','ECDD218','ECDD219','ECDD210']]      ,'CH2':[['CHD211','CHD212','CHD213','CHD214','CHD215','CHD216'],['CHD217','CHD218','CHD219']]      ,'ME3':[['MED311','MED312','MED313','MED314','MED315'],['MED317','MED318','MED319']]      ,'CE3':[['CED311','CED312','CED313','CED314','CED315'],['CED317','CED318','CED319']]      ,'CS3':[['CSD311','CSD312','CSD313','CSD314','CSD315'],['CSD317','CSD318','CSD319']]      ,'EC3':[['ECD311','ECD312','ECD313','ECD314','ECD315'],['ECD317','ECD318','ECD319']]      ,'MS3':[['MSD311','MSD312','MSD313','MSD314','MSD315','MSD316'],['MSD318','MSD319']]      ,'EE3':[['EED311','EED312','EED313','EED314','EED315'],['EED317','EED318','EED319']]      ,'CD3':[['CSDD311','CSDD312','CSDD313','CSDD314','CSDD315'],['CSDD317','CSDD318','CSDD319']]      ,'ED3':[['ECDD311','ECDD312','ECDD313','ECDD314','ECDD315'],['ECDD317','ECDD318','ECDD319']]      ,'CH3':[['CHD311','CHD312','CHD313','CHD314','CHD315'],['CHD317','CHD318','CHD319']]      ,'ME4':[['MED411','MED412','MED413','MEE414a','MEE414b','MEE415a','MEE415b'],['MED417','MED418']]      ,'CE4':[['CED411','CED412','CED413','CED414a','CED415b'],['CED416','CED417','CED418']]      ,'CS4':[['CSD410','CSD411','CSD412','CSD413','CSD414'],['CSD415','CSD416','CSD417']]      ,'EC4':[['ECH411','ECD412','ECD413','ECE414a','ECE415a'],['ECD417','ECD418','ECD419']]      ,'EE4':[['EED411','EED412','EED413','EED414','EED415'],['EED417','EED418']]      ,'CD4':[['CSD713','CSD716','CSD600','CSDD410','CSDD411','CSDD412'],['CSDD415','CSDD416']]      ,'ED4':[['ECD677','ECD609','ECD675','ECHD411','ECDD412','ECDD413'],['ECDD417','ECDD418','ECDD419']]      ,'CH4':[['CHD411','CHD412','CHD413','CHE414a','CHE414c','CHE415a'],['CHD416','CHD417','CHD418','CHD419']]}
dp = open("remaining_teacher.db","r")
remaining_teacher=js.load(dp)
    #print(data)
dp.close()
remaining_teacher=['PVY','RJS','CHA','YDS','PSI','SID','ANO','RJN','SUK','UKP','ASA','RSB','JTR','RPA','AMK'                  ,'RAJ','JYO','NAV','VIK','GKH','BUM','SML','MRB','PKS','RHD','VKS','CSP','RAK','NGU','PUN'                  ,'MA2','MS2','RMA','MS3','MS4','MS5','PKK','MA1','AYA','ABA','RNS','MSH','EE2','SKU','TGA','TCH'                  ,'ASI','MSA','PTK','SHI','RAD','KAT','SMA','MS1','AKG','LEE','TCK','VAR','MKS','SND','RIV','DAK'                  ,'NRA','CPR','RAV','VKB','AKR','DPM','JCH','NCH','NPS','KKU','ASH','ASO','ARA','HHA','GAG'                  ,'MS6','VVE','RVK','OPR','ZHU','AKA','JKA','VEE','SCH','PUS','TAB','PUK','DSY','RCH'                  ,'TPA','AGA','SSA','PKU','SSH','DSH','AKC','DDA','DHA','VSD','SBI','RKD','SNL','KNS','ACF'                  ,'PSH','RKR','PCH','LKC','NTR','BSU','YGU','NVE','VKA','VPS','RKJ','BBS','ACH','YRS','RAN'                  ,'NDO','DYA','APU','IVA','ADW','MAN','RAM','T1','T2','T3','T4','T5','T6','T7','T8','T9','T10'                  ,'T11','T12','T13','T14','T15','T16','T17','T18','T19','T20','T21','T22','T23','T24','T25','SRC'                  ,'SKG','SMJ','SUS']
dp = open("rooms.db","r")
rooms=js.load(dp)
    #print(data)
dp.close()
rooms={'B':['B1','B2','B3','B4','B5','B6'],'G':['G1','G2','G3','G4','G5','G6']                ,'F':['F1','F2','F3','F4','F5','F6'],'S':['S1','S2','S3','S4','S5','S6']}
dp = open("remaining_rooms.db","r")
remaining_rooms=js.load(dp)
    #print(data)
dp.close()
remaining_rooms={'B':['B1','B2','B3','B4','B5','B6'],'G':['G1','G2','G3','G4','G5','G6']                ,'F':['F1','F2','F3','F4','F5','F6'],'S':['S1','S2','S3','S4','S5','S6']}
dp = open("depts.db","r")
#depts=js.load(dp)
    #print(data)
#dp.close()
depts={'CS1':[['CSS111','CSS112','CSD113','CSD114','CSD115','CSH116'],['CSD117','CSD118','CSD119']]       ,'EE1':[['EED111','EED112','EED113','EED114','EED115','EED116'],['EED118','EED117']]      ,'CH1':[['CHS111','CHS112','CHH113','CHD114','CHD115'],['CHS116','CHH117']]      ,'MS1':[['MSS111','MSS112','MSS113','MSD114','MSD115','MSH116','MSH119'],['MSS117','MSD118']]      ,'ME1':[['MES111','MES112','MEH113','MED114','MED115'],['MES116','MEH117','MED118']]      ,'EC1':[['ECS111','ECS112','ECS113','ECD114','ECD115'],['ECS116','ECD117','ECD118']]      ,'CE1':[['CES111','CES112','CEH113','CED114','CED115'],['CEH117','CED118']]      ,'ME2':[['MES211','MED212','MED213','MED214','MED215'],['MED216','MED217','MED218','MED219']]      ,'CE2':[['CES211','CED212','CED213','CED214','CED215','CED216'],['CED210','CED217','CED218','CED219']]      ,'CS2':[['CSD211','CSD212','CSD213','CSD214','CSD215'],['CSD216','CSD217','CSD218','CSD219']]      ,'EC2':[['ECS211','ECD212','ECD213','ECD214','ECD215','ECD216'],['ECD217','ECD218','ECD219','ECD210']]      ,'MS2':[['MSS211','MSD212','MSD213','MSD214','MSD215','MSD216','MSD217'],['MSD218','MSD219']]      ,'EE2':[['EES211','EED212','EED213','EED214','EED215','EED216'],['EED217','EED218','EED219','EED210']]      ,'CD2':[['CSSD210','CSDD211','CSDD212','CSDD213','CSDD214','CSDD215'],['CSDD216','CSDD217','CSDD218','CSDD219']]      ,'ED2':[['ECSD211','ECDD212','ECDD213','ECDD214','ECDD215','ECDD216'],['ECDD217','ECDD218','ECDD219','ECDD210']]      ,'CH2':[['CHD211','CHD212','CHD213','CHD214','CHD215','CHD216'],['CHD217','CHD218','CHD219']]      ,'ME3':[['MED311','MED312','MED313','MED314','MED315'],['MED317','MED318','MED319']]      ,'CE3':[['CED311','CED312','CED313','CED314','CED315'],['CED317','CED318','CED319']]      ,'CS3':[['CSD311','CSD312','CSD313','CSD314','CSD315'],['CSD317','CSD318','CSD319']]      ,'EC3':[['ECD311','ECD312','ECD313','ECD314','ECD315'],['ECD317','ECD318','ECD319']]      ,'MS3':[['MSD311','MSD312','MSD313','MSD314','MSD315','MSD316'],['MSD318','MSD319']]      ,'EE3':[['EED311','EED312','EED313','EED314','EED315'],['EED317','EED318','EED319']]      ,'CD3':[['CSDD311','CSDD312','CSDD313','CSDD314','CSDD315'],['CSDD317','CSDD318','CSDD319']]      ,'ED3':[['ECDD311','ECDD312','ECDD313','ECDD314','ECDD315'],['ECDD317','ECDD318','ECDD319']]      ,'CH3':[['CHD311','CHD312','CHD313','CHD314','CHD315'],['CHD317','CHD318','CHD319']]      ,'ME4':[['MED411','MED412','MED413','MEE414a','MEE414b','MEE415a','MEE415b'],['MED417','MED418']]      ,'CE4':[['CED411','CED412','CED413','CED414a','CED415b'],['CED416','CED417','CED418']]      ,'CS4':[['CSD410','CSD411','CSD412','CSD413','CSD414'],['CSD415','CSD416','CSD417']]      ,'EC4':[['ECH411','ECD412','ECD413','ECE414a','ECE415a'],['ECD417','ECD418','ECD419']]      ,'EE4':[['EED411','EED412','EED413','EED414','EED415'],['EED417','EED418']]      ,'CD4':[['CSD713','CSD716','CSD600','CSDD410','CSDD411','CSDD412'],['CSDD415','CSDD416']]      ,'ED4':[['ECD677','ECD609','ECD675','ECHD411','ECDD412','ECDD413'],['ECDD417','ECDD418','ECDD419']]      ,'CH4':[['CHD411','CHD412','CHD413','CHE414a','CHE414c','CHE415a'],['CHD416','CHD417','CHD418','CHD419']]}
#t_cs1=0

"""


#make_time_table()


# In[529]:


__c=0
def make_time_table():
    global t_time,occupied_teacher,lab_occupied_teachers,occupied_labs,remaining_rooms,rooms,t_day,_count,__count,__c
    while(t_day<5):
        _count=0
        t_time=0
        while(t_time<10 and(t_time<4 or t_time>=6)):
            
            #print('ssd')
            _count=0
            pre_a=''
            __count=0
            cs1()
            _count=0
            pre_a=''
            ee1()
            _count=0
            pre_a=''
            __count=0
            me1()
            _count=0
            pre_a=''
            __count=0
            ec1()
            _count=0
            pre_a=''
            __count=0
            ch1()
            _count=0
            pre_a=''
            ce1()
            _count=0
            pre_a=''
            __count=0
            ms1()
            _count=0
            pre_a=''
            __count=0
            cs2()
            _count=0
            pre_a=''
            __count=0
            me2()
            _count=0
            pre_a=''
            __count=0
            ee2()
            _count=0
            pre_a=''
            __count=0
            ec2()
            _count=0
            pre_a=''
            __count=0
            cd2()
            _count=0
            pre_a=''
            __count=0
            ed2()
            _count=0
            pre_a=''
            __count=0
            ch2()
            _count=0
            pre_a=''
            ce2()
            _count=0
            pre_a=''
            __count=0
            ms2()
            _count=0
            pre_a=''
            __count=0
            cs3()
            _count=0
            pre_a=''
            __count=0
            me3()
            _count=0
            pre_a=''
            __count=0
            ee3()
            _count=0
            pre_a=''
            __count=0
            ec3()
            _count=0
            pre_a=''
            __count=0
            cd3()
            _count=0
            pre_a=''
            __count=0
            ed3()
            _count=0
            pre_a=''
            __count=0
            ch3()
            _count=0
            pre_a=''
            ce3()
            _count=0
            pre_a=''
            __count=0
            ms3()
            _count=0
            pre_a=''
            __count=0
            cs4()
            _count=0
            pre_a=''
            __count=0
            me4()
            _count=0
            pre_a=''
            __count=0
            __c=0
            ee4()
            _count=0
            pre_a=''
            __count=0
            ec4()
            _count=0
            pre_a=''
            __count=0
            __c=0
            cd4()
            _count=0
            pre_a=''
            __count=0
            ed4()
            occupied_teacher=copy.deepcopy(lab_occupied_teachers)
            if t_time==3:
                lab_occupied_teachers=[]
                occupied_teacher=[]
                occupied_labs=[]

            remaining_rooms=copy.deepcopy(rooms)
            #print(remaining_rooms)
            t_time+=1
            if t_time==4:
                t_time=6
            #print(t_time)
        #print(t_day)
        t_day+=1
        
pre_a=''
pre_a_cs1=''
choices_cs1=4*depts['CS1'][0]+2*depts['CS1'][1]
choices_ee1=4*depts['EE1'][0]+2*depts['EE1'][1]
choices_me1=4*depts['ME1'][0]+2*depts['ME1'][1]
choices_ec1=4*depts['EC1'][0]+2*depts['EC1'][1]
choices_ce1=4*depts['CE1'][0]+2*depts['CE1'][1]
choices_ch1=4*depts['CH1'][0]+2*depts['CH1'][1]
choices_ms1=4*depts['MS1'][0]+2*depts['MS1'][1]


choices_cs2=4*depts['CS2'][0]+2*depts['CS2'][1]
choices_ee2=4*depts['EE2'][0]+2*depts['EE2'][1]
choices_me2=4*depts['ME2'][0]+2*depts['ME2'][1]
choices_ec2=4*depts['EC2'][0]+2*depts['EC2'][1]
choices_cd2=4*depts['CD2'][0]+2*depts['CD2'][1]
choices_ed2=4*depts['ED2'][0]+2*depts['ED2'][1]
choices_ce2=4*depts['CE2'][0]+2*depts['CE2'][1]
choices_ch2=4*depts['CH2'][0]+2*depts['CH2'][1]
choices_ms2=4*depts['MS2'][0]+2*depts['MS2'][1]

choices_cs3=4*depts['CS3'][0]+2*depts['CS3'][1]
choices_ee3=4*depts['EE3'][0]+2*depts['EE3'][1]
choices_me3=4*depts['ME3'][0]+2*depts['ME3'][1]
choices_ec3=4*depts['EC3'][0]+2*depts['EC3'][1]
choices_cd3=4*depts['CD3'][0]+2*depts['CD3'][1]
choices_ed3=4*depts['ED3'][0]+2*depts['ED3'][1]
choices_ce3=4*depts['CE3'][0]+2*depts['CE3'][1]
choices_ch3=4*depts['CH3'][0]+2*depts['CH3'][1]
choices_ms3=4*depts['MS3'][0]+2*depts['MS3'][1]

choices_cs4=4*depts['CS4'][0]+2*depts['CS4'][1]
choices_ee4=4*depts['EE4'][0]+2*depts['EE4'][1]
choices_me4=4*depts['ME4'][0]+2*depts['ME4'][1]
choices_ec4=4*depts['EC4'][0]+2*depts['EC4'][1]
choices_cd4=4*depts['CD4'][0]+2*depts['CD4'][1]
choices_ed4=4*depts['ED4'][0]+2*depts['ED4'][1]
choices_ce4=4*depts['CE4'][0]+2*depts['CE4'][1]
choices_ch4=4*depts['CH4'][0]+2*depts['CH4'][1]


# In[530]:


tt_cs1=[[0 for i in range(10)] for j in range(10)]
tea_cs1=[[0 for i in range(10)] for j in range(10)]
rooms_cs1=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ee1=[[0 for i in range(10)] for j in range(10)]
tea_ee1=[[0 for i in range(10)] for j in range(10)]
rooms_ee1=[[0 for i in range(10)] for j in range(10)]
#t_ch1=0
tt_ch1=[[0 for i in range(10)] for j in range(10)]
tea_ch1=[[0 for i in range(10)] for j in range(10)]
rooms_ch1=[[0 for i in range(10)] for j in range(10)]
#t_ms1=0
tt_ms1=[[0 for i in range(10)] for j in range(10)]
tea_ms1=[[0 for i in range(10)] for j in range(10)]
rooms_ms1=[[0 for i in range(10)] for j in range(10)]
#t_me1=0
tt_me1=[[0 for i in range(10)] for j in range(10)]
tea_me1=[[0 for i in range(10)] for j in range(10)]
rooms_me1=[[0 for i in range(10)] for j in range(10)]
#t_ec1=0
tt_ec1=[[0 for i in range(10)] for j in range(10)]
tea_ec1=[[0 for i in range(10)] for j in range(10)]
rooms_ec1=[[0 for i in range(10)] for j in range(10)]
#t_ce1=0
tt_ce1=[[0 for i in range(10)] for j in range(10)]
tea_ce1=[[0 for i in range(10)] for j in range(10)]
rooms_ce1=[[0 for i in range(10)] for j in range(10)]


tt_cs2=[[0 for i in range(10)] for j in range(10)]
tea_cs2=[[0 for i in range(10)] for j in range(10)]
rooms_cs2=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ee2=[[0 for i in range(10)] for j in range(10)]
tea_ee2=[[0 for i in range(10)] for j in range(10)]
rooms_ee2=[[0 for i in range(10)] for j in range(10)]
#t_ch1=0
tt_ch2=[[0 for i in range(10)] for j in range(10)]
tea_ch2=[[0 for i in range(10)] for j in range(10)]
rooms_ch2=[[0 for i in range(10)] for j in range(10)]
#t_ms1=0
tt_ms2=[[0 for i in range(10)] for j in range(10)]
tea_ms2=[[0 for i in range(10)] for j in range(10)]
rooms_ms2=[[0 for i in range(10)] for j in range(10)]
#t_me1=0
tt_me2=[[0 for i in range(10)] for j in range(10)]
tea_me2=[[0 for i in range(10)] for j in range(10)]
rooms_me2=[[0 for i in range(10)] for j in range(10)]
#t_ec1=0
tt_ec2=[[0 for i in range(10)] for j in range(10)]
tea_ec2=[[0 for i in range(10)] for j in range(10)]
rooms_ec2=[[0 for i in range(10)] for j in range(10)]
#t_ce1=0
tt_ce2=[[0 for i in range(10)] for j in range(10)]
tea_ce2=[[0 for i in range(10)] for j in range(10)]
rooms_ce2=[[0 for i in range(10)] for j in range(10)]

tt_cd2=[[0 for i in range(10)] for j in range(10)]
tea_cd2=[[0 for i in range(10)] for j in range(10)]
rooms_cd2=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ed2=[[0 for i in range(10)] for j in range(10)]
tea_ed2=[[0 for i in range(10)] for j in range(10)]
rooms_ed2=[[0 for i in range(10)] for j in range(10)]



tt_cs3=[[0 for i in range(10)] for j in range(10)]
tea_cs3=[[0 for i in range(10)] for j in range(10)]
rooms_cs3=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ee3=[[0 for i in range(10)] for j in range(10)]
tea_ee3=[[0 for i in range(10)] for j in range(10)]
rooms_ee3=[[0 for i in range(10)] for j in range(10)]
#t_ch1=0
tt_ch3=[[0 for i in range(10)] for j in range(10)]
tea_ch3=[[0 for i in range(10)] for j in range(10)]
rooms_ch3=[[0 for i in range(10)] for j in range(10)]
#t_ms1=0
tt_ms3=[[0 for i in range(10)] for j in range(10)]
tea_ms3=[[0 for i in range(10)] for j in range(10)]
rooms_ms3=[[0 for i in range(10)] for j in range(10)]
#t_me1=0
tt_me3=[[0 for i in range(10)] for j in range(10)]
tea_me3=[[0 for i in range(10)] for j in range(10)]
rooms_me3=[[0 for i in range(10)] for j in range(10)]
#t_ec1=0
tt_ec3=[[0 for i in range(10)] for j in range(10)]
tea_ec3=[[0 for i in range(10)] for j in range(10)]
rooms_ec3=[[0 for i in range(10)] for j in range(10)]
#t_ce1=0
tt_ce3=[[0 for i in range(10)] for j in range(10)]
tea_ce3=[[0 for i in range(10)] for j in range(10)]
rooms_ce3=[[0 for i in range(10)] for j in range(10)]

tt_cd3=[[0 for i in range(10)] for j in range(10)]
tea_cd3=[[0 for i in range(10)] for j in range(10)]
rooms_cd3=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ed3=[[0 for i in range(10)] for j in range(10)]
tea_ed3=[[0 for i in range(10)] for j in range(10)]
rooms_ed3=[[0 for i in range(10)] for j in range(10)]


tt_cs4=[[0 for i in range(10)] for j in range(10)]
tea_cs4=[[0 for i in range(10)] for j in range(10)]
rooms_cs4=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ee4=[[0 for i in range(10)] for j in range(10)]
tea_ee4=[[0 for i in range(10)] for j in range(10)]
rooms_ee4=[[0 for i in range(10)] for j in range(10)]
#t_ch1=0
tt_ch4=[[0 for i in range(10)] for j in range(10)]
tea_ch4=[[0 for i in range(10)] for j in range(10)]
rooms_ch4=[[0 for i in range(10)] for j in range(10)]
#t_ms1=0
#tt_ms4=[[0 for i in range(10)] for j in range(10)]
#tea_ms4=[[0 for i in range(10)] for j in range(10)]
#rooms_ms4=[[0 for i in range(10)] for j in range(10)]
#t_me1=0
tt_me4=[[0 for i in range(10)] for j in range(10)]
tea_me4=[[0 for i in range(10)] for j in range(10)]
rooms_me4=[[0 for i in range(10)] for j in range(10)]
#t_ec1=0
tt_ec4=[[0 for i in range(10)] for j in range(10)]
tea_ec4=[[0 for i in range(10)] for j in range(10)]
rooms_ec4=[[0 for i in range(10)] for j in range(10)]
#t_ce1=0
tt_ce4=[[0 for i in range(10)] for j in range(10)]
tea_ce4=[[0 for i in range(10)] for j in range(10)]
rooms_ce4=[[0 for i in range(10)] for j in range(10)]

tt_cd4=[[0 for i in range(10)] for j in range(10)]
tea_cd4=[[0 for i in range(10)] for j in range(10)]
rooms_cd4=[[0 for i in range(10)] for j in range(10)]
#t_ee1=0
tt_ed4=[[0 for i in range(10)] for j in range(10)]
tea_ed4=[[0 for i in range(10)] for j in range(10)]
rooms_ed4=[[0 for i in range(10)] for j in range(10)]

t_day=0
t_time=0
q1=''
tuts_0=[]
tuts_1=[]
for i in range(len(depts)):
    tuts_0=list(depts.items())[i][1][0]+tuts_0
    tuts_1=list(depts.items())[i][1][0]+tuts_1

labs_0=[]
labs_1=[]
for i in range(len(depts)):
    labs_0=list(depts.items())[i][1][1]+labs_0
    labs_1=list(depts.items())[i][1][1]+labs_1
    
tuts_=[tuts_0]+[tuts_1]
labs_=[labs_0]+[labs_1]
lect_=[]
for i in range(len(depts)):
     lect_=list(depts.items())[i][1][0]+lect_
lect_=lect_*3
lab_occupied_teachers=[]
_count=0


# In[531]:


def Teacher_assign(x):
    z=[]
    for i,j in teacher_code.items():
        if x in j:
            z.append(i)
    if not z:
        return 'data_not_available'
    q1=random.choice(z)
    return q1

def lab_assign(x):
    z=[]
    for i,j in lab_code.items():
        if x in j:
            z.append(i)
    if not z:
        return 'not assigned yet'
    l=random.choice(z)
    
    return l


def occupy_teacher(q1):
    global occupied_teacher
    occupied_teacher.append(q1)
    return
    
    
def occupy_labs(l):
    global occupied_labs
    occupied_labs.append(l)
    return


# In[532]:


def cs1():
    global tt_cs1,tea_cs1,rooms_cs1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cs1,t_day,_count
    if (rooms_cs1[2*t_day][t_time]==0 and rooms_cs1[2*t_day+1][t_time]==0) and (tea_cs1[2*t_day][t_time]==0 and tea_cs1[2*t_day+1][t_time] ==0):
        if not choices_cs1:
            return
        a=random.choice(choices_cs1)
        #print(a)
        if not a:
            return
        if( a==pre_a_cs1 and len(a)>2):
            a=random.choice(choices_cs1)
        pre_a_cs1=a
        if a in depts['CS1'][0]:
            if a in lect_:
                
                tt_cs1[2*t_day][t_time]=a
                tt_cs1[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cs1()
                else:
                    occupy_teacher(q1)
                    tea_cs1[2*t_day][t_time]=q1
                    tea_cs1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cs1()
                    if not r:
                        return
                    rooms_cs1[2*t_day][t_time]=r
                    rooms_cs1[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cs1.remove(a)
                    
            elif a in remaining_tutorials_CS1[0]+remaining_tutorials_CS1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CS1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CS1[0]+remaining_tutorials_CS1[1])
                tutorial_assign1_cs1(t_day_t,a,0,_c)
        
            else:
                cs1()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cs1[t_day_l][t_time]=a
                    tt_cs1[t_day_l][t_time+1]=a
                    tt_cs1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cs1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cs1[t_day_l][t_time]=q1
                        tea_cs1[t_day_l][t_time+1]=q1
                        tea_cs1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cs1[t_day_l][t_time]=l
                        rooms_cs1[t_day_l][t_time+1]=l
                        rooms_cs1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cs1.remove(a)
                        q=lab_assign_alternate(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign(t_day_t,_c)
                        
            else:
                cs1()
                        
    return      
                        
                        
def lab_assign_alternate(t_day_t,_c):
    global tt_cs1,tea_cs1,rooms_cs1,t_time,labs_,lect_,lab_occupied_teachers,choices_cs1
    a=random.choice(depts['CS1'][1])
    if a in labs_:
        tt_cs1[t_day_t][t_time]=a
        tt_cs1[t_day_t][t_time+1]=a
        tt_cs1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cs1[t_day_t][t_time]=q1
            tea_cs1[t_day_t][t_time+1]=q1
            tea_cs1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cs1[t_day_t][t_time]=l
            rooms_cs1[t_day_t][t_time+1]=l
            rooms_cs1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cs1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CS1=[remaining_tutorials['CS1'][0]]+[remaining_tutorials['CS1'][0]]
def tutorial_assign(t_day_t,_c):
    global pre_a_cs1
    for i in range(2):
        if remaining_tutorials_CS1[0]+remaining_tutorials_CS1[1]:
            a=random.choice(remaining_tutorials_CS1[0]+remaining_tutorials_CS1[1])
            if( a==pre_a_cs1 and len(a)>2):
                a=random.choice(remaining_tutorials_CS1[0]+remaining_tutorials_CS1[1])
            pre_a_cs1=a
            tutorial_assign1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1(t_day_t,a,i,_c):
    global remaining_tutorials_CS1,tea_cs1,rooms_cs1,tt_cs1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CS1[_c].remove(a)
        choices_cs1.remove(a)
        occupy_teacher(q1)
        tea_cs1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cs1()
        rooms_cs1[t_day_t][t_time+i]=r
        tt_cs1[t_day_t][t_time+i]=a
        return
        

def room_assign1_cs1():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cs1[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs1[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cs1[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs1[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
    elif remaining_rooms['G']:
        r=random.choice(remaining_rooms['G'])
        remaining_rooms['G'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[533]:


count_ce1=0
pre_a_ch1=''
def ch1():
    global tt_ch1,tea_ch1,rooms_ch1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ch1,t_day,_count,count_ce1
    if rooms_ch1[2*t_day][t_time]==0 or tea_ch1[2*t_day][t_time] ==0:
        if not choices_ch1:
            return
        a=random.choice(choices_ch1)
        #print(a)
        if not a:
            return
        if a==pre_a_ch1 and len(a)>2:
            a=random.choice(choices_ch1)
        pre_a_ch1=a
        if a in depts['CH1'][0]:
            if a in lect_:
                
                tt_ch1[2*t_day][t_time]=a
                tt_ch1[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ch1()
                else:
                    occupy_teacher(q1)
                    tea_ch1[2*t_day][t_time]=q1
                    tea_ch1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ch1()
                    if not r:
                        return
                    rooms_ch1[2*t_day][t_time]=r
                    rooms_ch1[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ch1.remove(a)
                    
            elif a in remaining_tutorials_CH1[0]+remaining_tutorials_CH1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CH1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CH1[0]+remaining_tutorials_CH1[1])
                tutorial_assign1_ch1(t_day_t,a,0,_c)
        
            else:
                if count_ce1>2:
                    count_ce1=0
                    return
                count_ce1+=1
                ch1()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ch1[t_day_l][t_time]=a
                    tt_ch1[t_day_l][t_time+1]=a
                    tt_ch1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ch1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ch1[t_day_l][t_time]=q1
                        tea_ch1[t_day_l][t_time+1]=q1
                        tea_ch1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ch1[t_day_l][t_time]=l
                        rooms_ch1[t_day_l][t_time+1]=l
                        rooms_ch1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ch1.remove(a)
                        q=lab_assign_alternate_ch1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ch1(t_day_t,_c)
                        
            else:
                ch1()
                        
    return      
                        
                        
def lab_assign_alternate_ch1(t_day_t,_c):
    global tt_ch1,tea_ch1,rooms_ch1,t_time,labs_,lect_,lab_occupied_teachers,choices_ch1
    a=random.choice(depts['CH1'][1])
    if a in labs_:
        tt_ch1[t_day_t][t_time]=a
        tt_ch1[t_day_t][t_time+1]=a
        tt_ch1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ch1[t_day_t][t_time]=q1
            tea_ch1[t_day_t][t_time+1]=q1
            tea_ch1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ch1[t_day_t][t_time]=l
            rooms_ch1[t_day_t][t_time+1]=l
            rooms_ch1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ch1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CH1=[remaining_tutorials['CH1'][0]]+[remaining_tutorials['CH1'][0]]
def tutorial_assign_ch1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CH1[0]+remaining_tutorials_CH1[1]:
            a=random.choice(remaining_tutorials_CH1[0]+remaining_tutorials_CH1[1])
            tutorial_assign1_ch1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ch1(t_day_t,a,i,_c):
    global remaining_tutorials_CH1,tea_ch1,rooms_ch1,tt_ch1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CH1[_c].remove(a)
        choices_ch1.remove(a)
        occupy_teacher(q1)
        tea_ch1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ch1()
        rooms_ch1[t_day_t][t_time+i]=r
        tt_ch1[t_day_t][t_time+i]=a
        return
        

def room_assign1_ch1():
    global remaining_rooms,t_time,t_day
    return 'CHDEPT'


# In[534]:


count_ce1=0
pre_a_ce1=''
def ce1():
    global tt_ce1,tea_ce1,rooms_ce1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ce1,t_day,_count,count_ce1
    if rooms_ce1[2*t_day][t_time]==0 or tea_ce1[2*t_day][t_time] ==0:
        if not choices_ce1:
            return
        a=random.choice(choices_ce1)
        #print(a)
        if not a:
            return
        if a==pre_a_ce1 and len(a)>2:
            a=random.choice(choices_ce1)
        pre_a_ce1=a
        if a in depts['CE1'][0]:
            if a in lect_:
                
                tt_ce1[2*t_day][t_time]=a
                tt_ce1[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ce1()
                else:
                    occupy_teacher(q1)
                    tea_ce1[2*t_day][t_time]=q1
                    tea_ce1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ce1()
                    if not r:
                        return
                    rooms_ce1[2*t_day][t_time]=r
                    rooms_ce1[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ce1.remove(a)
                    
            elif a in remaining_tutorials_CE1[0]+remaining_tutorials_CE1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CE1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CE1[0]+remaining_tutorials_CE1[1])
                tutorial_assign1_ce1(t_day_t,a,0,_c)
        
            else:
                if count_ce1>2:
                    count_ce1=0
                    return
                count_ce1+=1
                ce1()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ce1[t_day_l][t_time]=a
                    tt_ce1[t_day_l][t_time+1]=a
                    tt_ce1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ce1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ce1[t_day_l][t_time]=q1
                        tea_ce1[t_day_l][t_time+1]=q1
                        tea_ce1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ce1[t_day_l][t_time]=l
                        rooms_ce1[t_day_l][t_time+1]=l
                        rooms_ce1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ce1.remove(a)
                        q=lab_assign_alternate_ce1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ce1(t_day_t,_c)
                        
            else:
                ce1()
                        
    return      
                        
                        
def lab_assign_alternate_ce1(t_day_t,_c):
    global tt_ce1,tea_ce1,rooms_ce1,t_time,labs_,lect_,lab_occupied_teachers,choices_ce1
    a=random.choice(depts['CE1'][1])
    if a in labs_:
        tt_ce1[t_day_t][t_time]=a
        tt_ce1[t_day_t][t_time+1]=a
        tt_ce1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ce1[t_day_t][t_time]=q1
            tea_ce1[t_day_t][t_time+1]=q1
            tea_ce1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ce1[t_day_t][t_time]=l
            rooms_ce1[t_day_t][t_time+1]=l
            rooms_ce1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ce1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CE1=[remaining_tutorials['CE1'][0]]+[remaining_tutorials['CE1'][0]]
def tutorial_assign_ce1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CE1[0]+remaining_tutorials_CE1[1]:
            a=random.choice(remaining_tutorials_CE1[0]+remaining_tutorials_CE1[1])
            tutorial_assign1_ce1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ce1(t_day_t,a,i,_c):
    global remaining_tutorials_CE1,tea_ce1,rooms_ce1,tt_ce1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CE1[_c].remove(a)
        choices_ce1.remove(a)
        occupy_teacher(q1)
        tea_ce1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ce1()
        rooms_ce1[t_day_t][t_time+i]=r
        tt_ce1[t_day_t][t_time+i]=a
        return
        

def room_assign1_ce1():
    global remaining_rooms,t_time,t_day
    return 'CEDEPT'


# In[535]:


__count=0
pre_a_ee1=''
def ee1():
    global tt_ee1,tea_ee1,rooms_ee1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ee1,t_day,_count,__count
    if rooms_ee1[2*t_day][t_time]==0 or tea_ee1[2*t_day][t_time] ==0:
        if not choices_ee1:
            return
        a=random.choice(choices_ee1)
        #print(a)
        if not a:
            return
        if a==pre_a_ee1 and len(a)>2:
            a=random.choice(choices_ee1)
        pre_a_ee1=a
        if a in depts['EE1'][0]:
            if a in lect_:
                
                tt_ee1[2*t_day][t_time]=a
                tt_ee1[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ee1()
                else:
                    occupy_teacher(q1)
                    tea_ee1[2*t_day][t_time]=q1
                    tea_ee1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ee1()
                    if not r:
                        return
                    rooms_ee1[2*t_day][t_time]=r
                    rooms_ee1[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ee1.remove(a)
            elif a in remaining_tutorials_EE1[0]+remaining_tutorials_EE1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EE1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_EE1[0]+remaining_tutorials_EE1[1])
                tutorial_assign1_ee1(t_day_t,a,0,_c)
            else:
                __count+=1
                ee1()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ee1[t_day_l][t_time]=a
                    tt_ee1[t_day_l][t_time+1]=a
                    tt_ee1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ee1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ee1[t_day_l][t_time]=q1
                        tea_ee1[t_day_l][t_time+1]=q1
                        tea_ee1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ee1[t_day_l][t_time]=l
                        rooms_ee1[t_day_l][t_time+1]=l
                        rooms_ee1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ee1.remove(a)
                        q=lab_assign_alternate_ee1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ee1(t_day_t,_c)
                        
            else:
                ee1()
                        
    return      
                        
                        
def lab_assign_alternate_ee1(t_day_t,_c):
    global tt_ee1,tea_ee1,rooms_ee1,t_time,labs_,lect_,lab_occupied_teachers,choices_ee1
    a=random.choice(depts['EE1'][1])
    if a in labs_:
        tt_ee1[t_day_t][t_time]=a
        tt_ee1[t_day_t][t_time+1]=a
        tt_ee1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ee1[t_day_t][t_time]=q1
            tea_ee1[t_day_t][t_time+1]=q1
            tea_ee1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ee1[t_day_t][t_time]=l
            rooms_ee1[t_day_t][t_time+1]=l
            rooms_ee1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ee1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EE1=[remaining_tutorials['EE1'][0]]+[remaining_tutorials['EE1'][0]]
def tutorial_assign_ee1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EE1[0]+remaining_tutorials_EE1[1]:
            a=random.choice(remaining_tutorials_EE1[0]+remaining_tutorials_EE1[1])
            tutorial_assign1_ee1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ee1(t_day_t,a,i,_c):
    global remaining_tutorials_EE1,tea_ee1,rooms_ee1,tt_ee1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EE1[_c].remove(a)
        choices_ee1.remove(a)
        occupy_teacher(q1)
        tea_ee1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ee1()
        rooms_ee1[t_day_t][t_time+i]=r
        tt_ee1[t_day_t][t_time+i]=a
        return

def room_assign1_ee1():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ee1[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee1[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ee1[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee1[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
    elif remaining_rooms['G']:
        r=random.choice(remaining_rooms['G'])
        remaining_rooms['G'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[536]:


__count=0
pre_a_me1=''
def me1():
    global tt_me1,tea_me1,rooms_me1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_me1,t_day,_count,__count
    if rooms_me1[2*t_day][t_time]==0 or tea_me1[2*t_day][t_time] ==0:
        if not choices_me1:
            return
        a=random.choice(choices_me1)
        #print(a)
        if not a:
            return
        if a==pre_a_me1 and len(a)>2:
            a=random.choice(choices_me1)
        pre_a_me1=a
        if a in depts['ME1'][0]:
            if a in lect_:
                
                tt_me1[2*t_day][t_time]=a
                tt_me1[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    me1()
                else:
                    occupy_teacher(q1)
                    tea_me1[2*t_day][t_time]=q1
                    tea_me1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_me1()
                    if not r:
                        return
                    rooms_me1[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_me1.remove(a)
            elif a in remaining_tutorials_ME1[0]+remaining_tutorials_ME1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ME1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_ME1[0]+remaining_tutorials_ME1[1])
                tutorial_assign1_me1(t_day_t,a,0,_c)
            else:
                __count+=1
                me1()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_me1[t_day_l][t_time]=a
                    tt_me1[t_day_l][t_time+1]=a
                    tt_me1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        me1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_me1[t_day_l][t_time]=q1
                        tea_me1[t_day_l][t_time+1]=q1
                        tea_me1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_me1[t_day_l][t_time]=l
                        rooms_me1[t_day_l][t_time+1]=l
                        rooms_me1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_me1.remove(a)
                        q=lab_assign_alternate_me1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_me1(t_day_t,_c)
                        
            else:
                me1()
                        
    return      
                        
                        
def lab_assign_alternate_me1(t_day_t,_c):
    global tt_me1,tea_me1,rooms_me1,t_time,labs_,lect_,lab_occupied_teachers,choices_me1
    a=random.choice(depts['ME1'][1])
    if a in labs_:
        tt_me1[t_day_t][t_time]=a
        tt_me1[t_day_t][t_time+1]=a
        tt_me1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_me1[t_day_t][t_time]=q1
            tea_me1[t_day_t][t_time+1]=q1
            tea_me1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_me1[t_day_t][t_time]=l
            rooms_me1[t_day_t][t_time+1]=l
            rooms_me1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_me1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ME1=[remaining_tutorials['ME1'][0]]+[remaining_tutorials['ME1'][0]]
def tutorial_assign_me1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ME1[0]+remaining_tutorials_ME1[1]:
            a=random.choice(remaining_tutorials_ME1[0]+remaining_tutorials_ME1[1])
            tutorial_assign1_me1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_me1(t_day_t,a,i,_c):
    global remaining_tutorials_ME1,tea_me1,rooms_me1,tt_me1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ME1[_c].remove(a)
        choices_me1.remove(a)
        occupy_teacher(q1)
        tea_me1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_me1()
        rooms_me1[t_day_t][t_time+i]=r
        tt_me1[t_day_t][t_time+i]=a
        return

def room_assign1_me1():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_me1[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me1[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_me1[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me1[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
    elif remaining_rooms['G']:
        r=random.choice(remaining_rooms['G'])
        remaining_rooms['G'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[537]:

pre_a_ms1=''
__count=0
def ms1():
    global tt_ms1,tea_ms1,rooms_ms1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ms1,t_day,_count,__count
    if rooms_ms1[2*t_day][t_time]==0 or tea_ms1[2*t_day][t_time] ==0:
        if not choices_ms1:
            return
        a=random.choice(choices_ms1)
        #print(a)
        if not a:
            return
        if a==pre_a_ms1 and len(a)>2:
            a=random.choice(choices_ms1)
        pre_a_ms1=a
        if a in depts['MS1'][0]:
            if a in lect_:
                
                tt_ms1[2*t_day][t_time]=a
                tt_ms1[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ms1()
                else:
                    occupy_teacher(q1)
                    tea_ms1[2*t_day][t_time]=q1
                    tea_ms1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ms1()
                    if not r:
                        return
                    rooms_ms1[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ms1.remove(a)
            elif a in remaining_tutorials_MS1[0]+remaining_tutorials_MS1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_MS1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_MS1[0]+remaining_tutorials_MS1[1])
                tutorial_assign1_ms1(t_day_t,a,0,_c)
            else:
                __count+=1
                ms1()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ms1[t_day_l][t_time]=a
                    tt_ms1[t_day_l][t_time+1]=a
                    tt_ms1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ms1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ms1[t_day_l][t_time]=q1
                        tea_ms1[t_day_l][t_time+1]=q1
                        tea_ms1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ms1[t_day_l][t_time]=l
                        rooms_ms1[t_day_l][t_time+1]=l
                        rooms_ms1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ms1.remove(a)
                        q=lab_assign_alternate_ms1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ms1(t_day_t,_c)
                        
            else:
                ms1()
                        
    return      
                        
                        
def lab_assign_alternate_ms1(t_day_t,_c):
    global tt_ms1,tea_ms1,rooms_ms1,t_time,labs_,lect_,lab_occupied_teachers,choices_ms1
    a=random.choice(depts['MS1'][1])
    if a in labs_:
        tt_ms1[t_day_t][t_time]=a
        tt_ms1[t_day_t][t_time+1]=a
        tt_ms1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ms1[t_day_t][t_time]=q1
            tea_ms1[t_day_t][t_time+1]=q1
            tea_ms1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ms1[t_day_t][t_time]=l
            rooms_ms1[t_day_t][t_time+1]=l
            rooms_ms1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ms1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_MS1=[remaining_tutorials['MS1'][0]]+[remaining_tutorials['MS1'][0]]
def tutorial_assign_ms1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_MS1[0]+remaining_tutorials_MS1[1]:
            a=random.choice(remaining_tutorials_MS1[0]+remaining_tutorials_MS1[1])
            tutorial_assign1_ms1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ms1(t_day_t,a,i,_c):
    global remaining_tutorials_MS1,tea_ms1,rooms_ms1,tt_ms1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_MS1[_c].remove(a)
        choices_ms1.remove(a)
        occupy_teacher(q1)
        tea_ms1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ms1()
        rooms_ms1[t_day_t][t_time+i]=r
        tt_ms1[t_day_t][t_time+i]=a
        return

def room_assign1_ms1():
    global remaining_rooms,t_time,t_day
    
    return 'MSDEPT'


# In[538]:

pre_a_ec1=''
__count=0
def ec1():
    global tt_ec1,tea_ec1,rooms_ec1,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ec1,t_day,_count,__count
    if rooms_ec1[2*t_day][t_time]==0 or tea_ec1[2*t_day][t_time] ==0:
        if not choices_ec1:
            return
        a=random.choice(choices_ec1)
        #print(a)
        if not a:
            return
        if a==pre_a_ec1 and len(a)>2:
            a=random.choice(choices_ec1)
        pre_a_ec1=a
        if a in depts['EC1'][0]:
            if a in lect_:
                
                tt_ec1[2*t_day][t_time]=a
                tt_ec1[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ec1()
                else:
                    occupy_teacher(q1)
                    tea_ec1[2*t_day][t_time]=q1
                    tea_ec1[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ec1()
                    if not r:
                        return
                    rooms_ec1[2*t_day][t_time]=r
                    rooms_ec1[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ec1.remove(a)
            elif a in remaining_tutorials_EC1[0]+remaining_tutorials_EC1[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EC1[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_EC1[0]+remaining_tutorials_EC1[1])
                tutorial_assign1_ec1(t_day_t,a,0,_c)
            else:
                __count+=1
                ec1()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ec1[t_day_l][t_time]=a
                    tt_ec1[t_day_l][t_time+1]=a
                    tt_ec1[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ec1()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ec1[t_day_l][t_time]=q1
                        tea_ec1[t_day_l][t_time+1]=q1
                        tea_ec1[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ec1[t_day_l][t_time]=l
                        rooms_ec1[t_day_l][t_time+1]=l
                        rooms_ec1[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ec1.remove(a)
                        q=lab_assign_alternate_ec1(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ec1(t_day_t,_c)
                        
            else:
                ec1()
                        
    return      
                        
                        
def lab_assign_alternate_ec1(t_day_t,_c):
    global tt_ec1,tea_ec1,rooms_ec1,t_time,labs_,lect_,lab_occupied_teachers,choices_ec1
    a=random.choice(depts['EC1'][1])
    if a in labs_:
        tt_ec1[t_day_t][t_time]=a
        tt_ec1[t_day_t][t_time+1]=a
        tt_ec1[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ec1[t_day_t][t_time]=q1
            tea_ec1[t_day_t][t_time+1]=q1
            tea_ec1[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ec1[t_day_t][t_time]=l
            rooms_ec1[t_day_t][t_time+1]=l
            rooms_ec1[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ec1.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EC1=[remaining_tutorials['EC1'][0]]+[remaining_tutorials['EC1'][0]]
def tutorial_assign_ec1(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EC1[0]+remaining_tutorials_EC1[1]:
            a=random.choice(remaining_tutorials_EC1[0]+remaining_tutorials_EC1[1])
            tutorial_assign1_ec1(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ec1(t_day_t,a,i,_c):
    global remaining_tutorials_EC1,tea_ec1,rooms_ec1,tt_ec1
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EC1[_c].remove(a)
        choices_ec1.remove(a)
        occupy_teacher(q1)
        tea_ec1[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ec1()
        rooms_ec1[t_day_t][t_time+i]=r
        tt_ec1[t_day_t][t_time+i]=a
        return

def room_assign1_ec1():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ec1[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec1[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ec1[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec1[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
    elif remaining_rooms['G']:
        r=random.choice(remaining_rooms['G'])
        remaining_rooms['G'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[539]:

pre_a_cs2=''
__count=0
def cs2():
    global tt_cs2,tea_cs2,rooms_cs2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cs2,t_day,_count,__count
    if (rooms_cs2[2*t_day][t_time]==0 and rooms_cs2[2*t_day+1][t_time]==0) and (tea_cs2[2*t_day][t_time] and tea_cs2[2*t_day+1][t_time]) ==0:
        if not choices_cs2:
            return
        a=random.choice(choices_cs2)
        #print(a)
        if not a:
            return
        while( a==pre_a_cs2 and len(a)>2):
            a=random.choice(choices_cs2)
        pre_a_cs2=a
        if a in depts['CS2'][0]:
            if a in lect_:
                
                tt_cs2[2*t_day][t_time]=a
                tt_cs2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cs2()
                else:
                    occupy_teacher(q1)
                    tea_cs2[2*t_day][t_time]=q1
                    tea_cs2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cs2()
                    if not r:
                        return
                    rooms_cs2[2*t_day][t_time]=r
                    rooms_cs2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cs2.remove(a)
            elif a in remaining_tutorials_CS2[0]+remaining_tutorials_CS2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CS2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CS2[0]+remaining_tutorials_CS2[1])
                tutorial_assign1_cs2(t_day_t,a,0,_c)
            else:
                __count+=1
                cs2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cs2[t_day_l][t_time]=a
                    tt_cs2[t_day_l][t_time+1]=a
                    tt_cs2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cs2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cs2[t_day_l][t_time]=q1
                        tea_cs2[t_day_l][t_time+1]=q1
                        tea_cs2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cs2[t_day_l][t_time]=l
                        rooms_cs2[t_day_l][t_time+1]=l
                        rooms_cs2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cs2.remove(a)
                        q=lab_assign_alternate_cs2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cs2(t_day_t,_c)
                        
            else:
                cs2()
                        
    return      
                        
                        
def lab_assign_alternate_cs2(t_day_t,_c):
    global tt_cs2,tea_cs2,rooms_cs2,t_time,labs_,lect_,lab_occupied_teachers,choices_cs2
    a=random.choice(depts['CS2'][1])
    if a in labs_:
        tt_cs2[t_day_t][t_time]=a
        tt_cs2[t_day_t][t_time+1]=a
        tt_cs2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cs2[t_day_t][t_time]=q1
            tea_cs2[t_day_t][t_time+1]=q1
            tea_cs2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cs2[t_day_t][t_time]=l
            rooms_cs2[t_day_t][t_time+1]=l
            rooms_cs2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cs2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CS2=[remaining_tutorials['CS2'][0]]+[remaining_tutorials['CS2'][0]]
def tutorial_assign_cs2(t_day_t,_c):
    global pre_a_cs2
    for i in range(2):
        if remaining_tutorials_CS2[0]+remaining_tutorials_CS2[1]:
            a=random.choice(remaining_tutorials_CS2[0]+remaining_tutorials_CS2[1])
            if( a==pre_a_cs2 and len(a)>2):
                a=random.choice(remaining_tutorials_CS2[0]+remaining_tutorials_CS2[1])
            pre_a_cs2=a
            tutorial_assign1_cs2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_cs2(t_day_t,a,i,_c):
    global remaining_tutorials_CS2,tea_cs2,rooms_cs2,tt_cs2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print('cs')
        #print(a)
        #print('1'+f'{remaining_tutorials_CS2}')
        remaining_tutorials_CS2[_c].remove(a)
        #print('2'+f'{choices_cs2}')
        choices_cs2.remove(a)
        occupy_teacher(q1)
        tea_cs2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cs2()
        rooms_cs2[t_day_t][t_time+i]=r
        tt_cs2[t_day_t][t_time+i]=a
        return

def room_assign1_cs2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cs2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cs2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)     
    elif rooms_cs2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cs2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[540]:

pre_a_ch2=''
def ch2():
    global tt_ch2,tea_ch2,rooms_ch2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ch2,t_day,_count
    if rooms_ch2[2*t_day][t_time]==0 or tea_ch2[2*t_day][t_time] ==0:
        if not choices_ch2:
            return
        a=random.choice(choices_ch2)
        #print(a)
        if not a:
            return
        if a==pre_a_ch2 and len(a)>2:
            a=random.choice(choices_ch2)
        pre_a_ch2=a
        if a in depts['CH2'][0]:
            if a in lect_:
                
                tt_ch2[2*t_day][t_time]=a
                tt_ch2[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ch2()
                else:
                    occupy_teacher(q1)
                    tea_ch2[2*t_day][t_time]=q1
                    tea_ch2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ch2()
                    if not r:
                        return
                    rooms_ch2[2*t_day][t_time]=r
                    rooms_ch2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ch2.remove(a)
                    
            elif a in remaining_tutorials_CH2[0]+remaining_tutorials_CH2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CH2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CH2[0]+remaining_tutorials_CH2[1])
                tutorial_assign1_ch2(t_day_t,a,0,_c)
        
            else:
                ch2()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ch2[t_day_l][t_time]=a
                    tt_ch2[t_day_l][t_time+1]=a
                    tt_ch2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ch2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ch2[t_day_l][t_time]=q1
                        tea_ch2[t_day_l][t_time+1]=q1
                        tea_ch2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ch2[t_day_l][t_time]=l
                        rooms_ch2[t_day_l][t_time+1]=l
                        rooms_ch2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ch2.remove(a)
                        q=lab_assign_alternate_ch2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ch2(t_day_t,_c)
                        
            else:
                ch2()
                        
    return      
                        
                        
def lab_assign_alternate_ch2(t_day_t,_c):
    global tt_ch2,tea_ch2,rooms_ch2,t_time,labs_,lect_,lab_occupied_teachers,choices_ch2
    a=random.choice(depts['CH2'][1])
    if a in labs_:
        tt_ch2[t_day_t][t_time]=a
        tt_ch2[t_day_t][t_time+1]=a
        tt_ch2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ch2[t_day_t][t_time]=q1
            tea_ch2[t_day_t][t_time+1]=q1
            tea_ch2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ch2[t_day_t][t_time]=l
            rooms_ch2[t_day_t][t_time+1]=l
            rooms_ch2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ch2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CH2=[remaining_tutorials['CH2'][0]]+[remaining_tutorials['CH2'][0]]
def tutorial_assign_ch2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CH2[0]+remaining_tutorials_CH2[1]:
            a=random.choice(remaining_tutorials_CH2[0]+remaining_tutorials_CH2[1])
            tutorial_assign1_ch2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ch2(t_day_t,a,i,_c):
    global remaining_tutorials_CH2,tea_ch2,rooms_ch2,tt_ch2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CH2[_c].remove(a)
        choices_ch2.remove(a)
        occupy_teacher(q1)
        tea_ch2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ch2()
        rooms_ch2[t_day_t][t_time+i]=r
        tt_ch2[t_day_t][t_time+i]=a
        return
        

def room_assign1_ch2():
    global remaining_rooms,t_time,t_day
    return 'CHDEPT'


# In[541]:

pre_a_ce2=''
def ce2():
    global tt_ce2,tea_ce2,rooms_ce2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ce2,t_day,_count
    if rooms_ce2[2*t_day][t_time]==0 or tea_ce2[2*t_day][t_time] ==0:
        if not choices_ce2:
            return
        a=random.choice(choices_ce2)
        #print(a)
        if not a:
            return
        if a==pre_a_ce2 and len(a)>2:
            a=random.choice(choices_ce2)
        pre_a_ce2=a
        if a in depts['CE2'][0]:
            if a in lect_:
                
                tt_ce2[2*t_day][t_time]=a
                tt_ce2[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ce2()
                else:
                    occupy_teacher(q1)
                    tea_ce2[2*t_day][t_time]=q1
                    tea_ce2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ce2()
                    if not r:
                        return
                    rooms_ce2[2*t_day][t_time]=r
                    rooms_ce2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ce2.remove(a)
                    
            elif a in remaining_tutorials_CE2[0]+remaining_tutorials_CE2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CE2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CE2[0]+remaining_tutorials_CE2[1])
                tutorial_assign1_ce2(t_day_t,a,0,_c)
        
            else:
                ce2()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ce2[t_day_l][t_time]=a
                    tt_ce2[t_day_l][t_time+1]=a
                    tt_ce2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ce2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ce2[t_day_l][t_time]=q1
                        tea_ce2[t_day_l][t_time+1]=q1
                        tea_ce2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ce2[t_day_l][t_time]=l
                        rooms_ce2[t_day_l][t_time+1]=l
                        rooms_ce2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ce2.remove(a)
                        q=lab_assign_alternate_ce2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ce2(t_day_t,_c)
                        
            else:
                ce2()
                        
    return      
                        
                        
def lab_assign_alternate_ce2(t_day_t,_c):
    global tt_ce2,tea_ce2,rooms_ce2,t_time,labs_,lect_,lab_occupied_teachers,choices_ce2
    a=random.choice(depts['CE2'][1])
    if a in labs_:
        tt_ce2[t_day_t][t_time]=a
        tt_ce2[t_day_t][t_time+1]=a
        tt_ce2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ce2[t_day_t][t_time]=q1
            tea_ce2[t_day_t][t_time+1]=q1
            tea_ce2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ce2[t_day_t][t_time]=l
            rooms_ce2[t_day_t][t_time+1]=l
            rooms_ce2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ce2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CE2=[remaining_tutorials['CE2'][0]]+[remaining_tutorials['CE2'][0]]
def tutorial_assign_ce2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CE2[0]+remaining_tutorials_CE2[1]:
            a=random.choice(remaining_tutorials_CE2[0]+remaining_tutorials_CE2[1])
            tutorial_assign1_ce2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ce2(t_day_t,a,i,_c):
    global remaining_tutorials_CE2,tea_ce2,rooms_ce2,tt_ce2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CE2[_c].remove(a)
        choices_ce2.remove(a)
        occupy_teacher(q1)
        tea_ce2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ce2()
        rooms_ce2[t_day_t][t_time+i]=r
        tt_ce2[t_day_t][t_time+i]=a
        return
        

def room_assign1_ce2():
    global remaining_rooms,t_time,t_day
    return 'CEDEPT'


# In[542]:

pre_a_ms2=''
__count=0
def ms2():
    global tt_ms2,tea_ms2,rooms_ms2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ms2,t_day,_count,__count
    if rooms_ms2[2*t_day][t_time]==0 or tea_ms2[2*t_day][t_time] ==0:
        if not choices_ms2:
            return
        a=random.choice(choices_ms2)
        #print(a)
        if not a:
            return
        if a==pre_a_ms2 and len(a)>2:
            a=random.choice(choices_ms2)
        pre_a_ms2=a
        if a in depts['MS2'][0]:
            if a in lect_:
                
                tt_ms2[2*t_day][t_time]=a
                tt_ms2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ms2()
                else:
                    occupy_teacher(q1)
                    tea_ms2[2*t_day][t_time]=q1
                    tea_ms2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ms2()
                    if not r:
                        return
                    rooms_ms2[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ms2.remove(a)
            elif a in remaining_tutorials_MS2[0]+remaining_tutorials_MS2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_MS2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_MS2[0]+remaining_tutorials_MS2[1])
                tutorial_assign1_ms2(t_day_t,a,0,_c)
            else:
                __count+=1
                ms2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ms2[t_day_l][t_time]=a
                    tt_ms2[t_day_l][t_time+1]=a
                    tt_ms2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ms2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ms2[t_day_l][t_time]=q1
                        tea_ms2[t_day_l][t_time+1]=q1
                        tea_ms2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ms2[t_day_l][t_time]=l
                        rooms_ms2[t_day_l][t_time+1]=l
                        rooms_ms2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ms2.remove(a)
                        q=lab_assign_alternate_ms2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ms2(t_day_t,_c)
                        
            else:
                ms2()
                        
    return      
                        
                        
def lab_assign_alternate_ms2(t_day_t,_c):
    global tt_ms2,tea_ms2,rooms_ms2,t_time,labs_,lect_,lab_occupied_teachers,choices_ms2
    a=random.choice(depts['MS2'][1])
    if a in labs_:
        tt_ms2[t_day_t][t_time]=a
        tt_ms2[t_day_t][t_time+1]=a
        tt_ms2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ms2[t_day_t][t_time]=q1
            tea_ms2[t_day_t][t_time+1]=q1
            tea_ms2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ms2[t_day_t][t_time]=l
            rooms_ms2[t_day_t][t_time+1]=l
            rooms_ms2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ms2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_MS2=[remaining_tutorials['MS2'][0]]+[remaining_tutorials['MS2'][0]]
def tutorial_assign_ms2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_MS2[0]+remaining_tutorials_MS2[1]:
            a=random.choice(remaining_tutorials_MS2[0]+remaining_tutorials_MS2[1])
            tutorial_assign1_ms2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ms2(t_day_t,a,i,_c):
    global remaining_tutorials_MS2,tea_ms2,rooms_ms2,tt_ms2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_MS2[_c].remove(a)
        choices_ms2.remove(a)
        occupy_teacher(q1)
        tea_ms2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ms2()
        rooms_ms2[t_day_t][t_time+i]=r
        tt_ms2[t_day_t][t_time+i]=a
        return

def room_assign1_ms2():
    global remaining_rooms,t_time,t_day
    
    return 'MSDEPT'


# In[543]:

pre_a_me2=''
__count=0
def me2():
    global tt_me2,tea_me2,rooms_me2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_me2,t_day,_count,__count
    if rooms_me2[2*t_day][t_time]==0 or tea_me2[2*t_day][t_time] ==0:
        if not choices_me2:
            return
        a=random.choice(choices_me2)
        #print(a)
        if not a:
            return
        if a==pre_a_me2 and len(a)>2:
            a=random.choice(choices_me2)
        pre_a_me2=a
        if a in depts['ME2'][0]:
            if a in lect_:
                
                tt_me2[2*t_day][t_time]=a
                tt_me2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    me2()
                else:
                    occupy_teacher(q1)
                    tea_me2[2*t_day][t_time]=q1
                    tea_me2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_me2()
                    if not r:
                        return
                    rooms_me2[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_me2.remove(a)
            elif a in remaining_tutorials_ME2[0]+remaining_tutorials_ME2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ME2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_ME2[0]+remaining_tutorials_ME2[1])
                tutorial_assign1_me2(t_day_t,a,0,_c)
            else:
                __count+=1
                me2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_me2[t_day_l][t_time]=a
                    tt_me2[t_day_l][t_time+1]=a
                    tt_me2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        me2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_me2[t_day_l][t_time]=q1
                        tea_me2[t_day_l][t_time+1]=q1
                        tea_me2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_me2[t_day_l][t_time]=l
                        rooms_me2[t_day_l][t_time+1]=l
                        rooms_me2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_me2.remove(a)
                        q=lab_assign_alternate_me2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_me2(t_day_t,_c)
                        
            else:
                me2()
                        
    return      
                        
                        
def lab_assign_alternate_me2(t_day_t,_c):
    global tt_me2,tea_me2,rooms_me2,t_time,labs_,lect_,lab_occupied_teachers,choices_me2
    a=random.choice(depts['ME2'][1])
    if a in labs_:
        tt_me2[t_day_t][t_time]=a
        tt_me2[t_day_t][t_time+1]=a
        tt_me2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_me2[t_day_t][t_time]=q1
            tea_me2[t_day_t][t_time+1]=q1
            tea_me2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_me2[t_day_t][t_time]=l
            rooms_me2[t_day_t][t_time+1]=l
            rooms_me2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_me2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ME2=[remaining_tutorials['ME2'][0]]+[remaining_tutorials['ME2'][0]]
def tutorial_assign_me2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ME2[0]+remaining_tutorials_ME2[1]:
            a=random.choice(remaining_tutorials_ME2[0]+remaining_tutorials_ME2[1])
            tutorial_assign1_me2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_me2(t_day_t,a,i,_c):
    global remaining_tutorials_ME2,tea_me2,rooms_me2,tt_me2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ME2[_c].remove(a)
        choices_me2.remove(a)
        occupy_teacher(q1)
        tea_me2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_me2()
        rooms_me2[t_day_t][t_time+i]=r
        tt_me2[t_day_t][t_time+i]=a
        return

def room_assign1_me2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_me2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_me2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_me2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_me2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[544]:

pre_a_ec2=''
__count=0
def ec2():
    global tt_ec2,tea_ec2,rooms_ec2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ec2,t_day,_count,__count
    if rooms_ec2[2*t_day][t_time]==0 or tea_ec2[2*t_day][t_time] ==0:
        if not choices_ec2:
            return
        a=random.choice(choices_ec2)
        #print(a)
        if not a:
            return
        if a==pre_a_ec2 and len(a)>2:
            a=random.choice(choices_ec2)
        pre_a_ec2=a
        if a in depts['EC2'][0]:
            if a in lect_:
                
                tt_ec2[2*t_day][t_time]=a
                tt_ec2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ec2()
                else:
                    occupy_teacher(q1)
                    tea_ec2[2*t_day][t_time]=q1
                    tea_ec2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ec2()
                    if not r:
                        return
                    rooms_ec2[2*t_day][t_time]=r
                    rooms_ec2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ec2.remove(a)
            elif a in remaining_tutorials_EC2[0]+remaining_tutorials_EC2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EC2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_EC2[0]+remaining_tutorials_EC2[1])
                tutorial_assign1_ec2(t_day_t,a,0,_c)
            else:
                __count+=1
                ec2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ec2[t_day_l][t_time]=a
                    tt_ec2[t_day_l][t_time+1]=a
                    tt_ec2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ec2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ec2[t_day_l][t_time]=q1
                        tea_ec2[t_day_l][t_time+1]=q1
                        tea_ec2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ec2[t_day_l][t_time]=l
                        rooms_ec2[t_day_l][t_time+1]=l
                        rooms_ec2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ec2.remove(a)
                        q=lab_assign_alternate_ec2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ec2(t_day_t,_c)
                        
            else:
                ec2()
                        
    return      
                        
                        
def lab_assign_alternate_ec2(t_day_t,_c):
    global tt_ec2,tea_ec2,rooms_ec2,t_time,labs_,lect_,lab_occupied_teachers,choices_ec2
    a=random.choice(depts['EC2'][1])
    if a in labs_:
        tt_ec2[t_day_t][t_time]=a
        tt_ec2[t_day_t][t_time+1]=a
        tt_ec2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ec2[t_day_t][t_time]=q1
            tea_ec2[t_day_t][t_time+1]=q1
            tea_ec2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ec2[t_day_t][t_time]=l
            rooms_ec2[t_day_t][t_time+1]=l
            rooms_ec2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ec2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EC2=[remaining_tutorials['EC2'][0]]+[remaining_tutorials['EC2'][0]]
def tutorial_assign_ec2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EC2[0]+remaining_tutorials_EC2[1]:
            a=random.choice(remaining_tutorials_EC2[0]+remaining_tutorials_EC2[1])
            tutorial_assign1_ec2(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ec2(t_day_t,a,i,_c):
    global remaining_tutorials_EC2,tea_ec2,rooms_ec2,tt_ec2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EC2[_c].remove(a)
        choices_ec2.remove(a)
        occupy_teacher(q1)
        tea_ec2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ec2()
        rooms_ec2[t_day_t][t_time+i]=r
        tt_ec2[t_day_t][t_time+i]=a
        return

def room_assign1_ec2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ec2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ec2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ec2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ec2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[545]:

pre_a_ee2=''
__count=0
def ee2():
    global tt_ee2,tea_ee2,rooms_ee2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ee2,t_day,_count,__count
    if rooms_ee2[2*t_day][t_time]==0 or tea_ee2[2*t_day][t_time] ==0:
        if not choices_ee2:
            return
        a=random.choice(choices_ee2)
        #print(a)
        if not a:
            return
        if a==pre_a_ee2 and len(a)>2:
            a=random.choice(choices_ee2)
        pre_a_ee2=a
        if a in depts['EE2'][0]:
            if a in lect_:
                
                tt_ee2[2*t_day][t_time]=a
                tt_ee2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ee2()
                else:
                    occupy_teacher(q1)
                    tea_ee2[2*t_day][t_time]=q1
                    tea_ee2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ee2()
                    if not r:
                        return
                    rooms_ee2[2*t_day][t_time]=r
                    rooms_ee2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ee2.remove(a)
            elif a in remaining_tutorials_EE2[0]+remaining_tutorials_EE2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EE2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ee2_1(t_day_t,_c)
            else:
                __count+=1
                ee2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ee2[t_day_l][t_time]=a
                    tt_ee2[t_day_l][t_time+1]=a
                    tt_ee2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ee2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ee2[t_day_l][t_time]=q1
                        tea_ee2[t_day_l][t_time+1]=q1
                        tea_ee2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ee2[t_day_l][t_time]=l
                        rooms_ee2[t_day_l][t_time+1]=l
                        rooms_ee2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ee2.remove(a)
                        q=lab_assign_alternate_ee2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ee2(t_day_t,_c)
                        
            else:
                ee2()
                        
    return      
                        
                        
def lab_assign_alternate_ee2(t_day_t,_c):
    global tt_ee2,tea_ee2,rooms_ee2,t_time,labs_,lect_,lab_occupied_teachers,choices_ee2
    a=random.choice(depts['EE2'][1])
    if a in labs_:
        tt_ee2[t_day_t][t_time]=a
        tt_ee2[t_day_t][t_time+1]=a
        tt_ee2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ee2[t_day_t][t_time]=q1
            tea_ee2[t_day_t][t_time+1]=q1
            tea_ee2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ee2[t_day_t][t_time]=l
            rooms_ee2[t_day_t][t_time+1]=l
            rooms_ee2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ee2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EE2=[remaining_tutorials['EE2'][0]]+[remaining_tutorials['EE2'][0]]
def tutorial_assign_ee2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EE2[0]+remaining_tutorials_EE2[1]:
            a=random.choice(remaining_tutorials_EE2[0]+remaining_tutorials_EE2[1])
            tutorial_assign1_ee2(t_day_t,a,i,_c)
    return

def tutorial_assign_ee2_1(t_day_t,_c):
    if remaining_tutorials_EE2[0]+remaining_tutorials_EE2[1]:
        a=random.choice(remaining_tutorials_EE2[0]+remaining_tutorials_EE2[1])
        tutorial_assign1_ee2(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ee2(t_day_t,a,i,_c):
    global remaining_tutorials_EE2,tea_ee2,rooms_ee2,tt_ee2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EE2[_c].remove(a)
        choices_ee2.remove(a)
        occupy_teacher(q1)
        tea_ee2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ee2()
        rooms_ee2[t_day_t][t_time+i]=r
        tt_ee2[t_day_t][t_time+i]=a
        return

def room_assign1_ee2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ee2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ee2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ee2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ee2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[546]:
pre_a_cd2=''

__count=0
def cd2():
    global tt_cd2,tea_cd2,rooms_cd2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cd2,t_day,_count,__count
    if rooms_cd2[2*t_day][t_time]==0 or tea_cd2[2*t_day][t_time] ==0:
        if not choices_cd2:
            return
        a=random.choice(choices_cd2)
        #print(a)
        if not a:
            return
        if a==pre_a_cd2 and len(a)>2:
            a=random.choice(choices_cd2)
        pre_a_cd2=a
        if a in depts['CD2'][0]:
            if a in lect_:
                
                tt_cd2[2*t_day][t_time]=a
                tt_cd2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cd2()
                else:
                    occupy_teacher(q1)
                    tea_cd2[2*t_day][t_time]=q1
                    tea_cd2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cd2()
                    if not r:
                        return
                    rooms_cd2[2*t_day][t_time]=r
                    rooms_cd2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cd2.remove(a)
                    #print(a)
            elif a in remaining_tutorials_CD2[0]+remaining_tutorials_CD2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CD2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_cd2_1(t_day_t,_c)
            else:
                __count+=1
                cd2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cd2[t_day_l][t_time]=a
                    tt_cd2[t_day_l][t_time+1]=a
                    tt_cd2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cd2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cd2[t_day_l][t_time]=q1
                        tea_cd2[t_day_l][t_time+1]=q1
                        tea_cd2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cd2[t_day_l][t_time]=l
                        rooms_cd2[t_day_l][t_time+1]=l
                        rooms_cd2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cd2.remove(a)
                        q=lab_assign_alternate_cd2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cd2(t_day_t,_c)
                        
            else:
                cd2()
                        
    return      
                        
                        
def lab_assign_alternate_cd2(t_day_t,_c):
    global tt_cd2,tea_cd2,rooms_cd2,t_time,labs_,lect_,lab_occupied_teachers,choices_cd2
    a=random.choice(depts['CD2'][1])
    if a in labs_:
        tt_cd2[t_day_t][t_time]=a
        tt_cd2[t_day_t][t_time+1]=a
        tt_cd2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cd2[t_day_t][t_time]=q1
            tea_cd2[t_day_t][t_time+1]=q1
            tea_cd2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cd2[t_day_t][t_time]=l
            rooms_cd2[t_day_t][t_time+1]=l
            rooms_cd2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cd2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CD2=[remaining_tutorials['CD2'][0]]+[remaining_tutorials['CD2'][0]]
def tutorial_assign_cd2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CD2[0]+remaining_tutorials_CD2[1]:
            a=random.choice(remaining_tutorials_CD2[0]+remaining_tutorials_CD2[1])
            tutorial_assign1_cd2(t_day_t,a,i,_c)
    return

def tutorial_assign_cd2_1(t_day_t,_c):

    if remaining_tutorials_CD2[0]+remaining_tutorials_CD2[1]:
        a=random.choice(remaining_tutorials_CD2[0]+remaining_tutorials_CD2[1])
        tutorial_assign1_cd2(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_cd2(t_day_t,a,i,_c):
    global remaining_tutorials_CD2,tea_cd2,rooms_cd2,tt_cd2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print(a)
        #print('cd')
        #print('1'+f'{remaining_tutorials_CD2}')
        remaining_tutorials_CD2[_c].remove(a)
        #print('2'+f'{choices_cd2}')
        choices_cd2.remove(a)
        occupy_teacher(q1)
        tea_cd2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cd2()
        rooms_cd2[t_day_t][t_time+i]=r
        tt_cd2[t_day_t][t_time+i]=a
        return

def room_assign1_cd2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cd2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cd2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_cd2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cd2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[547]:
pre_a_ed2=''

__count=0
def ed2():
    global tt_ed2,tea_ed2,rooms_ed2,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ed2,t_day,_count,__count
    if rooms_ed2[2*t_day][t_time]==0 or tea_ed2[2*t_day][t_time] ==0:
        if not choices_ed2:
            return
        a=random.choice(choices_ed2)
        #print(a)
        if not a:
            return
        if a==pre_a_ed2 and len(a)>2:
            a=random.choice(choices_ed2)
        pre_a_ed2=a
        if a in depts['ED2'][0]:
            if a in lect_:
                
                tt_ed2[2*t_day][t_time]=a
                tt_ed2[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ed2()
                else:
                    occupy_teacher(q1)
                    tea_ed2[2*t_day][t_time]=q1
                    tea_ed2[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ed2()
                    if not r:
                        return
                    rooms_ed2[2*t_day][t_time]=r
                    rooms_ed2[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ed2.remove(a)
            elif a in remaining_tutorials_ED2[0]+remaining_tutorials_ED2[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ED2[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ed2_1(t_day_t,_c)
            else:
                __count+=1
                ed2()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ed2[t_day_l][t_time]=a
                    tt_ed2[t_day_l][t_time+1]=a
                    tt_ed2[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ed2()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ed2[t_day_l][t_time]=q1
                        tea_ed2[t_day_l][t_time+1]=q1
                        tea_ed2[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ed2[t_day_l][t_time]=l
                        rooms_ed2[t_day_l][t_time+1]=l
                        rooms_ed2[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ed2.remove(a)
                        q=lab_assign_alternate_ed2(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ed2(t_day_t,_c)
                        
            else:
                ed2()
                        
    return      
                        
                        
def lab_assign_alternate_ed2(t_day_t,_c):
    global tt_ed2,tea_ed2,rooms_ed2,t_time,labs_,lect_,lab_occupied_teachers,choices_ed2
    a=random.choice(depts['ED2'][1])
    if a in labs_:
        tt_ed2[t_day_t][t_time]=a
        tt_ed2[t_day_t][t_time+1]=a
        tt_ed2[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ed2[t_day_t][t_time]=q1
            tea_ed2[t_day_t][t_time+1]=q1
            tea_ed2[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ed2[t_day_t][t_time]=l
            rooms_ed2[t_day_t][t_time+1]=l
            rooms_ed2[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ed2.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ED2=[remaining_tutorials['ED2'][0]]+[remaining_tutorials['ED2'][0]]
def tutorial_assign_ed2(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ED2[0]+remaining_tutorials_ED2[1]:
            a=random.choice(remaining_tutorials_ED2[0]+remaining_tutorials_ED2[1])
            tutorial_assign1_ed2(t_day_t,a,i,_c)
    return

def tutorial_assign_ed2_1(t_day_t,_c):
    if remaining_tutorials_ED2[0]+remaining_tutorials_ED2[1]:
            a=random.choice(remaining_tutorials_ED2[0]+remaining_tutorials_ED2[1])
            tutorial_assign1_ed2(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ed2(t_day_t,a,i,_c):
    global remaining_tutorials_ED2,tea_ed2,rooms_ed2,tt_ed2
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ED2[_c].remove(a)
        choices_ed2.remove(a)
        occupy_teacher(q1)
        tea_ed2[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ed2()
        rooms_ed2[t_day_t][t_time+i]=r
        tt_ed2[t_day_t][t_time+i]=a
        return

def room_assign1_ed2():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ed2[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed2[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ed2[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed2[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ed2[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed2[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ed2[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed2[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif remaining_rooms['F']:
        r=random.choice(remaining_rooms['F'])
        remaining_rooms['F'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[548]:

pre_a_cs3=''
__count=0
def cs3():
    global tt_cs3,tea_cs3,rooms_cs3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cs3,t_day,_count,__count
    if rooms_cs3[2*t_day][t_time]==0 or tea_cs3[2*t_day][t_time] ==0:
        if not choices_cs3:
            return
        a=random.choice(choices_cs3)
        #print(a)
        if not a:
            return
        if a==pre_a_cs3 and len(a)>2:
            a=random.choice(choices_cs3)
        pre_a_cs3=a
        if a in depts['CS3'][0]:
            if a in lect_:
                
                tt_cs3[2*t_day][t_time]=a
                tt_cs3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cs3()
                else:
                    occupy_teacher(q1)
                    tea_cs3[2*t_day][t_time]=q1
                    tea_cs3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cs3()
                    if not r:
                        return
                    rooms_cs3[2*t_day][t_time]=r
                    rooms_cs3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cs3.remove(a)
            elif a in remaining_tutorials_CS3[0]+remaining_tutorials_CS3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CS3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CS3[0]+remaining_tutorials_CS3[1])
                tutorial_assign1_cs3(t_day_t,a,0,_c)
            else:
                __count+=1
                cs3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cs3[t_day_l][t_time]=a
                    tt_cs3[t_day_l][t_time+1]=a
                    tt_cs3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cs3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cs3[t_day_l][t_time]=q1
                        tea_cs3[t_day_l][t_time+1]=q1
                        tea_cs3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cs3[t_day_l][t_time]=l
                        rooms_cs3[t_day_l][t_time+1]=l
                        rooms_cs3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cs3.remove(a)
                        q=lab_assign_alternate_cs3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cs3(t_day_t,_c)
                        
            else:
                cs3()
                        
    return      
                        
                        
def lab_assign_alternate_cs3(t_day_t,_c):
    global tt_cs3,tea_cs3,rooms_cs3,t_time,labs_,lect_,lab_occupied_teachers,choices_cs3
    a=random.choice(depts['CS3'][1])
    if a in labs_:
        tt_cs3[t_day_t][t_time]=a
        tt_cs3[t_day_t][t_time+1]=a
        tt_cs3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cs3[t_day_t][t_time]=q1
            tea_cs3[t_day_t][t_time+1]=q1
            tea_cs3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cs3[t_day_t][t_time]=l
            rooms_cs3[t_day_t][t_time+1]=l
            rooms_cs3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cs3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CS3=[remaining_tutorials['CS3'][0]]+[remaining_tutorials['CS3'][0]]
def tutorial_assign_cs3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CS3[0]+remaining_tutorials_CS3[1]:
            a=random.choice(remaining_tutorials_CS3[0]+remaining_tutorials_CS3[1])
            tutorial_assign1_cs3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_cs3(t_day_t,a,i,_c):
    global remaining_tutorials_CS3,tea_cs3,rooms_cs3,tt_cs3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print('cs')
        #print(a)
        #print('1'+f'{remaining_tutorials_CS3}')
        remaining_tutorials_CS3[_c].remove(a)
        #print('2'+f'{choices_cs3}')
        choices_cs3.remove(a)
        occupy_teacher(q1)
        tea_cs3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cs3()
        rooms_cs3[t_day_t][t_time+i]=r
        tt_cs3[t_day_t][t_time+i]=a
        return

def room_assign1_cs3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cs3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cs3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)     
    elif rooms_cs3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cs3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cs3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cs3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_cs3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cs3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
    return r


# In[549]:
pre_a_me3=''

__count=0
def me3():
    global tt_me3,tea_me3,rooms_me3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_me3,t_day,_count,__count
    if rooms_me3[2*t_day][t_time]==0 or tea_me3[2*t_day][t_time] ==0:
        if not choices_me3:
            return
        a=random.choice(choices_me3)
        #print(a)
        if not a:
            return
        if a==pre_a_me3 and len(a)>2:
            a=random.choice(choices_me3)
        pre_a_me3=a
        if a in depts['ME3'][0]:
            if a in lect_:
                
                tt_me3[2*t_day][t_time]=a
                tt_me3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    me3()
                else:
                    occupy_teacher(q1)
                    tea_me3[2*t_day][t_time]=q1
                    tea_me3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_me3()
                    if not r:
                        return
                    rooms_me3[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_me3.remove(a)
            elif a in remaining_tutorials_ME3[0]+remaining_tutorials_ME3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ME3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_ME3[0]+remaining_tutorials_ME3[1])
                tutorial_assign1_me3(t_day_t,a,0,_c)
            else:
                __count+=1
                me3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_me3[t_day_l][t_time]=a
                    tt_me3[t_day_l][t_time+1]=a
                    tt_me3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        me3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_me3[t_day_l][t_time]=q1
                        tea_me3[t_day_l][t_time+1]=q1
                        tea_me3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_me3[t_day_l][t_time]=l
                        rooms_me3[t_day_l][t_time+1]=l
                        rooms_me3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_me3.remove(a)
                        q=lab_assign_alternate_me3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_me3(t_day_t,_c)
                        
            else:
                me3()
                        
    return      
                        
                        
def lab_assign_alternate_me3(t_day_t,_c):
    global tt_me3,tea_me3,rooms_me3,t_time,labs_,lect_,lab_occupied_teachers,choices_me3
    a=random.choice(depts['ME3'][1])
    if a in labs_:
        tt_me3[t_day_t][t_time]=a
        tt_me3[t_day_t][t_time+1]=a
        tt_me3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_me3[t_day_t][t_time]=q1
            tea_me3[t_day_t][t_time+1]=q1
            tea_me3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_me3[t_day_t][t_time]=l
            rooms_me3[t_day_t][t_time+1]=l
            rooms_me3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_me3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ME3=[remaining_tutorials['ME3'][0]]+[remaining_tutorials['ME3'][0]]
def tutorial_assign_me3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ME3[0]+remaining_tutorials_ME3[1]:
            a=random.choice(remaining_tutorials_ME3[0]+remaining_tutorials_ME3[1])
            tutorial_assign1_me3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_me3(t_day_t,a,i,_c):
    global remaining_tutorials_ME3,tea_me3,rooms_me3,tt_me3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ME3[_c].remove(a)
        choices_me3.remove(a)
        occupy_teacher(q1)
        tea_me3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_me3()
        rooms_me3[t_day_t][t_time+i]=r
        tt_me3[t_day_t][t_time+i]=a
        return

def room_assign1_me3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_me3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_me3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_me3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_me3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_me3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_me3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_me3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_me3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['G'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
    return r


# In[550]:

pre_a_ec3=''
__count=0
def ec3():
    global tt_ec3,tea_ec3,rooms_ec3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ec3,t_day,_count,__count
    if rooms_ec3[2*t_day][t_time]==0 or tea_ec3[2*t_day][t_time] ==0:
        if not choices_ec3:
            return
        a=random.choice(choices_ec3)
        #print(a)
        if not a:
            return
        if a==pre_a_ec3 and len(a)>2:
            a=random.choice(choices_ec3)
        pre_a_ec3=a
        if a in depts['EC3'][0]:
            if a in lect_:
                
                tt_ec3[2*t_day][t_time]=a
                tt_ec3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ec3()
                else:
                    occupy_teacher(q1)
                    tea_ec3[2*t_day][t_time]=q1
                    tea_ec3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ec3()
                    if not r:
                        return
                    rooms_ec3[2*t_day][t_time]=r
                    rooms_ec3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ec3.remove(a)
            elif a in remaining_tutorials_EC3[0]+remaining_tutorials_EC3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EC3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_EC3[0]+remaining_tutorials_EC3[1])
                tutorial_assign1_ec3(t_day_t,a,0,_c)
            else:
                __count+=1
                ec3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ec3[t_day_l][t_time]=a
                    tt_ec3[t_day_l][t_time+1]=a
                    tt_ec3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ec3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ec3[t_day_l][t_time]=q1
                        tea_ec3[t_day_l][t_time+1]=q1
                        tea_ec3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ec3[t_day_l][t_time]=l
                        rooms_ec3[t_day_l][t_time+1]=l
                        rooms_ec3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ec3.remove(a)
                        q=lab_assign_alternate_ec3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ec3(t_day_t,_c)
                        
            else:
                ec3()
                        
    return      
                        
                        
def lab_assign_alternate_ec3(t_day_t,_c):
    global tt_ec3,tea_ec3,rooms_ec3,t_time,labs_,lect_,lab_occupied_teachers,choices_ec3
    a=random.choice(depts['EC3'][1])
    if a in labs_:
        tt_ec3[t_day_t][t_time]=a
        tt_ec3[t_day_t][t_time+1]=a
        tt_ec3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ec3[t_day_t][t_time]=q1
            tea_ec3[t_day_t][t_time+1]=q1
            tea_ec3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ec3[t_day_t][t_time]=l
            rooms_ec3[t_day_t][t_time+1]=l
            rooms_ec3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ec3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EC3=[remaining_tutorials['EC3'][0]]+[remaining_tutorials['EC3'][0]]
def tutorial_assign_ec3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EC3[0]+remaining_tutorials_EC3[1]:
            a=random.choice(remaining_tutorials_EC3[0]+remaining_tutorials_EC3[1])
            tutorial_assign1_ec3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ec3(t_day_t,a,i,_c):
    global remaining_tutorials_EC3,tea_ec3,rooms_ec3,tt_ec3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EC3[_c].remove(a)
        choices_ec3.remove(a)
        occupy_teacher(q1)
        tea_ec3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ec3()
        rooms_ec3[t_day_t][t_time+i]=r
        tt_ec3[t_day_t][t_time+i]=a
        return

def room_assign1_ec3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ec3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ec3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ec3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ec3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ec3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ec3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ec3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ec3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['G'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
    return r


# In[551]:

pre_a_ee3=''
__count=0
count_ee3=0
def ee3():
    global tt_ee3,tea_ee3,rooms_ee3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ee3,t_day,_count,__count,count_ee3
    if rooms_ee3[2*t_day][t_time]==0 or tea_ee3[2*t_day][t_time] ==0:
        if not choices_ee3:
            return
        a=random.choice(choices_ee3)
        #print(a)
        if not a:
            return
        if a==pre_a_ee3 and len(a)>2:
            a=random.choice(choices_ee3)
        pre_a_ee3=a
        if a in depts['EE3'][0]:
            if a in lect_:
                
                tt_ee3[2*t_day][t_time]=a
                tt_ee3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    if count_ee3>2:
                        count_ee3=0
                        return
                    count_ee3+=1
                    ee3()
                else:
                    occupy_teacher(q1)
                    tea_ee3[2*t_day][t_time]=q1
                    tea_ee3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ee3()
                    if not r:
                        return
                    rooms_ee3[2*t_day][t_time]=r
                    rooms_ee3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ee3.remove(a)
            elif a in remaining_tutorials_EE3[0]+remaining_tutorials_EE3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EE3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ee3_1(t_day_t,_c)
            else:
                __count+=1
                ee3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ee3[t_day_l][t_time]=a
                    tt_ee3[t_day_l][t_time+1]=a
                    tt_ee3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ee3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ee3[t_day_l][t_time]=q1
                        tea_ee3[t_day_l][t_time+1]=q1
                        tea_ee3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ee3[t_day_l][t_time]=l
                        rooms_ee3[t_day_l][t_time+1]=l
                        rooms_ee3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ee3.remove(a)
                        q=lab_assign_alternate_ee3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ee3(t_day_t,_c)
                        
            else:
                ee3()
                        
    return      
                        
                        
def lab_assign_alternate_ee3(t_day_t,_c):
    global tt_ee3,tea_ee3,rooms_ee3,t_time,labs_,lect_,lab_occupied_teachers,choices_ee3
    a=random.choice(depts['EE3'][1])
    if a in labs_:
        tt_ee3[t_day_t][t_time]=a
        tt_ee3[t_day_t][t_time+1]=a
        tt_ee3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ee3[t_day_t][t_time]=q1
            tea_ee3[t_day_t][t_time+1]=q1
            tea_ee3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ee3[t_day_t][t_time]=l
            rooms_ee3[t_day_t][t_time+1]=l
            rooms_ee3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ee3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EE3=[remaining_tutorials['EE3'][0]]+[remaining_tutorials['EE3'][0]]
def tutorial_assign_ee3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EE3[0]+remaining_tutorials_EE3[1]:
            a=random.choice(remaining_tutorials_EE3[0]+remaining_tutorials_EE3[1])
            tutorial_assign1_ee3(t_day_t,a,i,_c)
    return

def tutorial_assign_ee3_1(t_day_t,_c):
    if remaining_tutorials_EE3[0]+remaining_tutorials_EE3[1]:
        a=random.choice(remaining_tutorials_EE3[0]+remaining_tutorials_EE3[1])
        tutorial_assign1_ee3(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ee3(t_day_t,a,i,_c):
    global remaining_tutorials_EE3,tea_ee3,rooms_ee3,tt_ee3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EE3[_c].remove(a)
        choices_ee3.remove(a)
        occupy_teacher(q1)
        tea_ee3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ee3()
        rooms_ee3[t_day_t][t_time+i]=r
        tt_ee3[t_day_t][t_time+i]=a
        return

def room_assign1_ee3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ee3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ee3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ee3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ee3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ee3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ee3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ee3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ee3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['G'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
    return r


# In[552]:

pre_a_cd3=''
__count=0
def cd3():
    global tt_cd3,tea_cd3,rooms_cd3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cd3,t_day,_count,__count
    if rooms_cd3[2*t_day][t_time]==0 or tea_cd3[2*t_day][t_time] ==0:
        if not choices_cd3:
            return
        a=random.choice(choices_cd3)
        #print(a)
        if not a:
            return
        if a==pre_a_cd3 and len(a)>2:
            a=random.choice(choices_cd3)
        pre_a_cd3=a
        if a in depts['CD3'][0]:
            if a in lect_:
                
                tt_cd3[2*t_day][t_time]=a
                tt_cd3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cd3()
                else:
                    occupy_teacher(q1)
                    tea_cd3[2*t_day][t_time]=q1
                    tea_cd3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cd3()
                    if not r:
                        return
                    rooms_cd3[2*t_day][t_time]=r
                    rooms_cd3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cd3.remove(a)
                    #print(a)
            elif a in remaining_tutorials_CD3[0]+remaining_tutorials_CD3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CD3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_cd3_1(t_day_t,_c)
            else:
                __count+=1
                cd3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cd3[t_day_l][t_time]=a
                    tt_cd3[t_day_l][t_time+1]=a
                    tt_cd3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cd3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cd3[t_day_l][t_time]=q1
                        tea_cd3[t_day_l][t_time+1]=q1
                        tea_cd3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cd3[t_day_l][t_time]=l
                        rooms_cd3[t_day_l][t_time+1]=l
                        rooms_cd3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cd3.remove(a)
                        q=lab_assign_alternate_cd3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cd3(t_day_t,_c)
                        
            else:
                cd3()
                        
    return      
                        
                        
def lab_assign_alternate_cd3(t_day_t,_c):
    global tt_cd3,tea_cd3,rooms_cd3,t_time,labs_,lect_,lab_occupied_teachers,choices_cd3
    a=random.choice(depts['CD3'][1])
    if a in labs_:
        tt_cd3[t_day_t][t_time]=a
        tt_cd3[t_day_t][t_time+1]=a
        tt_cd3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cd3[t_day_t][t_time]=q1
            tea_cd3[t_day_t][t_time+1]=q1
            tea_cd3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cd3[t_day_t][t_time]=l
            rooms_cd3[t_day_t][t_time+1]=l
            rooms_cd3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cd3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CD3=[remaining_tutorials['CD3'][0]]+[remaining_tutorials['CD3'][0]]
def tutorial_assign_cd3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CD3[0]+remaining_tutorials_CD3[1]:
            a=random.choice(remaining_tutorials_CD3[0]+remaining_tutorials_CD3[1])
            tutorial_assign1_cd3(t_day_t,a,i,_c)
    return

def tutorial_assign_cd3_1(t_day_t,_c):

    if remaining_tutorials_CD3[0]+remaining_tutorials_CD3[1]:
        a=random.choice(remaining_tutorials_CD3[0]+remaining_tutorials_CD3[1])
        tutorial_assign1_cd3(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_cd3(t_day_t,a,i,_c):
    global remaining_tutorials_CD3,tea_cd3,rooms_cd3,tt_cd3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print(a)
        #print('cd')
        #print('1'+f'{remaining_tutorials_CD3}')
        remaining_tutorials_CD3[_c].remove(a)
        #print('2'+f'{choices_cd3}')
        choices_cd3.remove(a)
        occupy_teacher(q1)
        tea_cd3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cd3()
        rooms_cd3[t_day_t][t_time+i]=r
        tt_cd3[t_day_t][t_time+i]=a
        return

def room_assign1_cd3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cd3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cd3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_cd3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cd3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_cd3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cd3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_cd3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cd3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['G'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
    return r


# In[553]:

pre_a_ed3=''
__count=0
def ed3():
    global tt_ed3,tea_ed3,rooms_ed3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ed3,t_day,_count,__count
    if rooms_ed3[2*t_day][t_time]==0 or tea_ed3[2*t_day][t_time] ==0:
        if not choices_ed3:
            return
        a=random.choice(choices_ed3)
        #print(a)
        if not a:
            return
        if a==pre_a_ed3 and len(a)>2:
            a=random.choice(choices_ed3)
        pre_a_ed3=a
        if a in depts['ED3'][0]:
            if a in lect_:
                
                tt_ed3[2*t_day][t_time]=a
                tt_ed3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ed3()
                else:
                    occupy_teacher(q1)
                    tea_ed3[2*t_day][t_time]=q1
                    tea_ed3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ed3()
                    if not r:
                        return
                    rooms_ed3[2*t_day][t_time]=r
                    rooms_ed3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ed3.remove(a)
            elif a in remaining_tutorials_ED3[0]+remaining_tutorials_ED3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ED3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ed3_1(t_day_t,_c)
            else:
                __count+=1
                ed3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ed3[t_day_l][t_time]=a
                    tt_ed3[t_day_l][t_time+1]=a
                    tt_ed3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ed3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ed3[t_day_l][t_time]=q1
                        tea_ed3[t_day_l][t_time+1]=q1
                        tea_ed3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ed3[t_day_l][t_time]=l
                        rooms_ed3[t_day_l][t_time+1]=l
                        rooms_ed3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ed3.remove(a)
                        q=lab_assign_alternate_ed3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ed3(t_day_t,_c)
                        
            else:
                ed3()
                        
    return      
                        
                        
def lab_assign_alternate_ed3(t_day_t,_c):
    global tt_ed3,tea_ed3,rooms_ed3,t_time,labs_,lect_,lab_occupied_teachers,choices_ed3
    a=random.choice(depts['ED3'][1])
    if a in labs_:
        tt_ed3[t_day_t][t_time]=a
        tt_ed3[t_day_t][t_time+1]=a
        tt_ed3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ed3[t_day_t][t_time]=q1
            tea_ed3[t_day_t][t_time+1]=q1
            tea_ed3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ed3[t_day_t][t_time]=l
            rooms_ed3[t_day_t][t_time+1]=l
            rooms_ed3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ed3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ED3=[remaining_tutorials['ED3'][0]]+[remaining_tutorials['ED3'][0]]
def tutorial_assign_ed3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ED3[0]+remaining_tutorials_ED3[1]:
            a=random.choice(remaining_tutorials_ED3[0]+remaining_tutorials_ED3[1])
            tutorial_assign1_ed3(t_day_t,a,i,_c)
    return

def tutorial_assign_ed3_1(t_day_t,_c):
    if remaining_tutorials_ED3[0]+remaining_tutorials_ED3[1]:
            a=random.choice(remaining_tutorials_ED3[0]+remaining_tutorials_ED3[1])
            tutorial_assign1_ed3(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ed3(t_day_t,a,i,_c):
    global remaining_tutorials_ED3,tea_ed3,rooms_ed3,tt_ed3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ED3[_c].remove(a)
        choices_ed3.remove(a)
        occupy_teacher(q1)
        tea_ed3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ed3()
        rooms_ed3[t_day_t][t_time+i]=r
        tt_ed3[t_day_t][t_time+i]=a
        return

def room_assign1_ed3():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ed3[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed3[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ed3[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed3[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ed3[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed3[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ed3[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed3[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ed3[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ed3[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ed3[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ed3[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif remaining_rooms['S']:
        r=random.choice(remaining_rooms['S'])
        remaining_rooms['S'].remove(r)
    else:
        r=random.choice(remaining_rooms['B']+remaining_rooms['F']+remaining_rooms['G'])
        if r in rooms['B']:
            remaining_rooms['B'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
    return r


# In[554]:
pre_a_ch3=''

def ch3():
    global tt_ch3,tea_ch3,rooms_ch3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ch3,t_day,_count
    if rooms_ch3[2*t_day][t_time]==0 or tea_ch3[2*t_day][t_time] ==0:
        if not choices_ch3:
            return
        a=random.choice(choices_ch3)
        #print(a)
        if not a:
            return
        if a==pre_a_ch3 and len(a)>2:
            a=random.choice(choices_ch3)
        pre_a_ch3=a
        if a in depts['CH3'][0]:
            if a in lect_:
                
                tt_ch3[2*t_day][t_time]=a
                tt_ch3[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ch3()
                else:
                    occupy_teacher(q1)
                    tea_ch3[2*t_day][t_time]=q1
                    tea_ch3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ch3()
                    if not r:
                        return
                    rooms_ch3[2*t_day][t_time]=r
                    rooms_ch3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ch3.remove(a)
                    
            elif a in remaining_tutorials_CH3[0]+remaining_tutorials_CH3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CH3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CH3[0]+remaining_tutorials_CH3[1])
                tutorial_assign1_ch3(t_day_t,a,0,_c)
        
            else:
                ch3()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ch3[t_day_l][t_time]=a
                    tt_ch3[t_day_l][t_time+1]=a
                    tt_ch3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ch3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ch3[t_day_l][t_time]=q1
                        tea_ch3[t_day_l][t_time+1]=q1
                        tea_ch3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ch3[t_day_l][t_time]=l
                        rooms_ch3[t_day_l][t_time+1]=l
                        rooms_ch3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ch3.remove(a)
                        q=lab_assign_alternate_ch3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ch3(t_day_t,_c)
                        
            else:
                ch3()
                        
    return      
                        
                        
def lab_assign_alternate_ch3(t_day_t,_c):
    global tt_ch3,tea_ch3,rooms_ch3,t_time,labs_,lect_,lab_occupied_teachers,choices_ch3
    a=random.choice(depts['CH3'][1])
    if a in labs_:
        tt_ch3[t_day_t][t_time]=a
        tt_ch3[t_day_t][t_time+1]=a
        tt_ch3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ch3[t_day_t][t_time]=q1
            tea_ch3[t_day_t][t_time+1]=q1
            tea_ch3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ch3[t_day_t][t_time]=l
            rooms_ch3[t_day_t][t_time+1]=l
            rooms_ch3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ch3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CH3=[remaining_tutorials['CH3'][0]]+[remaining_tutorials['CH3'][0]]
def tutorial_assign_ch3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CH3[0]+remaining_tutorials_CH3[1]:
            a=random.choice(remaining_tutorials_CH3[0]+remaining_tutorials_CH3[1])
            tutorial_assign1_ch3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ch3(t_day_t,a,i,_c):
    global remaining_tutorials_CH3,tea_ch3,rooms_ch3,tt_ch3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CH3[_c].remove(a)
        choices_ch3.remove(a)
        occupy_teacher(q1)
        tea_ch3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ch3()
        rooms_ch3[t_day_t][t_time+i]=r
        tt_ch3[t_day_t][t_time+i]=a
        return
        

def room_assign1_ch3():
    global remaining_rooms,t_time,t_day
    return 'CHDEPT'


# In[555]:

pre_a_ce3=''
def ce3():
    global tt_ce3,tea_ce3,rooms_ce3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ce3,t_day,_count
    if rooms_ce3[2*t_day][t_time]==0 or tea_ce3[2*t_day][t_time] ==0:
        if not choices_ce3:
            return
        a=random.choice(choices_ce3)
        #print(a)
        if not a:
            return
        if a==pre_a_ce3 and len(a)>2:
            a=random.choice(choices_ce3)
        pre_a_ce3=a
        if a in depts['CE3'][0]:
            if a in lect_:
                
                tt_ce3[2*t_day][t_time]=a
                tt_ce3[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ce3()
                else:
                    occupy_teacher(q1)
                    tea_ce3[2*t_day][t_time]=q1
                    tea_ce3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ce3()
                    if not r:
                        return
                    rooms_ce3[2*t_day][t_time]=r
                    rooms_ce3[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ce3.remove(a)
                    
            elif a in remaining_tutorials_CE3[0]+remaining_tutorials_CE3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CE3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CE3[0]+remaining_tutorials_CE3[1])
                tutorial_assign1_ce3(t_day_t,a,0,_c)
        
            else:
                ce3()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ce3[t_day_l][t_time]=a
                    tt_ce3[t_day_l][t_time+1]=a
                    tt_ce3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ce3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ce3[t_day_l][t_time]=q1
                        tea_ce3[t_day_l][t_time+1]=q1
                        tea_ce3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ce3[t_day_l][t_time]=l
                        rooms_ce3[t_day_l][t_time+1]=l
                        rooms_ce3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ce3.remove(a)
                        q=lab_assign_alternate_ce3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ce3(t_day_t,_c)
                        
            else:
                ce3()
                        
    return      
                        
                        
def lab_assign_alternate_ce3(t_day_t,_c):
    global tt_ce3,tea_ce3,rooms_ce3,t_time,labs_,lect_,lab_occupied_teachers,choices_ce3
    a=random.choice(depts['CE3'][1])
    if a in labs_:
        tt_ce3[t_day_t][t_time]=a
        tt_ce3[t_day_t][t_time+1]=a
        tt_ce3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ce3[t_day_t][t_time]=q1
            tea_ce3[t_day_t][t_time+1]=q1
            tea_ce3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ce3[t_day_t][t_time]=l
            rooms_ce3[t_day_t][t_time+1]=l
            rooms_ce3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ce3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CE3=[remaining_tutorials['CE3'][0]]+[remaining_tutorials['CE3'][0]]
def tutorial_assign_ce3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CE3[0]+remaining_tutorials_CE3[1]:
            a=random.choice(remaining_tutorials_CE3[0]+remaining_tutorials_CE3[1])
            tutorial_assign1_ce3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ce3(t_day_t,a,i,_c):
    global remaining_tutorials_CE3,tea_ce3,rooms_ce3,tt_ce3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CE3[_c].remove(a)
        choices_ce3.remove(a)
        occupy_teacher(q1)
        tea_ce3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ce3()
        rooms_ce3[t_day_t][t_time+i]=r
        tt_ce3[t_day_t][t_time+i]=a
        return
        

def room_assign1_ce3():
    global remaining_rooms,t_time,t_day
    return 'CEDEPT'


# In[556]:

pre_a_ms3=''
__count=0
def ms3():
    global tt_ms3,tea_ms3,rooms_ms3,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ms3,t_day,_count,__count
    if rooms_ms3[2*t_day][t_time]==0 or tea_ms3[2*t_day][t_time] ==0:
        if not choices_ms3:
            return
        a=random.choice(choices_ms3)
        #print(a)
        if not a:
            return
        if a==pre_a_ms3 and len(a)>2:
            a=random.choice(choices_ms3)
        pre_a_ms3=a
        if a in depts['MS3'][0]:
            if a in lect_:
                
                tt_ms3[2*t_day][t_time]=a
                tt_ms3[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ms3()
                else:
                    occupy_teacher(q1)
                    tea_ms3[2*t_day][t_time]=q1
                    tea_ms3[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ms3()
                    if not r:
                        return
                    rooms_ms3[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ms3.remove(a)
            elif a in remaining_tutorials_MS3[0]+remaining_tutorials_MS3[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_MS3[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_MS3[0]+remaining_tutorials_MS3[1])
                tutorial_assign1_ms3(t_day_t,a,0,_c)
            else:
                __count+=1
                ms3()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ms3[t_day_l][t_time]=a
                    tt_ms3[t_day_l][t_time+1]=a
                    tt_ms3[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ms3()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ms3[t_day_l][t_time]=q1
                        tea_ms3[t_day_l][t_time+1]=q1
                        tea_ms3[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ms3[t_day_l][t_time]=l
                        rooms_ms3[t_day_l][t_time+1]=l
                        rooms_ms3[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ms3.remove(a)
                        q=lab_assign_alternate_ms3(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ms3(t_day_t,_c)
                        
            else:
                ms3()
                        
    return      
                        
                        
def lab_assign_alternate_ms3(t_day_t,_c):
    global tt_ms3,tea_ms3,rooms_ms3,t_time,labs_,lect_,lab_occupied_teachers,choices_ms3
    a=random.choice(depts['MS3'][1])
    if a in labs_:
        tt_ms3[t_day_t][t_time]=a
        tt_ms3[t_day_t][t_time+1]=a
        tt_ms3[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ms3[t_day_t][t_time]=q1
            tea_ms3[t_day_t][t_time+1]=q1
            tea_ms3[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ms3[t_day_t][t_time]=l
            rooms_ms3[t_day_t][t_time+1]=l
            rooms_ms3[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ms3.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_MS3=[remaining_tutorials['MS3'][0]]+[remaining_tutorials['MS3'][0]]
def tutorial_assign_ms3(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_MS3[0]+remaining_tutorials_MS3[1]:
            a=random.choice(remaining_tutorials_MS3[0]+remaining_tutorials_MS3[1])
            tutorial_assign1_ms3(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ms3(t_day_t,a,i,_c):
    global remaining_tutorials_MS3,tea_ms3,rooms_ms3,tt_ms3
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_MS3[_c].remove(a)
        choices_ms3.remove(a)
        occupy_teacher(q1)
        tea_ms3[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ms3()
        rooms_ms3[t_day_t][t_time+i]=r
        tt_ms3[t_day_t][t_time+i]=a
        return

def room_assign1_ms3():
    global remaining_rooms,t_time,t_day
    
    return 'MSDEPT'


# In[ ]:





# In[557]:

pre_a_cs4=''
__count=0
def cs4():
    global tt_cs4,tea_cs4,rooms_cs4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cs4,t_day,_count,__count
    if rooms_cs4[2*t_day][t_time]==0 or tea_cs4[2*t_day][t_time] ==0:
        if not choices_cs4:
            return
        a=random.choice(choices_cs4)
        #print(a)
        if not a:
            return
        if a==pre_a_cs4 and len(a)>2:
            a=random.choice(choices_cs4)
        pre_a_cs4=a
        if a in depts['CS4'][0]:
            if a in lect_:
                
                tt_cs4[2*t_day][t_time]=a
                tt_cs4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    cs4()
                else:
                    occupy_teacher(q1)
                    tea_cs4[2*t_day][t_time]=q1
                    tea_cs4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cs4()
                    if not r:
                        return
                    rooms_cs4[2*t_day][t_time]=r
                    rooms_cs4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cs4.remove(a)
            elif a in remaining_tutorials_CS4[0]+remaining_tutorials_CS4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CS4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CS4[0]+remaining_tutorials_CS4[1])
                tutorial_assign1_cs4(t_day_t,a,0,_c)
            else:
                __count+=1
                cs4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cs4[t_day_l][t_time]=a
                    tt_cs4[t_day_l][t_time+1]=a
                    tt_cs4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cs4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cs4[t_day_l][t_time]=q1
                        tea_cs4[t_day_l][t_time+1]=q1
                        tea_cs4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cs4[t_day_l][t_time]=l
                        rooms_cs4[t_day_l][t_time+1]=l
                        rooms_cs4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cs4.remove(a)
                        q=lab_assign_alternate_cs4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cs4(t_day_t,_c)
                        
            else:
                cs4()
                        
    return      
                        
                        
def lab_assign_alternate_cs4(t_day_t,_c):
    global tt_cs4,tea_cs4,rooms_cs4,t_time,labs_,lect_,lab_occupied_teachers,choices_cs4
    a=random.choice(depts['CS4'][1])
    if a in labs_:
        tt_cs4[t_day_t][t_time]=a
        tt_cs4[t_day_t][t_time+1]=a
        tt_cs4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cs4[t_day_t][t_time]=q1
            tea_cs4[t_day_t][t_time+1]=q1
            tea_cs4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cs4[t_day_t][t_time]=l
            rooms_cs4[t_day_t][t_time+1]=l
            rooms_cs4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cs4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CS4=[remaining_tutorials['CS4'][0]]+[remaining_tutorials['CS4'][0]]
def tutorial_assign_cs4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CS4[0]+remaining_tutorials_CS4[1]:
            a=random.choice(remaining_tutorials_CS4[0]+remaining_tutorials_CS4[1])
            tutorial_assign1_cs4(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_cs4(t_day_t,a,i,_c):
    global remaining_tutorials_CS4,tea_cs4,rooms_cs4,tt_cs4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print('cs')
        #print(a)
        #print('1'+f'{remaining_tutorials_CS4}')
        remaining_tutorials_CS4[_c].remove(a)
        #print('2'+f'{choices_cs4}')
        choices_cs4.remove(a)
        occupy_teacher(q1)
        tea_cs4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_cs4()
        rooms_cs4[t_day_t][t_time+i]=r
        tt_cs4[t_day_t][t_time+i]=a
        return

def room_assign1_cs4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cs4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cs4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cs4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)     
    elif rooms_cs4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cs4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cs4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cs4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cs4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_cs4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cs4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_cs4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_cs4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_cs4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_cs4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['F']+remaining_rooms['G']+remaining_rooms['S'])
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[558]:

pre_a_me4=''
__count=0
def me4():
    global tt_me4,tea_me4,rooms_me4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_me4,t_day,_count,__count
    if rooms_me4[2*t_day][t_time]==0 or tea_me4[2*t_day][t_time] ==0:
        if not choices_me4:
            return
        a=random.choice(choices_me4)
        #print(a)
        if not a:
            return
        if a==pre_a_me4 and len(a)>2:
            a=random.choice(choices_me4)
        pre_a_me4=a
        if a in depts['ME4'][0]:
            if a in lect_:
                
                tt_me4[2*t_day][t_time]=a
                tt_me4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    me4()
                else:
                    occupy_teacher(q1)
                    tea_me4[2*t_day][t_time]=q1
                    tea_me4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_me4()
                    if not r:
                        return
                    rooms_me4[2*t_day][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_me4.remove(a)
            elif a in remaining_tutorials_ME4[0]+remaining_tutorials_ME4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ME4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_ME4[0]+remaining_tutorials_ME4[1])
                tutorial_assign1_me4(t_day_t,a,0,_c)
            else:
                __count+=1
                me4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_me4[t_day_l][t_time]=a
                    tt_me4[t_day_l][t_time+1]=a
                    tt_me4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        me4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_me4[t_day_l][t_time]=q1
                        tea_me4[t_day_l][t_time+1]=q1
                        tea_me4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_me4[t_day_l][t_time]=l
                        rooms_me4[t_day_l][t_time+1]=l
                        rooms_me4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_me4.remove(a)
                        q=lab_assign_alternate_me4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_me4(t_day_t,_c)
                        
            else:
                me4()
                        
    return      
                        
                        
def lab_assign_alternate_me4(t_day_t,_c):
    global tt_me4,tea_me4,rooms_me4,t_time,labs_,lect_,lab_occupied_teachers,choices_me4
    a=random.choice(depts['ME4'][1])
    if a in labs_:
        tt_me4[t_day_t][t_time]=a
        tt_me4[t_day_t][t_time+1]=a
        tt_me4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_me4[t_day_t][t_time]=q1
            tea_me4[t_day_t][t_time+1]=q1
            tea_me4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_me4[t_day_t][t_time]=l
            rooms_me4[t_day_t][t_time+1]=l
            rooms_me4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_me4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ME4=[remaining_tutorials['ME4'][0]]+[remaining_tutorials['ME4'][0]]
def tutorial_assign_me4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ME4[0]+remaining_tutorials_ME4[1]:
            a=random.choice(remaining_tutorials_ME4[0]+remaining_tutorials_ME4[1])
            tutorial_assign1_me4(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_me4(t_day_t,a,i,_c):
    global remaining_tutorials_ME4,tea_me4,rooms_me4,tt_me4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_ME4[_c].remove(a)
        choices_me4.remove(a)
        occupy_teacher(q1)
        tea_me4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_me4()
        rooms_me4[t_day_t][t_time+i]=r
        tt_me4[t_day_t][t_time+i]=a
        return

def room_assign1_me4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_me4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_me4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_me4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_me4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_me4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_me4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_me4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_me4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_me4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_me4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
        
    elif rooms_me4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_me4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_me4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_me4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[559]:

pre_a_ec4=''
__count=0
def ec4():
    global tt_ec4,tea_ec4,rooms_ec4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ec4,t_day,_count,__count
    if rooms_ec4[2*t_day][t_time]==0 or tea_ec4[2*t_day][t_time] ==0:
        if not choices_ec4:
            return
        a=random.choice(choices_ec4)
        #print(a)
        if not a:
            return
        if a==pre_a_ec4 and len(a)>2:
            a=random.choice(choices_ec4)
        pre_a_ec4=a
        if a in depts['EC4'][0]:
            if a in lect_:
                
                tt_ec4[2*t_day][t_time]=a
                tt_ec4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ec4()
                else:
                    occupy_teacher(q1)
                    tea_ec4[2*t_day][t_time]=q1
                    tea_ec4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ec4()
                    if not r:
                        return
                    rooms_ec4[2*t_day][t_time]=r
                    rooms_ec4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ec4.remove(a)
            elif a in remaining_tutorials_EC4[0]+remaining_tutorials_EC4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EC4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_EC4[0]+remaining_tutorials_EC4[1])
                tutorial_assign1_ec4(t_day_t,a,0,_c)
            else:
                __count+=1
                ec4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ec4[t_day_l][t_time]=a
                    tt_ec4[t_day_l][t_time+1]=a
                    tt_ec4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ec4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ec4[t_day_l][t_time]=q1
                        tea_ec4[t_day_l][t_time+1]=q1
                        tea_ec4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ec4[t_day_l][t_time]=l
                        rooms_ec4[t_day_l][t_time+1]=l
                        rooms_ec4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ec4.remove(a)
                        q=lab_assign_alternate_ec4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ec4(t_day_t,_c)
                        
            else:
                ec4()
                        
    return      
                        
                        
def lab_assign_alternate_ec4(t_day_t,_c):
    global tt_ec4,tea_ec4,rooms_ec4,t_time,labs_,lect_,lab_occupied_teachers,choices_ec4
    a=random.choice(depts['EC4'][1])
    if a in labs_:
        tt_ec4[t_day_t][t_time]=a
        tt_ec4[t_day_t][t_time+1]=a
        tt_ec4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ec4[t_day_t][t_time]=q1
            tea_ec4[t_day_t][t_time+1]=q1
            tea_ec4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ec4[t_day_t][t_time]=l
            rooms_ec4[t_day_t][t_time+1]=l
            rooms_ec4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ec4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EC4=[remaining_tutorials['EC4'][0]]+[remaining_tutorials['EC4'][0]]
def tutorial_assign_ec4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EC4[0]+remaining_tutorials_EC4[1]:
            a=random.choice(remaining_tutorials_EC4[0]+remaining_tutorials_EC4[1])
            tutorial_assign1_ec4(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ec4(t_day_t,a,i,_c):
    global remaining_tutorials_EC4,tea_ec4,rooms_ec4,tt_ec4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EC4[_c].remove(a)
        choices_ec4.remove(a)
        occupy_teacher(q1)
        tea_ec4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ec4()
        rooms_ec4[t_day_t][t_time+i]=r
        tt_ec4[t_day_t][t_time+i]=a
        return

def room_assign1_ec4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ec4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ec4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ec4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ec4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ec4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ec4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ec4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ec4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ec4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ec4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ec4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ec4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_ec4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ec4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[560]:

pre_a_ee4=''
__count=0
def ee4():
    global tt_ee4,tea_ee4,rooms_ee4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ee4,t_day,_count,__count,__c
    if rooms_ee4[2*t_day][t_time]==0 or tea_ee4[2*t_day][t_time] ==0:
        if not choices_ee4:
            return
        a=random.choice(choices_ee4)
        #print(a)
        if not a:
            return
        if a==pre_a_ee4 and len(a)>2:
            a=random.choice(choices_ee4)
        if __c>7:
            return
        pre_a_ee4=a
        if a in depts['EE4'][0]:
            if a in lect_:
                
                tt_ee4[2*t_day][t_time]=a
                tt_ee4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    __c+=1
                    ee4()
                else:
                    occupy_teacher(q1)
                    tea_ee4[2*t_day][t_time]=q1
                    tea_ee4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ee4()
                    if not r:
                        return
                    rooms_ee4[2*t_day][t_time]=r
                    rooms_ee4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ee4.remove(a)
            elif a in remaining_tutorials_EE4[0]+remaining_tutorials_EE4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_EE4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ee4_1(t_day_t,_c)
            else:
                __count+=1
                ee4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ee4[t_day_l][t_time]=a
                    tt_ee4[t_day_l][t_time+1]=a
                    tt_ee4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ee4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ee4[t_day_l][t_time]=q1
                        tea_ee4[t_day_l][t_time+1]=q1
                        tea_ee4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ee4[t_day_l][t_time]=l
                        rooms_ee4[t_day_l][t_time+1]=l
                        rooms_ee4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ee4.remove(a)
                        q=lab_assign_alternate_ee4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ee4(t_day_t,_c)
                        
            else:
                ee4()
                        
    return      
                        
                        
def lab_assign_alternate_ee4(t_day_t,_c):
    global tt_ee4,tea_ee4,rooms_ee4,t_time,labs_,lect_,lab_occupied_teachers,choices_ee4
    a=random.choice(depts['EE4'][1])
    if a in labs_:
        tt_ee4[t_day_t][t_time]=a
        tt_ee4[t_day_t][t_time+1]=a
        tt_ee4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ee4[t_day_t][t_time]=q1
            tea_ee4[t_day_t][t_time+1]=q1
            tea_ee4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ee4[t_day_t][t_time]=l
            rooms_ee4[t_day_t][t_time+1]=l
            rooms_ee4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ee4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_EE4=[remaining_tutorials['EE4'][0]]+[remaining_tutorials['EE4'][0]]
def tutorial_assign_ee4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_EE4[0]+remaining_tutorials_EE4[1]:
            a=random.choice(remaining_tutorials_EE4[0]+remaining_tutorials_EE4[1])
            tutorial_assign1_ee4(t_day_t,a,i,_c)
    return

def tutorial_assign_ee4_1(t_day_t,_c):
    if remaining_tutorials_EE4[0]+remaining_tutorials_EE4[1]:
        a=random.choice(remaining_tutorials_EE4[0]+remaining_tutorials_EE4[1])
        tutorial_assign1_ee4(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ee4(t_day_t,a,i,_c):
    global remaining_tutorials_EE4,tea_ee4,rooms_ee4,tt_ee4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_EE4[_c].remove(a)
        choices_ee4.remove(a)
        occupy_teacher(q1)
        tea_ee4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ee4()
        rooms_ee4[t_day_t][t_time+i]=r
        tt_ee4[t_day_t][t_time+i]=a
        return

def room_assign1_ee4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ee4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ee4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ee4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ee4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ee4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ee4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ee4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ee4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ee4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ee4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
        
    elif rooms_ee4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ee4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_ee4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ee4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[561]:

pre_a_cd4=''
__count=0
def cd4():
    global tt_cd4,tea_cd4,rooms_cd4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_cd4,t_day,_count,__count,__c
    if rooms_cd4[2*t_day][t_time]==0 or tea_cd4[2*t_day][t_time] ==0:
        if not choices_cd4:
            return
        a=random.choice(choices_cd4)
        #print(a)
        if not a:
            return
        if __c>7:
            return
        if a==pre_a_cd4 and len(a)>2:
            a=random.choice(choices_cd4)
        pre_a_cd4=a
        if a in depts['CD4'][0]:
            if a in lect_:
                
                tt_cd4[2*t_day][t_time]=a
                tt_cd4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    __c+=1
                    cd4()
                else:
                    occupy_teacher(q1)
                    tea_cd4[2*t_day][t_time]=q1
                    tea_cd4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_cd4()
                    if not r:
                        return
                    rooms_cd4[2*t_day][t_time]=r
                    rooms_cd4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_cd4.remove(a)
                    #print(a)
            elif a in remaining_tutorials_CD4[0]+remaining_tutorials_CD4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CD4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_cd4_1(t_day_t,_c)
            else:
                __count+=1
                cd4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_cd4[t_day_l][t_time]=a
                    tt_cd4[t_day_l][t_time+1]=a
                    tt_cd4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        cd4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_cd4[t_day_l][t_time]=q1
                        tea_cd4[t_day_l][t_time+1]=q1
                        tea_cd4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_cd4[t_day_l][t_time]=l
                        rooms_cd4[t_day_l][t_time+1]=l
                        rooms_cd4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_cd4.remove(a)
                        q=lab_assign_alternate_cd4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_cd4(t_day_t,_c)
                        
            else:
                cd4()
                        
    return      
                        
                        
def lab_assign_alternate_cd4(t_day_t,_c):
    global tt_cd4,tea_cd4,rooms_cd4,t_time,labs_,lect_,lab_occupied_teachers,choices_cd4
    a=random.choice(depts['CD4'][1])
    if a in labs_:
        tt_cd4[t_day_t][t_time]=a
        tt_cd4[t_day_t][t_time+1]=a
        tt_cd4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_cd4[t_day_t][t_time]=q1
            tea_cd4[t_day_t][t_time+1]=q1
            tea_cd4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_cd4[t_day_t][t_time]=l
            rooms_cd4[t_day_t][t_time+1]=l
            rooms_cd4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_cd4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CD4=[remaining_tutorials['CD4'][0]]+[remaining_tutorials['CD4'][0]]
def tutorial_assign_cd4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CD4[0]+remaining_tutorials_CD4[1]:
            a=random.choice(remaining_tutorials_CD4[0]+remaining_tutorials_CD4[1])
            tutorial_assign1_cd4(t_day_t,a,i,_c)
    return

def tutorial_assign_cd4_1(t_day_t,_c):

    if remaining_tutorials_CD4[0]+remaining_tutorials_CD4[1]:
        a=random.choice(remaining_tutorials_CD4[0]+remaining_tutorials_CD4[1])
        tutorial_assign1_cd4(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_cd4(t_day_t,a,i,_c):
    global remaining_tutorials_CD4,tea_cd4,rooms_cd4,tt_cd4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        #print(a)
        #print('cd')
        #print('1'+f'{remaining_tutorials_CD4}')
        r=room_assign1_cd4()
        if not r:
            return
        remaining_tutorials_CD4[_c].remove(a)
        #print('2'+f'{choices_cd4}')
        
        choices_cd4.remove(a)
        occupy_teacher(q1)
        tea_cd4[t_day_t][t_time+i]=q1
                    
        
        rooms_cd4[t_day_t][t_time+i]=r
        tt_cd4[t_day_t][t_time+i]=a
        return

def room_assign1_cd4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_cd4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_cd4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_cd4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_cd4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_cd4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_cd4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_cd4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cd4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_cd4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_cd4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
        
    elif rooms_cd4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_cd4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_cd4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_cd4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[562]:

pre_a_ed4=''
__count=0
def ed4():
    global tt_ed4,tea_ed4,rooms_ed4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ed4,t_day,_count,__count,__c
    if rooms_ed4[2*t_day][t_time]==0 or tea_ed4[2*t_day][t_time] ==0:
        if not choices_ed4:
            return
        a=random.choice(choices_ed4)
        #print(a)
        if not a:
            return
        if a==pre_a_ed4 and len(a)>2:
            a=random.choice(choices_ed4)
        pre_a_ed4=a
        if a in depts['ED4'][0]:
            if a in lect_:
                
                tt_ed4[2*t_day][t_time]=a
                tt_ed4[2*t_day+1][t_time]=a
                #print(a)
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ed4()
                else:
                    occupy_teacher(q1)
                    tea_ed4[2*t_day][t_time]=q1
                    tea_ed4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ed4()
                    if not r:
                        return
                    rooms_ed4[2*t_day][t_time]=r
                    rooms_ed4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ed4.remove(a)
            elif a in remaining_tutorials_ED4[0]+remaining_tutorials_ED4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_ED4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                tutorial_assign_ed4_1(t_day_t,_c)
            else:
                __count+=1
                ed4()
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ed4[t_day_l][t_time]=a
                    tt_ed4[t_day_l][t_time+1]=a
                    tt_ed4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ed4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ed4[t_day_l][t_time]=q1
                        tea_ed4[t_day_l][t_time+1]=q1
                        tea_ed4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ed4[t_day_l][t_time]=l
                        rooms_ed4[t_day_l][t_time+1]=l
                        rooms_ed4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ed4.remove(a)
                        q=lab_assign_alternate_ed4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ed4(t_day_t,_c)
                        
            else:
                ed4()
                        
    return      
                        
                        
def lab_assign_alternate_ed4(t_day_t,_c):
    global tt_ed4,tea_ed4,rooms_ed4,t_time,labs_,lect_,lab_occupied_teachers,choices_ed4
    a=random.choice(depts['ED4'][1])
    if a in labs_:
        tt_ed4[t_day_t][t_time]=a
        tt_ed4[t_day_t][t_time+1]=a
        tt_ed4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ed4[t_day_t][t_time]=q1
            tea_ed4[t_day_t][t_time+1]=q1
            tea_ed4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ed4[t_day_t][t_time]=l
            rooms_ed4[t_day_t][t_time+1]=l
            rooms_ed4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ed4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_ED4=[remaining_tutorials['ED4'][0]]+[remaining_tutorials['ED4'][0]]
def tutorial_assign_ed4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_ED4[0]+remaining_tutorials_ED4[1]:
            a=random.choice(remaining_tutorials_ED4[0]+remaining_tutorials_ED4[1])
            tutorial_assign1_ed4(t_day_t,a,i,_c)
    return

def tutorial_assign_ed4_1(t_day_t,_c):
    if remaining_tutorials_ED4[0]+remaining_tutorials_ED4[1]:
            a=random.choice(remaining_tutorials_ED4[0]+remaining_tutorials_ED4[1])
            tutorial_assign1_ed4(t_day_t,a,0,_c)
    return
        
def tutorial_assign1_ed4(t_day_t,a,i,_c):
    global remaining_tutorials_ED4,tea_ed4,rooms_ed4,tt_ed4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        r=room_assign1_ed4()
        if not r:
            return
        remaining_tutorials_ED4[_c].remove(a)
        choices_ed4.remove(a)
        occupy_teacher(q1)
        tea_ed4[t_day_t][t_time+i]=q1
                    
        
        
        rooms_ed4[t_day_t][t_time+i]=r
        tt_ed4[t_day_t][t_time+i]=a
        return

def room_assign1_ed4():
    global remaining_rooms,t_time,t_day
    #rint(rooms)
    if not(remaining_rooms['B']+remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S']):
        return
    elif rooms_ed4[2*t_day][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed4[2*t_day][t_time-1]
        remaining_rooms['G'].remove(r)
    elif rooms_ed4[2*t_day+1][t_time-1] in remaining_rooms['G']:
        #print('yes')
        r=rooms_ed4[2*t_day+1][t_time-1]
        remaining_rooms['G'].remove(r)
        
    elif rooms_ed4[2*t_day][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed4[2*t_day][t_time-1]
        remaining_rooms['F'].remove(r)
    elif rooms_ed4[2*t_day+1][t_time-1] in remaining_rooms['F']:
        #print('yes')
        r=rooms_ed4[2*t_day+1][t_time-1]
        remaining_rooms['F'].remove(r)
        
    elif rooms_ed4[2*t_day][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ed4[2*t_day][t_time-1]
        remaining_rooms['S'].remove(r)
    elif rooms_ed4[2*t_day+1][t_time-1] in remaining_rooms['S']:
        #print('yes')
        r=rooms_ed4[2*t_day+1][t_time-1]
        remaining_rooms['S'].remove(r)
        
    elif rooms_ed4[2*t_day][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ed4[2*t_day][t_time-1]
        remaining_rooms['B'].remove(r)
    elif rooms_ed4[2*t_day+1][t_time-1] in remaining_rooms['B']:
        #print('yes')
        r=rooms_ed4[2*t_day+1][t_time-1]
        remaining_rooms['B'].remove(r)
    elif remaining_rooms['B']:
        r=random.choice(remaining_rooms['B'])
        remaining_rooms['B'].remove(r)
    else:
        r=random.choice(remaining_rooms['G']+remaining_rooms['F']+remaining_rooms['S'])
        if r in rooms['G']:
            remaining_rooms['G'].remove(r)
        if r in rooms['F']:
            remaining_rooms['F'].remove(r)
        if r in rooms['S']:
            remaining_rooms['S'].remove(r)
    return r


# In[563]:

pre_a_ch4=''
def ch4():
    global tt_ch4,tea_ch4,rooms_ch4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ch4,t_day,_count
    if rooms_ch4[2*t_day][t_time]==0 or tea_ch4[2*t_day][t_time] ==0:
        if not choices_ch4:
            return
        a=random.choice(choices_ch4)
        #print(a)
        if not a:
            return
        if a==pre_a_ch4 and len(a)>2:
            a=random.choice(choices_ch4)
        pre_a_ch4=a
        if a in depts['CH4'][0]:
            if a in lect_:
                
                tt_ch4[2*t_day][t_time]=a
                tt_ch4[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ch4()
                else:
                    occupy_teacher(q1)
                    tea_ch4[2*t_day][t_time]=q1
                    tea_ch4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ch4()
                    if not r:
                        return
                    rooms_ch4[2*t_day][t_time]=r
                    rooms_ch4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ch4.remove(a)
                    
            elif a in remaining_tutorials_CH4[0]+remaining_tutorials_CH4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CH4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CH4[0]+remaining_tutorials_CH4[1])
                tutorial_assign1_ch4(t_day_t,a,0,_c)
        
            else:
                ch4()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ch4[t_day_l][t_time]=a
                    tt_ch4[t_day_l][t_time+1]=a
                    tt_ch4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ch4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ch4[t_day_l][t_time]=q1
                        tea_ch4[t_day_l][t_time+1]=q1
                        tea_ch4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ch4[t_day_l][t_time]=l
                        rooms_ch4[t_day_l][t_time+1]=l
                        rooms_ch4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ch4.remove(a)
                        q=lab_assign_alternate_ch4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ch4(t_day_t,_c)
                        
            else:
                ch4()
                        
    return      
                        
                        
def lab_assign_alternate_ch4(t_day_t,_c):
    global tt_ch4,tea_ch4,rooms_ch4,t_time,labs_,lect_,lab_occupied_teachers,choices_ch4
    a=random.choice(depts['CH4'][1])
    if a in labs_:
        tt_ch4[t_day_t][t_time]=a
        tt_ch4[t_day_t][t_time+1]=a
        tt_ch4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ch4[t_day_t][t_time]=q1
            tea_ch4[t_day_t][t_time+1]=q1
            tea_ch4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ch4[t_day_t][t_time]=l
            rooms_ch4[t_day_t][t_time+1]=l
            rooms_ch4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ch4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CH4=[remaining_tutorials['CH4'][0]]+[remaining_tutorials['CH4'][0]]
def tutorial_assign_ch4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CH4[0]+remaining_tutorials_CH4[1]:
            a=random.choice(remaining_tutorials_CH4[0]+remaining_tutorials_CH4[1])
            tutorial_assign1_ch4(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ch4(t_day_t,a,i,_c):
    global remaining_tutorials_CH4,tea_ch4,rooms_ch4,tt_ch4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CH4[_c].remove(a)
        choices_ch4.remove(a)
        occupy_teacher(q1)
        tea_ch4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ch4()
        rooms_ch4[t_day_t][t_time+i]=r
        tt_ch4[t_day_t][t_time+i]=a
        return
        

def room_assign1_ch4():
    global remaining_rooms,t_time,t_day
    return 'CHDEPT'


# In[564]:
pre_a_ce4=''

def ce4():
    global tt_ce4,tea_ce4,rooms_ce4,t_time,labs_,lect_,lab_occupied_teachers,pre_a_ce4,t_day,_count
    if rooms_ce4[2*t_day][t_time]==0 or tea_ce4[2*t_day][t_time] ==0:
        if not choices_ce4:
            return
        a=random.choice(choices_ce4)
        #print(a)
        if not a:
            return
        if a==pre_a_ce4 and len(a)>2:
            a=random.choice(choices_ce4)
        pre_a_ce4=a
        if a in depts['CE4'][0]:
            if a in lect_:
                
                tt_ce4[2*t_day][t_time]=a
                tt_ce4[2*t_day+1][t_time]=a
                q1=Teacher_assign(a)
                if q1 in occupied_teacher:
                    ce4()
                else:
                    occupy_teacher(q1)
                    tea_ce4[2*t_day][t_time]=q1
                    tea_ce4[2*t_day+1][t_time]=q1
                    
                    r=room_assign1_ce4()
                    if not r:
                        return
                    rooms_ce4[2*t_day][t_time]=r
                    rooms_ce4[2*t_day+1][t_time]=r
                    #t_cs1=t_cs1+1
                    lect_.remove(a)
                    choices_ce4.remove(a)
                    
            elif a in remaining_tutorials_CE4[0]+remaining_tutorials_CE4[1] and __count>2:
                #print('yes')
                if a in remaining_tutorials_CE4[0]:
                    _c=0
                    t_day_t=2*t_day
                else:
                    _c=1
                    t_day_t=2*t_day+1
                a=random.choice(remaining_tutorials_CE4[0]+remaining_tutorials_CE4[1])
                tutorial_assign1_ce4(t_day_t,a,0,_c)
        
            else:
                ce4()
                
        else:
            if _count>15:
                _count=0
                return
            #print('yup')
            _count+=1
            if( a in labs_[0]+labs_[1] and (t_time==1 or t_time==6 or t_time==7)):
                _c=random.choice([0,1])
                if a not in labs_[_c]:
                    if _c==0:
                        _c=1
                    else:
                        _c=0
                if _c==0:
                    t_day_l=2*t_day
                    t_day_t=2*t_day+1
                elif _c==1:
                    t_day_l=2*t_day+1
                    t_day_t=2*t_day
                if t_time==1 or t_time==7 or t_time==6:
                    
                    tt_ce4[t_day_l][t_time]=a
                    tt_ce4[t_day_l][t_time+1]=a
                    tt_ce4[t_day_l][t_time+2]=a
                    q1=Teacher_assign(a)
                    #print('inside')
                    if q1 in occupied_teacher:
                        ce4()
                    else:
                        lab_occupied_teachers+=q1
                        tea_ce4[t_day_l][t_time]=q1
                        tea_ce4[t_day_l][t_time+1]=q1
                        tea_ce4[t_day_l][t_time+2]=q1
                        l=lab_assign(a)
                        #if l in occupied_labs:
                            #cs1()
                        rooms_ce4[t_day_l][t_time]=l
                        rooms_ce4[t_day_l][t_time+1]=l
                        rooms_ce4[t_day_l][t_time+2]=l
                        occupy_labs(l)
                        labs_[_c].remove(a)
                        choices_ce4.remove(a)
                        q=lab_assign_alternate_ce4(t_day_t,int(not _c))
                        if q==5:
                            tutorial_assign_ce4(t_day_t,_c)
                        
            else:
                ce4()
                        
    return      
                        
                        
def lab_assign_alternate_ce4(t_day_t,_c):
    global tt_ce4,tea_ce4,rooms_ce4,t_time,labs_,lect_,lab_occupied_teachers,choices_ce4
    a=random.choice(depts['CE4'][1])
    if a in labs_:
        tt_ce4[t_day_t][t_time]=a
        tt_ce4[t_day_t][t_time+1]=a
        tt_ce4[t_day_t][t_time+2]=a
        q1=Teacher_assign(a)
        if q1 in occupied_teacher:
            return 5
        else:
            lab_occupied_teachers+=q1
            tea_ce4[t_day_t][t_time]=q1
            tea_ce4[t_day_t][t_time+1]=q1
            tea_ce4[t_day_t][t_time+2]=q1
            l=lab_assign(a)
                            #if l in occupied_labs:
                                #cs1()
            rooms_ce4[t_day_t][t_time]=l
            rooms_ce4[t_day_t][t_time+1]=l
            rooms_ce4[t_day_t][t_time+2]=l
            occupy_labs(l)
            labs_[_c].remove(a)
            choices_ce4.remove(a)
            return 4
    else:
        return 5
remaining_tutorials_CE4=[remaining_tutorials['CE4'][0]]+[remaining_tutorials['CE4'][0]]
def tutorial_assign_ce4(t_day_t,_c):
    for i in range(2):
        if remaining_tutorials_CE4[0]+remaining_tutorials_CE4[1]:
            a=random.choice(remaining_tutorials_CE4[0]+remaining_tutorials_CE4[1])
            tutorial_assign1_ce4(t_day_t,a,i,_c)
    return
        
def tutorial_assign1_ce4(t_day_t,a,i,_c):
    global remaining_tutorials_CE4,tea_ce4,rooms_ce4,tt_ce4
    q1=Teacher_assign(a)
    if q1 in occupied_teacher:
        return
    else:
        remaining_tutorials_CE4[_c].remove(a)
        choices_ce4.remove(a)
        occupy_teacher(q1)
        tea_ce4[t_day_t][t_time+i]=q1
                    
        r=room_assign1_ce4()
        rooms_ce4[t_day_t][t_time+i]=r
        tt_ce4[t_day_t][t_time+i]=a
        return
        

def room_assign1_ce4():
    global remaining_rooms,t_time,t_day
    return 'CEDEPT'


# In[ ]:





# In[565]:




# In[566]:



import pandas as pd


# In[567]:









import sys




sys.setrecursionlimit(9999)




import numpy as np
#print(np.matrix(tt_cs1))
import pandas as pd
#print(pd.DataFrame(tt_cs1))


make_time_table()


# In[519]:

"""
def addlab(a,b,c,d):
    #a=input('enter the lab name:')
    #b=input('enter the lab code:')
    #c=input('enter the teacher who take the lab:')
    #d=input('enter the branch:')
    if a not in remaining_labs:
        remaining_labs.append(a)
        lab_code[a]=[b]
    else:
        lab_code[a].append(b)
    if b not in depts[d][1]:
        depts[d][1].append(b)
        remaining_tutorials[d][1].append(b)
    addteacher(b,c)


# In[524]:



def addteacher(b,c):
    global depts,remaining_tutorials,teacher_code
    _q=0
    #if b=='' or c=='':
     #   b=input('enter the subject code:')
      #  c=input('enter the teacher code:')
    for i,j in teacher_code.items():
        if c in i:
            teacher_code[c].append(b)
            _q=1
            break
        else:
            _q=0         
    if _q==1:
        remaining_teacher.append(b)
        teacher_code[c]=[b]
        
    dp = open("depts.db","w")
    data=js.dump(depts,dp)
    #print(data)
    dp.close()
    dp = open("remaining_tutorials.db","w")
    data=js.dump(remaining_tutorials,dp)
    #print(data)
    dp.close()
    dp = open("teacher_code.db","w")
    data=js.dump(teacher_code,dp)
    #print(data)
    dp.close()


# In[525]:


def addsubject(b,d):
    global depts,remaining_tutorials
    _q=0
    #b=input('enter the subject code:')
    #d=input('enter the branch:')
    if b not in depts[d][0]:
        depts[d][0].append(b)
        remaining_tutorials[d][0].append(b)
    dp = open("depts.db","w")
    data=js.dump(depts,dp)
    #print(data)
    dp.close()
    dp = open("remaining_tutorials.db","w")
    data=js.dump(remaining_tutorials,dp)
    #print(data)
    dp.close()
    #    _q=1
    #if _q==1:
     #   #c=input('enter the teacher code:')
      #  addteacher(b,c)


# In[526]:


def addroom(r,r1):
    global rooms
    #r=input('enter the room floor eg.B,G,F,S:')
    #r1=input('enter the room code:')
    rooms__=copy.deepcopy(rooms)
    #print(r)
    #print(r1)
    print(rooms__.keys())
    if r in rooms__.keys() and r1 not in rooms__[r]:
        print(rooms.keys())
        rooms__[r].append(r1)
    elif r not in rooms.keys():
        print(rooms__.keys())
        rooms__[r]=[r1]
    #print(rooms__)
    dp = open("rooms.db","w")
    data=js.dump(rooms__,dp)
    #print(data)
    dp.close()


# In[527]:


def removeroom(r,r1):
    global rooms
    #r=input('enter the room floor eg.B,G,F,S:')
    #r1=input('enter the room code:')
    rooms__=copy.deepcopy(rooms)
    if r in rooms.keys() and r1 in rooms[r]:
        rooms__[r].remove(r1)
    dp = open("rooms.db","w")
    data=js.dump(rooms__,dp)
    #print(data)
    dp.close()

dp = open("rooms.db","w")
data=js.dump(rooms,dp)
#print(data)
dp.close()

dp = open("lab_code.db","w")
data=js.dump(lab_code,dp)
#print(data)
dp.close()


dp = open("teacher_code.db","w")
data=js.dump(teacher_code,dp)
#print(data)
dp.close()


dp = open("remaining_labs.db","w")
data=js.dump(remaining_labs,dp)
#print(data)
dp.close()


dp = open("remaining_tutorials.db","w")
data=js.dump(remaining_tutorials,dp)
#print(data)
dp.close()



dp = open("remaining_rooms.db","w")
data=js.dump(remaining_rooms,dp)
#print(data)
dp.close()


dp = open("remaining_teacher.db","w")
data=js.dump(remaining_teacher,dp)
#print(data)
dp.close()


dp = open("depts.db","w")
data=js.dump(depts,dp)
#print(data)
dp.close()





make_time_table()

print(50*'.'+'CS2'+50*'.')
print(pd.DataFrame(tt_cs2))
print(pd.DataFrame(tea_cs2))
print(pd.DataFrame(rooms_cs2))



print(50*'.'+'ME2'+50*'.')
print(pd.DataFrame(tt_me2))
print(pd.DataFrame(tea_me2))
print(pd.DataFrame(rooms_me2))

print(50*'.'+'EE2'+50*'.')
print(pd.DataFrame(tt_ee2))
print(pd.DataFrame(tea_ee2))
print(pd.DataFrame(rooms_ee2))
print(50*'.'+'EC2'+50*'.')
print(pd.DataFrame(tt_ec2))
print(pd.DataFrame(tea_ec2))
print(pd.DataFrame(rooms_ec2))
print(50*'.'+'CD2'+50*'.')
print(pd.DataFrame(tt_cd2))
print(pd.DataFrame(tea_cd2))
print(pd.DataFrame(rooms_cd2))

print(50*'.'+'ED2'+50*'.')
print(pd.DataFrame(tt_ed2))
print(pd.DataFrame(tea_ed2))
print(pd.DataFrame(rooms_ed2))


# In[568]:


print(50*'.'+'CS3'+50*'.')
print(pd.DataFrame(tt_cs3))
print(pd.DataFrame(tea_cs3))
print(pd.DataFrame(rooms_cs3))



print(50*'.'+'ME3'+50*'.')
print(pd.DataFrame(tt_me3))
print(pd.DataFrame(tea_me3))
print(pd.DataFrame(rooms_me3))

print(50*'.'+'EE3'+50*'.')
print(pd.DataFrame(tt_ee3))
print(pd.DataFrame(tea_ee3))
print(pd.DataFrame(rooms_ee3))
print(50*'.'+'EC3'+50*'.')
print(pd.DataFrame(tt_ec3))
print(pd.DataFrame(tea_ec3))
print(pd.DataFrame(rooms_ec3))
print(50*'.'+'CD3'+50*'.')
print(pd.DataFrame(tt_cd3))
print(pd.DataFrame(tea_cd3))
print(pd.DataFrame(rooms_cd3))

print(50*'.'+'ED3'+50*'.')
print(pd.DataFrame(tt_ed3))
print(pd.DataFrame(tea_ed3))
print(pd.DataFrame(rooms_ed3))


# In[569]:


print(50*'.'+'CS4'+50*'.')
print(pd.DataFrame(tt_cs4))
print(pd.DataFrame(tea_cs4))
print(pd.DataFrame(rooms_cs4))



print(50*'.'+'ME4'+50*'.')
print(pd.DataFrame(tt_me4))
print(pd.DataFrame(tea_me4))
print(pd.DataFrame(rooms_me4))

print(50*'.'+'EE4'+50*'.')
print(pd.DataFrame(tt_ee4))
print(pd.DataFrame(tea_ee4))
print(pd.DataFrame(rooms_ee4))
print(50*'.'+'EC4'+50*'.')
print(pd.DataFrame(tt_ec4))
print(pd.DataFrame(tea_ec4))
print(pd.DataFrame(rooms_ec4))
print(50*'.'+'CD4'+50*'.')
print(pd.DataFrame(tt_cd4))
print(pd.DataFrame(tea_cd4))
print(pd.DataFrame(rooms_cd4))

print(50*'.'+'ED4'+50*'.')
print(pd.DataFrame(tt_ed4))
print(pd.DataFrame(tea_ed4))
print(pd.DataFrame(rooms_ed4))


# In[570]:


import pandas as pd
print(50*'.'+'CS1'+50*'.')
print(pd.DataFrame(tt_cs1))
print(pd.DataFrame(tea_cs1))
print(pd.DataFrame(rooms_cs1))

print(50*'.'+'EE1'+50*'.')
print(pd.DataFrame(tt_ee1))
print(pd.DataFrame(tea_ee1))
print(pd.DataFrame(rooms_ee1))


print(50*'.'+'ME1'+50*'.')
print(pd.DataFrame(tt_me1))
print(pd.DataFrame(tea_me1))
print(pd.DataFrame(rooms_me1))

print(50*'.'+'EC1'+50*'.')
print(pd.DataFrame(tt_ec1))
print(pd.DataFrame(tea_ec1))
print(pd.DataFrame(rooms_ec1))


print(50*'.'+'CH1'+50*'.')
print(pd.DataFrame(tt_ch1))
print(pd.DataFrame(tea_ch1))
print(pd.DataFrame(rooms_ch1))


print(50*'.'+'CE1'+50*'.')
print(pd.DataFrame(tt_ce1))
print(pd.DataFrame(tea_ce1))
print(pd.DataFrame(rooms_ce1))

print(50*'.'+'MS1'+50*'.')
print(pd.DataFrame(tt_ms1))
print(pd.DataFrame(tea_ms1))
print(pd.DataFrame(rooms_ms1))
"""
