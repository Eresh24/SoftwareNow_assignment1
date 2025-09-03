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