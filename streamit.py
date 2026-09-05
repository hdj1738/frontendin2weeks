import streamlit as st
import os

st.title("🏛️ City Civilization Simulation")

# Sidebar controls
st.sidebar.header("City Controls")
turn = st.sidebar.slider("Simulation Year / Turn", 1, 100, 1)
action = st.sidebar.selectbox("Zone Tool", ["Build Road", "Build House", "Build Farm"])

if st.sidebar.button("Simulate Turn"):
    st.sidebar.success(f"Year {turn} processed! City is growing.")

# Main Layout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("City Map View")
    
    # Expanded 5x5 City Grid Matrix (0=Grass, 1=Stone/Road, 2=Building)
    city_grid = [
        [0, 0, 1, 0, 0],
        [0, 2, 1, 2, 0],
        [1, 1, 1, 1, 1],
        [0, 2, 1, 2, 0],
        [0, 0, 1, 0, 0]
    ]
    
    # Render the larger city grid
    for row in city_grid:
        cols = st.columns(len(row))
        for i, tile in enumerate(row):
            with cols[i]:
                if tile == 1:
                    if os.path.exists("base_stone_flat_E.png"):
                        st.image("base_stone_flat_E.png", width=70)
                    else:
                        st.write("🧱")
                else:
                    if os.path.exists("base_grass_high_detail_E.png"):
                        st.image("base_grass_high_detail_E.png", width=70)
                    else:
                        st.write("🟩")

with col2:
    st.subheader("City Stats")
    st.metric("Population", f"{1200 + (turn * 45)}", f"+{45} this turn")
    st.metric("Treasury", "12,400 Gold", "+320")
    st.metric("Food Supply", "850 units", "-12")
