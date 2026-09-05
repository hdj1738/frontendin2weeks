import streamlit as st
import os

st.title("🏛️ City Civilization Simulation")

# Initialize the city grid in memory so it can change
if "city_grid" not in st.session_state:
    st.session_state.city_grid = [
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]

# Sidebar controls for building
st.sidebar.header("City Controls")
turn = st.sidebar.slider("Simulation Year / Turn", 1, 100, 1)

st.sidebar.subheader("Construction Tool")
r_choice = st.sidebar.selectbox("Row (0 to 4)", [0, 1, 2, 3, 4])
c_choice = st.sidebar.selectbox("Column (0 to 4)", [0, 1, 2, 3, 4])
tile_type = st.sidebar.selectbox("Select Tile", ["Grass (0)", "Stone Road (1)"])

if st.sidebar.button("Build / Change Tile"):
    val = 1 if "Stone" in tile_type else 0
    # Update the grid in memory!
    st.session_state.city_grid[r_choice][c_choice] = val
    st.sidebar.success(f"Updated Row {r_choice}, Col {c_choice}!")

# Main Layout
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("City Map View")
    
    # Render the interactive grid from session memory
    for row in st.session_state.city_grid:
        cols = st.columns(len(row))
        for i, tile in enumerate(row):
            with cols[i]:
                if tile == 1:
                    if os.path.exists("base_stone_flat_E.png"):
                        st.image("base_stone_flat_E.png", width=60)
                    else:
                        st.write("🧱")
                else:
                    if os.path.exists("base_grass_high_detail_E.png"):
                        st.image("base_grass_high_detail_E.png", width=60)
                    else:
                        st.write("🟩")

with col2:
    st.subheader("City Stats")
    st.metric("Population", f"{1200 + (turn * 45)}", f"+{45} this turn")
    st.metric("Treasury", "12,400 Gold", "+320")
