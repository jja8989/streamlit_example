import streamlit as st
import plotly.express as px
import pandas as pd



def main():
    # Load data
    st.title("Apple Stock Prices")

    st.code("""
    # load data
    data_url = "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
    df = pd.read_csv(data_url)

    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Create time series plot
    fig = px.line(df, x='Date', y='AAPL.High', title='Apple Stock Prices')
    st.plotly_chart(fig, use_container_width=True)
    """)
    data_url = "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv"
    df = pd.read_csv(data_url)

    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    
    # Create time series plot
    fig = px.line(df, x='Date', y='AAPL.High', title='Apple Stock Prices')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")


    st.title("Selectbox and Slider")

    st.code("""
    #load data
    data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    # Create a multiselect widget for selecting columns
    x_var = st.selectbox('Select X variable', ['pop', 'lifeExp', 'gdpPercap'])
    y_var = st.selectbox('Select Y variable', ['pop', 'lifeExp', 'gdpPercap'])

    # Create slider for filtering data based on year
    year = st.slider('Select year', int(data['year'].min()), int(data['year'].max()), step=5)

    # Filter data based on year
    data_filtered = data[data['year'] == year]

    # Create scatter plot using Plotly
    fig = px.scatter(data_filtered, x=x_var, y=y_var, color='continent', hover_name='country',
                    size='pop', log_x=True, log_y=True)
    
    fig.update_layout(xaxis=dict(dtick=1))

    # Display plot
    st.plotly_chart(fig, use_container_width=True)
    """)

   
    # Load data
    data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

    # Create a multiselect widget for selecting columns
    x_var = st.selectbox('Select X variable', ['pop', 'lifeExp', 'gdpPercap'])
    y_var = st.selectbox('Select Y variable', ['pop', 'lifeExp', 'gdpPercap'])

    # Create slider for filtering data based on year
    year = st.slider('Select year', int(data['year'].min()), int(data['year'].max()), step=5)

    # Filter data based on year
    data_filtered = data[data['year'] == year]

    # Create scatter plot using Plotly
    fig = px.scatter(data_filtered, x=x_var, y=y_var, color='continent', hover_name='country',
                    size='pop', log_x=True, log_y=True)
    
    fig.update_layout(xaxis=dict(dtick=1), yaxis=dict(dtick=1))

    # Display plot
    st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    main()