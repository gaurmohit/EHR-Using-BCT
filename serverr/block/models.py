from django.db import models
import pandas as pd
import json

file = open('average.json', 'r')
average = json.loads(file.read())
file.close()


def avg(key='', d=''):
    if key in average:
        return average[key]
    else:
        return d


class Block(models.Model):
    # Position = models.PositiveIntegerField(default=0)

    # Needed for block chain
    previous_hash = models.CharField(blank=True, null=True, max_length=255)
    my_hash = models.CharField(blank=True, null=True, max_length=255)
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    # Updation is not allowed

    # Final Values ...
    UserId = models.PositiveIntegerField(
        default=1, blank=True, null=True)
    Gender = models.CharField(default=avg(
        'Gender', 'Female'), blank=True, null=True, max_length=50)
    Years_in_US = models.PositiveSmallIntegerField(
        default=avg('Years_in_US', 0), blank=True, null=True)
    Maritial_Status = models.PositiveSmallIntegerField(
        default=avg('Maritial_Status', 1), blank=True, null=True)
    People_Family = models.PositiveSmallIntegerField(
        default=avg('People_Family', 4), blank=True, null=True)
    People_Household = models.PositiveSmallIntegerField(
        default=avg('People_Household', 4), blank=True, null=True)
    Family_income = models.FloatField(default=avg(
        'Family_income', 5.0), blank=True, null=True)
    Household_Income = models.FloatField(default=avg(
        'Household_Income', 4), blank=True, null=True)
    GlycoHemoglobin = models.FloatField(default=avg(
        'GlycoHemoglobin', 4), blank=True, null=True)
    ArmCircum = models.FloatField(default=avg(
        'ArmCircum', 28.52824824212779), blank=True, null=True)
    SaggitalAbdominal = models.FloatField(default=avg(
        'SaggitalAbdominal', 28.52824824212779), blank=True, null=True)
    GripStrength = models.FloatField(default=avg(
        'ArmCircum', 62.455232854376845), blank=True, null=True)
    Breast_fed = models.PositiveSmallIntegerField(
        default=avg('Breast_fed', 1), blank=True, null=True)

    Taking_Insulin = models.PositiveSmallIntegerField(
        default=avg('Taking_Insulin', 1), blank=True, null=True)
    Taking_Oral_Agents = models.PositiveSmallIntegerField(
        default=avg('Taking_Oral_Agents', 1), blank=True, null=True)
    Eyes_Affected = models.PositiveSmallIntegerField(
        default=avg('Eyes_Affected', 1), blank=True, null=True)
    Recent_BP = models.FloatField(default=avg(
        'Recent_BP', 5.0), blank=True, null=True)
    Diabetes = models.PositiveSmallIntegerField(
        default=avg('Diabetes', 1), blank=True, null=True)
    # Other fields .... ----
    medication = models.PositiveSmallIntegerField(
        default=avg('People_Household', 1), blank=True, null=True)
    age = models.PositiveSmallIntegerField(default=avg(
        'People_Household', 1), blank=True, null=True)
    # income = models.CharField(blank=True, null=True, max_length=2)
    native_country = models.CharField(default=avg(
        'native-country'), blank=True, null=True, max_length=150)
    occupation = models.CharField(default=avg(
        'occupation'), blank=True, null=True, max_length=100)
    race = models.CharField(default=avg(
        'race'), blank=True, null=True, max_length=100)
    workclass = models.CharField(default=avg(
        'workclass', 'Private'), blank=True, null=True, max_length=100)
    Total = models.FloatField(default=avg(
        'Total', 5.0), blank=True, null=True)

    @classmethod
    def add_k_params(cls, df):
        df['gender'] = df['Gender']
        df['marital-status'] = df['Maritial_Status']
        df['native-country'] = df['native_country']
        df['income'] = df.apply(
            lambda x:
                '<=50K' if x['Family_income'] + x['Household_Income'] <= 50.00
                else '>50K',
            axis=1)
        return df

    @classmethod
    def add_l_params(cls, df):
        df['Male'] = df.apply(
            lambda x:
            1
            if x['Gender'] == 'Male'
            else 0,
            axis=1)
        df['Female'] = df.apply(lambda x: 1 if x['Gender']
                                == 'Female' else 0, axis=1)
        return df

    @classmethod
    def add_t_params(cls, df):
        df['BP'] = df['Recent_BP'].apply(
            lambda x: 'Low' if x < 130 else 'High')
        df['Total People'] = df['People_Household']
        df['Total_Income'] = df['Family_income']
        return df

    @classmethod
    def filter_params(cls, df, f='k'):
        file_names = {
            'k': 'block/anonymous/data_final.csv',
            'l': 'block/anonymous/finalized-1.csv',
            't': 'block/anonymous/finalized-2.csv'
        }

        d = pd.read_csv(file_names.get(f, file_names['k']))
        return df.loc[:, [x for x in d.columns if x in df.columns]]

    @classmethod
    def fillNa(cls, df):
        for col in df.columns:
            if col in average:
                df[col] = df[col].fillna(average[col])
            else:
                print("Warning : ", col, "Name was not found in average dictionary")
        return df

    @classmethod
    def prepare(cls, df, f='k'):
        if f == 'k':
            df = cls.add_k_params(df)
        if f == 'l':
            df = cls.add_l_params(df)
        if f == 't':
            df = cls.add_t_params(df)
        df = cls.fillNa(df)
        df = cls.filter_params(df, f)
        return df
    # ---------------- The below fields were not found -------------

    # BloodPressure = models.PositiveSmallIntegerField(default=0)
