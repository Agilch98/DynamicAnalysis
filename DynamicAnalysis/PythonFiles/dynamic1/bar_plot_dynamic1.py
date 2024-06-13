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
data['y_diff'] = data['y1'] - data['y2']

# Define the specific time values
time_values = [
    2886, 2946, 2973, 3008, 3023, 3049, 3062, 3089, 3099, 3119, 3131, 
    3160, 3175, 3201, 3217, 3254, 3272, 3337
]

# Compute the differences
loading_rate_diffs = []
loading_rates = []
time_labels = []
colors = []

for i in range(0, len(time_values) - 1, 2):
    start_time = time_values[i]
    end_time = time_values[i + 1]
    start_y_diff = data[data['time'] == start_time]['y_diff'].values[0]
    end_y_diff = data[data['time'] == end_time]['y_diff'].values[0]
    
    loading_rate_diffs.append(end_y_diff - start_y_diff)
    time_labels.append(f'Time {start_time}-{end_time}')
    
    # Assign loading rate labels and colors based on the time ranges
    if (start_time == 2886 and end_time == 2946) or (start_time == 3272 and end_time == 3337):
        loading_rates.append("5 second load")
        colors.append('orange')
    elif (start_time == 2973 and end_time == 3008) or (start_time == 3217 and end_time == 3254):
        loading_rates.append("2.5 second load")
        colors.append('yellow')
    elif (start_time == 3023 and end_time == 3049) or (start_time == 3175 and end_time == 3201):
        loading_rates.append("1 second load")
        colors.append('purple')
    elif (start_time == 3062 and end_time == 3089) or (start_time == 3131 and end_time == 3160):
        loading_rates.append("0.5 second load")
        colors.append('blue')
    else:
        loading_rates.append("0.25 second load")
        colors.append('grey')  # Default color for any unspecified ranges

# Create the bar plot
fig = go.Figure()

# Add the bar trace
for i, load_rate in enumerate(set(loading_rates)):
    indices = [j for j, x in enumerate(loading_rates) if x == load_rate]
    fig.add_trace(
        go.Bar(
            x=[time_labels[j] for j in indices],
            y=[loading_rate_diffs[j] for j in indices],
            name=load_rate,
            marker=dict(color=colors[indices[0]]),
            text=[f'{diff:.2f}' for j, diff in zip(indices, [loading_rate_diffs[j] for j in indices])],
            textposition='outside'
        )
    )

# Update the layout for the title and labels
fig.update_layout(
    title='Difference between y1 and y2 at Specified Loading Rates, Dynamic1',
    xaxis_title='Time Intervals',
    yaxis_title='Difference (y1 - y2)',
    barmode='group',  # Unstack the bars
    showlegend=True
)

# Show the figure
fig.show()


