import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Precision Agriculture - UAV Technologies",
    page_icon="🌱",
    layout="wide"
)

# Main content
st.title("Precision Agriculture")
st.subheader("Revolutionizing Sugarcane Farming with Technology")

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("""
    ## What is Precision Agriculture?
    
    Precision agriculture is a farming management concept that uses digital techniques to monitor 
    and optimize agricultural production processes. Rather than applying the same amount of 
    fertilizers and other inputs across entire fields, farmers can use variable rate technology 
    to apply inputs only where and when they are needed.
    
    ### Core Principles:
    
    1. **Right Place**: Apply resources exactly where they are needed
    2. **Right Time**: Intervene at the optimal moment for maximum effectiveness
    3. **Right Amount**: Use precisely the amount of resources required, no more and no less
    4. **Right Method**: Select the most effective application technique
    
    ## Why is it Important for Sugarcane?
    
    Sugarcane is one of the world's most important crops, providing about 80% of the global sugar 
    production. It's also used for biofuel production and various by-products.
    
    Precision agriculture is particularly valuable for sugarcane farming because:
    
    - **Resource Efficiency**: Sugarcane is a resource-intensive crop that benefits from optimized 
      input application
    - **Field Variability**: Sugarcane fields often have significant variability in soil conditions 
      and topography
    - **Extended Growth Cycle**: With a typical growth cycle of 12-18 months, timely interventions 
      are critical
    - **High Value**: The economic value justifies investment in advanced technologies
    - **Sustainability Goals**: Helps meet increasing demands for sustainable farming practices
    """)

with col2:
    st.image("https://plus.unsplash.com/premium_photo-1661872779637-b6e14433dfc1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
             caption="Precision agriculture enables data-driven farming decisions",
             use_container_width=True)
    
    st.image("https://images.unsplash.com/photo-1549507803-6c47d24c46f7?q=80&w=2080&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
             caption="Sugarcane fields benefit from precision management",
             use_container_width=True)

# Additional information
st.markdown("""
## The Evolution of Precision Agriculture

### Traditional Farming
Historically, farmers treated fields uniformly, applying the same amount of seed, fertilizer, and 
pesticides across entire fields regardless of variations in soil type, fertility, or pest pressure.

### Modern Precision Agriculture
Today's precision agriculture uses various technologies to collect and analyze data about field 
variability, allowing for targeted management decisions:

- **Soil Sampling and Mapping**: Identifies variations in soil properties
- **Yield Monitoring**: Measures crop yield variations across fields
- **Remote Sensing**: Uses satellite or drone imagery to assess crop health
- **Variable Rate Technology**: Applies inputs at variable rates based on field conditions
- **GPS Guidance Systems**: Enables accurate field navigation and reduces overlap
- **Farm Management Software**: Integrates data for informed decision-making

## Benefits for Sugarcane Farmers

- **Increased Yield**: Typically 5-10% yield improvements
- **Reduced Input Costs**: 10-20% savings on fertilizers and pesticides
- **Improved Quality**: More uniform crop quality
- **Environmental Benefits**: Reduced chemical runoff and greenhouse gas emissions
- **Better Record-Keeping**: Enhanced traceability and compliance with regulations
- **Informed Decision-Making**: Data-driven approach reduces guesswork
""")

# Call to action
st.info("In the next sections, we'll explore how UAVs, LiDAR, and multispectral imaging are transforming precision agriculture for sugarcane farming.")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
