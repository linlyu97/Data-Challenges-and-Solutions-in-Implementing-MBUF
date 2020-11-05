import numpy as np
import csv
import pandas as pd

def data2015(input_hm,input_sf):
    hm60 = pd.read_excel(input_hm,header=None,skiprows=14)
    state = pd.read_excel(input_hm,header=None,skiprows=14,usecols=[0])
  
    state=state.drop(index=[52,53,54])
    hm_urban=hm60.iloc[0:52,9:15]
  
    hm_urban['SUBTOTAL'] = hm_urban.apply(lambda x: x.sum(), axis=1)
    hm_urban.rename(columns={9:'INTERSTATE',10:'OTHER FREEWAYS AND EXPRESSWAYS',11:'OTHER PRINCIPAL ARTERIAL',
    12:'MINOR ARTERIAL',13:'MAJOR COLLECTOR',14:'MINOR COLLECTOR'},inplace=True)

    sf12_small_urban=pd.read_excel(input_sf,sheet_name='SF12P2',header=None,skiprows=14)
    sf12_urban=pd.read_excel(input_sf,sheet_name='SF12P3',header=None,skiprows=14)
    
    sf_small_capital=sf12_small_urban.iloc[:,1:8]
    small_capital=sf_small_capital.drop(index=[51,53])

    sf_small_main=sf12_small_urban.iloc[:,8:]
    small_main=sf_small_main.drop(index=[51,53])

    sf_capital=sf12_urban.iloc[:,1:8]
    capital=sf_capital.drop(index=[51,53])

    sf_main=sf12_urban.iloc[:,8:]
    main=sf_main.drop(index=[51,53])

    new_capital=small_capital+capital
    new_capital.rename(index={52:51},columns={1:'INTERSTATE',2:'OTHER FREEWAYS AND EXPRESSWAYS',
    3:'OTHER PRINCIPAL ARTERIAL',4:'MINOR ARTERIAL',5:'MAJOR COLLECTOR',6:'MINOR COLLECTOR',7:'SUBTOTAL'},inplace=True)
    cal_capital=new_capital/hm_urban

    new_main=small_main+main
    new_main.rename(index={52:51},columns={8:'INTERSTATE',9:'OTHER FREEWAYS AND EXPRESSWAYS',
    10:'OTHER PRINCIPAL ARTERIAL',11:'MINOR ARTERIAL',12:'MAJOR COLLECTOR',13:'MINOR COLLECTOR',14:'SUBTOTAL'},inplace=True)
    # print(new_main)
    cal_main=new_main/hm_urban
    all=new_capital+new_main
    cal_all=all/hm_urban
    cal_all.rename(columns={'SUBTOTAL':'TOTAL'},inplace=True)

    title1={0:[""],'INTERSTATE':[""],'OTHER FREEWAYS AND EXPRESSWAYS':
    ["",],'OTHER PRINCIPAL ARTERIAL':[""],'MINOR ARTERIAL':['CAPITAL OUTLAY'],'MAJOR COLLECTOR':[""],
    'MINOR COLLECTOR':[""],"SUBTOTAL":[""]}
    title2={"INTERSTATE":[""],"OTHER FREEWAYS AND EXPRESSWAYS":[""],'OTHER PRINCIPAL ARTERIAL':[""],
    'MINOR ARTERIAL':['MAINTENANCE'],'MAJOR COLLECTOR':[""],'MINOR COLLECTOR':
    [""],'SUBTOTAL':[""]}
    
    title1=pd.DataFrame(title1)
    title2=pd.DataFrame(title2)
    title=pd.concat([title1,title2],axis=1)
    result=pd.concat([state,cal_capital,cal_main],axis=1)
    rel=pd.concat([title,result],axis=0)

    rel.to_csv('2015_capital_maintenance_result.csv',index=False)

    all_result=pd.concat([state,cal_all],axis=1)
    all_result.to_csv('2015_total_result.csv',index=False)
    

data2015('/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2015_hm80.xls',
'/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2015_sf12.xlsx')

def data(input_hm,input_sf):
    hm60 = pd.read_excel(input_hm,header=None,skiprows=14, sheet_name='A')
    # print(hm60)
    state = pd.read_excel(input_hm,header=None,skiprows=14,usecols=[0],sheet_name='A')
    # print(state)
    state=state.drop(index=[52,53,54])
    
    
    # print(type(hm60))
    
    hm_urban=hm60.iloc[0:52,9:15]
    # print(hm_urban)
    
    hm_urban.rename(columns={9:'INTERSTATE',10:'OTHER FREEWAYS AND EXPRESSWAYS',11:'OTHER PRINCIPAL ARTERIAL',
    12:'MINOR ARTERIAL',13:'MAJOR COLLECTOR',14:'MINOR COLLECTOR'},inplace=True)
    # print(hm_urban)

    hm_urban['COLLECTOR']=hm_urban['MAJOR COLLECTOR']+hm_urban['MINOR COLLECTOR']
    hm_urban=hm_urban.drop(columns=['MAJOR COLLECTOR','MINOR COLLECTOR'])
    hm_urban['SUBTOTAL'] = hm_urban.apply(lambda x: x.sum(), axis=1)
    # print(hm_urban)

    sf12_small_urban=pd.read_excel(input_sf,sheet_name='SF12P2',header=None,skiprows=14)
    sf12_urban=pd.read_excel(input_sf,sheet_name='SF12P3',header=None,skiprows=14)
    # print('sfsamll=',sf12_small_urban)
    # print('sfurban=',sf12_urban)

    sf_small_capital=sf12_small_urban.iloc[:,1:7]
    small_capital=sf_small_capital.drop(index=[51,53])
    # print(small_capital)

    sf_small_main=sf12_small_urban.iloc[:,7:]
    small_main=sf_small_main.drop(index=[51,53])
    # print(small_main)


    sf_capital=sf12_urban.iloc[:,1:7]
    capital=sf_capital.drop(index=[51,53])
    # print(capital)

    sf_main=sf12_urban.iloc[:,7:]
    main=sf_main.drop(index=[51,53])
    # print(main)

    new_capital=small_capital+capital
    new_capital.rename(index={52:51},columns={1:'INTERSTATE',2:'OTHER FREEWAYS AND EXPRESSWAYS',
    3:'OTHER PRINCIPAL ARTERIAL',4:'MINOR ARTERIAL',5:'COLLECTOR',6:'SUBTOTAL'},inplace=True)
    # print(new_capital)
    cal_capital=new_capital/hm_urban
    # print(cal_capital)

    new_main=small_main+main
    new_main.rename(index={52:51},columns={7:'INTERSTATE',8:'OTHER FREEWAYS AND EXPRESSWAYS',
    9:'OTHER PRINCIPAL ARTERIAL',10:'MINOR ARTERIAL',11:'COLLECTOR',12:'SUBTOTAL'},inplace=True)
    # print(new_main)
    cal_main=new_main/hm_urban
    # print(cal_main)

    all=new_capital+new_main
    # print(all)
    cal_all=all/hm_urban
    
    cal_all.rename(columns={'SUBTOTAL':'TOTAL'},inplace=True)
    # print(cal_all)


    title1={0:[""],'INTERSTATE':[""],'OTHER FREEWAYS AND EXPRESSWAYS':
    ["",],'OTHER PRINCIPAL ARTERIAL':[""],'MINOR ARTERIAL':['CAPITAL OUTLAY'],'COLLECTOR':[""]
    ,"SUBTOTAL":[""]}
    title2={"INTERSTATE":[""],"OTHER FREEWAYS AND EXPRESSWAYS":[""],'OTHER PRINCIPAL ARTERIAL':[""],
    'MINOR ARTERIAL':['MAINTENANCE'],'COLLECTOR':[""],'SUBTOTAL':[""]}
    
    title1=pd.DataFrame(title1)
    title2=pd.DataFrame(title2)
    title=pd.concat([title1,title2],axis=1)
    # print(title)

    result=pd.concat([state,cal_capital,cal_main],axis=1)
    frame=[title,result]
    rel=pd.concat([title,result],axis=0)
    # print(rel)

    # rel.to_csv('result.csv',index=False)

    all_result=pd.concat([state,cal_all],axis=1)
    # all_result.to_csv('all_result.csv',index=False)

    return rel,all_result

rel_2014,all_result_2014=data('/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2014_hm80.xls',
'/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2014_sf12.xls')
rel_2014.to_csv('2014_capital_maintenance_result.csv',index=False)
all_result_2014.to_csv('2014_total_result.csv',index=False)

rel_2013,all_result_2013=data('/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2013_hm80.xls',
'/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2013_sf12.xls')
rel_2013.to_csv('2013_capital_maintenance_result.csv',index=False)
all_result_2013.to_csv('2013_total_result.csv',index=False)

rel_2012,all_result_2012=data('/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2012_hm80.xls',
'/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2012_sf12.xls')
rel_2012.to_csv('2012_capital_maintenance_result.csv',index=False)
all_result_2012.to_csv('2012_total_result.csv',index=False)

rel_2009,all_result_2009=data('/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2009_hm80.xls',
'/Users/linlyu/Desktop/CMU/semester2/research/week8/2009-2019_data_hm80+sf12/2009_sf12.xls')
rel_2009.to_csv('2009_capital_maintenance_result.csv',index=False)
all_result_2009.to_csv('2009_total_result.csv',index=False)


