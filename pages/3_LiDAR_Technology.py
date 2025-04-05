import streamlit as st
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="LiDAR Technology - Precision Agriculture",
    page_icon="📡",
    layout="wide"
)

# Main content
st.title("LiDAR Technology")
st.subheader("Light Detection and Ranging for Sugarcane Biomass Estimation")

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ## What is LiDAR?
    
    **LiDAR** (Light Detection and Ranging) is a remote sensing technology that uses laser light to 
    measure distances with high precision. By rapidly sending out laser pulses and measuring the time 
    it takes for each pulse to return after hitting an object, LiDAR creates detailed 3D maps of surfaces.
    
    ### How LiDAR Works:
    
    1. A LiDAR sensor emits rapid laser pulses (up to hundreds of thousands per second)
    2. The laser light reflects off objects and returns to the sensor
    3. The system calculates the distance based on the time it takes for the light to return
    4. Multiple measurements create a "point cloud" - a 3D representation of the environment
    5. Software processes this point cloud into usable data formats
    
    ## LiDAR in Sugarcane Farming
    
    LiDAR provides valuable structural information about sugarcane crops:
    
    ### Key Applications:
    
    - **Biomass Estimation**: Accurately determine crop volume and density
    - **Plant Height Measurement**: Track growth rates over time
    - **Canopy Structure Analysis**: Understand the arrangement of plant material
    - **Terrain Mapping**: Create detailed elevation models for water management
    - **Plant Row Detection**: Verify crop spacing and identify gaps
    """)

with col2:
    # Use a placeholder SVG from Font Awesome for LiDAR concept
    st.markdown("""
    <div style="text-align: center; font-size: 100px; color: #4CAF50;">
        <i class="fa fa-signal"></i>
    </div>
    <p style="text-align: center; font-style: italic;">LiDAR pulses measuring crop structure</p>
    """, unsafe_allow_html=True)
    
    # LiDAR point cloud representation
    st.markdown("### LiDAR Point Cloud Representation")
    
    # Create a 3D scatter plot to represent a LiDAR point cloud
    import numpy as np
    
    # Generate sample data for a simplified sugarcane canopy
    np.random.seed(42)
    n_points = 1000
    
    # Create x and y coordinates in a grid pattern for rows
    x = np.repeat(np.linspace(0, 10, 10), 100)
    y = np.tile(np.linspace(0, 10, 100), 10)
    
    # Create z coordinates with higher values in the middle (plant structure)
    base_z = np.sin(x * 0.5) * 1.5 + np.cos(y * 0.5) * 1.5
    plant_shape = 3 * np.exp(-0.1 * ((x - 5)**2 + (y - 5)**2))
    z = base_z + plant_shape + np.random.normal(0, 0.2, n_points)
    
    # Create color gradient based on height
    colors = z
    
    # Create the 3D scatter plot
    fig = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=2,
            color=colors,
            colorscale='Greens',
            opacity=0.8
        )
    )])
    
    # Update layout
    fig.update_layout(
        title="Simulated LiDAR Point Cloud of Sugarcane",
        scene=dict(
            xaxis_title="X (meters)",
            yaxis_title="Y (meters)",
            zaxis_title="Height (meters)",
            aspectratio=dict(x=1, y=1, z=0.5)
        ),
        margin=dict(l=0, r=0, b=0, t=30)
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Full width content
st.markdown("""
## Types of LiDAR Systems Used in Agriculture

### Based on Platform:
1. **Satellite-based LiDAR**: Lower resolution but covers vast areas
2. **Airborne LiDAR**: Mounted on manned aircraft, offers medium resolution
3. **UAV-mounted LiDAR**: High-resolution mapping with flexible deployment
4. **Ground-based LiDAR**: Very high resolution but limited area coverage

### Based on Technology:
1. **Time-of-Flight (ToF) LiDAR**: Measures the time taken for the light pulse to return
2. **Phase-shift LiDAR**: Measures the phase difference between emitted and returned light
3. **Flash LiDAR**: Illuminates the entire scene at once with a single laser pulse
4. **Single-photon LiDAR**: Highly sensitive systems that can detect single photons

## LiDAR for Biomass Estimation in Sugarcane

LiDAR excels at estimating sugarcane biomass due to its ability to penetrate the canopy and create a comprehensive 3D representation of the crop structure. The process involves:

1. **Data Collection**: Flying UAVs equipped with LiDAR sensors over sugarcane fields
2. **Point Cloud Creation**: Generating millions of 3D points representing the crop surface
3. **Data Filtering**: Separating ground points from vegetation points
4. **Height Calculation**: Determining plant height by subtracting ground elevation from canopy elevation
5. **Volume Calculation**: Computing the volume occupied by the crop
6. **Biomass Modeling**: Converting volume measurements to biomass estimates using calibration models
""")

# Advantages and limitations
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### Advantages of LiDAR for Biomass Estimation
    
    - **Accuracy**: High precision in structural measurements
    - **Canopy Penetration**: Can "see" through gaps in vegetation
    - **3D Capability**: Captures the three-dimensional structure of crops
    - **Day/Night Operation**: Not dependent on sunlight
    - **Weather Flexible**: Can operate in various lighting conditions
    - **Multiple Returns**: Can record multiple surfaces from a single pulse
    """)

with col2:
    st.markdown("""
    ### Limitations of LiDAR
    
    - **Cost**: LiDAR sensors remain relatively expensive
    - **Data Volume**: Generates massive datasets requiring significant processing
    - **Expertise Required**: Needs specialized knowledge for data processing
    - **Limited Spectral Information**: Doesn't provide biochemical or physiological crop data
    - **Weather Constraints**: Heavy rain can interfere with laser pulses
    - **Battery Demand**: High power requirements limit UAV flight time
    """)

# Interactive demonstration
st.subheader("LiDAR in Action: Seasonal Growth Monitoring")

# Create sample data showing LiDAR-measured sugarcane height through a growing season
days = list(range(0, 361, 30))
heights = [0.2, 0.8, 1.5, 2.1, 2.6, 3.0, 3.3, 3.5, 3.6, 3.7, 3.7, 3.7]

# Plot the data
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=days,
    y=heights,
    mode='lines+markers',
    name='Plant Height',
    line=dict(color='green', width=3),
    marker=dict(size=10)
))

# Add growth phases
fig.add_shape(
    type="rect",
    x0=0, y0=0,
    x1=90, y1=4,
    fillcolor="rgba(76, 175, 80, 0.2)",
    line=dict(width=0),
    layer="below"
)
fig.add_annotation(
    x=45, y=0.2,
    text="Germination & Establishment",
    showarrow=False,
    font=dict(color="green")
)

fig.add_shape(
    type="rect",
    x0=90, y0=0,
    x1=180, y1=4,
    fillcolor="rgba(139, 195, 74, 0.2)",
    line=dict(width=0),
    layer="below"
)
fig.add_annotation(
    x=135, y=2.1,
    text="Grand Growth",
    showarrow=False,
    font=dict(color="green")
)

fig.add_shape(
    type="rect",
    x0=180, y0=0,
    x1=270, y1=4,
    fillcolor="rgba(205, 220, 57, 0.2)",
    line=dict(width=0),
    layer="below"
)
fig.add_annotation(
    x=225, y=3.4,
    text="Maturation",
    showarrow=False,
    font=dict(color="green")
)

fig.add_shape(
    type="rect",
    x0=270, y0=0,
    x1=360, y1=4,
    fillcolor="rgba(255, 235, 59, 0.2)",
    line=dict(width=0),
    layer="below"
)
fig.add_annotation(
    x=315, y=3.7,
    text="Ripening",
    showarrow=False,
    font=dict(color="green")
)

# Update layout
fig.update_layout(
    title="LiDAR-Measured Sugarcane Height Through Growing Season",
    xaxis_title="Days After Planting",
    yaxis_title="Crop Height (meters)",
    legend_title="Measurement Type",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
The graph above shows how LiDAR technology can track sugarcane growth throughout the season. Key observations:

- **Early Growth (0-90 days)**: Rapid vertical growth begins after establishment
- **Grand Growth (90-180 days)**: Period of most rapid height increase
- **Maturation (180-270 days)**: Growth rate decreases as plants reach full height
- **Ripening (270-360 days)**: Height stabilizes as energy goes to sugar accumulation

LiDAR measurements taken at regular intervals can create this type of growth curve, helping farmers track crop development and predict yields.
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
