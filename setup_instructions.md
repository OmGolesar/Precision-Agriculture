# Setup Instructions for Sugarcane UAV Monitoring Application

## Prerequisites
- Python 3.8 or newer
- VS Code with Python extension installed

## Installation Steps

1. **Extract the ZIP file** to your desired location

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install streamlit numpy pandas plotly
   ```
   
   Alternatively, you can use specific versions:
   ```bash
   pip install streamlit==1.32.0 numpy==1.26.0 pandas==2.1.0 plotly==5.18.0
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Access in browser**:
   Your browser should open automatically, or you can navigate to:
   http://localhost:8501

## Important Files

- `app.py`: Main application entry point
- `pages/`: Directory containing all application pages
- `assets/`: SVG graphics used throughout the application
- `data/`: Python modules for data generation
- `.streamlit/config.toml`: Streamlit configuration

## Troubleshooting

- If you encounter any issues with image loading, ensure that all files in the `assets/` directory were correctly extracted.
- For any "module not found" errors, verify that all required packages are installed in your virtual environment.
- If Streamlit warns about deprecated parameters, this is normal and won't affect functionality.

## Opening in VS Code

1. Open VS Code
2. Choose "File > Open Folder..." and select the extracted project folder
3. If prompted, select your Python interpreter (preferably the one in your virtual environment)
4. Open the Terminal in VS Code (Terminal > New Terminal) and run `streamlit run app.py`

## cmd to run
## .venv\Scripts\activate
## streamlit run app.py --server.port=5000 --server.address=localhost