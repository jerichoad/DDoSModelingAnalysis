# Project Title

This project conducts data analysis to model DDoS (Distributed Denial of Service) attacks. It includes reading, visualizing, and analyzing connection trends based on the provided dataset. The goal is to understand DDoS attack patterns and connection trends to enhance network security.

## Code Explanation

1. Import Libraries: Imports necessary libraries such as Pandas, Seaborn, NumPy, Matplotlib, and time.
2. Reading Data: Uses Pandas to read a CSV file from the given URL (DDoS_Modeling_data.csv). The dataset includes columns like "Time", "Source", "Destination", "Volume", and "Protocol". Data is indexed based on the "Sl Num" column.
3. Time Processing: Converts the "Time" column into a more readable format using time.strftime.
4. Data Visualization: Uses Matplotlib to create a scatter plot between time and data volume.
5. Connection Counting: Creates a connection_count dictionary that counts the number of connections per minute based on the source address (Source). This is done by iterating through the processed source and time data.
6. Seasonal Decomposition: Utilizes seasonal_decompose from statsmodels to perform seasonal decomposition of new_count_df. This helps in understanding any seasonal patterns or trends in the number of connections per minute.


## Data Files

- `DDoS_Modeling_data.csv`
- `DDoS_Modeling_data2.csv`
- `PlayTennis.csv`
- `airline.csv`
- `spamassassin-public-corpus.7z`
