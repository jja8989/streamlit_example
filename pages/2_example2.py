import streamlit as st
import streamlit as st
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

def main():
    st.title("Plotly plots")

    st.header("3D scatter plot")

    st.code("""
     # Create 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=[1, 2, 3, 4, 5],
        y=[5, 4, 3, 2, 1],
        z=[1, 2, 3, 4, 5],
        mode='markers',
        marker=dict(
            size=12,
            color=[0, 1, 2, 3, 4],
            colorscale='Viridis',
            opacity=0.8
        )
    )])
    
    # Add layout
    fig.update_layout(scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis')
    ), margin=dict(l=10, r=10, b=10, t=10))
    
    st.plotly_chart(fig, use_container_width=True)
    """)
    # Create 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=[1, 2, 3, 4, 5],
        y=[5, 4, 3, 2, 1],
        z=[1, 2, 3, 4, 5],
        mode='markers',
        marker=dict(
            size=12,
            color=[0, 1, 2, 3, 4],
            colorscale='Viridis',
            opacity=0.8
        )
    )])
    
    # Add layout
    fig.update_layout(scene=dict(
        xaxis=dict(title='X-axis'),
        yaxis=dict(title='Y-axis'),
        zaxis=dict(title='Z-axis')
    ), margin=dict(l=10, r=10, b=10, t=10))
    
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")


    st.header("Sankey diagram")
    
    st.code("""
    #
    data = dict(
        type='sankey',
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["A1", "A2", "B1", "B2", "C1", "C2"],
        color = ["blue", "blue", "blue", "blue", "blue", "blue"]
    ),
    link = dict(
        source = [0, 0, 1, 1, 2, 2],
        target = [2, 3, 4, 5, 4, 5],
        value = [8, 4, 2, 2, 4, 2]
    ))

    # Create plot
    fig = go.Figure(data=[data])

    # Show plot
    st.plotly_chart(fig)
    """)

    data = dict(
        type='sankey',
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["A1", "A2", "B1", "B2", "C1", "C2"],
        color = ["blue", "blue", "blue", "blue", "blue", "blue"]
        ),
        link = dict(
        source = [0, 0, 1, 1, 2, 2],
        target = [2, 3, 4, 5, 4, 5],
        value = [8, 4, 2, 2, 4, 2]
    ))

    # Create plot
    fig = go.Figure(data=[data])

    # Show plot
    st.plotly_chart(fig)

    st.markdown("---")


    st.header("Radar chart")

    st.code("""
    #
    df = pd.DataFrame(dict(
    r=[10, 20, 30, 40, 50],
    theta=['a', 'b', 'c', 'd', 'e']
    ))

    # Create plot
    fig = go.Figure(
        go.Scatterpolar(
            r=df['r'],
            theta=df['theta'],
            fill='toself'
        )
    )

    # Show plot
    st.plotly_chart(fig)
    """)

    df = pd.DataFrame(dict(
    r=[10, 20, 30, 40, 50],
    theta=['a', 'b', 'c', 'd', 'e']
    ))

    # Create plot
    fig = go.Figure(
        go.Scatterpolar(
            r=df['r'],
            theta=df['theta'],
            fill='toself'
        )
    )

    # Show plot
    st.plotly_chart(fig)
    
    st.markdown("---")


    st.header("Treemap and Bubble chart")

    st.code("""
    #
    st.plotly_chart(fig)

    df = px.data.gapminder().query("year == 2007")

    # Create plot
    fig = px.treemap(df, path=['continent', 'country'], values='pop',
                    color='gdpPercap', hover_data=['lifeExp', 'gdpPercap'],
                    color_continuous_scale='RdBu')

    # Show plot
    st.plotly_chart(fig)

    df = px.data.gapminder()

    # Create plot
    fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
                    hover_name='country', log_x=True, size_max=60)
    fig.update_layout(xaxis=dict(dtick=1))

    # Show plot
    st.plotly_chart(fig)

    """)

    df = px.data.gapminder().query("year == 2007")

    # Create plot
    fig = px.treemap(df, path=['continent', 'country'], values='pop',
                    color='gdpPercap', hover_data=['lifeExp', 'gdpPercap'],
                    color_continuous_scale='RdBu')

    # Show plot
    st.plotly_chart(fig)

    df = px.data.gapminder()

    # Create plot
    fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='continent',
                    hover_name='country', log_x=True, size_max=60)
    fig.update_layout(xaxis=dict(dtick=1))

    # Show plot
    st.plotly_chart(fig)



if __name__ == '__main__':
    main()