import streamlit as st

# Page configuration
st.set_page_config(
    page_title="UAV Technology - Precision Agriculture",
    page_icon="🚁",
    layout="wide"
)

# Main content
st.title("UAV Technology in Agriculture")
st.subheader("How Drones are Revolutionizing Sugarcane Farming")

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ## What are UAVs?
    
    Unmanned Aerial Vehicles (UAVs), commonly known as drones, are aircraft that operate without a human pilot on board. 
    They can be remotely controlled or fly autonomously through software-controlled flight plans.
    
    ### Types of UAVs Used in Agriculture:
    
    1. **Multirotor Drones**: Easy to maneuver but with limited flight time and coverage
       - Quadcopters (4 rotors)
       - Hexacopters (6 rotors)
       - Octocopters (8 rotors)
    
    2. **Fixed-Wing Drones**: Longer flight time and greater coverage but require takeoff and landing space
    
    3. **Hybrid VTOL (Vertical Take-Off and Landing)**: Combine benefits of multirotors and fixed-wing drones
    
    ## UAV Applications in Sugarcane Farming
    
    UAVs equipped with various sensors can perform multiple tasks:
    
    ### Monitoring & Assessment
    - **Crop Health Monitoring**: Identify stress, disease, and pest problems
    - **Growth Tracking**: Monitor plant height, density, and development over time
    - **Yield Estimation**: Predict harvest amounts before the harvesting season
    - **Water Management**: Detect irrigation issues and water stress
    
    ### Analysis & Planning
    - **Variable Rate Application Maps**: Create prescription maps for fertilizers and pesticides
    - **Harvest Planning**: Optimize harvest timing and logistics
    - **Drainage Analysis**: Identify areas with water drainage issues
    """)

with col2:
    st.image("https://images.unsplash.com/photo-1473968512647-3e447244af8f?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
             caption="Agricultural drone surveying crops",
             use_container_width=True)
    
    # Add simplified UAV diagram using Streamlit components
    st.markdown("### Basic Components of an Agricultural UAV")
    
    components = {
        "Flight Controller": "The 'brain' of the UAV that controls flight operations",
        "GPS Module": "Provides positioning and enables autonomous flight paths",
        "Sensors": "Various cameras and sensors for data collection",
        "Battery": "Power source that determines flight time",
        "Propulsion System": "Motors and propellers that allow flight",
        "Communication System": "Links the UAV to the ground control station",
        "Payload": "Specialized equipment for agricultural data collection"
    }
    
    for component, description in components.items():
        with st.expander(component):
            st.write(description)

# Additional content - full width
st.markdown("""
## UAV Data Collection Process

The typical workflow for using UAVs in sugarcane farming includes:

1. **Mission Planning**: Define the area to survey and flight parameters
2. **Flight Execution**: Deploy the UAV to automatically follow the planned route
3. **Data Collection**: Capture imagery and sensor data during flight
4. **Data Processing**: Convert raw data into usable information through specialized software
5. **Analysis**: Interpret the processed data to make agricultural decisions
6. **Implementation**: Apply findings to optimize farming practices

## Key Advantages for Sugarcane Farmers

- **Efficiency**: Survey large areas quickly (up to 1,000 acres per day)
- **Accessibility**: Reach areas difficult to access by ground vehicles
- **Timeliness**: Collect data when needed, regardless of field conditions
- **High Resolution**: Capture detailed information not visible to the naked eye
- **Cost-Effective**: Reduce labor costs and time for field scouting
- **Non-Invasive**: Monitor crops without physically entering and potentially damaging fields
""")

# UAV benefits visualization
st.subheader("Benefits of UAVs in Sugarcane Farming")

benefits_data = {
    "Traditional Methods": [7, 5, 3, 4, 6],
    "UAV-Enhanced": [9, 8, 9, 9, 8]
}

categories = ["Field Coverage", "Data Resolution", "Cost Efficiency", "Time Savings", "Problem Detection"]

# Create a radar chart using Plotly
import plotly.graph_objects as go
import numpy as np

fig = go.Figure()

# Add traditional methods
fig.add_trace(go.Scatterpolar(
    r=benefits_data["Traditional Methods"],
    theta=categories,
    fill='toself',
    name='Traditional Methods',
    line_color='rgba(184, 134, 11, 0.8)',
    fillcolor='rgba(184, 134, 11, 0.2)'
))

# Add UAV-enhanced methods
fig.add_trace(go.Scatterpolar(
    r=benefits_data["UAV-Enhanced"],
    theta=categories,
    fill='toself',
    name='UAV-Enhanced',
    line_color='rgba(76, 175, 80, 0.8)',
    fillcolor='rgba(76, 175, 80, 0.2)'
))

# Update layout
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10]
        )
    ),
    showlegend=True,
    title="Comparison: Traditional vs. UAV-Enhanced Farming"
)

st.plotly_chart(fig, use_container_width=True)

# Regulatory considerations
with st.expander("Regulatory Considerations for Agricultural UAVs"):
    st.markdown("""
    When operating UAVs for agricultural purposes, farmers need to be aware of:
    
    1. **Registration Requirements**: Most countries require registration of UAVs above certain weight thresholds
    2. **Pilot Certification**: Commercial operations often require certified pilots
    3. **Flight Restrictions**: 
       - Maximum altitude (typically 400 feet/120 meters)
       - Visual line of sight requirements
       - No-fly zones near airports, populated areas, etc.
    4. **Insurance**: Liability coverage for potential accidents
    5. **Privacy Concerns**: Avoiding data collection over neighboring properties
    6. **Data Ownership**: Understanding who owns the collected data
    
    *Regulations vary by country and region, so always check local laws before operating UAVs for agricultural purposes.*
    """)

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
