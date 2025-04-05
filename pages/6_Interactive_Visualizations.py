import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Interactive Visualizations - UAV Technologies",
    page_icon="📊",
    layout="wide"
)

# Main content
st.title("Interactive Visualizations")
st.subheader("Explore Data from UAV-Based Sugarcane Monitoring")

# Create sample data for visualization
@st.cache_data
def generate_sample_data():
    # Days after harvest for x-axis
    days = list(range(100, 311, 42))  # 100, 142, 184, 226, 268, 310
    
    # Biomass values (tons/hectare) for different models
    np.random.seed(42)  # For reproducibility
    
    # Sample data for biomass predictions
    multispectral_biomass = [20, 45, 65, 85, 95, 98]
    multispectral_error = [3, 5, 7, 9, 11, 12]
    
    lidar_biomass = [15, 42, 68, 90, 102, 105]
    lidar_error = [4, 5, 6, 6, 5, 4]
    
    fusion_biomass = [18, 44, 67, 88, 99, 103]
    fusion_error = [3, 4, 5, 5, 4, 3]
    
    ndvi_biomass = [22, 43, 60, 75, 85, 90]
    ndvi_error = [4, 6, 8, 10, 12, 14]
    
    # Sample data for nitrogen content
    nitrogen_values = [2.2, 2.0, 1.9, 1.7, 1.5, 1.3]
    nitrogen_error = [0.2, 0.2, 0.15, 0.15, 0.1, 0.1]
    
    # R-squared values for biomass prediction
    r2_multispectral = [0.52, 0.57, 0.49, 0.43, 0.41, 0.38]
    r2_lidar = [0.31, 0.44, 0.53, 0.61, 0.68, 0.71]
    r2_fusion = [0.54, 0.59, 0.57, 0.63, 0.69, 0.72]
    r2_ndvi = [0.48, 0.46, 0.39, 0.36, 0.33, 0.31]
    
    # R-squared values for nitrogen prediction (consistent across growth stages)
    r2_n_multispectral = [0.57, 0.58, 0.56, 0.57, 0.56, 0.55]
    r2_n_lidar = [0.28, 0.29, 0.30, 0.31, 0.30, 0.28]
    r2_n_fusion = [0.59, 0.60, 0.58, 0.59, 0.57, 0.56]
    r2_n_ndvi = [0.51, 0.50, 0.49, 0.48, 0.47, 0.46]
    
    return {
        "days": days,
        "multispectral_biomass": multispectral_biomass,
        "multispectral_error": multispectral_error,
        "lidar_biomass": lidar_biomass,
        "lidar_error": lidar_error,
        "fusion_biomass": fusion_biomass,
        "fusion_error": fusion_error,
        "ndvi_biomass": ndvi_biomass,
        "ndvi_error": ndvi_error,
        "nitrogen_values": nitrogen_values,
        "nitrogen_error": nitrogen_error,
        "r2_multispectral": r2_multispectral,
        "r2_lidar": r2_lidar,
        "r2_fusion": r2_fusion,
        "r2_ndvi": r2_ndvi,
        "r2_n_multispectral": r2_n_multispectral,
        "r2_n_lidar": r2_n_lidar,
        "r2_n_fusion": r2_n_fusion,
        "r2_n_ndvi": r2_n_ndvi
    }

# Get the data
data = generate_sample_data()

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "Biomass Prediction", 
    "Model Performance", 
    "Nitrogen Content",
    "Growth Stage Advisor"
])

with tab1:
    st.markdown("""
    ### Sugarcane Biomass Prediction
    
    The chart below shows biomass predictions from different UAV-based models throughout the growing season.
    Select which models to display and explore how predictions change over time.
    """)
    
    # Model selection checkboxes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        show_multispectral = st.checkbox("Multispectral Model", value=True)
    with col2:
        show_lidar = st.checkbox("LiDAR Model", value=True)
    with col3:
        show_fusion = st.checkbox("Fusion Model", value=True)
    with col4:
        show_ndvi = st.checkbox("NDVI Benchmark", value=False)
    
    # Create the line chart
    fig = go.Figure()
    
    # Add traces based on checkbox selections
    if show_multispectral:
        fig.add_trace(go.Scatter(
            x=data["days"],
            y=data["multispectral_biomass"],
            mode="lines+markers",
            name="Multispectral",
            line=dict(color="green", width=3),
            error_y=dict(
                type="data",
                array=data["multispectral_error"],
                visible=True
            )
        ))
    
    if show_lidar:
        fig.add_trace(go.Scatter(
            x=data["days"],
            y=data["lidar_biomass"],
            mode="lines+markers",
            name="LiDAR",
            line=dict(color="blue", width=3),
            error_y=dict(
                type="data",
                array=data["lidar_error"],
                visible=True
            )
        ))
    
    if show_fusion:
        fig.add_trace(go.Scatter(
            x=data["days"],
            y=data["fusion_biomass"],
            mode="lines+markers",
            name="Fusion",
            line=dict(color="purple", width=3),
            error_y=dict(
                type="data",
                array=data["fusion_error"],
                visible=True
            )
        ))
    
    if show_ndvi:
        fig.add_trace(go.Scatter(
            x=data["days"],
            y=data["ndvi_biomass"],
            mode="lines+markers",
            name="NDVI Benchmark",
            line=dict(color="gray", width=2, dash="dash"),
            error_y=dict(
                type="data",
                array=data["ndvi_error"],
                visible=True
            )
        ))
    
    # Add growth stage regions
    fig.add_vrect(
        x0=80, x1=150,
        fillcolor="rgba(144, 238, 144, 0.3)",
        layer="below", line_width=0,
        annotation_text="Early Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=150, x1=250,
        fillcolor="rgba(60, 179, 113, 0.2)",
        layer="below", line_width=0,
        annotation_text="Grand Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=250, x1=330,
        fillcolor="rgba(46, 139, 87, 0.2)",
        layer="below", line_width=0,
        annotation_text="Maturation",
        annotation_position="top left"
    )
    
    # Update layout
    fig.update_layout(
        title="Sugarcane Biomass Predictions by Different Models",
        xaxis_title="Days After Harvest (DAH)",
        yaxis_title="Biomass (tons/hectare)",
        legend_title="Model Type",
        height=600
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Add explanatory text
    st.markdown("""
    #### Insights from Biomass Prediction:
    
    - **Early Growth Stage (100-150 DAH)**: All models show similar predictions, with multispectral slightly more accurate
    - **Mid Growth Stage (150-250 DAH)**: LiDAR begins to show better accuracy as plant structure develops
    - **Late Growth Stage (250-310 DAH)**: LiDAR predictions are most accurate as plant height and structure become dominant factors
    - **Error Bars**: Show the prediction uncertainty for each model at different growth stages
    
    The ideal approach may be to use multispectral imaging for early season predictions and switch to LiDAR as the crop matures.
    """)

with tab2:
    st.markdown("""
    ### Model Performance Comparison
    
    The bar charts below compare the performance (R² values) of different models for predicting biomass and nitrogen content at various growth stages.
    R² values range from 0 to 1, with higher values indicating better model performance.
    """)
    
    # Add a toggle to switch between biomass and nitrogen
    prediction_type = st.radio(
        "Select Prediction Type",
        ["Biomass Prediction", "Nitrogen Prediction"],
        horizontal=True
    )
    
    # Create a slider for growth stage selection
    stage_index = st.select_slider(
        "Select Growth Stage (Days After Harvest)",
        options=[0, 1, 2, 3, 4, 5],
        format_func=lambda x: f"{data['days'][x]} DAH"
    )
    
    # Prepare data based on selection
    if prediction_type == "Biomass Prediction":
        r2_values = [
            data["r2_multispectral"][stage_index],
            data["r2_lidar"][stage_index],
            data["r2_fusion"][stage_index],
            data["r2_ndvi"][stage_index]
        ]
        title = f"Model Performance for Biomass Prediction at {data['days'][stage_index]} DAH"
    else:  # Nitrogen Prediction
        r2_values = [
            data["r2_n_multispectral"][stage_index],
            data["r2_n_lidar"][stage_index],
            data["r2_n_fusion"][stage_index],
            data["r2_n_ndvi"][stage_index]
        ]
        title = f"Model Performance for Nitrogen Prediction at {data['days'][stage_index]} DAH"
    
    # Create the bar chart
    models = ["Multispectral", "LiDAR", "Fusion", "NDVI Benchmark"]
    colors = ["green", "blue", "purple", "gray"]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=models,
        y=r2_values,
        marker_color=colors,
        text=[f"{val:.3f}" for val in r2_values],
        textposition="auto"
    ))
    
    # Update layout
    fig.update_layout(
        title=title,
        xaxis_title="Model Type",
        yaxis_title="R² Value",
        yaxis=dict(range=[0, 0.8]),
        height=500
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Add horizontal best model indicator
    current_best = models[np.argmax(r2_values)]
    st.success(f"**Best Model at {data['days'][stage_index]} DAH**: {current_best} (R² = {max(r2_values):.3f})")
    
    # Add explanatory text based on selection
    if prediction_type == "Biomass Prediction":
        if stage_index < 2:
            st.markdown("""
            **Early Growth Stage Analysis:**
            - Multispectral models perform better in early growth stages
            - Vegetation indices like NDVI are strong predictors when canopy is developing
            - LiDAR is less effective because plant structure is still limited
            """)
        elif stage_index < 4:
            st.markdown("""
            **Mid Growth Stage Analysis:**
            - LiDAR performance improves as plant structure develops
            - Fusion models begin to show their advantage
            - NDVI benchmark declines as canopy becomes dense and saturates the index
            """)
        else:
            st.markdown("""
            **Late Growth Stage Analysis:**
            - LiDAR models show superior performance
            - Plant height and structure are strongly correlated with biomass
            - Multispectral indices lose sensitivity in dense, mature canopy
            """)
    else:  # Nitrogen Prediction
        st.markdown("""
        **Nitrogen Prediction Analysis:**
        - Multispectral consistently outperforms LiDAR for nitrogen prediction
        - Specific bands like Red Edge are strongly correlated with leaf nitrogen content
        - LiDAR provides minimal information about biochemical properties
        - Fusion model offers only marginal improvement over multispectral alone
        """)

with tab3:
    st.markdown("""
    ### Nitrogen Content Tracking
    
    This visualization shows the nitrogen content in sugarcane leaves throughout the growing season, 
    as predicted by multispectral imaging. Nitrogen content typically decreases as the crop matures.
    """)
    
    # Create the nitrogen content line chart
    fig = go.Figure()
    
    # Add nitrogen content trace
    fig.add_trace(go.Scatter(
        x=data["days"],
        y=data["nitrogen_values"],
        mode="lines+markers",
        name="Leaf N Content",
        line=dict(color="darkgreen", width=3),
        error_y=dict(
            type="data",
            array=data["nitrogen_error"],
            visible=True
        )
    ))
    
    # Add threshold lines
    fig.add_trace(go.Scatter(
        x=[data["days"][0], data["days"][-1]],
        y=[2.0, 2.0],
        mode="lines",
        name="Optimal N (Early)",
        line=dict(color="green", width=1, dash="dash")
    ))
    
    fig.add_trace(go.Scatter(
        x=[data["days"][0], data["days"][-1]],
        y=[1.5, 1.5],
        mode="lines",
        name="Optimal N (Late)",
        line=dict(color="orange", width=1, dash="dash")
    ))
    
    # Add growth stage regions
    fig.add_vrect(
        x0=80, x1=150,
        fillcolor="rgba(144, 238, 144, 0.3)",
        layer="below", line_width=0,
        annotation_text="Early Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=150, x1=250,
        fillcolor="rgba(60, 179, 113, 0.2)",
        layer="below", line_width=0,
        annotation_text="Grand Growth",
        annotation_position="top left"
    )
    
    fig.add_vrect(
        x0=250, x1=330,
        fillcolor="rgba(46, 139, 87, 0.2)",
        layer="below", line_width=0,
        annotation_text="Maturation",
        annotation_position="top left"
    )
    
    # Update layout
    fig.update_layout(
        title="Leaf Nitrogen Content Throughout Growing Season",
        xaxis_title="Days After Harvest (DAH)",
        yaxis_title="Leaf Nitrogen Content (%)",
        legend_title="Measurements",
        height=500
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
    
    # Interactive management recommendation
    st.subheader("Nitrogen Management Recommendations")
    
    # Create a selection slider for specific days
    selected_day = st.slider(
        "Select a specific day after harvest for nitrogen management recommendations",
        min_value=data["days"][0],
        max_value=data["days"][-1],
        value=data["days"][2],
        step=10
    )
    
    # Find the closest day in our data
    closest_idx = np.argmin(np.abs(np.array(data["days"]) - selected_day))
    n_content = data["nitrogen_values"][closest_idx]
    
    # Determine recommendation based on growth stage and N content
    if selected_day < 150:
        optimal_n = 2.0
        if n_content > optimal_n + 0.2:
            recommendation = "Nitrogen levels are above optimal for this growth stage. Consider reducing fertilizer application in future cycles. Monitor for excessive vegetative growth."
            status = "High"
            color = "orange"
        elif n_content < optimal_n - 0.2:
            recommendation = "Nitrogen levels are below optimal for early growth. Consider supplemental nitrogen application to support vegetative growth and tillering."
            status = "Low"
            color = "red"
        else:
            recommendation = "Nitrogen levels are within optimal range for early growth stage. Continue with standard management practices."
            status = "Optimal"
            color = "green"
    elif selected_day < 250:
        optimal_n = 1.8
        if n_content > optimal_n + 0.2:
            recommendation = "Nitrogen levels are slightly high for mid-growth stage. No immediate action needed, but monitor crop development."
            status = "Slightly High"
            color = "yellowgreen"
        elif n_content < optimal_n - 0.2:
            recommendation = "Nitrogen levels are below optimal for grand growth phase. Consider a light supplemental application if canopy is not fully developed."
            status = "Low"
            color = "orange"
        else:
            recommendation = "Nitrogen levels are within optimal range for grand growth stage. Continue with standard management practices."
            status = "Optimal"
            color = "green"
    else:
        optimal_n = 1.5
        if n_content > optimal_n + 0.2:
            recommendation = "Nitrogen levels are higher than desired for maturation stage. This may delay ripening and reduce sugar content. Consider adjusting pre-harvest management."
            status = "High"
            color = "orange"
        elif n_content < optimal_n - 0.2:
            recommendation = "Nitrogen levels are low, which is favorable for ripening. No nitrogen application recommended at this late stage."
            status = "Low (Favorable)"
            color = "green"
        else:
            recommendation = "Nitrogen levels are within optimal range for maturation. Focus on ripening management for optimal sugar content."
            status = "Optimal"
            color = "green"
    
    # Display recommendation
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric(
            label="Current N Status",
            value=f"{n_content:.2f}%",
            delta=f"{n_content - optimal_n:.2f}" if abs(n_content - optimal_n) > 0.05 else None,
            delta_color="inverse"
        )
        st.info(f"Status: **{status}**")
        
    with col2:
        st.markdown(f"""
        #### Management Recommendation at {selected_day} DAH:
        
        <div style="color:{color}; font-weight:bold;">{recommendation}</div>
        """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    ### Growth Stage Advisor
    
    Use the slider below to select the current growth stage of your sugarcane crop. 
    The advisor will recommend the most appropriate UAV technology and survey parameters 
    based on the research findings.
    """)
    
    # Create a slider for days after harvest
    days_after_harvest = st.slider(
        "Select Days After Harvest (DAH)",
        min_value=100,
        max_value=310,
        value=180,
        step=10
    )
    
    # Determine the growth stage
    if days_after_harvest < 150:
        growth_stage = "Early Growth Stage"
        stage_desc = "Tillering and initial stem elongation. Crop height typically 0.5-1.5m."
        color = "lightgreen"
    elif days_after_harvest < 250:
        growth_stage = "Grand Growth Stage"
        stage_desc = "Rapid growth with maximum stem elongation. Crop height typically 1.5-3.0m."
        color = "green"
    else:
        growth_stage = "Maturation Stage"
        stage_desc = "Sugar accumulation and ripening. Limited height increase, focus on sucrose content."
        color = "darkgreen"
    
    # Display growth stage
    st.markdown(f"""
    ## <span style="color:{color}">Current Stage: {growth_stage}</span>
    
    **({days_after_harvest} DAH)**
    
    {stage_desc}
    """, unsafe_allow_html=True)
    
    # Create technology recommendation based on growth stage
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Recommended Technology")
        
        # Determine recommendations based on growth stage
        if days_after_harvest < 150:
            primary_tech = "Multispectral Imaging"
            secondary_tech = "LiDAR (optional)"
            key_indices = "NDVI, NDRE, GNDVI"
            flight_altitude = "100m AGL"
            flight_frequency = "Every 3-4 weeks"
            
            # Create gauges to show relative effectiveness
            ms_effectiveness = 85
            lidar_effectiveness = 45
        elif days_after_harvest < 250:
            primary_tech = "Multispectral + LiDAR"
            secondary_tech = "Multispectral only (if budget constrained)"
            key_indices = "NDRE, Canopy Height, Volume"
            flight_altitude = "100m AGL"
            flight_frequency = "Every 4-6 weeks"
            
            # Create gauges to show relative effectiveness
            ms_effectiveness = 65
            lidar_effectiveness = 75
        else:
            primary_tech = "LiDAR"
            secondary_tech = "Multispectral (for nitrogen only)"
            key_indices = "Canopy Height, Volume, Density"
            flight_altitude = "120m AGL"
            flight_frequency = "Every 3-4 weeks"
            
            # Create gauges to show relative effectiveness
            ms_effectiveness = 45
            lidar_effectiveness = 85
        
        # Display recommendations
        st.markdown(f"""
        **Primary Technology:** {primary_tech}
        
        **Alternative Approach:** {secondary_tech}
        
        **Key Metrics to Collect:** {key_indices}
        
        **Recommended Flight Parameters:**
        - Altitude: {flight_altitude}
        - Frequency: {flight_frequency}
        """)
        
        # Create gauges to show relative effectiveness
        col1a, col1b = st.columns(2)
        
        with col1a:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = ms_effectiveness,
                title = {'text': "Multispectral"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "green"},
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    },
                    'steps': [
                        {'range': [0, 30], 'color': "lightgray"},
                        {'range': [30, 70], 'color': "gray"},
                        {'range': [70, 100], 'color': "darkgray"}
                    ]
                }
            ))
            fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10))
            st.plotly_chart(fig, use_container_width=True)
            
        with col1b:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = lidar_effectiveness,
                title = {'text': "LiDAR"},
                gauge = {
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "blue"},
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    },
                    'steps': [
                        {'range': [0, 30], 'color': "lightgray"},
                        {'range': [30, 70], 'color': "gray"},
                        {'range': [70, 100], 'color': "darkgray"}
                    ]
                }
            ))
            fig.update_layout(height=200, margin=dict(l=10, r=10, t=50, b=10))
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Management Focus Areas")
        
        # Determine management focus based on growth stage
        if days_after_harvest < 150:
            management_areas = [
                {"area": "Nitrogen Management", "priority": "High", "description": "Ensure adequate nitrogen for canopy development. Use NDRE index to guide variable rate application."},
                {"area": "Gap Detection", "priority": "High", "description": "Identify areas with poor emergence for potential replanting."},
                {"area": "Weed Management", "priority": "Medium", "description": "Detect weed pressure while crop canopy is still developing."},
                {"area": "Water Management", "priority": "Medium", "description": "Monitor for water stress to support vegetative growth."}
            ]
        elif days_after_harvest < 250:
            management_areas = [
                {"area": "Water Management", "priority": "High", "description": "Critical to maintain optimal moisture during grand growth phase."},
                {"area": "Biomass Monitoring", "priority": "High", "description": "Track growth rate to predict yield and identify underperforming areas."},
                {"area": "Nitrogen Status", "priority": "Medium", "description": "Ensure adequate but not excessive N levels for optimal growth."},
                {"area": "Pest & Disease", "priority": "Medium", "description": "Scan for hotspots of pest activity or disease outbreak."}
            ]
        else:
            management_areas = [
                {"area": "Ripening Assessment", "priority": "High", "description": "Monitor maturation to determine optimal harvest timing."},
                {"area": "Yield Prediction", "priority": "High", "description": "Generate accurate yield maps for harvest planning and logistics."},
                {"area": "Lodging Detection", "priority": "Medium", "description": "Identify areas with fallen cane that may require special harvest techniques."},
                {"area": "Nitrogen Status", "priority": "Low", "description": "Low N is favorable for ripening; ensure levels are declining appropriately."}
            ]
        
        # Display management areas as an expandable table
        for area in management_areas:
            priority_color = {"High": "red", "Medium": "orange", "Low": "blue"}[area["priority"]]
            with st.expander(f"{area['area']} - Priority: {area['priority']}"):
                st.markdown(f"""
                <div style="border-left: 5px solid {priority_color}; padding-left: 10px;">
                {area["description"]}
                </div>
                """, unsafe_allow_html=True)
    
    # Add a calendar view for recommended survey schedule
    st.subheader("Recommended Survey Schedule")
    
    # Create a calendar-style visualization
    today = datetime.now()
    harvest_date = today - timedelta(days=days_after_harvest)
    
    # Generate survey dates based on current stage
    if days_after_harvest < 150:
        interval = 21  # 3 weeks
    elif days_after_harvest < 250:
        interval = 35  # 5 weeks
    else:
        interval = 21  # 3 weeks
    
    # Generate next 4 recommended survey dates
    survey_dates = []
    last_survey = today
    for i in range(4):
        next_survey = last_survey + timedelta(days=interval)
        survey_dates.append(next_survey)
        last_survey = next_survey
    
    # Create a calendar-like visualization
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    # Group dates by month
    calendar_data = {}
    for date in [today] + survey_dates:
        month = months[date.month-1]
        if month not in calendar_data:
            calendar_data[month] = []
        calendar_data[month].append(date.day)
    
    # Display as a simple calendar
    col1, col2, col3, col4 = st.columns(4)
    cols = [col1, col2, col3, col4]
    
    for i, (month, days) in enumerate(calendar_data.items()):
        if i < 4:  # Limit to 4 columns
            with cols[i]:
                st.markdown(f"### {month}")
                for day in days:
                    if i == 0 and day == today.day:
                        st.markdown(f"**{day}** - TODAY")
                    else:
                        st.markdown(f"**{day}** - Survey")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
