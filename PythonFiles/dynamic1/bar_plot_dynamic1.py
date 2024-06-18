import pandas as pd
import plotly.graph_objects as go

# Define the path to the text file
file_path = r"dynamic1\dyanmic_analysis1.txt"

# Read the file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, delimiter=',', names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Convert all columns to float
data = data.astype(float, errors='raise')

# Drop rows with NaN values
data.dropna(inplace=True)

# Calculate the difference between y1 and y2
data['y_diff'] = data['y1'] - data['y2']

# Define the specific time values
time_values = [
    2886, 2946, 2973, 3008, 3023, 3049, 3062, 3089, 3099, 3119, 3131, 
    3160, 3175, 3201, 3217, 3254, 3272, 3337
]

# Compute the differences
loading_rate_diffs = []
loading_rates = []

for i in range(0, len(time_values) - 1, 2):
    start_time = time_values[i]
    end_time = time_values[i + 1]
    start_y_diff = data[data['time'] == start_time]['y_diff'].values[0]
    end_y_diff = data[data['time'] == end_time]['y_diff'].values[0]
    
    loading_rate_diffs.append(end_y_diff - start_y_diff)
    loading_rates.append(end_time - start_time)

# Create the bar plot
fig = go.Figure()

# Add the bar trace
fig.add_trace(
    go.Bar(
        x=loading_rates,
        y=loading_rate_diffs,
        text=[f'Time {time_values[i]}-{time_values[i+1]}: {diff:.2f}' for i, diff in zip(range(0, len(time_values) - 1, 2), loading_rate_diffs)],
        textposition='outside',
        name='y_diff'
    )
)

# Update the layout for the title and labels
fig.update_layout(
    title='Difference between y1 and y2 at Specified Loading Rates, Dynamic1',
    xaxis_title="Loading Rate (Time Difference)",
    yaxis_title="Difference (y1 - y2)",
    showlegend=False
)

# Show the figure
fig.show()

#Ask GPt to format it "greyscale for publication in journal" or similar
