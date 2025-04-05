"""
Biomass data for the UAV sugarcane monitoring application.
This file contains sample data for biomass prediction based on different sensing technologies.
"""

import numpy as np
import pandas as pd

# Define days after harvest intervals for the six surveys
DAH_INTERVALS = [100, 142, 184, 226, 268, 310]

def generate_biomass_data():
    """
    Generate synthetic biomass data for visualization and modeling purposes.
    Returns a pandas DataFrame with biomass prediction data.
    """
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Create a dataframe with days after harvest
    df = pd.DataFrame({'dah': DAH_INTERVALS})
    
    # Add growth stage information
    df['growth_stage'] = df['dah'].apply(get_growth_stage)
    
    # Actual biomass curve (typical sugarcane growth follows a sigmoidal curve)
    # Values in tons/hectare, based on literature for sugarcane
    df['actual_biomass'] = [20, 45, 70, 90, 100, 105]
    
    # Add small random variations to actual biomass for realism
    df['actual_biomass'] = df['actual_biomass'] + np.random.normal(0, 2, len(df))
    
    # Predicted biomass by different technologies
    # Multispectral - better in early stages
    early_factor = 1.1  # Slightly overestimates in early stages
    late_factor = 0.85  # Underestimates in late stages
    multispectral_errors = [3, 5, 7, 9, 11, 12]  # Increasing error with growth
    
    df['multispectral_biomass'] = df.apply(
        lambda row: row['actual_biomass'] * (
            early_factor if row['dah'] < 184 else 
            late_factor if row['dah'] > 226 else 
            1.0
        ) + np.random.normal(0, 3), axis=1
    )
    df['multispectral_error'] = multispectral_errors
    
    # LiDAR - better in late stages
    early_factor = 0.85  # Underestimates in early stages
    late_factor = 1.05  # Slightly overestimates in late stages
    lidar_errors = [4, 5, 6, 6, 5, 4]  # Decreasing error with growth
    
    df['lidar_biomass'] = df.apply(
        lambda row: row['actual_biomass'] * (
            early_factor if row['dah'] < 184 else 
            late_factor if row['dah'] > 226 else 
            1.0
        ) + np.random.normal(0, 3), axis=1
    )
    df['lidar_error'] = lidar_errors
    
    # Fusion model - generally better across all stages but still has errors
    fusion_errors = [3, 4, 5, 5, 4, 3]  # More consistent error across growth
    
    df['fusion_biomass'] = df.apply(
        lambda row: row['actual_biomass'] * (
            1.02 if row['dah'] < 184 else 
            1.03 if row['dah'] > 226 else 
            1.01
        ) + np.random.normal(0, 2), axis=1
    )
    df['fusion_error'] = fusion_errors
    
    # NDVI benchmark - simplistic model with limitations in dense canopy
    ndvi_errors = [4, 6, 8, 10, 12, 14]  # Increasing error with growth
    
    df['ndvi_biomass'] = df.apply(
        lambda row: row['actual_biomass'] * (
            1.05 if row['dah'] < 184 else 
            0.9 if row['dah'] > 226 else 
            0.95
        ) + np.random.normal(0, 4), axis=1
    )
    df['ndvi_error'] = ndvi_errors
    
    # Model performance metrics (R-squared values)
    # These follow the pattern described in the research summary
    df['r2_multispectral'] = [0.52, 0.57, 0.49, 0.43, 0.41, 0.38]
    df['r2_lidar'] = [0.31, 0.44, 0.53, 0.61, 0.68, 0.71]
    df['r2_fusion'] = [0.54, 0.59, 0.57, 0.63, 0.69, 0.72]
    df['r2_ndvi'] = [0.48, 0.46, 0.39, 0.36, 0.33, 0.31]
    
    return df

def get_biomass_prediction_data():
    """
    Returns processed biomass prediction data ready for visualization.
    """
    return generate_biomass_data()

def get_growth_stage(dah):
    """
    Determine the growth stage based on days after harvest (DAH).
    """
    if dah < 150:
        return "Early Growth Stage"
    elif dah < 250:
        return "Grand Growth Stage"
    else:
        return "Maturation Stage"

def get_best_model_by_stage(growth_stage):
    """
    Returns the recommended model based on growth stage.
    """
    if growth_stage == "Early Growth Stage":
        return "Multispectral"
    elif growth_stage == "Grand Growth Stage":
        return "Fusion"
    else:  # Maturation Stage
        return "LiDAR"

def get_biomass_time_series_for_model(model_name):
    """
    Returns time series data for a specific model.
    """
    df = generate_biomass_data()
    
    if model_name.lower() == "multispectral":
        return df[['dah', 'multispectral_biomass', 'multispectral_error']]
    elif model_name.lower() == "lidar":
        return df[['dah', 'lidar_biomass', 'lidar_error']]
    elif model_name.lower() == "fusion":
        return df[['dah', 'fusion_biomass', 'fusion_error']]
    elif model_name.lower() == "ndvi":
        return df[['dah', 'ndvi_biomass', 'ndvi_error']]
    else:
        return df[['dah', 'actual_biomass']]

def get_model_performance_by_stage():
    """
    Returns model performance data (R² values) for each growth stage.
    """
    df = generate_biomass_data()
    
    early_stage = df[df['dah'] < 150].iloc[0]
    mid_stage = df[(df['dah'] >= 150) & (df['dah'] < 250)].iloc[0]
    late_stage = df[df['dah'] >= 250].iloc[0]
    
    performance_data = {
        "Early Growth Stage": {
            "Multispectral": early_stage["r2_multispectral"],
            "LiDAR": early_stage["r2_lidar"],
            "Fusion": early_stage["r2_fusion"],
            "NDVI": early_stage["r2_ndvi"]
        },
        "Grand Growth Stage": {
            "Multispectral": mid_stage["r2_multispectral"],
            "LiDAR": mid_stage["r2_lidar"],
            "Fusion": mid_stage["r2_fusion"],
            "NDVI": mid_stage["r2_ndvi"]
        },
        "Maturation Stage": {
            "Multispectral": late_stage["r2_multispectral"],
            "LiDAR": late_stage["r2_lidar"],
            "Fusion": late_stage["r2_fusion"],
            "NDVI": late_stage["r2_ndvi"]
        }
    }
    
    return performance_data

if __name__ == "__main__":
    # Test the data generation
    df = generate_biomass_data()
    print(df.head())
