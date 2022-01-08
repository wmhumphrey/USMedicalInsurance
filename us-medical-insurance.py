""""
This is an analysis of US medical insurance data provided bu insuranace.csv
This program analyzes: Average age, Average insurance cost, Most frequent 
regions, average number of smokers per age groups (18-29,30-39,40-49,50-59,60-69
, and 70+), and adverage BMI.

Program Created By: Wyatt Humphrey
Last Modified: 1-8-21
"""
import csv

# Parses insurace.csv data into age,sex,bmi,children,smoker,region,charges
class MedicalData:

    age=[]
    sex=[]
    bmi=[]
    children=[]
    smoker=[]
    region=[]
    charges=[]

    def __init__(self) -> None:
        with open('insurance.csv', newline='') as medfile:
            medfile_dict=csv.DictReader(medfile)
            for row in medfile_dict:
                self.age.append(int(row['age']))
                self.sex.append(row['sex'])
                self.bmi.append(float(row['bmi']))
                self.children.append(row['children'])
                self.smoker.append(row['smoker'])
                self.region.append(row['region'])
                self.charges.append(float(row['charges']))

us=MedicalData()

#calculates average age of data set

def average_age(us):
    total_age=0
    for i in range(len(us.age)):
        total_age+=us.age[i]
    av_age= total_age/len(us.age)
    print('The avergae age in this data set is {av_age}'.format(av_age=av_age))

#average_age(us)

#calculates average insurance cost of the dataset

def average_cost(us):
    total_cost=0
    for i in range(len(us.charges)):
        total_cost+=us.charges[i]
    av_cost=total_cost/len(us.charges)
    print("The average insurance charge for this dataset is {charge}".format(charge=av_cost))

#average_cost(us)

def most_frequent_region(us):
    region_freq={}
    for i in us.region:
        if i not in region_freq:
            region_freq[i]=1
        if i in region_freq:
            region_freq[i]+=1
    print(region_freq)
    max_region=''
    max_count=0
    for reg in region_freq:
        if region_freq[reg]> max_count:
            max_count=region_freq[reg]
            max_region=reg
        
    print("The region with the most frequency is {region} with a frequency of {frequency}.".format(region=max_region.capitalize, frequency= max_count))

most_frequent_region(us)