# Bikeshare Data Analysis Using SQL Temporary Tables

## Objective
Analyze bikeshare data to find the most-used bike and the station where it’s most commonly found using SQL temporary tables.

## Skills Demonstrated
- SQL (Temporary tables, data aggregation, querying)
- Data analysis with large datasets
- Problem-solving with real-world data

## Process
1. **Data Importation**: Imported bikeshare trip data from the database.
2. **Temporary Table Creation**: Used a temporary table to store aggregated data of bike trips and stations.
3. **Querying for Insights**: Queried the temporary table to find the most-used bike and associated station.
   
### Key SQL Code Snippet
```sql
CREATE TEMPORARY TABLE temp_bike_usage AS
SELECT bike_id, start_station_name, COUNT(*) AS trip_count
FROM bikeshare_trips
GROUP BY bike_id, start_station_name;
