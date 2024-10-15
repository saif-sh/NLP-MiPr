import folium
from datetime import datetime  # Import datetime for timestamping

def create_map(df):
    # Create a map centered around the average location of the tweets
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=5)

    for index, row in df.iterrows():
        # Determine the marker color based on severity
        if row['severity'] > 8:
            marker_color = 'red'  # Severity > 8
        elif 4 <= row['severity'] <= 8:
            marker_color = 'orange'  # Severity 4 to 8
        else:
            marker_color = 'blue'  # Severity < 4

        # Create a marker for each tweet
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['disaster_type']} (Severity: {row['severity']}/10)",
            icon=folium.Icon(color=marker_color)
        ).add_to(m)

    # Create a unique filename with timestamp for the HTML file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
    unique_filename = f"data/NLPDIS_{timestamp}.html"  # Prefix with NLPDIS and add timestamp

    # Save the map to an HTML file
    m.save(unique_filename)
    print(f"Map saved as {unique_filename}")  # Print the filename for confirmation
