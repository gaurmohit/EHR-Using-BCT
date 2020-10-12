import pandas as pd
import numpy as np

'''
d_f = pd.read_csv('data_final.csv')
f_1 = pd.read_csv('finalized-1.csv')
f_2 = pd.read_csv('finalized-2.csv')

#print(d_f.columns)
#print(f_1.columns)
#print(f_2.columns)


d_f_d = {'ID':[91114], 'age':[21], 'gender':['Male'], 'native-country':['United States'], 'race':['black'], 'marital-status':['Never Married'],
       'workclass':['Private'], 'occupation':['Other Service'], 'income':[45], 'People_Family':[4], 'education':['11th'],
       'GlycoHemoglobin':[13.7], 'ArmCircum':[35.1], 'SaggitalAbdominal':[20.9], 'GripStrength':[56.3],
       'Taking_Insulin':[0], 'Taking_Oral_Agents':[1], 'Eyes_Affected':[1], 'Recent_BP':[125],
       'Diabetes':[1]}

f_1_d = {'ID':[91114], 'Gender':['Male'], 'Male':[1], 'Female':[0], 'Years_in_US':[0], 'Maritial_Status':[1],
       'People_Family':[3], 'People_Household':[3], 'Family_income':[7],
       'Household_Income':[4], 'GlycoHemoglobin':[13.7], 'ArmCircum':[35.3], 'SaggitalAbdominal':[20.6],
       'GripStrength':[56.3], 'Total':[125], 'Breast_fed':[0], 'medication':[1], 'Taking_Insulin':[1],
       'Taking_Oral_Agents':[1], 'Eyes_Affected':[1], 'Recent_BP':[120], 'Diabetes':[2]}

f_2_d = {'ID':[91114], 'Gender':['Male'], 'Years_in_US':[0], 'Maritial_Status':[1], 'People_Family':[3],
       'People_Household':[3], 'Total People':[6], 'Family_income':[7], 'Household_Income':[4],
       'Total_Income':[11], 'GlycoHemoglobin':[13.9], 'ArmCircum':[35.3], 'SaggitalAbdominal':[20.6],
       'GripStrength':[56.3], 'Total':[125], 'Breast_fed':[1], 'medication':[1], 'Taking_Insulin':[1],
       'Taking_Oral_Agents':[1], 'Eyes_Affected':[1], 'Recent_BP':[120], 'BP':{'Low'}, 'Diabetes':[2]}

df_k = pd.DataFrame(data=d_f_d)
#print(df.iloc[0][:])
df_1 = pd.DataFrame(data=f_1_d)
df_2 = pd.DataFrame(data=f_2_d)
'''


def anonymize(data_frame, ch):
    if ch == 'k':
        '''data_frame.to_csv('data_final.csv',
                          index=False)
        df = pd.read_csv('data_final.csv')'''
        df = data_frame

        for i, j in enumerate(df['age']):
            if j >= 17 and j <= 36:
                df['age'][i] = '[17, 36]'
            elif j >= 37 and j <= 56:
                df['age'][i] = '[37, 56]'
            elif j >= 57 and j <= 76:
                df['age'][i] = '[57, 76]'
            elif j >= 77 and j <= 90:
                df['age'][i] = '[77, 90]'
            else:
                df['age'][i] = '*'

        for i, j in enumerate(df['People_Family']):
            if j >= 1 and j <= 7:
                df['People_Family'][i] = '[1, 7]'
            else:
                df['People_Family'][i] = '*'

        for i, j in enumerate(df['GlycoHemoglobin']):
            if j >= 6.9 and j <= 10.0:
                df['GlycoHemoglobin'][i] = '[6.9, 10.0]'
            elif j >= 3.5 and j <= 6.8:
                df['GlycoHemoglobin'][i] = '[3.5, 6.8]'
            elif j >= 10.1 and j <= 14.3:
                df['GlycoHemoglobin'][i] = '[10.1, 14.3]'
            else:
                df['GlycoHemoglobin'][i] = '*'

        for i, j in enumerate(df['SaggitalAbdominal']):
            if j >= 19.9 and j <= 21.0:
                df['SaggitalAbdominal'][i] = '[19.9, 21.0]'
            elif j >= 23.5 and j <= 24.6:
                df['SaggitalAbdominal'][i] = '[23.5, 24.6]'
            elif j >= 24.7 and j <= 25.8:
                df['SaggitalAbdominal'][i] = '[24.5, 25.8]'
            elif j >= 13.9 and j <= 15.0:
                df['SaggitalAbdominal'][i] = '[13.9, 15.0]'
            elif j >= 16.3 and j <= 17.4:
                df['SaggitalAbdominal'][i] = '[16.3, 17.4]'
            elif j >= 22.3 and j <= 24.4:
                df['SaggitalAbdominal'][i] = '[22.3, 24.4]'
            elif j >= 17.5 and j <= 18.6:
                df['SaggitalAbdominal'][i] = '[17.5, 18.6]'
            elif j >= 16.3 and j <= 17.4:
                df['SaggitalAbdominal'][i] = '[16.3, 17.4]'
            elif j >= 12.7 and j <= 13.8:
                df['SaggitalAbdominal'][i] = '[12.3, 13.8]'
            elif j >= 21.1 and j <= 22.2:
                df['SaggitalAbdominal'][i] = '[21.1, 22.2]'
            elif j >= 18.7 and j <= 19.8:
                df['SaggitalAbdominal'][i] = '[18.7, 19.8]'
            elif j >= 27.1 and j <= 28.2:
                df['SaggitalAbdominal'][i] = '[27.1, 28.2]'

            elif j >= 30.7 and j <= 31.8:
                df['SaggitalAbdominal'][i] = '[30.7, 31.8]'
            elif j >= 11.5 and j <= 12.6:
                df['SaggitalAbdominal'][i] = '[11.5, 12.6]'
            elif j >= 34.5 and j <= 35.7:
                df['SaggitalAbdominal'][i] = '[34.7, 35.7]'
            elif j >= 37.1 and j <= 40.1:
                df['SaggitalAbdominal'][i] = '[37.1, 40.1]'

            elif j >= 31.9 and j <= 33.0:
                df['SaggitalAbdominal'][i] = '[31.9, 33.0]'
            elif j >= 35.8 and j <= 37.0:
                df['SaggitalAbdominal'][i] = '[35.8, 37.0]'
            elif j >= 33.1 and j <= 34.4:
                df['SaggitalAbdominal'][i] = '[33.1, 34.4]'
            elif j >= 30.1 and j <= 11.4:
                df['SaggitalAbdominal'][i] = '[30.1, 11.4]'
            else:
                df['SaggitalAbdominal'][i] = '*'

        for i, j in enumerate(df['Recent_BP']):
            #array(['[88.0, 135.0]', '[136.0, 7777.0]', '*'], dtype=object)
            if j >= 88.0 and j <= 135.0:
                df['Recent_BP'][i] = '[88.0, 135.0]'
            elif j >= 136.0 and j <= 7777.0:
                df['Recent_BP'][i] = '[136.0, 7777.0]'
            else:
                df['Recent_BP'][i] = '*'

        # df.to_csv('new_data.csv', index=False)

        return df  # .iloc[-1][:]
    elif ch == 'l':
        '''data_frame.to_csv('finalized-1.csv',
                          index=False)

        df = pd.read_csv('finalized-1.csv')'''
        df = data_frame

        df['Family_income'] = df['Family_income'].fillna(
            df['Family_income'].mean())
        df['Household_Income'] = df['Household_Income'].fillna(
            df['Household_Income'].mean())

        df['People_Family'] = pd.cut(df['People_Family'], 3)
        df['People_Household'] = pd.cut(df['People_Household'], 4)
        df['Household_Income'] = pd.cut(df['Household_Income'], 4)
        df['Family_income'] = pd.cut(df['Family_income'], 4)
        df['GlycoHemoglobin'] = pd.cut(df['GlycoHemoglobin'], 6)
        df['ArmCircum'] = pd.cut(df['ArmCircum'], 6)
        df['SaggitalAbdominal'] = pd.cut(df['SaggitalAbdominal'], 7)
        df['GripStrength'] = pd.cut(df['GripStrength'], 2)

        # df.to_csv('new_data_1.csv', index=False)

        return df  # .iloc[-1][:]

    elif ch == 't':
        '''data_frame.to_csv('finalized-2.csv',
                          index=False, header=True)


        df2 = pd.read_csv('finalized-2.csv')
        '''
        df2 = data_frame
        df2['Household_Income'] = df2['Household_Income'].fillna(
            df2['Household_Income'].mean())
        df2['Total_Income'] = df2['Total_Income'].fillna(
            df2['Total_Income'].mean())

        df2['GlycoHemoglobin'] = pd.cut(df2['GlycoHemoglobin'], 6)
        df2['ArmCircum'] = pd.cut(df2['ArmCircum'], 6)
        df2['SaggitalAbdominal'] = pd.cut(df2['SaggitalAbdominal'], 7)
        df2['GripStrength'] = pd.cut(df2['GripStrength'], 2)
        df2['Total'] = pd.cut(df2['Total'], 3)
        df2['Total People'] = pd.cut(df2['Total People'], 3)
        df2['Family_income'] = pd.cut(df2['Family_income'], 5)
        df2['Household_Income'] = pd.cut(df2['Household_Income'], 5)
        df2['Total_Income'] = pd.cut(df2['Total_Income'], 15)
        df2['Recent_BP'] = pd.cut(df2['Recent_BP'], 3)
        df2['People_Family'] = pd.cut(df2['People_Family'], 3)
        df2['People_Household'] = pd.cut(df2['People_Household'], 3)

        # df2.to_csv('new_data_2.csv', index=False)

        return df2  # .iloc[-1][:]

    else:
        print('Invalid Arguement')

# print(anonymize(df_2,'t'))
