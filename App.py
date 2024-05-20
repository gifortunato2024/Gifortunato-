import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("arquivo.csv")

grafico = plt.plot(df["Country"], df["Financial allocations($ billion)"])
st.pyplot(grafico)
