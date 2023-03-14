import streamlit as st
import plotly.express as px
import pandas as pd



def main():
    st.title("Animation")

    st.code("""
     
    # load data
    gapminder = px.data.gapminder()

    # Set default values for slider bar
    year_start = 1952
    year_end = 2007
    year_step = 5

    # Sidebar layout
    st.sidebar.markdown("## Gapminder Data")
    year_range = st.sidebar.slider("Select Year Range", 1952, 2007, (year_start, year_end), year_step)
    continent = st.sidebar.multiselect("Select Continent", gapminder['continent'].unique())

    # Filter data based on user selection
    gapminder_filtered = gapminder[(gapminder['year'] >= year_range[0]) & (gapminder['year'] <= year_range[1])]
    if continent:
        gapminder_filtered = gapminder_filtered[gapminder_filtered['continent'].isin(continent)]

    # Main app layout
    st.write("Showing data from", year_range[0], "to", year_range[1])

    # Plot data using Plotly Express
    fig = px.scatter(gapminder_filtered, x='gdpPercap', y='lifeExp', color='continent', size='pop', hover_name='country', animation_frame='year', range_x=[0, 60000], range_y=[20, 90])
    fig.update_layout(title='GDP per capita vs. Life expectancy', xaxis_title='GDP per capita', yaxis_title='Life expectancy')
    st.plotly_chart(fig)
    """)
        
    # Load Gapminder dataset
    gapminder = px.data.gapminder()

    # Set default values for slider bar
    year_start = 1952
    year_end = 2007
    year_step = 5

    # Sidebar layout
    st.sidebar.markdown("## Gapminder Data")
    year_range = st.sidebar.slider("Select Year Range", 1952, 2007, (year_start, year_end), year_step)
    continent = st.sidebar.multiselect("Select Continent", gapminder['continent'].unique())

    # Filter data based on user selection
    gapminder_filtered = gapminder[(gapminder['year'] >= year_range[0]) & (gapminder['year'] <= year_range[1])]
    if continent:
        gapminder_filtered = gapminder_filtered[gapminder_filtered['continent'].isin(continent)]

    # Main app layout
    st.write("Showing data from", year_range[0], "to", year_range[1])

    # Plot data using Plotly Express
    fig = px.scatter(gapminder_filtered, x='gdpPercap', y='lifeExp', color='continent', size='pop', hover_name='country', animation_frame='year', range_x=[0, 60000], range_y=[20, 90])
    fig.update_layout(title='GDP per capita vs. Life expectancy', xaxis_title='GDP per capita', yaxis_title='Life expectancy')
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()