import pandas as pd
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

# Define the specific time values, including 0 for the start of the timeframe
time_values = [
    0, 39, 50, 79, 96, 117, 139, 163, 177, 206, 228, 245, 270, 280, 308, 335, 351, 379,
    393, 413, 434, 458, 473, 503, 519, 537, 555, 586, 601, 621, 643, 667, 673, 696,
    728, 755, 768, 780, 811, 833, 845, 860
]

# Find the indices of the specific times
time_indices = [data[data['time'] == time].index[0] for time in time_values]

# Create the figure
fig = go.Figure()

# Add the segments of the line trace with alternating colors
for i in range(len(time_indices) - 1):
    color = 'green' if i % 2 != 0 else 'blue'  # Alternating colors
    fig.add_trace(
        go.Scatter(
            x=data['time'][time_indices[i]:time_indices[i+1]+1],
            y=data['y_diff'][time_indices[i]:time_indices[i+1]+1],
            mode='lines',
            name=f'Unloaded' if i % 2 == 0 else 'Loaded',  # Ensure 0-39 is labeled as "Unloaded"
            line=dict(color=color)
        )
    )

# Add vertical lines to partition time frames
for time in time_values[1:]:  # Skip the first 0 time value for vertical lines
    fig.add_shape(
        dict(
            type="line",
            x0=time,
            y0=data['y_diff'].min(),
            x1=time,
            y1=data['y_diff'].max(),
            line=dict(color="black", width=1, dash="dashdot"),
        )
    )

# Update the layout for the title and labels
fig.update_layout(
    title='Difference between y1 and y2 over Time, Cyclic 200N',
    xaxis_title='Time',
    yaxis_title='Difference (y2 - y1)',
    legend_title='Legend'
)

fig.show()
