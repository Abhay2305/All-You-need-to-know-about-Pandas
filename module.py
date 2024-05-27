import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

data=pd.read_csv("/content/drive/MyDrive/Coursera.csv")
data = pd.DataFrame(data)

data.describe(include=['object']).T

data.describe()

data.shape

data.info()

data.isnull()

data.isnull().sum() 

data['Difficulty Level'].value_counts()

data['Course Rating'].value_counts()

data = data[['Course Name','Difficulty Level','Course Description','Skills']]

data.head(5)

data['Course Name'] = data['Course Name'].str.replace(' ',',')
data['Course Name'] = data['Course Name'].str.replace(',,',',')
data['Course Name'] = data['Course Name'].str.replace(':','')
data['Course Description'] = data['Course Description'].str.replace(' ',',')
data['Course Description'] = data['Course Description'].str.replace(',,',',')
data['Course Description'] = data['Course Description'].str.replace('_','')
data['Course Description'] = data['Course Description'].str.replace(':','')
data['Course Description'] = data['Course Description'].str.replace('(','')
data['Course Description'] = data['Course Description'].str.replace(')','')

#removing paranthesis from skills columns 
data['Skills'] = data['Skills'].str.replace('(','')
data['Skills'] = data['Skills'].str.replace(')','')

data.head(5)

data['tags'] = data['Course Name'] + data['Difficulty Level'] + data['Course Description'] + data['Skills']

data.head(5)

data['tags'].iloc[1]

new_df = data[['Course Name','tags']]

new_df.head(5)

new_df['tags'] = data['tags'].str.replace(',',' ')

new_df['Course Name'] = data['Course Name'].str.replace(',',' ')

new_df.rename(columns = {'Course Name':'course_name'}, inplace = True)

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

new_df.head(5)

new_df.shape

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000,stop_words='english')

vectors = cv.fit_transform(new_df['tags']).toarray()

import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

#defining the stemming function
def stem(text):
    y=[]
    
    for i in text.split():
        y.append(ps.stem(i))
    
    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

def recommend(course):
    course_index = new_df[new_df['course_name'] == course].index[0]
    distances = similarity[course_index]
    course_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[1:7]
    
    for i in course_list:
        print(new_df.iloc[i[0]].course_name)

recommend('Business Strategy Business Model Canvas Analysis with Miro')
