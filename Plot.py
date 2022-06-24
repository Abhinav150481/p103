import plotly.express as px
df=pd.read_cvs("covid.csv")

fig = px.line(df,x='date',y='cases',color= 'country')
fig.show()