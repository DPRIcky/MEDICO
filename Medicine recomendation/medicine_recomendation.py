#------------------------COADED IN NOTEBOOK- GOOGLE COLAB------------------------------------------------------

#import the libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from google.colab import files
files.upload()

df = pd.read_csv("Medicine_Recomendation.csv", encoding = 'unicode_escape', error_bad_lines=False)
#Show the data
df

#Create a list of columns to keep
columns = ['Drug_Name', 'Reason', 'Company_Name', 'Rating']
#Create a function to combine important features
def combine_features(data):
  features = []
  for i in range (0, data.shape[0]):
    features.append(data['Drug_Name'][i]+" "+data['Reason'][i]+' '+data['Company_Name'][i]+" "+data['Rating'][i])
  return features
#create a column to show combined features
df['Combined_Features'] = combine_features(df)
#show the data
df
#Convert the text from new column to a matrix of word counts
cm = CountVectorizer().fit_transform(df['Combined_Features'])
#Get the cosine similarity matrix from the count matrix
cs = cosine_similarity(cm)
#print scores
print(cs)
#Get the name of the medicine from the user
k = input('Enter the sl no. of the medicine from the excel sheet: ')
title = df['Drug_Name'][(int(k)-1)]
#show the Drug Name
title
#Find the index
index = df[df.Drug_Name == title]['SlNo'].values[0]
index
#Create a list of tuples in the form (Drug_Name, similarity scores)
scores = list(enumerate(cs[index]))
print(scores)
#sort the list of similar drugs in decending order
sorted_scores = sorted(scores, key = lambda x:x[int(k)-1], reverse = True)
#show the sorted scores
sorted_scores
#create loop to print the first 5 drugs from the sorted list
j = 0
print("Other recomended medicines to the given medicine" + title + 'are: \n')
for item in sorted_scores:
  drug_name = df[df.SlNo == item[0]]['Drug_Name'].values[0]
  print(j+1, drug_name)
  j = j+1
  if j>=5:
    break