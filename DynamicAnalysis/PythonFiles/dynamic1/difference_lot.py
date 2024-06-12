import pandas as pd
import plotly.express as px

# Define the path to the text file
file_path = r"\\HULC-NAS\users\Alex\pilot2\Cyclic1\cyclic_analysis1.2.txt"

# Read the file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, delimiter=',', names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Convert all columns to float
data = data.astype(float, errors='raise')

# Drop rows with NaN values
data.dropna(inplace=True)

# Calculate the difference between y1 and y2
data['y_diff'] = data['y2'] - data['y1']

# Calculate y_diff at specific times
y_diff_at_time_3 = data[data['time'] == 3]['y_diff'].values[0] 
y_diff_at_time_78 = data[data['time'] == 78]['y_diff'].values[0]

print(f"y_diff at time 3: {y_diff_at_time_3}")
print(f"y_diff at time 78: {y_diff_at_time_78}")

# Plot the difference with respect to time using Plotly
fig = px.line(data, x='time', y='y_diff', title='Difference between y1 and y2 over Time, Cyclic1.2 at 200N', labels={'y_diff': 'Difference (y2 - y1)', 'time': 'Time'})
fig.show()
