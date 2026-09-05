import streamlit as st
import os

# Set page layout to wide for a true game screen feel
st.set_page_config(page_title="Civilization World Builder", layout="wide")

# Custom game styling header
st.markdown("## 🛡️ EMPIRE BUILDER : VIRTUAL WORLD")

# Initialize game state memory
if "world_grid" not in st.session_state:
    st.session_state.world_grid = [
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0]
    ]
if "gold" not in st.session_state:
    st.session_state.gold = 1000
if "population" not in st.session_state:
    st.session_state.population = 250

# --- GAME HUD (SIDEBAR) ---
st.sidebar.markdown("### 🎮 Command Center")
turn = st.sidebar.slider("Game Turn / Year", 1, 100, 1)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏗️ Build Menu")
build_choice = st.sidebar.selectbox("Select Asset to Place:", ["Grass Tile (0)", "Stone Road/Building (1)"])
target_row = st.sidebar.selectbox("Map Row", [0, 1, 2, 3])
target_col = st.sidebar.selectbox("Map Column", [0, 1, 2, 3, 4, 5])

if st.sidebar.button("🔨 Place on Map"):
    new_val = 1 if "Stone" in build_choice else 0
    st.session_state.world_grid[target_row][target_col] = new_val
    st.session_state.gold -= 50  # Build cost
    st.session_state.population += 10
    st.rerun()

# --- MAIN GAME SCREEN ---
col_map, col_hud = st.columns([3, 1])

with col_map:
    st.markdown("#### 🗺️ Isometric World Map")
    
    # Render the map entirely out of your image assets
    for r_idx, row in enumerate(st.session_state.world_grid):
        cols = st.columns(len(row))
        for c_idx, tile_type in enumerate(row):
            with cols[c_idx]:
                if tile_type == 1:
                    if os.path.exists("base_stone_flat_E.png"):
                        st.image("base_stone_flat_E.png", width=85)
                    else:
                        st.write("🧱")
                else:
                    if os.path.exists("base_grass_high_detail_E.png"):
                        st.image("base_grass_high_detail_E.png", width=85)
                    else:
                        st.write("🟩")

with col_hud:
    st.markdown("#### 📊 Resource HUD")
    st.metric("💰 Gold", f"{st.session_state.gold}", "+45/turn")
    st.metric("👥 Population", f"{st.session_state.population}", "+10/turn")
    st.metric("🌾 Food", "480", "-5")
    
    st.markdown("---")
    st.info("💡 **Tip:** Use the sidebar build menu to place stone paths or buildings onto your isometric world map coordinates!")
