""""
This is an analysis of US medical insurance data provided bu insuranace.csv
This program analyzes: Average age, Average insurance cost, Most frequent 
regions, number of smokers per age groups (18-29,30-39,40-49,50-59,60-69
, and 70+), and adverage BMI.

Program Created By: Wyatt Humphrey
Last Modified: 1-8-21
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

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
    print('The avergae age in this data set is {av_age} years old.'.format(av_age=av_age))

#average_age(us)

#calculates average insurance cost of the dataset

def average_cost(us):
    total_cost=0
    for i in range(len(us.charges)):
        total_cost+=us.charges[i]
    av_cost=total_cost/len(us.charges)
    print("The average insurance charge for this dataset is ${charge}.".format(charge=av_cost))

#average_cost(us)

#calculates region with the most frequency and the amount

def most_frequent_region(us):
    region_freq={}
    for i in us.region:
        if i not in region_freq:
            region_freq[i]=1
        if i in region_freq:
            region_freq[i]+=1
    max_region=''
    max_count=0
    for reg in region_freq:
        if region_freq[reg]> max_count:
            max_count=region_freq[reg]
            max_region=reg
    print("The region with the most frequency is {region} with a frequency of {frequency}.".format(region=max_region, frequency= max_count))

#most_frequent_region(us)


# calculates the amount of smokers per age group(18-29,30-39,40-49,50-59,60-69, and 70+)

def smoker_per_age(us):
    smoker=[]
    #smoke=[]
    smokers={"18 to 29":0,"30 to 39":0,"40 to 49":0,"50 to 59":0,"60 to 69":0}
    counter=0
    for s in us.smoker:
        if s == 'yes':
            smoker.append(us.age[counter])
            # smoke.append(us.smoker[counter])
        counter += 1
    for a in smoker:
        if (a<30):
            smokers['18 to 29']+=1
        elif (a<40) and (a>=30):
            smokers['30 to 39']+=1
        elif (a<50) and (a>=40):
            smokers['40 to 49']+=1
        elif (a<60) and (a>=50):
            smokers['50 to 59']+=1
        elif (a<70) and (a>=60):
            smokers['60 to 69']+=1
    return smokers

    

#smoker_per_age(us)

def average_bmi(bmis):
    for bmi in bmis.items():
        name=bmi[0]
        bmi_av=bmi[1][0]/bmi[1][1]
        print("The average BMI for a person from the age {age} is {bmi}.".format(age=name,bmi=bmi_av))


def average_bmi_per_age(us):
    ages=us.age
    bmis=us.bmi
    age_bmi = {"18 to 29": [0.0, 0], "30 to 39": [0.0, 0], "40 to 49": [
        0.0, 0], "50 to 59": [0.0, 0], "60 to 69": [0.0, 0]}
    # eighteen_to_29 = {}
    # thirty_to_39 = 
    # fourty_to_49 = 
    # fifty_to_59 = 
    # sixty_to_69 = 
    # seventy_plus =
    count=0 
    for a in ages:
        if (a<30):
            age_bmi['18 to 29'][0]+=bmis[count]
            age_bmi['18 to 29'][1] += 1
        elif (a<40) and (a>=30):
            age_bmi['30 to 39'][0] += bmis[count]
            age_bmi['30 to 39'][1] += 1
        elif (a<50) and (a>=40):
            age_bmi['40 to 49'][0] += bmis[count]
            age_bmi['40 to 49'][1] += 1
        elif (a<60) and (a>=50):
            age_bmi['50 to 59'][0] += bmis[count]
            age_bmi['50 to 59'][1] += 1
        elif (a<70) and (a>=60):
            age_bmi['60 to 69'][0] += bmis[count]
            age_bmi['60 to 69'][1] += 1
        count+=1
    average_bmi(age_bmi)

#average_bmi_per_age(us)













def print_data(us):
    print('The anallysis for the data is as follows: \n')
    average_age(us)
    print('\n')
    average_cost(us)
    print('\n')
    most_frequent_region(us)
    print('\n')
    smokers=smoker_per_age(us)
    for age in smokers:
        print("The amount of smokers that are {age} years old is {number}.".format(
            age=age, number=smokers[age]))
    print('\n')
    average_bmi_per_age(us)

print_data(us)

# plt.hist(us.age,bins=[18,30,40,50,60,70],rwidth=0.95)
plt.bar(smoker_per_age(us).keys(),smoker_per_age(us).values(),width=.75)
plt.xlabel("Age Groups")
plt.ylabel("Amount of Smokers")
plt.title("Frequency of Smokers Per Age Group")
plt.show()
