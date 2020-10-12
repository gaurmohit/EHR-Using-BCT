import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics


def finalized_1():

    dataset = pd.read_csv("finalized.csv") 

    ##for Family_income

    np.random.seed(40)
    dataset['Family_income'] = np.random.randint(1,10,size=dataset.shape[0])

    
    ## for total   
    dataset['Total'] = dataset['GlycoHemoglobin'] + dataset['ArmCircum'] +dataset['SaggitalAbdominal']+dataset['GripStrength']
    
    ##for medication
    dataset['medication'] = np.logical_or(dataset['Taking_Insulin'] == 1,dataset['Taking_Oral_Agents'] == 1)
    dataset.loc[dataset['medication'] == True, 'medication'] = 1    
    dataset.loc[dataset['medication'] == False, 'medication'] = 0 
        
        
    
    ##For MAking male and female columns    
        
    dataset.loc[dataset['Gender'] == 'Male', 'Male'] = 1    
    dataset.loc[dataset['Gender'] == 'Female', 'Male'] = 0  
        
    dataset.loc[dataset['Gender'] == 'Male', 'Female'] = 0    
    dataset.loc[dataset['Gender'] == 'Female', 'Female'] = 1  
    #dataset.info()
    #print('\n')
    
    
    dataset.to_csv("finalized-1.csv", columns= ['ID','Gender','Male','Female','Years_in_US','Maritial_Status','People_Family',
    'People_Household','Family_income','Household_Income','GlycoHemoglobin','ArmCircum','SaggitalAbdominal',
    'GripStrength','Total','Breast_fed','medication','Taking_Insulin','Taking_Oral_Agents','Eyes_Affected',
    'Recent_BP','Diabetes'
    ], index=False)

    df=pd.read_csv('finalized-1.csv')

    df['Family_income']=df['Family_income'].fillna(df['Family_income'].mean())

    df['Household_Income']=df['Household_Income'].fillna(df['Household_Income'].mean())

    df['People_Family'] = pd.cut(df['People_Family'],3)

    df['People_Household'] = pd.cut(df['People_Household'],4)

    df['Household_Income'] = pd.cut(df['Household_Income'],4)
    df['Family_income'] = pd.cut(df['Family_income'],4)

    df['GlycoHemoglobin'] = pd.cut(df['GlycoHemoglobin'],6)

    df['ArmCircum'] = pd.cut(df['ArmCircum'],6)

    df['SaggitalAbdominal'] = pd.cut(df['SaggitalAbdominal'],7)

    df['GripStrength'] = pd.cut(df['GripStrength'],2)

    df.to_csv('new_data_1.csv',index=False)
       


def finalized_2():
    dataset = pd.read_csv("finalized.csv")
    ## for total   
    dataset['Total'] = dataset['GlycoHemoglobin'] + dataset['ArmCircum'] +dataset['SaggitalAbdominal']+dataset['GripStrength']
    
    ##for medication
    dataset['medication'] = np.logical_or(dataset['Taking_Insulin'] == 1,dataset['Taking_Oral_Agents'] == 1)
    dataset.loc[dataset['medication'] == True, 'medication'] = 1    
    dataset.loc[dataset['medication'] == False, 'medication'] = 0 

    ##for Family_income

    np.random.seed(40)
    dataset['Family_income'] = np.random.randint(1,10,size=dataset.shape[0])

    ## for total people  
    dataset['Total People'] = dataset['People_Family'] + dataset['People_Household'] 

    dataset['Household_Income']=dataset['Household_Income'].fillna(dataset['Household_Income'].mean())

    
    ##for total income 
    dataset['Total_Income'] = dataset['Family_income'] + dataset['Household_Income']

    ## for bp
    dataset.loc[dataset['Recent_BP'] <= 135 , 'BP'] = 'Low'    
    dataset.loc[dataset['Recent_BP'] > 135, 'BP'] ='High' 


    #print(dataset.isna().sum())
    
    dataset.to_csv("finalized-2.csv", columns= ['ID','Gender','Years_in_US','Maritial_Status','People_Family',
    'People_Household','Total People','Family_income','Household_Income','Total_Income','GlycoHemoglobin','ArmCircum','SaggitalAbdominal',
    'GripStrength','Total','Breast_fed','medication','Taking_Insulin','Taking_Oral_Agents','Eyes_Affected',
    'Recent_BP','BP','Diabetes'
    ], index=False)




    df2=pd.read_csv('finalized-2.csv')


    df2['Household_Income']=df2['Household_Income'].fillna(df2['Household_Income'].mean())
    
    df2['Total_Income']=df2['Total_Income'].fillna(df2['Total_Income'].mean())

    df2['GlycoHemoglobin'] = pd.cut(df2['GlycoHemoglobin'],6)
    df2['ArmCircum'] = pd.cut(df2['ArmCircum'],6)
    df2['SaggitalAbdominal'] = pd.cut(df2['SaggitalAbdominal'],7)
    df2['GripStrength'] = pd.cut(df2['GripStrength'],2)
    df2['Total'] = pd.cut(df2['Total'],3)
    df2['Total People'] = pd.cut(df2['Total People'],3)
    df2['Family_income']=pd.cut(df2['Family_income'],5)
    df2['Household_Income']=pd.cut(df2['Household_Income'],5)
    df2['Total_Income'] = pd.cut(df2['Total_Income'],15)
    df2['Recent_BP'] = pd.cut(df2['Recent_BP'],3)
    df2['People_Family'] = pd.cut(df2['People_Family'],3)
    df2['People_Household'] = pd.cut(df2['People_Household'],3)

    #print('\n')
    #print(df2.isna().sum())

    df2.to_csv('new_data_2.csv',index=False)



    
    
 
## for genrating Finalized-1   
finalized_1()
## for genrating Finalized-2  
finalized_2()   














