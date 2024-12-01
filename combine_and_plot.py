#!/usr/bin/env python3


import json
import os
import pandas as pd
import matplotlib.pyplot as plt

# Define the weather folder and output files
weather_folder = "data2/timestamps/weather"
combined_csv_file = "weather_data_combined.csv"
trend_graph_file = "temperature_trend.png"

# Initialize an empty list to store all the data
data = []

# Process each JSON file in the weather folder
for filename in sorted(os.listdir(weather_folder)):
    if filename.endswith(".json"):
        filepath = os.path.join(weather_folder, filename)
        with open(filepath, "r") as f:
            try:
                file_data = json.load(f)  # Load JSON file
                if isinstance(file_data, list):  # file_data is a list of dictionaries
                    for entry in file_data:
                        # Add the filename as metadata for debugging
                        entry["source_file"] = filename
                    data.extend(file_data)
                else:
                    print(f"Unexpected structure in {filename}: {file_data}")
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON in {filename}: {e}")

# Convert the list of dictionaries to a DataFrame
if data:
    df = pd.DataFrame(data)

    # Ensure date and time columns are in the correct format
    df["datetime"] = pd.to_datetime(df["date"] + " " + df["reportTime"], format="%d-%m-%Y %H:%M")
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")  # Convert temperature to numeric

    # Sort by datetime to maintain order
    df = df.sort_values("datetime")

    # Save combined data to CSV
    df.to_csv(combined_csv_file, index=False)

    # Plot the temperature trend
    plt.figure(figsize=(12, 6))
    plt.plot(df["datetime"], df["temperature"], marker="o", linestyle="-", label="Temperature (°C)")
    plt.title("Temperature Trend")
    plt.xlabel("Datetime")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.legend()
    plt.savefig(trend_graph_file)
    plt.show()

    print(f"Combined data saved to {combined_csv_file}")
    print(f"Temperature trend graph saved to {trend_graph_file}")
else:
    print("No data to process.")

