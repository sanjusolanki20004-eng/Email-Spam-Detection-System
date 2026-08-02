import pandas as pd 
df = pd.read_csv("/Users/apple/Desktop/E-MAIL-SPAM_PROJECT/data/email_spam_dataset (1).csv")
print (df.head(10))
#---------------------------------#
  #understand the shape of data#
#---------------------------------#  
print (df.tail(10))
#---------------------------------#
  #understand the shape of data#
#---------------------------------#  
print (df.shape)
#---------------------------------#
  #understand the info of data#
#---------------------------------#  
print(df.info())
#---------------------------------#
  #chack the value non or not#
#---------------------------------# 
print(df.isnull())
#---------------------------------#
# chack the value duplicate or not #
#---------------------------------# 
print(df.duplicated().sum())
#---------------------------------#
  # remove the duplicate value #
#---------------------------------# 
print(df.drop_duplicates())
#---------------------------------#
  # counts the value #
#---------------------------------# 
print(df.value_counts())
#---------------------------------#
  # check the statical summary #
#---------------------------------# 
print(df.describe(include="all"))
