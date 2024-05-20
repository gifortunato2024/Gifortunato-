import streamlit as st 
import pandas as pd 
import seaborn as sns 

df = pd.read_csv("arquivo.csv")

grafico = sns.barplot(data=df, x="Country", y="Financial allocations($ billion)")
st.write(grafico)
