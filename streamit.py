import streamlit as st

# Set up the page layout
st.title("🏛️ Civilization Simulation Dashboard")
st.write("Welcome to your hackathon project frontend!")

# Create a sidebar for game controls
st.sidebar.header("Simulation Controls")
turn_number = st.sidebar.slider("Current Turn", 1, 100, 1)
run_simulation = st.sidebar.button("Process Turn")

if run_simulation:
    st.sidebar.success(f"Processing turn {turn_number}...")

# Main dashboard area split into columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Map Grid")
    # Placeholder grid layout for your Kenney isometric tiles
    # In your actual project, you'll loop through your map matrix here
    grid_cols = st.columns(3)
    for col in grid_cols:
        with col:
            # You can replace this with st.image() for your tiles
            st.info("Tile [Iso Asset]")

with col2:
    st.subheader("Resource Metrics")
    st.metric(label="Gold", value="500", delta="+25")
    st.metric(label="Population", value="1,200", delta="+12")
    st.metric(label="Food Supplies", value="340", delta="-5")
