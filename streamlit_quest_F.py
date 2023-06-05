import streamlit as st
import pandas as pd
import seaborn as sns
import pydeck as pdk

cars = pd.read_csv(r"C:\Users\geoff\Desktop\Wild_Code_School\test_streamlit\file_cars.csv")

df_usa = cars[cars["continent"] == " US."]
df_europe = cars[cars["continent"] == " Europe."]
df_japan = cars[cars["continent"] == " Japan."]


st.title(":red[_Analyse de corrélation_]")
st.write("")

button_1, button_2, button_3 = st.columns(3)

usa_button = button_1.button("USA")
europe_button = button_2.button("Europe")
japan_button = button_3.button("Japan")

if usa_button:

	viz_line1 = sns.lineplot(data = df_usa, x="hp", y="time_to_60")
	st.pyplot(viz_line1.figure) 

	viz_correlation1 = sns.heatmap(df_usa.corr(), 
								center = 0,
								cmap = "vlag"
								)
	st.pyplot(viz_correlation1.figure)


if europe_button:

	viz_line2 = sns.lineplot(data = df_europe, x="hp", y="time_to_60")
	st.pyplot(viz_line2.figure)

	viz_correlation2 = sns.heatmap(df_europe.corr(), 
								center = 0,
								cmap = "vlag"
								)
	st.pyplot(viz_correlation2.figure)


if japan_button:

	viz_line3 = sns.lineplot(data = df_japan, x="hp", y="time_to_60")
	st.pyplot(viz_line3.figure)
	
	viz_correlation3 = sns.heatmap(df_japan.corr(), 
								center = 0,
								cmap = "vlag"
								)
	st.pyplot(viz_correlation3.figure)