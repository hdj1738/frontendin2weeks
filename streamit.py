import streamlit as st
import os

st.title("🏛️ City Civilization Simulation")

# 1. Initialize a base world map grid in session memory (0 = Grass, 1 = Stone/Road)
if "city_grid" not in st.session_state:
    st.session_state.city_grid = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

# Sidebar tool selection
st.sidebar.header("City Controls")
turn = st.sidebar.slider("Simulation Year / Turn", 1, 100, 1)

st.sidebar.subheader("Build Tool")
selected_tool = st.sidebar.radio("Select Tile to Paint:", ["Grass (0)", "Stone Road (1)"])
paint_val = 1 if "Stone" in selected_tool else 0

# Main Layout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Interactive Base World Map")
    st.write("Click any tile below to build/change it instantly:")
    
    # 2. Render the grid using actual clickable buttons with images on them
    for r_idx, row in enumerate(st.session_state.city_grid):
        cols = st.columns(len(row))
        for c_idx, tile_val in enumerate(row):
            with cols[c_idx]:
                # Choose icon or label based on tile value
                label = "🧱 Road" if tile_val == 1 else "🟩 Grass"
                
                # When a map tile button is clicked, update that specific coordinate!
                if st.button(label, key=f"tile_{r_idx}_{c_idx}"):
                    st.session_state.city_grid[r_idx][c_idx] = paint_val
                    st.rerun()

with col2:
    st.subheader("City Stats")
    st.metric("Population", f"{1200 + (turn * 45)}", f"+{45} this turn")
    st.metric("Treasury", "12,400 Gold", "+320")
