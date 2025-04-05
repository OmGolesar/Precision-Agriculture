import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Practical Applications - UAV Technologies",
    page_icon="🚜",
    layout="wide"
)

# Main content
st.title("Practical Applications")
st.subheader("Real-World Implementation of UAV Technologies in Sugarcane Farming")

# Introduction
st.markdown("""
Translating research findings into practical applications is essential for maximizing the benefits of UAV technology 
in sugarcane farming. This section explores how farmers can implement these technologies in their day-to-day operations 
and what benefits they can expect.
""")

# Add a showcase of practical applications
st.markdown("## Key Applications in Commercial Sugarcane Farming")

# Create three columns for different applications
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Fertilization Management")
    
    # Create an SVG icon using Font Awesome
    st.markdown("""
    <div style="text-align: center; font-size: 50px; color: #4CAF50;">
        <i class="fas fa-seedling"></i>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    #### Technology Used
    - **Primary**: Multispectral imaging
    - **Key Metrics**: NDRE, GNDVI, Chlorophyll maps
    
    #### Implementation Steps
    1. Conduct UAV surveys with multispectral camera
    2. Generate nitrogen prediction maps
    3. Create variable rate application maps
    4. Upload to fertilizer spreader equipment
    5. Apply nitrogen at variable rates
    
    #### Expected Benefits
    - 10-20% reduction in fertilizer usage
    - Improved nitrogen use efficiency
    - More uniform crop development
    - Reduced environmental impact
    """)

with col2:
    st.markdown("### Yield Prediction & Harvest Planning")
    
    # Create an SVG icon using Font Awesome
    st.markdown("""
    <div style="text-align: center; font-size: 50px; color: #4CAF50;">
        <i class="fas fa-chart-line"></i>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    #### Technology Used
    - **Primary**: LiDAR + Multispectral
    - **Key Metrics**: Biomass maps, Plant height, NDVI
    
    #### Implementation Steps
    1. Conduct surveys 2-3 months before harvest
    2. Generate yield prediction maps
    3. Identify high/low-yielding zones
    4. Plan harvest logistics accordingly
    5. Prioritize fields based on predicted maturity
    
    #### Expected Benefits
    - 5-10% improvement in harvest efficiency
    - Better allocation of transport resources
    - Optimized mill supply chain
    - Improved harvest timing decisions
    """)

with col3:
    st.markdown("### Irrigation Management")
    
    # Create an SVG icon using Font Awesome
    st.markdown("""
    <div style="text-align: center; font-size: 50px; color: #4CAF50;">
        <i class="fas fa-tint"></i>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    #### Technology Used
    - **Primary**: Multispectral imaging
    - **Key Metrics**: NDWI, Thermal imagery, Evapotranspiration maps
    
    #### Implementation Steps
    1. Regular UAV surveys during dry periods
    2. Create water stress maps
    3. Identify areas of over/under-irrigation
    4. Adjust irrigation scheduling and volume
    5. Monitor crop response with follow-up surveys
    
    #### Expected Benefits
    - 15-30% water conservation
    - Reduced energy costs for pumping
    - Prevention of yield loss from water stress
    - Early detection of irrigation system issues
    """)

# ROI Calculator
st.markdown("## Return on Investment Calculator")
st.markdown("""
Use this calculator to estimate the potential return on investment for implementing UAV technologies in your sugarcane farming operation.
Adjust the sliders to match your specific farming conditions.
""")

# Create two columns
col1, col2 = st.columns([2, 3])

with col1:
    # Input parameters
    st.markdown("### Farm Parameters")
    
    farm_size = st.slider("Farm Size (hectares)", 50, 2000, 500)
    avg_yield = st.slider("Average Yield (tons/hectare)", 50, 150, 80)
    sugarcane_price = st.slider("Sugarcane Price (₹/ton)", 20, 60, 30)
    fertilizer_cost = st.slider("Fertilizer Cost (₹/hectare/year)", 100, 600, 300)
    irrigation_cost = st.slider("Irrigation Cost (₹/hectare/year)", 100, 800, 400)
    
    # Technology adoption options
    st.markdown("### Technology Options")
    
    technology_choice = st.radio(
        "Select Technology Adoption Approach",
        ["Service Provider (Pay per Survey)", "Equipment Purchase (Own UAV & Sensors)"]
    )
    
    if technology_choice == "Service Provider (Pay per Survey)":
        survey_cost = st.slider("Survey Cost (₹/hectare)", 5, 30, 15)
        surveys_per_year = st.slider("Number of Surveys per Year", 2, 12, 6)
        annual_cost = farm_size * survey_cost * surveys_per_year
        implementation_cost = st.slider("Initial Implementation Cost (₹)", 5000, 20000, 10000)
        total_cost = annual_cost + implementation_cost
    else:
        equipment_cost = st.slider("Equipment Cost (₹\)", 20000, 100000, 50000)
        annual_maintenance = st.slider("Annual Maintenance & Operation (₹)", 5000, 25000, 10000)
        equipment_lifespan = st.slider("Equipment Lifespan (years)", 3, 8, 5)
        amortized_cost = equipment_cost / equipment_lifespan
        total_cost = amortized_cost + annual_maintenance

with col2:
    # Calculate benefits
    st.markdown("### Expected Benefits")
    
    # Expected improvement percentages
    fertilizer_reduction = st.slider("Expected Fertilizer Reduction (%)", 5, 30, 15)
    yield_improvement = st.slider("Expected Yield Improvement (%)", 2, 15, 5)
    irrigation_reduction = st.slider("Expected Irrigation Cost Reduction (%)", 5, 30, 10)
    
    # Calculate financial benefits
    fertilizer_savings = (fertilizer_cost * farm_size * fertilizer_reduction / 100)
    yield_benefit = (avg_yield * farm_size * yield_improvement / 100 * sugarcane_price)
    irrigation_savings = (irrigation_cost * farm_size * irrigation_reduction / 100)
    
    total_benefit = fertilizer_savings + yield_benefit + irrigation_savings
    net_benefit = total_benefit - total_cost
    roi_percent = (net_benefit / total_cost) * 100 if total_cost > 0 else 0
    
    # Display results
    st.markdown("### ROI Analysis")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Annual Benefit", f"₹{total_benefit:,.2f}")
        
    with col2:
        st.metric("Annual Cost", f"₹{total_cost:,.2f}")
        
    with col3:
        st.metric("Net Benefit", f"₹{net_benefit:,.2f}", delta=f"{roi_percent:.1f}% ROI")
    
    # Create a breakdown of benefits
    labels = ['Fertilizer Savings', 'Yield Improvement', 'Irrigation Savings']
    values = [fertilizer_savings, yield_benefit, irrigation_savings]
    colors = ['green', 'gold', 'blue']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=.4,
        marker_colors=colors
    )])
    
    fig.update_layout(
        title="Breakdown of Financial Benefits",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add interpretation
    if roi_percent > 50:
        st.success(f"""
        **Strong ROI**: With an estimated ROI of {roi_percent:.1f}%, implementing UAV technology appears to be 
        highly beneficial for your operation. The investment is likely to pay for itself within {100/roi_percent:.1f} years.
        """)
    elif roi_percent > 0:
        st.info(f"""
        **Positive ROI**: With an estimated ROI of {roi_percent:.1f}%, implementing UAV technology shows promise. 
        Consider starting with a smaller implementation to validate the benefits before scaling up.
        """)
    else:
        st.warning(f"""
        **Negative ROI**: The current parameters result in a negative ROI of {roi_percent:.1f}%. 
        Consider adjusting your approach, such as using a service provider instead of purchasing equipment, 
        or focusing on the applications that provide the highest value for your specific operation.
        """)

# Implementation Roadmap
st.markdown("## Implementation Roadmap")
st.markdown("""
Implementing UAV technology in sugarcane farming requires a systematic approach. The following roadmap 
provides a step-by-step guide to successful adoption.
""")

# Create an expandable section for each implementation step
implementation_steps = [
    {
        "title": "1. Assessment & Planning (1-2 months)",
        "content": """
        - Evaluate farm characteristics and specific challenges
        - Identify key applications that address your highest-priority needs
        - Research technology options (service providers vs. equipment purchase)
        - Define success metrics and establish baseline data
        - Create a budget and implementation timeline
        """
    },
    {
        "title": "2. Initial Technology Deployment (2-3 months)",
        "content": """
        - Select technology provider or purchase equipment
        - Receive training on equipment operation or data interpretation
        - Conduct initial surveys to establish baseline maps
        - Set up data storage and management systems
        - Integrate with existing farm management software if applicable
        """
    },
    {
        "title": "3. Small-Scale Validation (3-6 months)",
        "content": """
        - Implement technology on a subset of fields (10-20%)
        - Create treatment zones with and without UAV-guided management
        - Collect ground-truth data to validate UAV measurements
        - Calculate initial ROI on test fields
        - Adjust protocols based on early results
        """
    },
    {
        "title": "4. Full Implementation (6-12 months)",
        "content": """
        - Scale to full farm implementation based on validation results
        - Establish regular survey schedules aligned with crop growth stages
        - Develop standard operating procedures for data collection and analysis
        - Train additional staff on data interpretation and application
        - Set up automated reporting and decision support systems
        """
    },
    {
        "title": "5. Continuous Improvement (Ongoing)",
        "content": """
        - Regularly evaluate technology performance against success metrics
        - Stay informed about new sensor technologies and analysis methods
        - Refine prediction models with accumulated historical data
        - Expand applications to additional aspects of farm management
        - Share experiences and collaborate with other growers
        """
    }
]

# Display implementation steps as expandable sections
for step in implementation_steps:
    with st.expander(step["title"]):
        st.markdown(step["content"])

# Case Studies
st.markdown("## Case Studies")
st.markdown("""
The following case studies demonstrate successful implementations of UAV technology in commercial sugarcane operations 
around the world.
""")

# Create tabs for different case studies
tab1, tab2, tab3 = st.tabs(["Large-Scale Brazil Operation", "Australian Cooperative", "Small-Scale Thailand Farm"])

with tab1:
    st.markdown("### UAV-Guided Variable Rate Fertilization in Brazil")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        #### Farm Profile
        - **Location**: São Paulo State, Brazil
        - **Size**: 12,000 hectares
        - **Challenge**: Optimize nitrogen application across diverse soil conditions
        
        #### Approach
        The operation implemented multispectral UAV surveys on a monthly basis during the grand growth phase. 
        NDRE index maps were created and used to generate variable rate fertilizer application maps.
        
        #### Technology Used
        - Fixed-wing UAV with multispectral camera
        - Variable rate fertilizer equipment
        - Farm management software for data integration
        
        #### Results After Two Years
        - 18% reduction in nitrogen fertilizer use
        - 7% increase in average yield
        - More uniform crop development
        - ₹420,000 annual net benefit after technology costs
        - Full ROI achieved in 14 months
        """)
        
    with col2:
        # Create a simple bar chart showing results
        categories = ['Fertilizer Use', 'Yield', 'Operating Cost', 'Net Profit']
        before = [100, 100, 100, 100]
        after = [82, 107, 93, 114]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=categories,
            y=before,
            name='Before UAV Technology',
            marker_color='lightgrey'
        ))
        
        fig.add_trace(go.Bar(
            x=categories,
            y=after,
            name='After UAV Technology',
            marker_color='green'
        ))
        
        fig.update_layout(
            title="Performance Relative to Baseline (100%)",
            barmode='group',
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("### Cooperative UAV Service Model in Queensland, Australia")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        #### Cooperative Profile
        - **Location**: Queensland, Australia
        - **Members**: 35 farms (average size: 200 hectares)
        - **Challenge**: Make advanced technology accessible to medium-sized growers
        
        #### Approach
        Instead of individual investments, the cooperative purchased UAV equipment and trained dedicated operators. 
        Surveys were conducted on a rotating schedule, with data analysis and recommendations provided as a service 
        to members.
        
        #### Technology Used
        - Multirotor UAV with combined LiDAR and multispectral sensors
        - Centralized data processing system
        - Mobile app for farmers to request surveys and view results
        
        #### Results After Three Years
        - 75% cost reduction compared to individual technology adoption
        - 300+ successful surveys completed
        - 9% average yield improvement across member farms
        - Standardized data collection allowing regional benchmarking
        - Successful technology transfer to smaller operations
        """)
        
    with col2:
        # Create a line chart showing adoption rate
        years = [2019, 2020, 2021, 2022, 2023]
        adoption_rate = [15, 40, 65, 85, 95]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=years,
            y=adoption_rate,
            mode='lines+markers',
            name='Member Adoption Rate (%)',
            line=dict(color='green', width=3)
        ))
        
        fig.update_layout(
            title="Cooperative Member Adoption Rate",
            xaxis_title="Year",
            yaxis_title="Farms Using UAV Technology (%)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("### Small-Scale Implementation in Thailand")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        #### Farm Profile
        - **Location**: Khon Kaen Province, Thailand
        - **Size**: 50 hectares
        - **Challenge**: Maximize efficiency with limited resources
        
        #### Approach
        This small farm utilized a third-party UAV service provider for quarterly surveys. 
        Focus was placed on disease detection and irrigation optimization, addressing the two 
        most critical challenges for the operation.
        
        #### Technology Used
        - Contract UAV service (no equipment purchase)
        - Free mobile apps for basic data visualization
        - Simple paper maps for field implementation
        
        #### Results After One Year
        - Early detection of fungal disease saved 4 hectares from significant yield loss
        - 22% reduction in irrigation water usage
        - 4% overall yield improvement
        - ₹4,200 net benefit after service costs
        - Simple implementation requiring minimal technical expertise
        """)
        
    with col2:
        # Create a simple ROI chart
        months = list(range(1, 13))
        costs = [1500] + [0] * 11
        cumulative_costs = np.cumsum(costs)
        
        # Calculate monthly benefits (increasing over time)
        monthly_benefits = [0, 0, 400, 400, 500, 500, 600, 600, 700, 700, 800, 1000]
        cumulative_benefits = np.cumsum(monthly_benefits)
        
        # Calculate net position
        net_position = cumulative_benefits - cumulative_costs
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=months,
            y=cumulative_costs,
            mode='lines',
            name='Cumulative Costs',
            line=dict(color='red')
        ))
        
        fig.add_trace(go.Scatter(
            x=months,
            y=cumulative_benefits,
            mode='lines',
            name='Cumulative Benefits',
            line=dict(color='green')
        ))
        
        fig.add_trace(go.Scatter(
            x=months,
            y=net_position,
            mode='lines',
            name='Net Position',
            line=dict(color='blue')
        ))
        
        fig.add_shape(
            type="line",
            x0=1, y0=0,
            x1=12, y1=0,
            line=dict(color="black", dash="dash")
        )
        
        # Add break-even point annotation
        breakeven_month = 9  # Approximate based on the data
        fig.add_annotation(
            x=breakeven_month,
            y=200,
            text="Break Even",
            showarrow=True,
            arrowhead=1
        )
        
        fig.update_layout(
            title="Small Farm ROI Timeline",
            xaxis_title="Month",
            yaxis_title="Value (₹)",
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Challenges and Solutions
st.markdown("## Common Challenges and Solutions")

# Create a dataframe for challenges and solutions
challenges_data = {
    "Challenge": [
        "High initial technology cost",
        "Technical expertise requirements",
        "Weather dependencies for surveys",
        "Data processing complexity",
        "Integration with existing practices",
        "Regulatory compliance for UAV operation"
    ],
    "Solution": [
        "Utilize third-party service providers or form cooperatives for shared equipment ownership",
        "Partner with consultants or universities for training; use simplified data interpretation tools",
        "Schedule flexible survey windows; combine with satellite imagery for continuous monitoring",
        "Use cloud-based processing services with pre-configured analysis workflows",
        "Start with simple applications; gradually expand as comfort level increases",
        "Work with licensed operators; stay informed about local UAV regulations"
    ]
}

# Convert to DataFrame and display as a table
challenges_df = pd.DataFrame(challenges_data)
st.table(challenges_df)

# Future Trends
st.markdown("## Future Trends in UAV Technology for Sugarcane")

# Create three columns for future trends
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Automated Survey Systems")
    st.markdown("""
    - **Docking stations** for autonomous recharging
    - **Pre-programmed flight paths** triggered by weather conditions
    - **Edge computing** for real-time data processing
    - **Regulatory frameworks** for beyond visual line of sight operation
    """)
    
    st.image("https://assets.grok.com/users/a06ca20a-97de-4d76-90d8-39fb0f0183fd/generated/m66V7X7zl2IZXxTU/image.jpg", 
             caption="Next-generation automated UAV systems",
             use_container_width=True)

with col2:
    st.markdown("### Advanced Sensor Integration")
    st.markdown("""
    - **Hyperspectral imaging** for more detailed crop analysis
    - **Miniaturized LiDAR** with higher resolution and lower cost
    - **Real-time gas sensors** for photosynthesis and respiration monitoring
    - **Integrated sensor packages** combining multiple technologies
    """)
    
    st.image("https://assets.grok.com/users/a06ca20a-97de-4d76-90d8-39fb0f0183fd/generated/marFVgkccqzoYrV4/image.jpg", 
             caption="Multi-sensor integration on advanced UAVs",
             use_container_width=True)

with col3:
    st.markdown("### AI and Machine Learning")
    st.markdown("""
    - **Automated crop stress detection** algorithms
    - **Predictive analytics** for disease outbreak risks
    - **Digital twin technology** for simulating management scenarios
    - **Computer vision** for individual plant monitoring
    """)
    
    st.image("https://assets.grok.com/users/a06ca20a-97de-4d76-90d8-39fb0f0183fd/generated/m4Jo8ftlLaelVKfM/image.jpg", 
             caption="AI-powered analytics for agricultural data",
             use_container_width=True)

# Conclusive call to action
st.markdown("## Getting Started with UAV Technology")
st.markdown("""
Ready to explore how UAV technology can benefit your sugarcane operation? Here are some recommended next steps:
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### For Immediate Implementation
    
    1. **Contact UAV service providers** in your region for demonstration surveys
    2. **Identify 1-2 specific applications** that address your most pressing challenges
    3. **Start with a small pilot project** on a portion of your farm
    4. **Establish clear success metrics** to evaluate the technology's impact
    5. **Connect with other growers** who have implemented similar technologies
    """)

with col2:
    st.markdown("""
    ### For Technology Evaluation
    
    1. **Attend agricultural technology trade shows** and demonstrations
    2. **Request case studies** from technology providers specific to sugarcane
    3. **Consult with agricultural extension services** about available resources
    4. **Explore government incentives** for technology adoption in agriculture
    5. **Consider joining a cooperative** for shared technology access
    """)

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
