import streamlit as st
import matplotlib.pyplot as plt

# Function to create a simple globe icon
def create_globe_icon():
    fig, ax = plt.subplots(figsize=(0.25, 0.25), dpi=100)  # Adjust the figsize to make the globe smaller
    ax.set_aspect('equal')
    ax.set_axis_off()

    # Draw the globe (circle)
    circle = plt.Circle((0.5, 0.5), 0.4, color='deepskyblue', ec='black', lw=1)
    ax.add_patch(circle)

    # Draw simple continents
    continents = [[[0.35, 0.65], [0.5, 0.6], [0.55, 0.7], [0.4, 0.8],
                   [0.3, 0.75]],
                  [[0.7, 0.4], [0.75, 0.45], [0.8, 0.35], [0.85, 0.4],
                   [0.8, 0.45], [0.75, 0.4]]]

    for continent in continents:
        poly = plt.Polygon(continent, closed=True, color='green', ec='black')
        ax.add_patch(poly)

    return fig

# Display the globe icon
st.pyplot(create_globe_icon())

# Add custom CSS to center the entire block
st.write(
    """
    <style>
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }
    .stRadio > div {
        display: flex;
        flex-direction: row;
        justify-content: center;
    }
    .stRadio label {
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center the entire "Navigation" section
st.markdown('<div class="center-container">', unsafe_allow_html=True)
option = st.radio(
    "Choose one:",
    ('World', 'Galaxy', 'Universe'))
st.markdown(f'You selected {option}.', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
