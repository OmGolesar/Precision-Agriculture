import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Multispectral Imaging - Precision Agriculture",
    page_icon="📸",
    layout="wide"
)

# Main content
st.title("Multispectral Imaging Technology")
st.subheader("Using Light Beyond Human Vision for Crop Analysis")

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ## What is Multispectral Imaging?
    
    **Multispectral imaging** captures data at specific wavelengths across the electromagnetic spectrum, 
    including those beyond human vision (like near-infrared). By measuring how plants reflect or absorb 
    different light wavelengths, we can gather crucial information about their health, stress levels, 
    and biochemical composition.
    
    ### Key Spectral Bands Used in Agriculture:
    
    - **Blue (450-495 nm)**: Chlorophyll absorption, useful for soil/vegetation differentiation
    - **Green (495-570 nm)**: Chlorophyll reflection, indicates leaf structure changes
    - **Red (620-700 nm)**: Chlorophyll absorption, sensitive to plant health
    - **Red Edge (700-730 nm)**: Transition between red and NIR, highly sensitive to chlorophyll content
    - **Near-Infrared (NIR, 700-1100 nm)**: Strongly reflected by healthy vegetation, key for biomass estimation
    - **Short-Wave Infrared (SWIR, 1100-2500 nm)**: Sensitive to water content in vegetation
    
    ## Applications in Sugarcane Farming
    
    Multispectral imaging helps sugarcane farmers:
    
    - **Assess Crop Health**: Identify stressed or diseased areas before visible symptoms appear
    - **Monitor Nitrogen Levels**: Estimate leaf nitrogen content for fertilization decisions
    - **Predict Biomass**: Calculate vegetation indices correlated with crop biomass
    - **Detect Water Stress**: Identify areas with irrigation issues
    - **Map Maturity Levels**: Determine optimal harvest timing across fields
    """)

with col2:
    # Display electromagnetic spectrum
    st.markdown("### The Electromagnetic Spectrum in Agricultural Sensing")
    
    # Create a visualization of the electromagnetic spectrum
    wavelengths = [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
    labels = ["Violet", "Blue", "Cyan", "Green", "Yellow", "Orange", "Red", 
              "Red Edge", "Near Infrared", "Near Infrared", "Near Infrared", "Near Infrared", "Near Infrared"]
    colors = ["violet", "blue", "cyan", "green", "yellow", "orange", "red", 
              "darkred", "darkred", "darkred", "darkred", "darkred", "darkred"]
    
    agricultural_use = [
        "Limited use in agriculture",
        "Chlorophyll absorption",
        "Pigment assessment",
        "Chlorophyll reflection",
        "Vegetation differentiation",
        "Chlorophyll absorption begins",
        "Strong chlorophyll absorption",
        "Transition zone - very sensitive to plant health",
        "Cell structure reflection - biomass estimation",
        "Water content assessment",
        "Protein and nitrogen indication",
        "Starch and sugar content",
        "Moisture content assessment"
    ]
    
    # Create dataframe
    df = pd.DataFrame({
        "Wavelength (nm)": wavelengths,
        "Band": labels,
        "Color": colors,
        "Agricultural Use": agricultural_use
    })
    
    # Create figure
    fig = px.bar(
        df, 
        x="Wavelength (nm)", 
        y=[1]*len(wavelengths),
        color="Band",
        color_discrete_sequence=colors,
        hover_data={"Agricultural Use": True, "Band": True, "Wavelength (nm)": True},
        labels={"y": ""}
    )
    
    # Update layout
    fig.update_layout(
        title="Spectral Bands Used in Agricultural Remote Sensing",
        showlegend=False,
        plot_bgcolor="white",
        height=400,
        yaxis=dict(showticklabels=False, showgrid=False),
        xaxis=dict(title="Wavelength (nm)"),
        margin=dict(l=0, r=0, t=40, b=0)
    )
    
    # Remove y-axis
    fig.update_yaxes(visible=False)
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Show multispectral camera concept
    st.image("https://ee.cdnartwhere.eu/wp-content/uploads/import/default/files/sites/default/files/images/news-pixinov1.jpg", 
             caption="UAV equipped with multispectral camera (representative image)",
             use_container_width=True)

# Full width content - Vegetation Indices
st.markdown("""
## Vegetation Indices for Sugarcane Analysis

**Vegetation indices** are mathematical combinations of spectral bands that highlight specific plant characteristics. 
These indices transform multispectral data into meaningful metrics for crop assessment.

### Important Vegetation Indices for Sugarcane:
""")

# Create a three-column layout for indices
col1, col2, col3 = st.columns(3)

with col1:
    with st.expander("NDVI (Normalized Difference Vegetation Index)"):
        st.markdown("""
        **Formula:** (NIR - Red) / (NIR + Red)
        
        **Range:** -1 to +1
        
        **Usage:** The most common vegetation index, strongly correlated with biomass, leaf area index, and overall plant vigor.
        
        **Interpretation:**
        - < 0: Water, bare soil, artificial surfaces
        - 0.1-0.2: Sparse vegetation
        - 0.2-0.5: Moderate vegetation
        - > 0.5: Dense, healthy vegetation
        """)
        
        # Simple NDVI visualization
        x = np.linspace(0, 10, 100)
        healthy = 0.7 + 0.1 * np.sin(x/2) + np.random.normal(0, 0.02, 100)
        stressed = 0.35 + 0.05 * np.sin(x/2) + np.random.normal(0, 0.02, 100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=healthy, mode='lines', name='Healthy Sugarcane', line=dict(color='green')))
        fig.add_trace(go.Scatter(x=x, y=stressed, mode='lines', name='Stressed Sugarcane', line=dict(color='orange')))
        
        fig.update_layout(
            title="NDVI Comparison: Healthy vs. Stressed Sugarcane",
            xaxis_title="Field Position",
            yaxis_title="NDVI Value",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

with col2:
    with st.expander("GNDVI (Green Normalized Difference Vegetation Index)"):
        st.markdown("""
        **Formula:** (NIR - Green) / (NIR + Green)
        
        **Range:** -1 to +1
        
        **Usage:** More sensitive to chlorophyll concentration than NDVI, useful for assessing nitrogen levels in sugarcane.
        
        **Interpretation:**
        - Similar to NDVI but more sensitive during mid to late growth stages
        - Better for detecting subtle changes in crop health
        - Less saturation in dense canopies compared to NDVI
        """)
        
        # GNDVI comparison visualization
        stages = ["Early", "Mid", "Late", "Harvest"]
        ndvi_sensitivity = [0.8, 0.7, 0.6, 0.5]
        gndvi_sensitivity = [0.7, 0.8, 0.8, 0.7]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=stages, y=ndvi_sensitivity, name='NDVI Sensitivity', marker_color='green'))
        fig.add_trace(go.Bar(x=stages, y=gndvi_sensitivity, name='GNDVI Sensitivity', marker_color='mediumseagreen'))
        
        fig.update_layout(
            title="Index Sensitivity by Growth Stage",
            xaxis_title="Growth Stage",
            yaxis_title="Relative Sensitivity",
            height=300,
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)

with col3:
    with st.expander("NDRE (Normalized Difference Red Edge)"):
        st.markdown("""
        **Formula:** (NIR - Red Edge) / (NIR + Red Edge)
        
        **Range:** -1 to +1
        
        **Usage:** Excellent for nitrogen content estimation in crops with dense canopy like sugarcane.
        
        **Interpretation:**
        - Typically lower values than NDVI (usually 0.1-0.4 range)
        - Less prone to saturation in dense vegetation
        - Highly correlated with chlorophyll content
        - Very sensitive to early stress detection
        """)
        
        # NDRE visualization for nitrogen levels
        nitrogen_levels = ["Deficient", "Low", "Adequate", "Optimal", "Excessive"]
        ndre_values = [0.12, 0.18, 0.25, 0.32, 0.35]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=nitrogen_levels, 
            y=ndre_values, 
            marker_color=['#d73027', '#fc8d59', '#fee090', '#91cf60', '#1a9850'],
            text=ndre_values,
            textposition='auto'
        ))
        
        fig.update_layout(
            title="NDRE Response to Nitrogen Levels",
            xaxis_title="Nitrogen Status",
            yaxis_title="NDRE Value",
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Process explanation
st.subheader("How Multispectral Data is Processed")

st.markdown("""
The process of collecting and analyzing multispectral data for sugarcane assessment follows these steps:
""")

# Create a process flow diagram with expanders
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    with st.expander("1. Data Acquisition"):
        st.markdown("""
        - UAV equipped with multispectral camera flies over sugarcane fields
        - Camera captures separate images for each spectral band
        - GPS records precise location of each image
        - Images typically taken at 50-120m altitude
        - Resolution ranges from 2-10cm per pixel
        """)

with col2:
    with st.expander("2. Pre-processing"):
        st.markdown("""
        - Radiometric calibration to correct for lighting conditions
        - Geometric correction to account for UAV movement
        - Image mosaicking to create a complete field view
        - Co-registration to align all spectral bands precisely
        - Noise reduction to improve data quality
        """)

with col3:
    with st.expander("3. Index Calculation"):
        st.markdown("""
        - Calculation of vegetation indices (NDVI, GNDVI, NDRE, etc.)
        - Creation of index maps showing spatial variation
        - Statistical analysis of index distributions
        - Comparison with previous datasets
        - Anomaly detection to identify problem areas
        """)

with col4:
    with st.expander("4. Analysis & Modeling"):
        st.markdown("""
        - Correlation of index values with field measurements
        - Biomass prediction model application
        - Nitrogen status estimation
        - Water stress assessment
        - Disease and pest hotspot identification
        """)

with col5:
    with st.expander("5. Application"):
        st.markdown("""
        - Generation of prescription maps for variable rate applications
        - Decision support for irrigation management
        - Harvest planning and yield estimation
        - Monitoring of crop response to treatments
        - Season-to-season performance comparison
        """)

# Multispectral vs. LiDAR comparison
st.subheader("Multispectral vs. LiDAR for Sugarcane Assessment")

comparison_data = {
    "Characteristic": [
        "Primary Information",
        "Canopy Penetration",
        "Plant Health Assessment",
        "Biomass Estimation Early Season",
        "Biomass Estimation Late Season",
        "Nitrogen Content Estimation",
        "Water Stress Detection",
        "Disease Detection",
        "Processing Complexity",
        "Data Volume",
        "Weather Dependency"
    ],
    "Multispectral": [
        "Biochemical & Physiological",
        "Limited",
        "Excellent",
        "Very Good",
        "Moderate",
        "Excellent",
        "Good",
        "Very Good",
        "Moderate",
        "Moderate",
        "High (needs consistent lighting)"
    ],
    "LiDAR": [
        "Structural & Physical",
        "Good",
        "Limited",
        "Moderate",
        "Excellent",
        "Poor",
        "Poor",
        "Poor",
        "High",
        "Very High",
        "Low (works in varied conditions)"
    ]
}

# Create dataframe
comparison_df = pd.DataFrame(comparison_data)

# Display as interactive table
st.dataframe(comparison_df, use_container_width=True)

st.markdown("""
As shown in the comparison above, multispectral imaging and LiDAR technology offer complementary information about sugarcane crops:

- **Multispectral excels** at assessing plant health, nutrient status, and early-season biomass
- **LiDAR excels** at measuring structural characteristics and late-season biomass

The research study discussed in later sections demonstrates that combining these technologies (data fusion) can provide more comprehensive crop assessment, though the benefits may not always justify the increased complexity and cost.
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
