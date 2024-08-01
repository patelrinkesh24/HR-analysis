#!/usr/bin/env python
# coding: utf-8
# In[1]:
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
import cufflinks as cf 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

# In[2]:
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
train.head()

# In[3]:
train.columns

# In[4]:
test.head()

# In[5]:
train.shape

# In[6]:
train.info()

# In[7]:
train.isnull().sum()

# In[8]:
#### Visualizing the null values using missingo function
import missingno as msno
msno.matrix(train)

# In[9]:
test.shape

# In[10]:
test.info()

# In[11]:
test.isnull().sum()

# In[12]:
import missingno as msno
msno.bar(test, color = 'r', figsize = (10,8))  #### Check the missing values in test data

# In[13]:
sns.pairplot(train)

# In[14]:
train.hist(edgecolor='red', linewidth=2, figsize=(15, 15));

# In[15]:
plt.figure(figsize=(30, 30))
sns.heatmap(train.corr(), annot=True, cmap="RdYlGn", annot_kws={"size":15})

# In[16]:
train['department'].value_counts()

# In[17]:
plt.subplots(figsize=(15,5))
train['department'].value_counts(normalize = True)
train['department'].value_counts(dropna = False).plot.bar(color=['black', 'red', 'green', 'blue', 'cyan'])
plt.show()

# In[18]:
# checking the different regions of the company
plt.subplots(figsize=(15,5))
sns.countplot(train['region'], color = 'red')
plt.title('Different Regions in the company', fontsize = 30)
plt.xticks(rotation = 60)
plt.xlabel('Region Code')
plt.ylabel('count')
plt.show()

# In[19]:
train['education'].value_counts()

# In[20]:
# Prepare Data
df = train.groupby('education').size()
# Make the plot with pandas
df.plot(kind='pie', subplots=True, figsize=(15, 8))
plt.title("Pie Chart of different types of education")
plt.ylabel("")
plt.show()

# In[21]:
train['gender'].value_counts()

# In[25]:
size = [38496, 16312]
labels = "Male", "Female"
colors = ['BLUE', 'RED']
explode = [0, 0.1]
plt.subplots(figsize=(8,8))
plt.pie(size, labels = labels, colors = colors, explode = explode, shadow = True, autopct = "%.2f%%")
plt.title('A Pie Chart Representing GenderGap', fontsize = 30)
plt.axis('off')
plt.legend()
plt.show()

# In[27]:
plt.subplots(figsize=(15,5))
sns.countplot(x = 'education', data = train, hue = 'gender', palette = 'dark')
plt.show()

# In[28]:
# comparison of promoted gender male & female
plt.subplots(figsize=(15,5))
sns.countplot(x = 'gender', data = train, hue = 'is_promoted', palette = 'dark')
plt.show()

# In[147]:
train['recruitment_channel'].value_counts()

# In[148]:
# plotting a donut chart for visualizing each of the recruitment channel's share
size = [30446, 23220, 1142]
colors = ['black', 'red', 'blue']
labels = "Others", "Sourcing", "Reffered"
my_circle = plt.Circle((0, 0), 0.7, color = 'white')
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size, colors = colors, labels = labels, shadow = True, autopct = '%.2f%%')
plt.title('Showing share of different Recruitment Channels', fontsize = 30)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.legend()
plt.show()

# In[149]:
plt.subplots(figsize=(15,5))
sns.distplot(train['age'])
plt.title('Distribution of Age of Employees', fontsize = 30)

# In[150]:
train['previous_year_rating'].value_counts().sort_values().plot.bar(color = 'violet', figsize = (15, 7))
plt.title('Distribution of Previous year rating of the Employees', fontsize = 30)
plt.xlabel('Ratings', fontsize = 15)
plt.ylabel('count')
plt.show()

# In[151]:
plt.subplots(figsize=(15,8))
sns.distplot(train['length_of_service'], color = 'green')
plt.title('Distribution of length of service among the Employees', fontsize = 30)
plt.xlabel('Length of Service in years')
plt.ylabel('count')
plt.show()

# In[152]:
train['KPIs_met >80%'].value_counts()

# In[153]:


# plotting a pie chart


size = [35517, 19291]
labels = "Not Met KPI > 80%", "Met KPI > 80%"
colors = ['violet', 'grey']
explode = [0, 0.1]

plt.rcParams['figure.figsize'] = (8, 8)
plt.pie(size, labels = labels, colors = colors, explode = explode, shadow = True, autopct = "%.2f%%")
plt.title('A Pie Chart Representing Gap in Employees in terms of KPI', fontsize = 30)
plt.axis('off')
plt.legend()
plt.show()


# In[154]:
train['awards_won?'].value_counts()

# In[155]:
# plotting a donut chart for visualizing each of the recruitment channel's share
size = [53538, 1270]
colors = ['blue', 'red']
labels = "Awards Won", "NO Awards Won"
my_circle = plt.Circle((0, 0), 0.7, color = 'white')
plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size, colors = colors, labels = labels, shadow = True, autopct = '%.2f%%')
plt.title('Showing a Percentage of employees who won awards', fontsize = 30)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.legend()
plt.show()

# In[156]:
# checking the distribution of the avg_training score of the Employees
plt.subplots(figsize=(15,7))
sns.distplot(train['avg_training_score'], color = 'blue')
plt.title('Distribution of Training Score among the Employees', fontsize = 30)
plt.xlabel('Average Training Score', fontsize = 20)
plt.ylabel('count')
plt.show()

# In[29]:
train['is_promoted'].value_counts()

# In[30]:
# finding the %age of people promoted
promoted = (4668/54808)*100
print("Percentage of Promoted Employees is {:.2f}%".format(promoted))

# In[159]:
#plotting a scatter plot 
plt.hist(train['is_promoted'])
plt.title('plot to show the gap in Promoted and Non-Promoted Employees', fontsize = 30)
plt.xlabel('0 -No Promotion and 1- Promotion', fontsize = 20)
plt.ylabel('count')
plt.show()

# In[160]:
# scatter plot between average training score and is_promoted
data = pd.crosstab(train['avg_training_score'], train['is_promoted'])
data.div(data.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True, figsize = (20, 9), color = ['darkred', 'lightgreen'])
plt.title('Looking at the Dependency of Training Score in promotion', fontsize = 30)
plt.xlabel('Average Training Scores', fontsize = 15)
plt.legend()
plt.show()

# In[161]:
# checking dependency of different regions in promotion
data = pd.crosstab(train['region'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (20, 8), color = ['lightblue', 'purple'])
plt.title('Dependency of Regions in determining Promotion of Employees', fontsize = 30)
plt.xlabel('Different Regions of the Company', fontsize = 20)
plt.legend()
plt.show()

# In[162]:
# dependency of awards won on promotion
data = pd.crosstab(train['awards_won?'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (10, 8), color = ['magenta', 'purple'])
plt.title('Dependency of Awards in determining Promotion', fontsize = 30)
plt.xlabel('Awards Won or Not', fontsize = 20)
plt.legend()
plt.show()

# In[163]:
#dependency of KPIs with Promotion
data = pd.crosstab(train['KPIs_met >80%'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (10, 8), color = ['pink', 'darkred'])
plt.title('Dependency of KPIs in determining Promotion', fontsize = 30)
plt.xlabel('KPIs Met or Not', fontsize = 20)
plt.legend()
plt.show()

# In[164]:
# checking dependency on previous years' ratings
data = pd.crosstab(train['previous_year_rating'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (15, 8), color = ['violet', 'pink'])
plt.title('Dependency of Previous year Ratings in determining Promotion', fontsize = 30)
plt.xlabel('Different Ratings', fontsize = 20)
plt.legend()
plt.show()

# In[165]:
# checking how length of service determines the promotion of employees
data = pd.crosstab(train['length_of_service'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (20, 8), color = ['pink', 'lightblue'])
plt.title('Dependency of Length of service in Promotions of Employees', fontsize = 30)
plt.xlabel('Length of service of employees', fontsize = 20)
plt.legend()
plt.show()


# In[166]:
# checking dependency of age factor in promotion of employees
data = pd.crosstab(train['age'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (20, 8), color = ['lightblue', 'green'])
plt.title('Dependency of Age in determining Promotion of Employees', fontsize = 30)
plt.xlabel('Age of Employees', fontsize = 20)
plt.legend()
plt.show()

# In[167]:
# checking which department got most number of promotions
data = pd.crosstab(train['department'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (20, 8), color = ['orange', 'lightgreen'])
plt.title('Dependency of Departments in determining Promotion of Employees', fontsize = 30)
plt.xlabel('Different Departments of the Company', fontsize = 20)
plt.legend()
plt.show()

# In[168]:
# checking dependency of gender over promotion
data = pd.crosstab(train['gender'], train['is_promoted'])
data.div(data.sum(1).astype('float'), axis = 0).plot(kind = 'bar', stacked = True, figsize = (7, 5), color = ['pink', 'yellow'])
plt.title('Dependency of Genders in determining Promotion of Employees', fontsize = 30)
plt.xlabel('Gender', fontsize = 20)
plt.legend()

# In[31]:
# filling missing values
train['education'].fillna(train['education'].mode()[0], inplace = True)
train['previous_year_rating'].fillna(1, inplace = True)
# again checking if there is any Null value left in the data
train.isnull().sum().sum()

# In[32]:
# filling missing values
test['education'].fillna(test['education'].mode()[0], inplace = True)
test['previous_year_rating'].fillna(1, inplace = True)
# again checking if there is any Null value left in the data
test.isnull().sum().sum()

# In[33]:
# removing the employee_id column
train = train.drop(['employee_id'], axis = 1)
train.columns

# In[202]:
# saving the employee_id
emp_id = test['employee_id']
# removing the employee_id column
test = test.drop(['employee_id'], axis = 1)
test.columns

# In[203]:
# defining the test set
x_test = test
x_test.columns

# In[204]:
# one hot encoding for the test set
x_test = pd.get_dummies(x_test)
x_test.columns

# In[205]:
# splitting the train set into dependent and independent sets
x = train.iloc[:, :-1]
y = train.iloc[:, -1]
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

# In[206]:
# one hot encoding for the train set
x = pd.get_dummies(x)
x.columns

# In[208]:
from imblearn.over_sampling import SMOTE
x_sample, y_sample = SMOTE().fit_resample(x, y.values.ravel())
x_sample = pd.DataFrame(x_sample)
y_sample = pd.DataFrame(y_sample)
# checking the sizes of the sample data
print("Size of x-sample :", x_sample.shape)
print("Size of y-sample :", y_sample.shape)

# In[209]:
# splitting x and y into train and validation sets
from sklearn.model_selection import train_test_split
x_train, x_valid, y_train, y_valid = train_test_split(x_sample, y_sample, test_size = 0.2, random_state = 0)
print("Shape of x_train: ", x_train.shape)
print("Shape of x_valid: ", x_valid.shape)
print("Shape of y_train: ", y_train.shape)
print("Shape of y_valid: ", y_valid.shape)


# In[211]:
# standard scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test  = sc.transform(x_test)
x_valid = sc.transform(x_valid)

# In[213]:
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import average_precision_score
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
rfc_pred = rfc.predict(x_test)
print("Training Accuracy :", rfc.score(x_train, y_train))

# In[214]:
from xgboost.sklearn import XGBClassifier
xgb = XGBClassifier()
xgb.fit(x_train, y_train)
xgb_pred = xgb.predict(x_test)
print("Training Accuracy :", xgb.score(x_train, y_train))

# In[216]:
from lightgbm import LGBMClassifier
lgb = LGBMClassifier()
lgb.fit(x_train, y_train)
lgb_pred = lgb.predict(x_test)
print("Training Accuracy :", lgb.score(x_train, y_train))

# In[217]:
from sklearn.ensemble import ExtraTreesClassifier
etc = ExtraTreesClassifier()
etc.fit(x_train, y_train)
etc_pred = etc.predict(x_test)
print("Training Accuracy :", etc.score(x_train, y_train))
