import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB as gnb
from sklearn.metrics import accuracy_score
data = pd.read_csv('pima-indians-diabetes.csv')
print (data.describe())
features = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Age', 'Insulin', 'DiabetesPedigreeFunction']
target = 'Class'
train, test = train_test_split(data, test_size=0.2)
clf = gnb().fit(train[features], train[target]) 
y_predicted = clf.predict(test[features])
print ("Accuracy ",round(accuracy_score(test[target], y_predicted)*100,2)," %")

num=[]
for i in range(0,8):
	num.append(float(input("Enter User data to predict")))

a=num[0]
b=num[1]
c=num[2]
d=num[3]
e=num[4]
f=num[5]
g=num[6]
h=num[7]
newuser=pd.DataFrame([[a,b,c,d,e,f,g,h]]) 
result=clf.predict(newuser)

if (result==1):
	print("User may have Daibetes")
else:
	print("User Dont have Daibetes,")
