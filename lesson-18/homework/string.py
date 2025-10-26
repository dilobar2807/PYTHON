import pandas as pd
df=pd.read_csv('tackoverflow_qa (1).csv')
df.head()
df
#Find all questions that were created before 2014
df['creationdate']=pd.to_datetime(df['creationdate'])
old_questions=df[df['creationdate']<'2014-01-01']
old_questions

#Find all questions with a score more than 50
score_50=df[df['score']>50]
score_50

#Find all questions with a score between 50 and 100
score_b=df[(df['score']>50) & (df['score']<100)]
score_b

df

#Find all questions answered by Scott Boston
scott_questions=df[df['quest_name']=='Scott Boston']
scott_questions

#Find all questions answered by the following 5 users
follow=df[df['answercount']==5]
follow

#Find all questions that were created between March, 2014 and October 2014 that were answered by 
# Unutbu and have score less than 5.

df['creationdate']=pd.to_datetime(df['creationdate'])
moret=df[(df['creationdate']>'2014-03-01') &
        (df['creationdate']<'2014-10-01') & 
        (df['ans_name']=="unutbu") & 
        (df['score']<5)]
moret

#Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

all_question=df[(df['score']>5) & (df['score']<10) | (df['viewcount']>10000)]
all_question

#Find all questions that are not answered by Scott Boston

answer_not_scott=df[df['ans_name']!='Scott Boston']
answer_not_scott

######## HOMEWORK-3 #######

titanic_df=pd.read_csv("titanic.csv")
titanic_df.head()
#Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female
#passengers in Class 1 with ages between 20 and 30.

female_c=titanic_df[(titanic_df['Pclass']==1) & 
                    (titanic_df['Sex']=='female') & 
                    (titanic_df['Age'] > 20) & 
                    (titanic_df['Age']<30)]
female_c

#Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

passengers=titanic_df[titanic_df['Fare']>100]
passengers

#Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone
#(no siblings, spouses, parents, or children).

passengers_alone=titanic_df[(titanic_df['Survived']==0) & (titanic_df['SibSp']==0) & (titanic_df['Parch']==0)]
passengers_alone

#Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked
#from 'C' and paid more than $50.

passengers_s=titanic_df[(titanic_df['Fare']>50) & (titanic_df['Embarked']=='C')]
passengers_s

#Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or
#spouses aboard and parents or children aboard.

passengers_both=titanic_df[(titanic_df['SibSp']==1) & (titanic_df['Parch']!=0) & titanic_df['SibSp']]
passengers_both

#Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers 
#aged 15 or younger who did not survive.

younger_passengers=titanic_df[(titanic_df['Survived']==0) & (titanic_df['Age']<15)]
younger_passengers

#Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a 
#fare greater than $200.

passengers_with_cabin=titanic_df[(titanic_df['Fare']>200) & 
                                  (titanic_df['Cabin'].notna()==True)]
passengers_with_cabin

#Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with 
# passengers whose PassengerId is an odd number.

passenger_with_odd=titanic_df[titanic_df['PassengerId'] % 2 != 0]
passenger_with_odd

#Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.

passenger_with_unique_ticket=titanic_df[~titanic_df['Ticket'].duplicated(keep=False)]
passenger_with_unique_ticket

#Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with
#female passengers having 'Miss' in their name and were in Class 1.
titanic_df['Name'].astype('string')
#miss_passeng=titanic_df[(titanic_df['Pclass']==1) & (titanic_df['Sex']=='female') & ]





