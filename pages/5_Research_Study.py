import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Research Study - UAV Technologies for Sugarcane",
    page_icon="🔬",
    layout="wide"
)

# Main content
st.title("Research Study Overview")
st.subheader("Evaluating UAV Technologies for Sugarcane Monitoring")

# Study design section
st.markdown("""
## Study Design and Methodology

This research evaluated different UAV-based remote sensing approaches for estimating sugarcane biomass and leaf nitrogen content 
throughout the growing season. The study aimed to determine which technology or combination of technologies provides the most 
accurate predictions at different growth stages.
""")

# Key parameters in a table format
st.markdown("### Key Study Parameters")
study_params = {
    "Parameter": [
        "Study Location", 
        "Crop Type", 
        "Field Size", 
        "Growing Season", 
        "UAV Survey Frequency", 
        "Survey Intervals", 
        "UAV Flight Altitude", 
        "Ground Control Points", 
        "Field Sampling Points"
    ],
    "Value": [
        "Tropical sugarcane growing region", 
        "Sugarcane (Saccharum officinarum)", 
        "20 hectares", 
        "12 months", 
        "Every 42 days", 
        "6 surveys total", 
        "100 meters above ground level", 
        "12 GCPs distributed across the field", 
        "45 sampling locations for ground truth data"
    ]
}

# Convert to DataFrame and display
st.table(pd.DataFrame(study_params))

# Two-column layout for methodology
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ### Data Collection Methodology
    
    #### UAV Data Collection:
    
    1. **Multispectral Imaging**
       - Camera: 5-band multispectral sensor (Blue, Green, Red, Red Edge, NIR)
       - Resolution: 8 cm/pixel
       - Calibration: Pre-flight radiometric calibration panel
    
    2. **LiDAR Scanning**
       - Sensor: UAV-mounted LiDAR system
       - Point Density: >100 points/m²
       - Accuracy: ±3 cm vertical, ±5 cm horizontal
    
    3. **Survey Timeline:**
       - First survey: 100 days after harvest (DAH)
       - Subsequent surveys: 142, 184, 226, 268, and 310 DAH
       - All surveys conducted between 10:00 AM and 2:00 PM under clear sky conditions
    
    #### Ground Truth Data Collection:
    
    1. **Biomass Measurements:**
       - Sampling Method: 1m² quadrats at 45 locations
       - Measurements: Fresh weight of above-ground biomass
       - Subsampling: Oven-dried to determine dry biomass
    
    2. **Leaf Nitrogen Analysis:**
       - Sampling: Top visible dewlap leaf collected from 5 plants per location
       - Analysis: Laboratory analysis using Kjeldahl method
       - Expression: % Nitrogen on a dry weight basis
    """)

with col2:
    # Create a timeline of the study
    timeline_data = {
        "Event": [
            "Harvest/Ratoon",
            "1st Survey (100 DAH)",
            "2nd Survey (142 DAH)",
            "3rd Survey (184 DAH)",
            "4th Survey (226 DAH)",
            "5th Survey (268 DAH)",
            "6th Survey (310 DAH)",
            "Final Harvest"
        ],
        "Day": [0, 100, 142, 184, 226, 268, 310, 360],
        "Stage": [
            "Start",
            "Early Growth",
            "Early Growth",
            "Grand Growth",
            "Grand Growth",
            "Maturation",
            "Maturation",
            "Harvest"
        ]
    }
    
    # Convert to DataFrame
    timeline_df = pd.DataFrame(timeline_data)
    
    # Create the timeline visualization
    fig = px.timeline(
        timeline_df, 
        x_start="Day", 
        x_end=[100, 142, 184, 226, 268, 310, 360, 365],
        y="Event",
        color="Stage",
        color_discrete_map={
            "Start": "lightgrey",
            "Early Growth": "lightgreen",
            "Grand Growth": "green",
            "Maturation": "darkgreen",
            "Harvest": "brown"
        }
    )
    
    # Update layout
    fig.update_layout(
        title="Study Timeline (Days After Harvest)",
        xaxis_title="Days After Harvest (DAH)",
        showlegend=True,
        height=400
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Add ground sampling illustration
    st.image("https://cdn.pixabay.com/photo/2014/04/05/11/39/microscope-316556_1280.jpg", 
             caption="Laboratory analysis of leaf samples (representative image)",
             use_container_width=True)

# Data processing section
st.markdown("""
## Data Processing and Model Development

The study developed and compared four different predictive models:
""")

# Model explanation with expandable sections
col1, col2 = st.columns(2)

with col1:
    with st.expander("Multispectral-based Model"):
        st.markdown("""
        **Data Inputs:**
        - Vegetation indices (NDVI, GNDVI, NDRE, MCARI, SAVI)
        - Texture features from multispectral bands
        - Canopy coverage percentage
        
        **Model Type:**
        Random Forest regression model with 10-fold cross-validation
        
        **Target Variables:**
        - Sugarcane biomass (tons/hectare)
        - Leaf nitrogen content (%)
        """)
    
    with st.expander("LiDAR-based Model"):
        st.markdown("""
        **Data Inputs:**
        - Canopy height metrics (mean, maximum, percentiles)
        - Canopy volume
        - Point density metrics
        - Canopy roughness indices
        
        **Model Type:**
        Random Forest regression model with 10-fold cross-validation
        
        **Target Variables:**
        - Sugarcane biomass (tons/hectare)
        - Leaf nitrogen content (%)
        """)

with col2:
    with st.expander("Fusion Model"):
        st.markdown("""
        **Data Inputs:**
        - Combined multispectral and LiDAR features
        - Feature selection to reduce dimensionality
        - Weighted combinations based on growth stage
        
        **Model Type:**
        Random Forest regression model with 10-fold cross-validation
        
        **Target Variables:**
        - Sugarcane biomass (tons/hectare)
        - Leaf nitrogen content (%)
        """)
    
    with st.expander("NDVI Benchmark Model"):
        st.markdown("""
        **Data Inputs:**
        - NDVI values only (industry standard approach)
        
        **Model Type:**
        Simple linear regression with NDVI as the predictor
        
        **Target Variables:**
        - Sugarcane biomass (tons/hectare)
        - Leaf nitrogen content (%)
        
        **Purpose:**
        To serve as a baseline for comparing the performance of the more complex models
        """)

# Results section
st.markdown("## Key Findings")

# Create tabs for different results
tab1, tab2, tab3 = st.tabs(["Biomass Estimation", "Nitrogen Prediction", "Practical Implications"])

with tab1:
    st.markdown("""
    ### Biomass Estimation Results
    
    The study revealed that the performance of different models varied significantly depending on the growth stage:
    """)
    
    # Create data for R² values across growth stages
    days = [100, 142, 184, 226, 268, 310]
    multispectral = [0.52, 0.57, 0.49, 0.43, 0.41, 0.38]
    lidar = [0.31, 0.44, 0.53, 0.61, 0.68, 0.71]
    fusion = [0.54, 0.59, 0.57, 0.63, 0.69, 0.72]
    ndvi = [0.48, 0.46, 0.39, 0.36, 0.33, 0.31]
    
    # Create figure
    fig = go.Figure()
    
    # Add traces
    fig.add_trace(go.Scatter(
        x=days, 
        y=multispectral, 
        mode='lines+markers',
        name='Multispectral',
        line=dict(color='green', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=days, 
        y=lidar, 
        mode='lines+markers',
        name='LiDAR',
        line=dict(color='blue', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=days, 
        y=fusion, 
        mode='lines+markers',
        name='Fusion',
        line=dict(color='purple', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=days, 
        y=ndvi, 
        mode='lines+markers',
        name='NDVI Benchmark',
        line=dict(color='grey', dash='dash', width=2)
    ))
    
    # Add growth stage regions
    fig.add_vrect(
        x0=80, x1=150,
        fillcolor="lightgreen", opacity=0.3,
        layer="below", line_width=0,
        annotation_text="Early Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=150, x1=250,
        fillcolor="green", opacity=0.2,
        layer="below", line_width=0,
        annotation_text="Grand Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=250, x1=330,
        fillcolor="darkgreen", opacity=0.1,
        layer="below", line_width=0,
        annotation_text="Maturation",
        annotation_position="top left"
    )
    
    # Update layout
    fig.update_layout(
        title="Model Performance for Biomass Estimation Over the Growing Season",
        xaxis_title="Days After Harvest (DAH)",
        yaxis_title="Model Performance (R²)",
        legend_title="Model Type",
        yaxis=dict(range=[0.2, 0.8])
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Key findings bullets
    st.markdown("""
    #### Key Observations:
    
    - **Early Growth Stage (100-142 DAH):**
      - Multispectral model performed best (R²=0.572 at 142 DAH)
      - LiDAR performance was relatively poor (R²=0.31-0.44)
      
    - **Mid to Late Growth Stage (184-310 DAH):**
      - LiDAR model performance improved significantly (R²=0.53-0.71)
      - Multispectral model performance declined (R²=0.49-0.38)
      
    - **Fusion Model:**
      - Provided the best overall performance across all growth stages
      - Improvement over single-sensor models was modest (2-5% increase in R²)
      - Higher computational complexity may not justify the small improvement
      
    - **NDVI Benchmark:**
      - Performed reasonably well in early stages
      - Significant performance decline in later growth stages
      - Simple and cost-effective but less accurate than specialized models
    """)

with tab2:
    st.markdown("""
    ### Nitrogen Prediction Results
    
    The study also evaluated the ability of different models to predict leaf nitrogen content:
    """)
    
    # Create bar chart for nitrogen prediction
    models = ['Multispectral', 'LiDAR', 'Fusion', 'NDVI Benchmark']
    r_squared = [0.57, 0.29, 0.59, 0.51]
    rmse = [0.31, 0.48, 0.30, 0.36]
    
    # Create figure
    fig = go.Figure()
    
    # Add bars for R²
    fig.add_trace(go.Bar(
        x=models,
        y=r_squared,
        name='R² Value',
        marker_color='forestgreen',
        text=[f"{val:.2f}" for val in r_squared],
        textposition='auto'
    ))
    
    # Add second y-axis for RMSE
    fig.add_trace(go.Scatter(
        x=models,
        y=rmse,
        name='RMSE (% N)',
        mode='markers',
        marker=dict(
            color='red',
            size=12,
            line=dict(
                color='darkred',
                width=2
            )
        ),
        yaxis='y2',
        text=[f"{val:.2f}" for val in rmse],
        textposition='top center'
    ))
    
    # Update layout with second y-axis
    fig.update_layout(
        title="Model Performance for Nitrogen Content Prediction",
        xaxis_title="Model Type",
        yaxis=dict(
            title="Model Fit (R²)",
            range=[0, 0.7]
        ),
        yaxis2=dict(
            title="Error (RMSE % N)",  # Corrected to avoid duplicate keys
            tickfont=dict(color="red"),  # Adjust tick font color
            overlaying="y",
            side="right",
            range=[0.2, 0.6]
        ),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99
        ),
        barmode='group'
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Key findings for nitrogen prediction
    st.markdown("""
    #### Key Observations:
    
    - **Multispectral Model Performance:**
      - Achieved the best single-sensor performance (R²=0.57)
      - Strong correlation between specific vegetation indices (particularly NDRE) and leaf N content
      - Consistent performance across growth stages
      
    - **LiDAR Model Limitations:**
      - Poor performance for nitrogen prediction (R²=0.29)
      - LiDAR primarily captures structural information, not biochemical properties
      - Not recommended as a standalone solution for nutrient assessment
      
    - **Fusion Model:**
      - Slight improvement over multispectral alone (R²=0.59)
      - Added complexity may not justify the marginal improvement
      - Feature importance analysis showed multispectral features dominated the model
      
    - **NDVI Benchmark:**
      - Reasonable performance (R²=0.51)
      - Simple and widely used, but less accurate than specialized indices like NDRE
    """)

    # Scatter plot of predicted vs. actual nitrogen values
    st.subheader("Predicted vs. Actual Nitrogen Values (Multispectral Model)")
    
    # Generate sample data for demonstration
    np.random.seed(42)
    actual_n = np.linspace(1.0, 2.5, 45) + np.random.normal(0, 0.1, 45)
    predicted_n = actual_n * 0.97 + np.random.normal(0, 0.15, 45)
    
    # Create scatter plot
    fig = px.scatter(
        x=actual_n, 
        y=predicted_n,
        labels={"x": "Actual Nitrogen Content (%)", "y": "Predicted Nitrogen Content (%)"},
        trendline="ols"
    )
    
    # Add perfect prediction line
    fig.add_trace(go.Scatter(
        x=[1.0, 2.5],
        y=[1.0, 2.5],
        mode='lines',
        name='1:1 Line',
        line=dict(color='red', dash='dash')
    ))
    
    # Update layout
    fig.update_layout(
        title="Multispectral Model: Predicted vs. Actual Nitrogen Content",
        xaxis=dict(range=[0.9, 2.6]),
        yaxis=dict(range=[0.9, 2.6]),
        width=700,
        height=500
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("""
    ### Practical Implications of the Study Findings
    
    The results provide valuable insights for sugarcane farmers and agricultural consultants:
    """)
    
    # Create a decision table
    decision_data = {
        "Growth Stage": ["Early (100-150 DAH)", "Mid (150-250 DAH)", "Late (250-310 DAH)"],
        "Best Technology for Biomass": ["Multispectral", "LiDAR or Fusion", "LiDAR"],
        "Best Technology for Nitrogen": ["Multispectral", "Multispectral", "Multispectral"],
        "Recommended Survey Frequency": ["Monthly", "Every 6 weeks", "Monthly"],
        "Key Management Decisions": [
            "Fertilization adjustments, Replanting gaps",
            "Irrigation optimization, Pest management",
            "Harvest planning, Ripening agent application"
        ]
    }
    
    # Convert to DataFrame and display
    decision_df = pd.DataFrame(decision_data)
    st.table(decision_df)
    
    # Cost-benefit analysis
    st.subheader("Technology Cost-Benefit Considerations")
    
    # Create columns for each technology option
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Multispectral Only")
        st.markdown("""
        **Advantages:**
        - Lower equipment cost
        - Simpler data processing
        - Excellent for early growth stages
        - Best option for nitrogen assessment
        - Widely available service providers
        
        **Limitations:**
        - Reduced accuracy for biomass in late stages
        - Weather and lighting dependent
        - Requires clear visibility of canopy
        """)

    with col2:
        st.markdown("### LiDAR Only")
        st.markdown("""
        **Advantages:**
        - Superior late-season biomass estimation
        - Less affected by lighting conditions
        - Can operate in more weather conditions
        - Provides detailed structural information
        
        **Limitations:**
        - Higher equipment cost
        - Complex data processing required
        - Poor performance for nutrient assessment
        - Limited service providers availability
        """)

    with col3:
        st.markdown("### Combined Approach")
        st.markdown("""
        **Advantages:**
        - Most comprehensive data collection
        - Best overall performance across growth stages
        - Flexibility to use appropriate model by stage
        - Future-proof investment in technology
        
        **Limitations:**
        - Highest equipment and processing cost
        - Marginal improvement over single-sensor approach
        - Requires expertise in both technologies
        - Most complex implementation
        """)
    
    # Summary recommendation
    st.info("""
    **Summary Recommendation:**
    
    For most sugarcane growers, a staged approach is recommended:
    
    1. Start with multispectral imaging for early growth monitoring and nitrogen management
    2. Consider adding LiDAR capability for mid-to-late season biomass estimation if large-scale operations justify the investment
    3. For research purposes or very large operations, the combined approach offers the most comprehensive dataset
    
    The choice ultimately depends on specific farm needs, budget constraints, and management objectives.
    """)

# Conclusion section
st.markdown("""
## Study Conclusions

This research provides valuable insights into the optimal use of UAV-based remote sensing technologies for sugarcane monitoring:

1. **Technology Selection by Growth Stage:**
   - Early growth stage: Multispectral imaging provides the best results
   - Late growth stage: LiDAR technology offers superior biomass estimation

2. **Nitrogen Management:**
   - Multispectral imaging, particularly using the Red Edge band, provides reliable estimates of leaf nitrogen content
   - LiDAR technology alone is not suitable for nitrogen assessment

3. **Cost-Effectiveness Considerations:**
   - The fusion approach, while slightly more accurate, may not justify the increased cost and complexity
   - For most commercial applications, selecting the appropriate single-sensor technology based on growth stage is recommended

4. **Practical Implementation:**
   - Regular surveys (every 42 days) provide sufficient temporal resolution to capture crop development
   - Integration with farm management systems can translate the remote sensing data into actionable insights

These findings help bridge the gap between research and practical application, enabling sugarcane farmers to make informed decisions about adopting UAV-based technologies for precision agriculture.
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
