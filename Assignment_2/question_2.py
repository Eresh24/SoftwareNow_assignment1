'''
Create a program that analyses temperature data collected from multiple weather
stations in Australia. The data is stored in multiple CSV files under a "temperatures"
folder, with each file representing data from one year. Process ALL .csv files in the
temperatures folder. Ignore missing temperature values (NaN) in calculations.

Main Functions to Implement:
Seasonal Average: Calculate the average temperature for each season across ALL
stations and ALL years. Save the results to "average_temp.txt".
    • Use Australian seasons: Summer (Dec-Feb), Autumn (Mar-May), Winter (JunAug), Spring (Sep-Nov)
    • Output format example: "Summer: 28.5°C"
Temperature Range: Find the station(s) with the largest temperature range (difference
between the highest and lowest temperature ever recorded at that station). Save the
results to "largest_temp_range_station.txt".
    • Output format example: "Station ABC: Range 45.2°C (Max: 48.3°C, Min: 3.1°C)"
    • If multiple stations tie, list all of them
Temperature Stability: Find which station(s) have the most stable temperatures
(smallest standard deviation) and which have the most variable temperatures (largest
standard deviation). Save the results to "temperature_stability_stations.txt".
    • Output format example:
        o "Most Stable: Station XYZ: StdDev 2.3°C"
        o "Most Variable: Station DEF: StdDev 12.8°C"
    • If multiple stations tie, list all of them

'''

import pandas as pd
import glob
import os

# Folder containing CSV files
data_folder = "temperatures"
csv_files = glob.glob(os.path.join(data_folder, "*.csv"))

if not csv_files:
    print(f"No CSV files found in folder '{data_folder}'.")
    exit()

# Dictionary to hold all temperatures per station
station_data = {}
# List to hold all temperatures with corresponding month for seasonal calculations
all_records = []

# Month-to-number mapping
month_columns = ["January","February","March","April","May","June",
                 "July","August","September","October","November","December"]
month_numbers = {month: i+1 for i, month in enumerate(month_columns)}

# 1. Read all CSV files
for file in csv_files:
    try:
        df = pd.read_csv(file)
        # Ensure required columns exist
        required_cols = ["STATION_NAME"] + month_columns
        if not set(required_cols).issubset(df.columns):
            print(f"Skipping {file}: Missing required columns")
            continue

        # Process each row
        for _, row in df.iterrows():
            station = row["STATION_NAME"]
            temps = row[month_columns].values.astype(float)

            # Store temps per station
            if station not in station_data:
                station_data[station] = []
            station_data[station].extend(temps)

            # Add to all_records for seasonal avg
            for month, temp in zip(month_columns, temps):
                if pd.notna(temp):
                    all_records.append({"Station": station, "Month": month_numbers[month], "Temperature": temp})

    except Exception as e:
        print(f"Error reading {file}: {e}")

# Convert all_records to DataFrame
all_df = pd.DataFrame(all_records)

# 2. Seasonal Average

season_mapping = {
    "Summer": [12, 1, 2],
    "Autumn": [3, 4, 5],
    "Winter": [6, 7, 8],
    "Spring": [9, 10, 11]
}

season_avg = {}
for season, months in season_mapping.items():
    temps = all_df[all_df["Month"].isin(months)]["Temperature"]
    season_avg[season] = temps.mean() if not temps.empty else float('nan')

# Save seasonal averages
with open("average_temp.txt", "w") as f:
    for season, avg in season_avg.items():
        if pd.notna(avg):
            f.write(f"{season}: {avg:.1f}°C\n")
        else:
            f.write(f"{season}: No data\n")

# 3. Temperature Range per Station

station_ranges = {}
max_range = -1

for station, temps in station_data.items():
    temps = [t for t in temps if pd.notna(t)]
    if not temps:
        continue
    max_temp = max(temps)
    min_temp = min(temps)
    temp_range = max_temp - min_temp
    station_ranges[station] = {"range": temp_range, "max": max_temp, "min": min_temp}
    if temp_range > max_range:
        max_range = temp_range

# Find stations with largest range
largest_range_stations = [s for s, v in station_ranges.items() if v["range"] == max_range]

# Save largest temperature range stations
with open("largest_temp_range_station.txt", "w") as f:
    for station in largest_range_stations:
        v = station_ranges[station]
        f.write(f"Station {station}: Range {v['range']:.1f}°C (Max: {v['max']:.1f}°C, Min: {v['min']:.1f}°C)\n")

# 4. Temperature Stability (Std Dev)

station_std = {}
for station, temps in station_data.items():
    temps = [t for t in temps if pd.notna(t)]
    if len(temps) > 1:
        std = pd.Series(temps).std()
    else:
        std = 0.0
    station_std[station] = std

min_std = min(station_std.values())
max_std = max(station_std.values())

most_stable_stations = [s for s, v in station_std.items() if v == min_std]
most_variable_stations = [s for s, v in station_std.items() if v == max_std]

# Save stability results
with open("temperature_stability_stations.txt", "w") as f:
    for station in most_stable_stations:
        f.write(f"Most Stable: Station {station}: StdDev {station_std[station]:.1f}°C\n")
    for station in most_variable_stations:
        f.write(f"Most Variable: Station {station}: StdDev {station_std[station]:.1f}°C\n")

print("Analysis completed. Results saved to:")
print("- average_temp.txt")
print("- largest_temp_range_station.txt")
print("- temperature_stability_stations.txt")
