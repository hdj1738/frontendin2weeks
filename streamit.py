import streamlit as st
import os

# Set page layout for a wide retro game screen
st.set_page_config(page_title="Retro City 2000 - 2.5D", layout="wide")

# Retro Game Styling (Dark tactical HUD theme)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    .game-title {
        font-family: 'Courier New', Courier, monospace;
        color: #00ffcc;
        text-shadow: 2px 2px #ff00ff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='game-title'>🌆 SIM-EMPIRE 2000 // 2.5D STRATEGY</h1>", unsafe_allow_html=True)

# Initialize the world grid in game memory (0 = Grass, 1 = Stone Road/Building)
if "world_map" not in st.session_state:
    st.session_state.world_map = [
        [0, 0, 1, 1, 0, 0],
        [0, 1, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0]
    ]

if "treasury" not in st.session_state:
    st.session_state.treasury = 5000
if "citizens" not in st.session_state:
    st.session_state.citizens = 320

# --- GAME CONTROLS HUD (SIDEBAR) ---
st.sidebar.markdown("### 🕹️ MAYOR COMMANDS")
game_year = st.sidebar.slider("Game Year", 2026, 2100, 2026)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏗️ CONSTRUCTION TOOL")
# Pick what you want to build with your mouse
active_tool = st.sidebar.radio(
    "Select Zone/Building:",
    ["🟩 Clear Land (Grass)", "🧱 Stone Road / Base"]
)
tool_id = 1 if "Stone" in active_tool else 0

st.sidebar.markdown("---")
st.sidebar.info("💡 **How to play:** Select your tool above, then click any tile button directly on the map grid to build instantly!")

# --- MAIN GAME VIEW (2.5D ISOMETRIC GRID) ---
col_map, col_stats = st.columns([3, 1])

with col_map:
    st.markdown("#### 🗺️ Isometric Sector Alpha")
    
    # Render the map as an interactive grid of tiles and build buttons
    for r_idx, row in enumerate(st.session_state.world_map):
        cols = st.columns(len(row))
        for c_idx, tile_val in enumerate(row):
            with cols[c_idx]:
                # 1. Display the visual isometric asset graphic
                if tile_val == 1:
                    if os.path.exists("base_stone_flat_E.png"):
                        st.image("base_stone_flat_E.png", width=75)
                    else:
                        st.markdown("🧱")
                else:
                    if os.path.exists("base_grass_high_detail_E.png"):
                        st.image("base_grass_high_detail_E.png", width=75)
                    else:
                        st.markdown("🟩")
                
                # 2. Direct click-to-build button right underneath each tile
                if st.button("Build here", key=f"btn_{r_idx}_{c_idx}"):
                    st.session_state.world_map[r_idx][c_idx] = tool_id
                    st.session_state.treasury -= 25 # Construction cost
                    st.session_state.citizens += 15
                    st.rerun()

with col_stats:
    st.markdown("#### 📊 CITY METRICS")
    st.metric("💰 Treasury", f"${st.session_state.treasury}", "+$120/mo")
    st.metric("👥 Population", f"{st.session_state.citizens}", "+15")
    st.metric("⚡ Power Grid", "85%", "Stable")
    st.metric("💧 Water Supply", "92%", "Optimal")
    
    st.markdown("---")
    if st.button("🚀 Advance Month"):
        st.session_state.treasury += 250
        st.success("Month processed! Taxes collected.")
        st.rerun()
