import pandas as pd
import plotly.express as px

# Define the path to the text file
file_path = r"\\HULC-NAS\users\Alex\pilot2\dynamic1\dyanmic_analysis1.txt"

# Read the file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, delimiter=',', names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Convert all columns to float
data = data.astype(float, errors='raise')

# Drop rows with NaN values
data.dropna(inplace=True)

# Calculate the difference between y1 and y2
data['y_diff'] = data['y1'] - data['y2']

# Calculate y_diff at specific times
y_diff_at_time_2048 = data[data['time'] == 2048]['y_diff'].values[0]
y_diff_at_time_2162 = data[data['time'] == 2162]['y_diff'].values[0]
y_diff_at_time_2234 = data[data['time'] == 2234]['y_diff'].values[0]
y_diff_at_time_2288 = data[data['time'] == 2288]['y_diff'].values[0]
y_diff_at_time_2334 = data[data['time'] == 2334]['y_diff'].values[0]
y_diff_at_time_2368 = data[data['time'] == 2368]['y_diff'].values[0]
y_diff_at_time_2407 = data[data['time'] == 2407]['y_diff'].values[0]
y_diff_at_time_2437 = data[data['time'] == 2437]['y_diff'].values[0]
y_diff_at_time_2480 = data[data['time'] == 2480]['y_diff'].values[0]
y_diff_at_time_2555 = data[data['time'] == 2555]['y_diff'].values[0]
y_diff_at_time_2634 = data[data['time'] == 2634]['y_diff'].values[0]
y_diff_at_time_2700 = data[data['time'] == 2700]['y_diff'].values[0]
y_diff_at_time_2752 = data[data['time'] == 2752]['y_diff'].values[0]
y_diff_at_time_2815 = data[data['time'] == 2815]['y_diff'].values[0]
y_diff_at_time_2840 = data[data['time'] == 2840]['y_diff'].values[0]
y_diff_at_time_2845 = data[data['time'] == 2845]['y_diff'].values[0]
y_diff_at_time_2867 = data[data['time'] == 2867]['y_diff'].values[0]
y_diff_at_time_2903 = data[data['time'] == 2903]['y_diff'].values[0]

print(f"y_diff at time 2048: {y_diff_at_time_2048}")
print(f"y_diff at time 2162: {y_diff_at_time_2162}")
print(f"y_diff at time 2234: {y_diff_at_time_2234}")
print(f"y_diff at time 2288: {y_diff_at_time_2288}")
print(f"y_diff at time 2368: {y_diff_at_time_2368}")
print(f"y_diff at time 2407: {y_diff_at_time_2407}")
print(f"y_diff at time 2437: {y_diff_at_time_2437}")
print(f"y_diff at time 2480: {y_diff_at_time_2480}")
print(f"y_diff at time 2555: {y_diff_at_time_2555}")
print(f"y_diff at time 2634: {y_diff_at_time_2634}")
print(f"y_diff at time 2700: {y_diff_at_time_2700}")
print(f"y_diff at time 2752: {y_diff_at_time_2752}")
print(f"y_diff at time 2815: {y_diff_at_time_2815}")
print(f"y_diff at time 2840: {y_diff_at_time_2840}")

# Plot the difference with respect to time using Plotly
fig = px.line(data, x='time', y='y_diff', title='Difference between y1 and y2 over Time', labels={'y_diff': 'Difference (y1 - y2)', 'time': 'Time'})
fig.show()
