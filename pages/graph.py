
import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import plotly.express as px

def app():
    st.title('Data as graph')

    st.write("This is the `Data graph` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    Y = pd.Series(iris.target, name='class')
    df = pd.concat([X, Y], axis=1)
    df['class'] = df['class'].map({0: "setosa", 1: "versicolor", 2: "virginica"})

    st.write(df)

    # Plotting the graph
    fig = px.scatter(df, x='sepal length (cm)', y='sepal width (cm)', color='class',
                     color_discrete_map={'setosa': 'blue', 'versicolor': 'violet', 'virginica': 'black'})
    
    # Customizing layout
    fig.update_layout(title="Sepal Length vs Sepal Width",
                      xaxis_title="Sepal Length (cm)",
                      yaxis_title="Sepal Width (cm)")
    
    st.plotly_chart(fig)


    # Plotting the graph
    fig = px.scatter(df, x='petal length (cm)', y='petal width (cm)', color='class',
                     color_discrete_map={'setosa': 'blue', 'versicolor': 'green', 'virginica': 'red'})
    
    # Customizing layout
    fig.update_layout(title="Petal Length vs Petal Width",
                      xaxis_title="Petal Length (cm)",
                      yaxis_title="Petal Width (cm)")
    
    st.plotly_chart(fig)


app()





