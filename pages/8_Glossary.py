import streamlit as st
from utils import create_term_definition

# Page configuration
st.set_page_config(
    page_title="Glossary - UAV Technologies",
    page_icon="📚",
    layout="wide"
)

# Main content
st.title("Glossary of Terms")
st.subheader("Key Terminology for Precision Agriculture in Sugarcane Farming")

# Introduction text
st.markdown("""
This glossary provides definitions for technical terms used throughout this educational application. 
Click on any term to expand its definition.
""")

# Filter functionality
st.markdown("### Filter Terms")
filter_categories = ["All", "UAV Technology", "Remote Sensing", "Agriculture", "Data Analysis"]
selected_category = st.radio("Select a category", filter_categories, horizontal=True)

# Search functionality
search_term = st.text_input("Search for a term", "")

# Create the glossary dictionary
glossary_terms = {
    # UAV Technology terms
    "UAV": {
        "category": "UAV Technology",
        "definition": """
        **UAV (Unmanned Aerial Vehicle)** refers to an aircraft that operates without a human pilot on board. 
        Also commonly known as drones, UAVs can be remotely controlled by a pilot on the ground or fly autonomously 
        based on pre-programmed flight plans. In precision agriculture, UAVs are used to collect aerial imagery and 
        data for crop monitoring and analysis.
        
        **Key characteristics in agricultural applications:**
        - Flight time: Typically 20-60 minutes depending on payload and type
        - Altitude: Usually operated at 50-120 meters above ground level for agricultural surveys
        - Payload capacity: From a few hundred grams to several kilograms
        - Types: Multirotor (versatile but shorter flight time) or fixed-wing (longer range but requires space for takeoff/landing)
        """
    },
    "Multirotor": {
        "category": "UAV Technology",
        "definition": """
        **Multirotor** is a type of UAV with multiple rotors (typically 4, 6, or 8) that provide lift and control. 
        Common configurations include quadcopters (4 rotors), hexacopters (6 rotors), and octocopters (8 rotors).
        
        **Advantages for agricultural use:**
        - Vertical takeoff and landing capability
        - Ability to hover in place for detailed imaging
        - Precise control for low-altitude flights
        - Simpler to operate for beginners
        
        **Limitations:**
        - Shorter flight time (typically 20-30 minutes)
        - Smaller coverage area per flight
        - More susceptible to wind compared to fixed-wing UAVs
        """
    },
    "Fixed-wing UAV": {
        "category": "UAV Technology",
        "definition": """
        **Fixed-wing UAV** is an unmanned aircraft that uses wings for lift (similar to traditional airplanes) rather 
        than vertical lift rotors. These UAVs typically have a single propeller or jet engine for forward thrust.
        
        **Advantages for agricultural use:**
        - Longer flight time (typically 45-90+ minutes)
        - Greater area coverage per flight
        - More energy-efficient
        - Better stability in windy conditions
        
        **Limitations:**
        - Requires space for takeoff and landing
        - Cannot hover in place
        - More complex flight planning
        - Often more expensive than basic multirotor options
        """
    },
    "Ground Control Station": {
        "category": "UAV Technology",
        "definition": """
        **Ground Control Station (GCS)** refers to the hardware and software used by the UAV operator to plan missions, 
        control the aircraft, and monitor telemetry data during flight. The GCS may consist of a laptop, tablet, or 
        dedicated controller with specialized software.
        
        **Key functions in agricultural applications:**
        - Flight planning and waypoint creation
        - Real-time monitoring of UAV position, altitude, and battery status
        - Sensor control and data preview
        - Flight log recording and analysis
        - Fail-safe programming and emergency controls
        """
    },
    "Payload": {
        "category": "UAV Technology",
        "definition": """
        **Payload** refers to the equipment or instruments carried by the UAV to fulfill its mission objectives. 
        In agricultural applications, common payloads include various types of cameras and sensors.
        
        **Common agricultural payloads:**
        - RGB cameras for visual inspection and basic mapping
        - Multispectral cameras for vegetation analysis
        - Thermal cameras for water stress detection
        - LiDAR sensors for 3D mapping and crop structure analysis
        - Hyperspectral sensors for advanced crop analysis
        - Spraying systems for precision application of chemicals
        
        The payload capacity of a UAV is a critical specification, as it determines what sensors can be carried and 
        consequently what data can be collected.
        """
    },
    
    # Remote Sensing terms
    "LiDAR": {
        "category": "Remote Sensing",
        "definition": """
        **LiDAR (Light Detection and Ranging)** is a remote sensing technology that uses laser light to measure 
        distances to objects. It works by emitting rapid laser pulses and measuring the time it takes for each pulse 
        to bounce back after hitting an object.
        
        **In sugarcane farming, LiDAR provides:**
        - Accurate plant height measurements
        - Canopy structure analysis
        - Biomass estimation
        - 3D field topography for water management
        - Plant row detection
        
        LiDAR data is typically represented as a "point cloud" - a three-dimensional set of points that represent 
        the surfaces the laser has measured. Each point contains X, Y, Z coordinates and sometimes additional attributes.
        
        Agricultural LiDAR systems typically operate with near-infrared wavelengths (around 905 nm or 1550 nm) and 
        can collect hundreds of thousands of points per second.
        """
    },
    "Multispectral Imaging": {
        "category": "Remote Sensing",
        "definition": """
        **Multispectral Imaging** is a technology that captures image data at specific wavelengths across the 
        electromagnetic spectrum. Unlike regular cameras that capture only visible light (RGB), multispectral 
        cameras capture additional bands, particularly in the near-infrared range.
        
        **Typical bands in agricultural multispectral cameras:**
        - Blue (450-495 nm)
        - Green (495-570 nm)
        - Red (620-700 nm)
        - Red Edge (700-730 nm)
        - Near-Infrared (NIR, 700-1100 nm)
        
        **In sugarcane farming, multispectral imaging enables:**
        - Vegetation health assessment
        - Nitrogen status estimation
        - Water stress detection
        - Disease and pest monitoring
        - Early growth stage biomass estimation
        
        Multispectral data is often used to calculate various vegetation indices (like NDVI, NDRE, GNDVI) that 
        highlight specific plant characteristics not visible to the human eye.
        """
    },
    "NDVI": {
        "category": "Remote Sensing",
        "definition": """
        **NDVI (Normalized Difference Vegetation Index)** is one of the most common vegetation indices used in 
        remote sensing for vegetation analysis. It is calculated from multispectral imagery using the formula:
        
        NDVI = (NIR - Red) / (NIR + Red)
        
        Where NIR is the near-infrared reflectance and Red is the red reflectance.
        
        **NDVI values range from -1 to +1:**
        - -1 to 0: Non-vegetated surfaces (water, bare soil, buildings)
        - 0.1 to 0.3: Sparse vegetation
        - 0.3 to 0.6: Moderate vegetation
        - 0.6 to 0.9: Dense, healthy vegetation
        
        In sugarcane monitoring, NDVI is used to assess overall crop vigor, track seasonal growth patterns, and 
        identify areas of stress or poor development. However, NDVI tends to saturate in dense canopies, making it 
        less effective for mature sugarcane.
        """
    },
    "NDRE": {
        "category": "Remote Sensing",
        "definition": """
        **NDRE (Normalized Difference Red Edge)** is a vegetation index that utilizes the red edge band, which is 
        highly sensitive to chlorophyll content in plants. It is calculated using the formula:
        
        NDRE = (NIR - Red Edge) / (NIR + Red Edge)
        
        Where NIR is the near-infrared reflectance and Red Edge is the reflectance in the red edge portion of the spectrum.
        
        **Advantages of NDRE for sugarcane monitoring:**
        - Less saturation in dense canopies compared to NDVI
        - Better sensitivity to nitrogen status
        - More effective at later growth stages
        - Stronger correlation with leaf chlorophyll content
        
        NDRE has been shown to be particularly valuable for nitrogen management in sugarcane, as it can detect subtle 
        variations in plant nitrogen status even in well-developed crop canopies.
        """
    },
    "Hyperspectral Imaging": {
        "category": "Remote Sensing",
        "definition": """
        **Hyperspectral Imaging** is an advanced form of spectral imaging that collects and processes information from 
        across the electromagnetic spectrum. While multispectral imaging captures a few specific bands, hyperspectral 
        imaging captures hundreds of narrow, contiguous spectral bands.
        
        **Key characteristics:**
        - Typically captures 100-300+ spectral bands
        - Each band may be only 5-10 nm wide
        - Provides detailed spectral signatures of objects
        - Requires sophisticated processing and analysis
        
        **Applications in sugarcane research:**
        - Detailed biochemical analysis of crops
        - Early disease detection with specific pathogen signatures
        - Advanced nutrient status assessment
        - Water use efficiency studies
        - Varietal identification and classification
        
        While hyperspectral imaging offers more detailed information than multispectral imaging, it is currently less 
        common in commercial agriculture due to higher costs, larger data volumes, and more complex processing requirements.
        """
    },
    "Thermal Imaging": {
        "category": "Remote Sensing",
        "definition": """
        **Thermal Imaging** is a technique that detects infrared radiation (heat) emitted from objects and converts it 
        into a visible image. In the context of UAV-based agriculture, thermal cameras capture the temperature variations 
        in crops and soil.
        
        **Applications in sugarcane farming:**
        - Water stress detection (stressed plants show higher temperatures)
        - Irrigation system evaluation (identifying dry spots or leaks)
        - Early disease detection (some infections alter plant temperature)
        - Equipment maintenance (detecting overheating in farm machinery)
        
        Thermal cameras typically operate in the long-wave infrared range (8-14 μm) and can detect temperature differences 
        as small as 0.05°C. The imagery is often displayed using color palettes where different colors represent different 
        temperatures.
        """
    },
    
    # Agriculture terms
    "Precision Agriculture": {
        "category": "Agriculture",
        "definition": """
        **Precision Agriculture** is a farming management concept that uses information technology and specialized 
        equipment to optimize field-level management with regard to crop farming. It aims to ensure profitability, 
        sustainability, and environmental protection.
        
        **Core principles:**
        - Right place: Apply inputs where they are needed
        - Right time: Take action at the optimal time
        - Right amount: Use precisely what is needed
        - Right manner: Use the most effective methods
        
        **In sugarcane production, precision agriculture enables:**
        - Variable rate application of fertilizers and chemicals
        - Site-specific irrigation management
        - Targeted pest and disease control
        - Optimized harvest timing
        - Detailed record-keeping for analysis and compliance
        
        Precision agriculture relies on various technologies including GPS guidance, sensors, drones, robotics, and 
        software to manage spatial and temporal variability across fields.
        """
    },
    "Biomass": {
        "category": "Agriculture",
        "definition": """
        **Biomass** in the context of sugarcane farming refers to the total mass of living plant material in a given area. 
        It is typically measured in tons per hectare (or tons per acre) and is an important indicator of crop growth 
        and potential yield.
        
        **In sugarcane production:**
        - Above-ground biomass includes stalks, leaves, and tops
        - Stalk biomass is directly related to sugar yield
        - Fresh biomass includes water content
        - Dry biomass refers to the material after removing water content
        
        Remote sensing technologies estimate biomass by measuring plant height (using LiDAR) or analyzing spectral 
        reflectance patterns (using multispectral imaging). For sugarcane, biomass typically ranges from 70-120 tons 
        per hectare of fresh material depending on variety, growing conditions, and management practices.
        """
    },
    "Sugarcane Growth Stages": {
        "category": "Agriculture",
        "definition": """
        **Sugarcane Growth Stages** refer to the distinct phases of development in the sugarcane crop cycle. 
        Understanding these stages is crucial for timing management interventions and interpreting remote sensing data.
        
        **Main growth stages:**
        
        1. **Germination & Establishment (0-90 DAH):**
           - Bud sprouting and initial shoot development
           - Root system establishment
           - Initial tillering (production of multiple shoots)
        
        2. **Grand Growth (90-180 DAH):**
           - Rapid stalk elongation
           - Maximum growth rate period
           - Canopy closure
           - Continued tillering
        
        3. **Maturation (180-270 DAH):**
           - Reduced growth rate
           - Beginning of sugar accumulation
           - Reduction in leaf production
           - Stalk hardening
        
        4. **Ripening (270-360 DAH):**
           - Minimal vegetative growth
           - Maximum sugar accumulation
           - Leaf senescence
           - Preparation for harvest
        
        DAH refers to "Days After Harvest" for ratoon crops (regrowth after harvest) or "Days After Planting" for 
        plant crops (newly planted cane).
        """
    },
    "Nitrogen Management": {
        "category": "Agriculture",
        "definition": """
        **Nitrogen Management** refers to the strategic application and monitoring of nitrogen fertilizers to optimize 
        crop growth while minimizing environmental impact and input costs. Nitrogen is one of the most critical nutrients 
        for sugarcane production.
        
        **In sugarcane farming:**
        - Nitrogen requirements vary by growth stage (higher during grand growth)
        - Typical application rates range from 100-200 kg N/ha depending on soil type and yield potential
        - Excessive N can reduce sugar content and increase lodging risk
        - Insufficient N limits growth and yield potential
        
        **Remote sensing for N management:**
        - Multispectral indices (especially NDRE) correlate with leaf N content
        - Chlorophyll mapping indicates N status
        - Time-series analysis tracks N uptake throughout the season
        
        Variable rate application based on UAV-derived N status maps can improve nitrogen use efficiency by 15-30% 
        in sugarcane production.
        """
    },
    "Ratoon Crop": {
        "category": "Agriculture",
        "definition": """
        **Ratoon Crop** refers to the regrowth of sugarcane from the stubble that remains after harvesting the previous 
        crop. Unlike most other crops that require replanting after each harvest, sugarcane can be ratooned multiple times.
        
        **Key characteristics of ratoon crops:**
        - No need for replanting, which reduces costs and soil disturbance
        - Typically faster initial growth compared to newly planted cane
        - Yield potential generally decreases with successive ratoons
        - Most commercial operations maintain 3-5 ratoons before replanting
        - First ratoon often produces the highest yields
        
        **Management considerations for ratoon crops:**
        - Gap filling may be necessary if stubble damage occurred during harvest
        - Trash management (leaving or removing crop residue) affects ratoon emergence
        - Nutrient requirements differ from plant cane
        - Higher risk of disease accumulation in later ratoons
        
        UAV-based remote sensing is particularly valuable for assessing ratoon vigor and identifying areas that may 
        require replanting due to poor ratoon performance.
        """
    },
    
    # Data Analysis terms
    "Machine Learning": {
        "category": "Data Analysis",
        "definition": """
        **Machine Learning** is a branch of artificial intelligence that focuses on developing systems that can learn 
        from and make decisions based on data. In the context of UAV-based agricultural monitoring, machine learning 
        algorithms are used to analyze remote sensing data and derive actionable insights.
        
        **Common applications in sugarcane remote sensing:**
        - Crop classification and mapping
        - Yield prediction models
        - Disease and pest detection
        - Weed identification
        - Growth stage determination
        
        **Types of machine learning used in agricultural analysis:**
        - **Supervised learning**: Training models on labeled data (e.g., known biomass measurements)
        - **Unsupervised learning**: Finding patterns without labeled data (e.g., clustering similar crop conditions)
        - **Deep learning**: Using neural networks for complex image analysis
        
        These techniques can process the large volumes of data collected by UAVs to identify patterns and relationships 
        that would be difficult or impossible to detect manually.
        """
    },
    "R-squared (R²)": {
        "category": "Data Analysis",
        "definition": """
        **R-squared (R²)** is a statistical measure that represents the proportion of the variance in a dependent 
        variable that is predictable from the independent variable(s). In the context of the UAV research study, R² 
        values indicate how well the remote sensing data predicts actual crop parameters like biomass or nitrogen content.
        
        **Key characteristics:**
        - R² ranges from 0 to 1 (sometimes expressed as 0% to 100%)
        - Higher values indicate better model fit
        - R² = 0.5 means that 50% of the variation in the dependent variable is explained by the model
        
        **Interpretation guidelines in agricultural remote sensing:**
        - R² < 0.3: Weak relationship, limited predictive value
        - R² 0.3-0.5: Moderate relationship, useful for trend analysis
        - R² 0.5-0.7: Strong relationship, good for predictive applications
        - R² > 0.7: Very strong relationship, excellent predictive capability
        
        In the sugarcane study, multispectral models achieved R² values around 0.57 for early growth biomass prediction, 
        while LiDAR models reached R² values of 0.71 for late-season biomass prediction.
        """
    },
    "Point Cloud": {
        "category": "Data Analysis",
        "definition": """
        **Point Cloud** is a set of data points in three-dimensional space. In LiDAR remote sensing, each point represents 
        a location where the laser pulse hit an object and returned to the sensor. Each point contains X, Y, Z coordinates 
        and may include additional attributes like intensity or classification.
        
        **In sugarcane analysis, point clouds provide:**
        - Detailed 3D representation of the crop canopy
        - Precise height measurements
        - Canopy density information
        - Row spacing validation
        - Micro-topography of the field
        
        **Point cloud processing steps:**
        1. **Filtering**: Separating ground points from vegetation points
        2. **Classification**: Identifying different types of objects (ground, vegetation, structures)
        3. **Normalization**: Converting heights to above-ground level
        4. **Metrics extraction**: Calculating statistics like mean height, percentiles, etc.
        5. **Visualization**: Rendering the data for interpretation
        
        Point cloud density (points per square meter) determines the level of detail, with agricultural LiDAR typically 
        collecting 50-200 points/m² depending on flight parameters.
        """
    },
    "Data Fusion": {
        "category": "Data Analysis",
        "definition": """
        **Data Fusion** refers to the process of integrating multiple data sources to produce more consistent, accurate, 
        and useful information than could be provided by any individual data source. In the context of UAV-based 
        agricultural monitoring, data fusion often combines different sensor types.
        
        **Examples in sugarcane monitoring:**
        - Combining LiDAR and multispectral data for improved biomass estimation
        - Merging thermal and RGB imagery for comprehensive stress analysis
        - Integrating UAV data with ground sensor networks
        - Fusing UAV imagery with satellite data for temporal analysis
        
        **Fusion approaches:**
        - **Early fusion**: Combining raw data before analysis
        - **Feature-level fusion**: Extracting features from each source and then combining
        - **Decision-level fusion**: Making separate predictions from each source and then combining results
        
        The research study found that while fusion models combining LiDAR and multispectral data achieved the highest 
        overall accuracy (R²=0.72), the improvement over single-sensor approaches was relatively modest considering 
        the increased complexity.
        """
    },
    "Variable Rate Application": {
        "category": "Data Analysis",
        "definition": """
        **Variable Rate Application (VRA)** is a precision agriculture technology that allows farmers to apply inputs 
        (fertilizers, pesticides, seeds, water) at variable rates across a field, according to the specific needs of 
        different areas. UAV-derived maps are often used to create prescription maps for VRA.
        
        **Process for UAV-based variable rate application:**
        1. Collect UAV imagery (typically multispectral)
        2. Process data to create zone maps (e.g., nitrogen status zones)
        3. Develop prescription maps specifying input rates for each zone
        4. Upload prescription maps to compatible application equipment
        5. Apply inputs at rates specified by the prescription map
        
        **Benefits in sugarcane production:**
        - Typical fertilizer savings of 10-20%
        - Reduced environmental impact from excess chemical application
        - More uniform crop development
        - Potential yield increases of 3-7%
        - Better return on investment for inputs
        
        Modern VRA systems can adjust application rates in real-time based on GPS location and the uploaded prescription map.
        """
    },
    "Orthomosaic": {
        "category": "Data Analysis",
        "definition": """
        **Orthomosaic** is a geometrically corrected aerial image composed of multiple individual images that have been 
        stitched together and adjusted to create a seamless composite with a consistent scale. Orthomosaics are a 
        fundamental output of UAV mapping missions.
        
        **Key characteristics:**
        - Corrected for perspective (orthorectified)
        - Adjusted for topography using elevation data
        - Geographically referenced (georeferenced)
        - Uniform scale throughout the image
        
        **Creation process:**
        1. UAV captures overlapping images (typically 70-80% overlap)
        2. Photogrammetry software identifies common points between images
        3. Camera positions and orientations are calculated
        4. Digital elevation model is created
        5. Images are orthorectified and stitched together
        
        Orthomosaics provide the base layer for most agricultural analyses, allowing for precise measurements and 
        mapping. In sugarcane monitoring, they typically have resolutions of 3-10 cm/pixel depending on flight altitude.
        """
    }
}

# Define the display order for the glossary terms
display_order = sorted(glossary_terms.keys())

# Filter terms based on selection
if selected_category != "All":
    filtered_terms = {term: details for term, details in glossary_terms.items() 
                      if details["category"] == selected_category}
else:
    filtered_terms = glossary_terms

# Further filter based on search
if search_term:
    search_filtered_terms = {term: details for term, details in filtered_terms.items() 
                           if search_term.lower() in term.lower()}
    filtered_terms = search_filtered_terms

# Display count of filtered terms
st.write(f"Displaying {len(filtered_terms)} of {len(glossary_terms)} terms")

# Display the filtered glossary terms
if not filtered_terms:
    st.warning("No terms match your current filters. Try adjusting your search or category selection.")
else:
    # Create columns for category badges
    for term in display_order:
        if term in filtered_terms:
            category = glossary_terms[term]["category"]
            category_colors = {
                "UAV Technology": "#1E88E5",  # Blue
                "Remote Sensing": "#43A047",  # Green
                "Agriculture": "#FDD835",     # Yellow
                "Data Analysis": "#8E24AA"    # Purple
            }
            color = category_colors.get(category, "#757575")  # Default gray
            
            # Display the term with a category badge
            st.markdown(f"""
            ## {term} <span style="font-size: 14px; background-color: {color}; color: white; padding: 3px 8px; border-radius: 10px;">{category}</span>
            """, unsafe_allow_html=True)
            
            # Use the utility function to create an expandable term definition
            create_term_definition("View Definition", glossary_terms[term]["definition"])
            
            # Add a separator
            st.markdown("---")

# Add alphabet quick navigation
st.sidebar.markdown("### Quick Navigation")
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create a grid of letter buttons
cols = st.sidebar.columns(4)
for i, letter in enumerate(alphabet):
    col_idx = i % 4
    # Check if there are terms starting with this letter
    letter_terms = [term for term in glossary_terms.keys() if term.startswith(letter)]
    if letter_terms:
        cols[col_idx].markdown(f"[{letter}](#{letter.lower()})")
    else:
        cols[col_idx].markdown(f"{letter}")

# Additional resources
st.sidebar.markdown("### Additional Resources")
st.sidebar.markdown("""
- [FAO Guide to Precision Agriculture](https://www.fao.org)
- [UAV Regulations Database](https://uavcoach.com/drone-laws/)
- [Sugarcane Research Publications](https://www.sugarresearch.com.au)
- [Remote Sensing in Agriculture](https://www.mdpi.com/journal/remotesensing)
""")

# Footer
st.markdown("---")
st.markdown("© 2023 Precision Agriculture Education Initiative")
