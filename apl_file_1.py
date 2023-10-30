import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:\\Users\\raks2\\Downloads\\iphone_purchase_records.csv")
print(df)

print(df.describe())


males_above_25_df = df.loc[(df["Gender"] == "Male") & (df["Age"]>25) & (df["Purchase Iphone"]== 1)]
print(males_above_25_df)
fig_001 = px.bar(x=males_above_25_df.Age, y =males_above_25_df.Salary, title="Males above the age of 25", labels = {"Age": "Age", "Salary": "Salary"})
fig_001.update_layout(xaxis_title="Age", yaxis_title = "Salary")
fig_001.show()




female_above_30k_df = df.loc[(df["Gender"] == "Female") & (df["Salary"] > 30000) & (df["Purchase Iphone"]== 1)]
print(female_above_30k_df)
fig_002 = px.scatter(data_frame=female_above_30k_df, x= "Age", y="Salary", title="Females above the salary of 30k", size="Salary", labels = {"Age": "Age", "Salary": "Salary"})
fig_002.update_layout(xaxis_title="Age", yaxis_title="Salary")
fig_002.show()



salary_desc_df = df.sort_values(by = ["Salary"], ascending= False)
male_buyer_salAbove_50k_df = df.loc[(df["Salary"]>=50000) & (df["Purchase Iphone"] == 1) & (df["Gender"] == "Male")]
female_buyer_salAbove_50k_df = df.loc[(df["Salary"]>=50000) & (df["Purchase Iphone"] == 1) & (df["Gender"] == "Female")]
fig_003 = go.Figure(go.Scatter(x = male_buyer_salAbove_50k_df.Age, y=male_buyer_salAbove_50k_df.Salary, name = "Male", mode = 'lines'))
fig_003.add_trace(go.Scatter( x = female_buyer_salAbove_50k_df.Age, y=female_buyer_salAbove_50k_df.Salary, name = "Female", mode = 'lines'))
fig_003.update_layout(title="Buyers above 50k Salary",xaxis_title = "Age of Buyers", yaxis_title = "Salary of Buyers")
fig_003.show()
#print(buyer_salAbove_50k_df)




malebuyer_below30 = df.loc[(df["Age"]<=30) & (df["Purchase Iphone"] == 1) &(df["Gender"] == "Male")]
femalebuyer_below30 = df.loc[(df["Age"]<=30) & (df["Purchase Iphone"] == 1) & (df["Gender"] == "Female")]
fig_004 = go.Figure(go.Scatter(x = malebuyer_below30.Age, y = malebuyer_below30.Salary, mode = "markers", name="Male",showlegend=True, marker_size = [20,30,40,50]))
fig_004.add_trace(go.Scatter(x = femalebuyer_below30.Age, y = femalebuyer_below30.Salary, mode = "markers", name="Female", marker_size = [20,30]))
fig_004.update_layout(title = "Buyers below the age of 30", xaxis_title = "Age", yaxis_title = "Salary")
fig_004.show()

#print(buyer_below30)












