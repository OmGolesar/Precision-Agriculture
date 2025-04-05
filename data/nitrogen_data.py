"""
Nitrogen data for the UAV sugarcane monitoring application.
This file contains sample data for leaf nitrogen prediction based on different sensing technologies.
"""

import numpy as np
import pandas as pd
from data.biomass_data import DAH_INTERVALS, get_growth_stage

def generate_nitrogen_data():
    """
    Generate synthetic nitrogen data for visualization and modeling purposes.
    Returns a pandas DataFrame with nitrogen prediction data.
    """
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Create a dataframe with days after harvest
    df = pd.DataFrame({'dah': DAH_INTERVALS})
    
    # Add growth stage information
    df['growth_stage'] = df['dah'].apply(get_growth_stage)
    
    # Actual nitrogen content curve (typically decreases over time)
    # Values in percentage of dry weight, based on literature for sugarcane
    # Nitrogen content typically decreases as the crop matures
    df['actual_nitrogen'] = [2.2, 2.0, 1.9, 1.7, 1.5, 1.3]
    
    # Add small random variations to actual nitrogen for realism
    df['actual_nitrogen'] = df['actual_nitrogen'] + np.random.normal(0, 0.05, len(df))
    
    # Predicted nitrogen content by different technologies
    # Multispectral - consistently good for nitrogen prediction
    multispectral_errors = [0.2, 0.2, 0.15, 0.15, 0.1, 0.1]  # Decreasing error with growth
    
    df['multispectral_nitrogen'] = df.apply(
        lambda row: row['actual_nitrogen'] * (
            1.05 if row['dah'] < 184 else 
            0.95 if row['dah'] > 226 else 
            1.0
        ) + np.random.normal(0, 0.1), axis=1
    )
    df['multispectral_nitrogen_error'] = multispectral_errors
    
    # LiDAR - poor for nitrogen prediction across all stages
    lidar_errors = [0.4, 0.4, 0.35, 0.35, 0.3, 0.3]  # Higher errors
    
    df['lidar_nitrogen'] = df.apply(
        lambda row: row['actual_nitrogen'] * (
            0.85 if row['dah'] < 184 else 
            0.9 if row['dah'] > 226 else 
            0.87
        ) + np.random.normal(0, 0.2), axis=1
    )
    df['lidar_nitrogen_error'] = lidar_errors
    
    # Fusion model - slightly better than multispectral but not by much
    fusion_errors = [0.19, 0.19, 0.14, 0.14, 0.09, 0.09]  # Slightly better than multispectral
    
    df['fusion_nitrogen'] = df.apply(
        lambda row: row['actual_nitrogen'] * (
            1.04 if row['dah'] < 184 else 
            0.96 if row['dah'] > 226 else 
            1.0
        ) + np.random.normal(0, 0.09), axis=1
    )
    df['fusion_nitrogen_error'] = fusion_errors
    
    # NDVI benchmark - decent but not as good as specialized indices
    ndvi_errors = [0.25, 0.25, 0.20, 0.20, 0.15, 0.15]  # Higher than multispectral
    
    df['ndvi_nitrogen'] = df.apply(
        lambda row: row['actual_nitrogen'] * (
            1.1 if row['dah'] < 184 else 
            0.9 if row['dah'] > 226 else 
            1.0
        ) + np.random.normal(0, 0.15), axis=1
    )
    df['ndvi_nitrogen_error'] = ndvi_errors
    
    # Model performance metrics (R-squared values)
    # These are relatively consistent across growth stages for nitrogen prediction
    # Following the pattern described in the research summary
    df['r2_n_multispectral'] = [0.57, 0.58, 0.56, 0.57, 0.56, 0.55]
    df['r2_n_lidar'] = [0.28, 0.29, 0.30, 0.31, 0.30, 0.28]
    df['r2_n_fusion'] = [0.59, 0.60, 0.58, 0.59, 0.57, 0.56]
    df['r2_n_ndvi'] = [0.51, 0.50, 0.49, 0.48, 0.47, 0.46]
    
    return df

def get_nitrogen_prediction_data():
    """
    Returns processed nitrogen prediction data ready for visualization.
    """
    return generate_nitrogen_data()

def get_nitrogen_model_performance():
    """
    Returns overall model performance for nitrogen prediction across all stages.
    """
    df = generate_nitrogen_data()
    
    # Calculate mean performance across all stages
    performance = {
        "Multispectral": df['r2_n_multispectral'].mean(),
        "LiDAR": df['r2_n_lidar'].mean(),
        "Fusion": df['r2_n_fusion'].mean(),
        "NDVI": df['r2_n_ndvi'].mean()
    }
    
    # Calculate RMSE values (inverse relationship to R²)
    # Simplified calculation for demo purposes
    rmse = {
        "Multispectral": 0.31,
        "LiDAR": 0.48,
        "Fusion": 0.30,
        "NDVI": 0.36
    }
    
    return {"r_squared": performance, "rmse": rmse}

def get_nitrogen_time_series():
    """
    Returns time series data for nitrogen content over the growing season.
    """
    df = generate_nitrogen_data()
    return df[['dah', 'actual_nitrogen', 'multispectral_nitrogen', 'multispectral_nitrogen_error']]

def get_nitrogen_recommendation(dah, nitrogen_value):
    """
    Generate a recommendation based on the current nitrogen level and growth stage.
    """
    growth_stage = get_growth_stage(dah)
    
    if growth_stage == "Early Growth Stage":
        optimal_n = 2.0
        if nitrogen_value > optimal_n + 0.2:
            return {
                "status": "High",
                "color": "orange",
                "recommendation": "Nitrogen levels are above optimal for this growth stage. Consider reducing fertilizer application in future cycles. Monitor for excessive vegetative growth."
            }
        elif nitrogen_value < optimal_n - 0.2:
            return {
                "status": "Low",
                "color": "red",
                "recommendation": "Nitrogen levels are below optimal for early growth. Consider supplemental nitrogen application to support vegetative growth and tillering."
            }
        else:
            return {
                "status": "Optimal",
                "color": "green",
                "recommendation": "Nitrogen levels are within optimal range for early growth stage. Continue with standard management practices."
            }
    elif growth_stage == "Grand Growth Stage":
        optimal_n = 1.8
        if nitrogen_value > optimal_n + 0.2:
            return {
                "status": "Slightly High",
                "color": "yellowgreen",
                "recommendation": "Nitrogen levels are slightly high for mid-growth stage. No immediate action needed, but monitor crop development."
            }
        elif nitrogen_value < optimal_n - 0.2:
            return {
                "status": "Low",
                "color": "orange",
                "recommendation": "Nitrogen levels are below optimal for grand growth phase. Consider a light supplemental application if canopy is not fully developed."
            }
        else:
            return {
                "status": "Optimal",
                "color": "green",
                "recommendation": "Nitrogen levels are within optimal range for grand growth stage. Continue with standard management practices."
            }
    else:  # Maturation Stage
        optimal_n = 1.5
        if nitrogen_value > optimal_n + 0.2:
            return {
                "status": "High",
                "color": "orange",
                "recommendation": "Nitrogen levels are higher than desired for maturation stage. This may delay ripening and reduce sugar content. Consider adjusting pre-harvest management."
            }
        elif nitrogen_value < optimal_n - 0.2:
            return {
                "status": "Low (Favorable)",
                "color": "green",
                "recommendation": "Nitrogen levels are low, which is favorable for ripening. No nitrogen application recommended at this late stage."
            }
        else:
            return {
                "status": "Optimal",
                "color": "green",
                "recommendation": "Nitrogen levels are within optimal range for maturation. Focus on ripening management for optimal sugar content."
            }

def generate_scatter_data_for_nitrogen():
    """
    Generate scatter plot data showing the relationship between 
    predicted and actual nitrogen values.
    """
    # Set seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data for demonstration
    actual_n = np.linspace(1.0, 2.5, 45) + np.random.normal(0, 0.1, 45)
    predicted_n = actual_n * 0.97 + np.random.normal(0, 0.15, 45)
    
    # Create a dataframe
    df = pd.DataFrame({
        'actual_nitrogen': actual_n,
        'predicted_nitrogen': predicted_n
    })
    
    return df

if __name__ == "__main__":
    # Test the data generation
    df = generate_nitrogen_data()
    print(df.head())
