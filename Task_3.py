#importing library
import pandas as pd
import numpy as np

#importing data
data=pd.read_csv('CarPrice_Assignment.csv')

# Split the "CarName" column by space and take the first part (company name)
data['CompanyName'] = data['CarName'].str.split(' ', 1).str[0]

# Drop the original "CarName" column if you don't need it anymore
data = data.drop(columns=['CarName'])
print(data)

from sklearn.preprocessing import OrdinalEncoder
categorical_columns = ['CompanyName','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem'
] 

encoder = OrdinalEncoder()
data[categorical_columns] = encoder.fit_transform(data[categorical_columns])


x=data[['symboling','CompanyName','fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','wheelbase','carlength','carwidth','carheight','curbweight','enginetype','cylindernumber','enginesize','fuelsystem','boreratio','stroke','compressionratio','horsepower','peakrpm','citympg','highwaympg']]
y=data['price']

print(data)

#test train split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.10)

from sklearn.tree import DecisionTreeRegressor
#from sklearn.tree import RandomForestRegressor
a=[]
for i in range(100,10000,100):
    lr = DecisionTreeRegressor(max_leaf_nodes=int(i))
    #rf = RandomForestRegressor()

    #training the model
    lr.fit(X_train,y_train)
    #running the model
    y_test_1=lr.predict(X_test)

    #Evaluating the model
    from sklearn.metrics import mean_absolute_error
    a.append(mean_absolute_error(y_test,y_test_1))

min_index=a.index(min(a))

mln = 100+(min_index)*100
mln

print("Mean Absolute Error ",min(a))

finalmodel = DecisionTreeRegressor(max_leaf_nodes=mln)
finalmodel.fit(x,y)


df2 = pd.DataFrame({'symboling':[3],'CompanyName':[2],'fueltype':[1],'aspiration':[1],'doornumber':[2],'carbody':[1],'drivewheel':[1],'enginelocation':[1],'wheelbase':[100],'carlength':[200],'carwidth':[70],'carheight':[50],'curbweight':[2500],'enginetype':[0],'cylindernumber':[3],'enginesize':[150],'fuelsystem':[5],'boreratio':[3],'stroke':[3],'compressionratio':[9],'horsepower':[150],'peakrpm':[5000],'citympg':[30],'highwaympg':[35]})


predicted_sales = finalmodel.predict(df2)
print("Predicted Sales :", predicted_sales)
