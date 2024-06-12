import pandas as pd
import plotly.graph_objects as go

# Define the path to the text file
file_path = r"\\HULC-NAS\users\Alex\pilot2\dynamic1\dyanmic_analysis1.txt"

# Read the file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, delimiter=',', names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Convert all columns to float
data = data.astype(float, errors='raise')

# Drop rows with NaN values
data.dropna(inplace=True)

# Calculate the difference between y1 and y2
data['y_diff'] = data['y2'] - data['y1']

# Define the specific time values
time_values = [
    2815, 2869, 2886, 2946, 2973, 3008, 3023, 3049, 3062, 3089, 3099, 3119, 3131, 
    3160, 3175, 3201, 3217, 3254, 3272, 3337, 3353, 3463, 3487, 3597, 3616, 3683, 
    3705, 3742, 3758, 3783, 3796, 3852, 3874, 3890, 3911, 3933, 3955, 3989, 4003, 
    4075, 4098, 4202, 4210
]

# Find the indices of the specific times
time_indices = [data[data['time'] == time].index[0] for time in time_values]

# Create the figure
fig = go.Figure()

# Add the segments of the line trace with alternating colors
for i in range(len(time_indices) - 1):
    color = 'red' if i % 2 == 0 else 'blue'  # Alternating colors
    fig.add_trace(
        go.Scatter(
            x=data['time'][time_indices[i]:time_indices[i+1]+1],
            y=data['y_diff'][time_indices[i]:time_indices[i+1]+1],
            mode='lines',
            name=f'Segment {i+1}',
            line=dict(color=color)
        )
    )

# Add multiple x and y points to the same trace for the 0.5 second load segment
# Concatenate x and y points for the desired segments
x_points = []
y_points = []
segments = [(8, 9), (15, 16)]  # Example segments, add as needed

for start, end in segments:
    x_points += list(data['time'][time_indices[start]:time_indices[end]+1])
    y_points += list(data['y_diff'][time_indices[start]:time_indices[end]+1])

fig.add_trace(
    go.Scatter(
        x=x_points,
        y=y_points,
        mode='lines',
        name='0.5 Second Load',
        line=dict(color='blue')
    )
)

# Add labels at specific points with different colors
for time in time_values:
    index = data[data['time'] == time].index[0]
    fig.add_trace(
        go.Scatter(
            x=[time],
            y=[data.at[index, 'y_diff']],
            mode='markers+text',
            text=[f'Time {time}: {data.at[index, "y_diff"]}'],
            textposition='top center',
            name=f'Time {time}',
            marker=dict(color='green')
        )
    )

# Update the layout for the title and labels
fig.update_layout(
    title='Difference between y1 and y2 over Time, Cyclic1.2 at 200N',
    xaxis_title='Time',
    yaxis_title='Difference (y2 - y1)',
    legend_title='Legend'
)

fig.show()
