import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("arquivo.csv")
st.dataframe(df)
fig,ax=plt.subplots()
ax.bar(df["Country"],df["Financial allocations($ billion)"])
st.pyplot(fig)
