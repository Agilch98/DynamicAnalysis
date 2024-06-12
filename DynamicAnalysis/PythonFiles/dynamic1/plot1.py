import pandas as pd
import plotly.express as px

# Define the path to the text file
file_path = r"\\HULC-NAS\users\Alex\pilot2\dynamic2\dynamic_analysis2.2.txt"
# Read the data from the text file, skipping the first 11 lines
data = pd.read_csv(file_path, skiprows=11, names=['frame', 'time', 'x1', 'y1', 'x2', 'y2'])

# Calculate the difference between y2 and y1
data['y_diff'] = data['y2'] - data['y1']

# Create a plot using Plotly
fig = px.line(data, x='time', y='y_diff', title='Difference between y2 and y1 with respect to time, dynamic2.2',
              labels={'y_diff': 'y2 - y1', 'time': 'Time'})

# Show the plot
fig.show()
