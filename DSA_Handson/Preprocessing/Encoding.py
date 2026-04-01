



'''from sklearn.preprocessing import LabelEncoder
import pandas as pd
data=pd.DataFrame({
    'Gender':['Male','Male','Female'],
    'City':['New York','Paris','Tokyo']
})
le=LabelEncoder()
data['Gender']=le.fit_transform(data['Gender'])
print(data)
one_hot=pd.get_dummies(data['City'])
print(one_hot)'''