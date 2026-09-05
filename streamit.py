import streamlit as st
import os

st.set_page_config(page_title="SIM-EMPIRE 2000", layout="wide")

# --- RETRO GAME CSS STYLING ---
st.markdown("""
    <style>
    .stApp {
        background-color: #080a0f;
        color: #00ffcc;
    }
    /* Restyle Streamlit buttons to look like retro game grid tiles */
    .stButton>button {
        background-color: #161b22;
        color: #00ffcc;
        border: 1px solid #30363d;
        border-radius: 4px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 11px;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #21262d;
        border-color: #00ffcc;
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("## 🌆 SIM-EMPIRE 2000 // 2.5D STRATEGY MAP")

# Initialize world map
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

# Sidebar controls
st.sidebar.markdown("### 🕹️ MAYOR COMMANDS")
game_year = st.sidebar.slider("Game Year", 2026, 2100, 2026)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🏗️ BUILD TOOL")
active_tool = st.sidebar.radio(
    "Select Zone:",
    ["🟩 Grass / Clear Land", "🧱 Stone Road"]
)
tool_id = 1 if "Stone" in active_tool else 0

st.sidebar.markdown("---")
st.sidebar.info("🎮 **Tip:** Click any grid button under the map tiles to build instantly!")

# Main game layout
col_map, col_stats = st.columns([3, 1])

with col_map:
    st.markdown("#### 🗺️ Isometric World Sector")
    
    for r_idx, row in enumerate(st.session_state.world_map):
        cols = st.columns(len(row))
        for c_idx, tile_val in enumerate(row):
            with cols[c_idx]:
                # Render the isometric tile graphic
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
                
                # The sleek retro grid button
                if st.button("BUILD", key=f"btn_{r_idx}_{c_idx}"):
                    st.session_state.world_map[r_idx][c_idx] = tool_id
                    st.session_state.treasury -= 25
                    st.session_state.citizens += 15
                    st.rerun()

with col_stats:
    st.markdown("#### 📊 CITY HUD")
    st.metric("💰 Treasury", f"${st.session_state.treasury}", "+$120/mo")
    st.metric("👥 Population", f"{st.session_state.citizens}", "+15")
    st.metric("⚡ Power", "85%", "Stable")
    
    st.markdown("---")
    if st.button("🚀 Advance Turn"):
        st.session_state.treasury += 250
        st.success("Taxes collected!")
        st.rerun()
