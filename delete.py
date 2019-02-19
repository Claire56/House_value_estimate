import pandas as pd

df = pd.read_csv("pop_cities.csv")
df = df.drop(['Unnamed: 0', 'Unnamed: 0.1','zip_code'],axis =1 )

def column_names():
    
    cols = df.columns.tolist() #make list 
    return cols

def x_features():

    return df.drop('sale_price', axis =1 ).columns


print(column_names())    
print(x_features())

print(type(column_names())) 


# col_names = column_names()
# for name in col_names[0:10]:
#     name = db.Column(db.Integer, nullable=True)

