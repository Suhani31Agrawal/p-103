import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.line(df,x="cases",y="country",color="date",title="CASES IN EACH COUNTRY")
fig.show()