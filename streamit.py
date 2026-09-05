import streamlit as st
import os

st.title("🏛️ Civilization Simulation Dashboard")

# Simulation controls in the sidebar
st.sidebar.header("Controls")
turn = st.sidebar.slider("Turn", 1, 50, 1)

# Main layout split into map and stats
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Isometric Map Grid")
    
    # 0 = Grass Tile, 1 = Stone Tile
    map_grid = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]
    
    # Render the grid using columns and your uploaded assets
    for row in map_grid:
        cols = st.columns(len(row))
        for i, tile_type in enumerate(row):
            with cols[i]:
                if tile_type == 1:
                    if os.path.exists("base_stone_flat_E.png"):
                        st.image("base_stone_flat_E.png", width=100)
                    else:
                        st.info("🏢 Stone Tile")
                else:
                    if os.path.exists("base_grass_high_detail_E.png"):
                        st.image("base_grass_high_detail_E.png", width=100)
                    else:
                        st.success("🟩 Grass Tile")

with col2:
    st.subheader("Stats")
    st.metric("Gold", "500", "+25")
    st.metric("Population", "1,200", "+12")
