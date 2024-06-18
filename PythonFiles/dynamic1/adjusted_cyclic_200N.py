import pandas as pd
import plotly.express as px
import os

# Define the path to the text file
file_path = r"Cyclic1\cyclic_analysis1p2.txt"

# Read the data from the text file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Calculate the difference between y2 and y1
data['y_diff'] = data['y2'] - data['y1']

# List of specific times
times = [
    0, 39, 50, 79, 96, 117, 139, 163, 177, 206, 228, 245, 270, 280, 308, 335, 351, 379,
    393, 413, 434, 458, 473, 503, 519, 537, 555, 586, 601, 621, 643, 667, 673, 696,
    728, 755, 768, 780, 811, 833, 845, 860
]

# Create a list to store y_diff values at specified times
y_diff_values = []

# Extract y_diff values for each specified time
for time in times:
    y_diff = data[data['time'] == time]['y_diff'].values[0]
    y_diff_values.append({'time': time, 'y_diff': y_diff})

# Create a new DataFrame from the list of y_diff values
filtered_data = pd.DataFrame(y_diff_values)

# Print the y_diff values
for time, y_diff in filtered_data.values:
    print(f"y_diff_at_time_{int(time)} = {y_diff}")

# Plot the difference with respect to time using Plotly
fig = px.line(filtered_data, x='time', y='y_diff', title='Adjusted Difference Between y1 and y2 at Specified Times, Cyclic1.2',
              labels={'y_diff': 'Difference (y2 - y1)', 'time': 'Time'})

# Check current working directory
print("Current working directory:", os.getcwd())

# Save the figure as a PNG file
output_path = r"Cyclic1\cyclic1_2_difference.png"  # Ensure this directory exists or use an absolute path
try:
    fig.write_image(output_path)
    print(f"Figure saved at {output_path}")
except Exception as e:
    print("An error occurred while saving the figure:", e)

# Show the figure (optional)
fig.show()
