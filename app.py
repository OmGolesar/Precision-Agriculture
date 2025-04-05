import streamlit as st

# App configuration
st.set_page_config(
    page_title="Precision Agriculture with UAV Technology",
    page_icon="🚁",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title and description
st.title("Precision Agriculture with UAV Technology")
st.subheader("Understanding UAV, LiDAR and Multispectral Imaging for Sugarcane Farming")

# Introduction
st.markdown("""
Welcome to this educational resource on precision agriculture technologies for sugarcane farming.
            
This application aims to educate users about how Unmanned Aerial Vehicles (UAVs) equipped with LiDAR 
and multispectral imaging technologies can revolutionize sugarcane farming through precise biomass 
and leaf nitrogen level predictions.

### Navigation
Use the sidebar to explore different sections of the application:

1. **Precision Agriculture** - Introduction to precision agriculture concepts and benefits
2. **UAV Technology** - Understanding drone technology in agriculture
3. **LiDAR Technology** - How light detection and ranging works for crop monitoring
4. **Multispectral Imaging** - Using multiple light bands to assess crop health
5. **Research Study** - Summary of research methods and findings
6. **Interactive Visualizations** - Explore data through interactive graphs
7. **Practical Applications** - Real-world usage of these technologies
8. **Glossary** - Definitions of technical terms

Let's begin our journey into the future of sugarcane farming!
""")

# Display sugarcane field image
st.image(
    "https://images.unsplash.com/photo-1585155113372-6c1808141bf3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
    caption="Sugarcane fields (representative image)",
    use_container_width=True  # Updated parameter
)

# Brief summary
st.markdown("""
### Key Benefits of Precision Agriculture in Sugarcane Farming

- **Increased Efficiency**: Optimize resource usage including water, fertilizers, and pesticides
- **Higher Yields**: Improve crop productivity through targeted interventions
- **Reduced Environmental Impact**: Minimize chemical usage and runoff
- **Data-Driven Decisions**: Make informed farming decisions based on accurate field data
- **Early Problem Detection**: Identify issues before they become visible to the naked eye

Explore each section to learn more about these revolutionary technologies!
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
