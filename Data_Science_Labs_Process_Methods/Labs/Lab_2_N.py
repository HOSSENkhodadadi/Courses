# -*- coding: utf-8 -*-
"""
Spyder Editor
This is the solution for Data Science Lab_2
"""
 
import matplotlib.pyplot as plt
from random import gauss
 
l = [gauss(0, 1) for _ in range (500)]
plt.hist(l)
plt.title ('Gaussian Distribution (mu = 0, sigma = 1)')
plt.show()
#______________________________________________________________
# 2.1.1 Reading GLT Dataset
# 2.1.1
# Nominal: Country,City
# Continous: Temprature
# Discrete: lattitude, logntitude
# Ordinal: Date

# Uncomment for working directly on dataset rows

#import csv
#with open (r"F:\myPolito\DSL\Data Science Lab\Lab_2\GLT_filtered.csv") as GltObj:
#    for cols in csv.reader(GltObj):
#       print (float(cols[0]) + float(cols[1]),  cols[2])
        
import csv 
with open ("F:\myPolito\DSL\Data Science Lab\Lab_2\GLT_filtered.csv", "r") as GltObj:
    csv_reader = csv.reader(GltObj)
    listOfGlt = list (csv_reader)
    header = next (csv_reader)

listOfGlt[3][1]
print (len(listOfGlt))
#______________________________________________________________
# 2.1.2
for i in range (len(listOfGlt)-1):
    if listOfGlt[i][1] == "":
        k = i+1
        nextFullIndex = k
        while(listOfGlt[k][1] == "" and k != len(listOfGlt)-1):
            nextFullIndex = k+1
            k += 1
        if i == 0 :
            listOfGlt[i][1] = str((0 + float(listOfGlt[nextFullIndex][1]))/2)
        elif i == len(listOfGlt):
            listOfGlt[i][1] = str((0 + float(listOfGlt[i-1][1]))/2)
        else:
            listOfGlt[i][1] = str((float(listOfGlt[i-1][1]) + float(listOfGlt[nextFullIndex][1])) / 2)

# uncomment to check the result            
#for i in range(100):
#    print(i+1,": ", listOfGlt[i][1])   
   
#______________________________________________________________
# 2.1.3

def CityTopTemp(CityName,N):
    keeper = []
    for i in range(219576):
        if listOfGlt[i][3] == CityName:
            keeper.append(float(listOfGlt[i][1]))
    SortedTemp = sorted(keeper, reverse = True)
    print(SortedTemp[:N])
# uncomment to check
#CityTopTemp("Abidjan",10)

def CityLowestTemp(CityName,N):
    keeper = []
    for i in range(219576):
        if listOfGlt[i][3] == CityName:
            keeper.append(float(listOfGlt[i][1]))
    SortedTemp = sorted(keeper)
    print(SortedTemp[:N])

# uncomment to check
#CityLowestTemp("Abidjan",10)

#______________________________________________________________
# 2.2.1
from collections import Counter
reviews, labels = [],[]
import csv
with open(r'F:\myPolito\DSL\Data Science Lab\Lab_2\aclimdb_reviews_train.txt',encoding='utf-8') as reviewObj:
    review_reader = csv.reader(reviewObj)
    next(review_reader)
    for row in review_reader:
        reviews.append(row[0])
        labels.append(row[1])
#______________________________________________________________
# 2.2.2    
import string
def tokenize (docs):
   """Compute the tokens for each document.
   Input: a list of strings. Each item is a document to tokenize.
   Output: a list of lists. Each item is a list containing the tokens of the
   relative document.
   """     
   tokens = []
   # learn how to debug
   for doc in docs:
       for punct in string.punctuation:
           doc = doc.replace(punct," ")
       split_doc = [ token.lower() for token in doc.split(" ") if token]
       tokens.append(split_doc)
   return tokens

token_list = tokenize(reviews)
print(token_list[1:5])
# we cannot directly access a specific range of rows with specified column in list variables 
# so list[0:5][6] is wrong instead we should use numpy
# ?how we can append a 2d list
#import numpy 
#reviewNp = numpy.array(review_as_list)
#print(reviewNp[0:5,0])

tokenize(review_as_list)
#______________________________________________________________
# 2.2.3 
TF = {}
TF_list = []
for i in range(len(token_list)):  #-1 ?
    for j in range(len(token_list[i])-1):
        if token_list[i][j] in TF.keys():
            TF[token_list[i][j]] += 1
        else:
            TF[token_list[i][j]] = 1
    TF_list.append(TF)
    TF = {}
    
#______________________________________________________________
# SOME OF MY TESTS
car = {"pride":1,
       "porche": 1,
       "benz": 1,
       "pejo":1}
car[0]
l = ["pride", "god", "damn", "prophet","pejo", "benz"]

for i in range(len(l)-1):
    if (Doesnt_exists):
    car.setdefault(l[i],1)
    else:
        car[l[i]] += 1
        
print(car)
print (car["pride"])
car["pride"] += 1
car.setdefault("paper",5)
print(car["pride"])
print(car["paper"])


print(car["pride"])
if car["paper"]:
    print('yes it exists')
else:
    print("nope it doesn't")
    
try:
    car["paper"]
except NameError:
    print("oops it doesn't exist")
else:
    print("it exists")
    
#______________________________________________________________
# 2.2.4a

DF = {}
counter = 0         
for i in range(len(TF_list)-1):
    for key in TF_list[i].keys():
        if key in DF.keys():
            continue
        for k in range(len(TF_list)-1):
            if key in TF_list[k].keys():
                counter += 1
        DF[key] = counter
        counter = 0
        
# 2.2.4b

import math
IDF = {}
for key in DF.keys():
    IDF_val = math.log10(25000/float(DF[key]))
    IDF.setdefault(key,IDF_val )      
# 2.2.4b
        

x = {"hello": 2, "goodbye": 4, "so be it": 3, "shut": 1, "haha": 0}


dict(sorted(x.items(), key=lambda item: item[1], reverse = True))        
sortedIDF = dict(sorted(IDF.items(),key = lambda item: item[1], reverse = True))        
