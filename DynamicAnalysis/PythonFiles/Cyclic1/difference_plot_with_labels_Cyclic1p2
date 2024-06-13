import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
y_diff_at_time_35 = data[data['time'] == 35]['y_diff'].values[0]
y_diff_at_time_64 = data[data['time'] == 64]['y_diff'].values[0]
y_diff_at_time_117 = data[data['time'] == 117]['y_diff'].values[0]
y_diff_at_time_159 = data[data['time'] == 159]['y_diff'].values[0]
y_diff_at_time_191 = data[data['time'] == 191]['y_diff'].values[0]
y_diff_at_time_232 = data[data['time'] == 232]['y_diff'].values[0]
y_diff_at_time_280 = data[data['time'] == 280]['y_diff'].values[0]
y_diff_at_time_326 = data[data['time'] == 326]['y_diff'].values[0]
y_diff_at_time_372 = data[data['time'] == 372]['y_diff'].values[0]
y_diff_at_time_413 = data[data['time'] == 413]['y_diff'].values[0]
y_diff_at_time_450 = data[data['time'] == 450]['y_diff'].values[0]
y_diff_at_time_481 = data[data['time'] == 481]['y_diff'].values[0]
y_diff_at_time_537 = data[data['time'] == 537]['y_diff'].values[0]
y_diff_at_time_586 = data[data['time'] == 586]['y_diff'].values[0]
y_diff_at_time_617 = data[data['time'] == 617]['y_diff'].values[0]
y_diff_at_time_667 = data[data['time'] == 667]['y_diff'].values[0]
y_diff_at_time_696 = data[data['time'] == 696]['y_diff'].values[0]
y_diff_at_time_755 = data[data['time'] == 755]['y_diff'].values[0]
y_diff_at_time_780 = data[data['time'] == 780]['y_diff'].values[0]
y_diff_at_time_833 = data[data['time'] == 833]['y_diff'].values[0]
y_diff_at_time_857 = data[data['time'] == 857]['y_diff'].values[0]


print(f"y_diff at time 35: {y_diff_at_time_35}")
print(f"y_diff at time 64: {y_diff_at_time_64}")
print(f"y_diff at time 117: {y_diff_at_time_117}")
print(f"y_diff at time 159: {y_diff_at_time_159}")
print(f"y_diff at time 191: {y_diff_at_time_191}")
print(f"y_diff at time 232: {y_diff_at_time_232}")
print(f"y_diff at time 280: {y_diff_at_time_280}")
print(f"y_diff at time 326: {y_diff_at_time_326}")
print(f"y_diff at time 372: {y_diff_at_time_372}")
print(f"y_diff at time 413: {y_diff_at_time_413}")
print(f"y_diff at time 450: {y_diff_at_time_450}")
print(f"y_diff at time 481: {y_diff_at_time_481}")
print(f"y_diff at time 537: {y_diff_at_time_537}")
print(f"y_diff at time 586: {y_diff_at_time_586}")
print(f"y_diff at time 617: {y_diff_at_time_617}")
print(f"y_diff at time 667: {y_diff_at_time_667}")
print(f"y_diff at time 696: {y_diff_at_time_696}")
print(f"y_diff at time 755: {y_diff_at_time_755}")
print(f"y_diff at time 780: {y_diff_at_time_780}")
print(f"y_diff at time 833: {y_diff_at_time_833}")
print(f"y_diff at time 857: {y_diff_at_time_857}")


# Plot the difference with respect to time using Plotly
fig = px.line(data, x='time', y='y_diff', title='Difference between y1 and y2 over Time, Cyclic1.2 at 200N', labels={'y_diff': 'Difference (y2 - y1)', 'time': 'Time'})

# Define the x and y values for the annotations
x_values = [35, 64, 117, 159, 191, 232, 280, 326, 372, 413, 450, 481, 537, 586, 617, 667, 696, 755, 780, 833, 856]

# Assuming y_diff_at_time_X variables are defined previously or calculated from the data
y_values = [
    y_diff_at_time_35, y_diff_at_time_64, y_diff_at_time_117, y_diff_at_time_159, y_diff_at_time_191, y_diff_at_time_232, 
    y_diff_at_time_280, y_diff_at_time_326, y_diff_at_time_372, y_diff_at_time_413, y_diff_at_time_450, y_diff_at_time_481,
    y_diff_at_time_537, y_diff_at_time_586, y_diff_at_time_617, y_diff_at_time_667, y_diff_at_time_696, y_diff_at_time_755,
    y_diff_at_time_780, y_diff_at_time_833, y_diff_at_time_857
]

# Create the text array by combining the time and y_diff values
text = [f'Time {x}: {y}' for x, y in zip(x_values, y_values)]

# Add labels at specific points
fig.add_trace(
    go.Scatter(
        x=x_values,
        y=y_values,
        mode='markers+text',
        text=text,
        textposition='top center',
        name='Annotations'
    )
)


fig.show()
