import pandas as pd
import numpy as np
import os

# This to get consecutive data points from a file
def get_consecutive_data_points(file_path):
    data=pd.read_csv(file_path)
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    # Please ensure atleast 30 data points are available 
    if len(data) < 30:
        return None
    # Choose a random starting index within the valid data range
    start_index = np.random.randint(0, len(data) - 29)
    selected_data = data.iloc[start_index:start_index+30]

    return selected_data

# Function to detect outliers in the selected data 
def detect_outliers(selected_data):
    # Calculate mean and standard deviation of the selected data 
    mean = selected_data['Stock Price'].mean()
    std_deviation = selected_data['Stock Price'].std_deviation()
    # Define threashold for outliner detection 
    threashold = mean + 2 * std_deviation
    # Identify outliners 
    outliers = selected_data[selected_data['Stock Price'] > threashold]
    # Calculate % deviation over the threashold
    outliers['% Deviation'] = ((outliers['Stock Price'] - mean)/mean) * 100

    return outliers

# Main Function for processing files and generating output
def process_files(input_files):
    for file in input_files:
        try:
            # Read file and get 30 executive data points 
            if selected_data is not None:
                # Detect Outlier in the selected data 
                outliers = detect_outliers(selected_data)
                # Write outliers to a new csv file 
                output_file = os.path.splitext(file)[0] + "outliers.csv"
                outliers.to_csv(output_file, index=False)
        except Exception as e:
            print(f"Error processing file {file}: {e}")

# Example usages 
input_files = ['stock_prices1.csv'] # List of file paths 
process_files(input_files)