import math as m
import csv
import datetime
import re

##print(m.pi)
##a=m.sqrt(m.pi)
##
##b=(m.ceil(m.pi))
##c=m.floor(m.pi)
##print a,b,c

##import csv
##f=open("nfl.csv")
##print(f)
##csvreader=csv.reader(f)
##print(csvreader)
##nfl=list(csvreader)
##print (nfl)
##
##
##def count (alist, word):
##    cn=0
##    for each in alist:
##        if word == each[2]:
##            cn+=1
##        else:
##            pass
##    return cn
##
##print(count(nfl, "Pittsburgh Steelers"))


# Default display code
##class Dataset:
##    def __init__(self, data):
##        self.header = data[0]
##        self.data = data[1:]
##
##    def __str__(self):
##        my_list=self.data[:10]
##        str_list=str(my_list)
##        return str_list
##    
##    
##    def column(self, label):
##        if label not in self.header:
##            return None
##        
##        index = 0
##        for idx, element in enumerate(self.header):
##            if label == element:
##                index = idx
##        
##        column = []
##        for row in self.data:
##            column.append(row[index])
##        return column
##    
##    # Add your count unique method here
##    def count_unique(self, label):
##        unique=self.column(label)
##        unique_results=set(unique)
##        return len(unique_results)
##
##nfl_dataset = Dataset(nfl_data)
##total_years=nfl_dataset.count_unique("year")



f=open("guns.csv", "r")
data=list(csv.reader(f))
headers=data[0]
data=[data[each] for each in range(1, len(data))]
#print(headers)
#print (data[:5])


###To check for rates per year 
##year_counts={}
##years=[row[1] for row in data]
##for year in years:
##    if year in year_counts:
##        year_counts[year]+=1
##    else:
##        year_counts[year]=1
###print(year_counts)
##
##
##dates=[datetime.datetime(year=int(row[1]), month=int(row[2]), day=1) for row in data]
###print(dates[:5])
##date_counts={}
##for date in dates: 
##    if date in date_counts:
##        date_counts[date]+=1
##    else: 
##        date_counts[date]=1
###print(date_counts)
##
##
###To check by race and sex

##sex_counts={}
##race_counts={}
##races=[row[7]for row in data]
##sexes= [row[5] for row in data]
##for race in races:
##    if race in race_counts:
##        race_counts[race]+=1
##    else:
##        race_ counts[race]=1
##for sex in sexes:
##    if sex in sex_counts:
##        sex_counts[sex]+=1
##    else: 
##        sex_counts[sex]=1
###print(sex_counts)
###print(race_counts)
##
##
###Open population census file 
##cens_file=open("census.csv", "r")
##census=list(csv.reader(cens_file))
###print(census)
mapping={
    "Asian/Pacific Islander":15834141,
    "Black":40250635,
    "Native American/Native Alaskan":3739506,
    "Hispanic":44618105,
    "White":197318956
}
##
### Check for death rate per race population 
##race_per_hundredk={}
##for key, value in race_counts.items():
##    race_per_hundredk[key]=(value/mapping[key])*100000
###print(race_per_hundredk)
##
##intents=[row[3] for row in data]
#print("intents are : ", intents[:10])
##races=[row[7] for row in data]
###print("races are " , races[:10])
##homicide_race_counts={}
##
##for i, race in enumerate(races):
##    if intents[i]=="Homicide":
##        if race not in homicide_race_counts:
##            homicide_race_counts[race]=1
##        else:
##            homicide_race_counts[race]+=1
##        
##print(homicide_race_counts)
##
##for race, val in homicide_race_counts.items():
##    homicide_race_counts[race]=(val/mapping[race])*100000
##    
##print(homicide_race_counts)


# to examine relationship between month and homicide rate

##month_rates={}
##for row in data:
##    month=(datetime.date(2018, month=int(row[2]), day=1).strftime("%B"))
##    if month not in month_rates:
##        month_rates[month]=1
##    else:
##        month_rates[month]+=1
##
##print (month_rates)


#exploring homicide rate by gender
##homicide_gender_count={
##    "Female":0,
##    "Male":0
##    }
##for row in data:
##    if row[3]=="Homicide" and row[5]=="M":
##        homicide_gender_count["Male"]+=1
##    if row[3]=="Homicide" and row[5]=="F":
##        homicide_gender_count["Female"]+=1
##
##print("Homicidal count by gender", homicide_gender_count)
##
#exploring Accidental gun deaths by gender

##accidental_gender_count={
##    "Female":0,
##    "Male":0
##    }
##for row in data:
##    if row[3]=="Accidental" and row[5]=="M":
##        accidental_gender_count["Male"]+=1
##    if row[3]=="Accidental" and row[5]=="F":
##        accidental_gender_count["Female"]+=1
##        
##print("Accidental count by gender", accidental_gender_count)


###Exploring gun death by education
##education_count={}
##for row in data:
##    if row[10] in education_count:
##        education_count[row[10]]+=1
##    else:
##        education_count[row[10]]=1
##print(education_count)


#Exploring death by place
##place_count={}
##for row in data:
##    if row[9] in place_count:
##        place_count[row[9]]+=1
##    else:
##        place_count[row[9]]=1
##print(place_count)
# Home has the highest rate, that's wild.
# Ppl are more likely to die at home. What a wawu


#exploring gun death specifically at home and by gender
##home_gender_count={
##    "Female":0,
##    "Male":0
##    }
##for row in data:
##    if row[9]=="Home" and row[5]=="M":
##        home_gender_count["Male"]+=1
##    if row[9]=="Home" and row[5]=="F":
##        home_gender_count["Female"]+=1
##    
##print("without fxn ans is: ", home_gender_count)

#exploring gun death by street and by gender
street_gender_count={
    "Female":0,
    "Male":0
    }
for row in data:
    if row[9]=="Street" and row[5]=="M":
        street_gender_count["Male"]+=1
    if row[9]=="Street" and row[5]=="F":
        street_gender_count["Female"]+=1
    
print("gun deaths on the Street by gender: ", street_gender_count)
# As expected, the rates for men is more than 10X then that of women 

# Apparently, more men are dying from guns at home than women.
# I honestly thought it would be more men because, domestic violence
# maybe armed robberies are responsible for this 


##def generalFunction(num1, num2):
##    home_gender_count={
##        "Female":0,
##        "Male":0
##        }
##    for row in data:
##        if row[num1]=="Home" and row[num2]=="M":
##            home_gender_count["Male"]+=1
##        if row[num1]=="Home" and row[num2]=="F":
##            home_gender_count["Female"]+=1
##        
##    print("with fxn, and is : " , home_gender_count)
##
##generalFunction(9,5)


#Exploring location (street) and race,
##street_race_count={}
##locales =[row[9] for row in data]
##
##for idx, locale in enumerate(locales):
##    if locale=="Street":
##        tsr=races[idx]
##        if tsr in street_race_count:
##            street_race_count[tsr]+=1
##        else:
##            street_race_count[tsr]=1
##print(street_race_count)
#more black people die from guns on the streets, alarmingly high rate,
#more than *2 of the next group, whites 
