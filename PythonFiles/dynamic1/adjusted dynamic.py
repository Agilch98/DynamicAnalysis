import pandas as pd
import plotly.express as px

# Define the path to the text file
file_path = r"\\HULC-NAS\users\Alex\pilot2\dynamic1\dyanmic_analysis1.txt"

# Read the data from the text file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Calculate the difference between y2 and y1
data['y_diff'] = data['y1'] - data['y2']

# List of specific times
times = [2048, 2162, 2234, 2288, 2334, 2368, 2407, 2437, 2480, 2555, 2634, 2700, 2752, 2815, 2840, 2845, 2867, 2903, 2973, 3023, 3061, 3098, 3131, 3175, 3215, 3272, 3356, 3494, 3544, 3554, 3564, 3577, 3592, 3624, 3705, 3758, 3796, 3835, 3874, 3911, 3955, 4003, 4098, 4151, 4200]

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
fig = px.line(filtered_data, x='time', y='y_diff', title='Adjusted Difference Between y1 and y2 at Specified Times, Dynamic1',
              labels={'y_diff': 'Difference (y1 - y2)', 'time': 'Time'})
fig.show()
