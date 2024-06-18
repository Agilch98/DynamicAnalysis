import pandas as pd
import plotly.graph_objects as go

# Define the path to the text file
file_path = r"./dynamic1/dyanmic_analysis1.txt"

# Read the file, skipping the first 11 lines
data = pd.read_csv(
    file_path,
    skiprows=11,
    delimiter=",",
    names=["frame", "time", "x1", "y1", "x2", "y2"],
)

# Convert all columns to float
data = data.astype(float, errors="raise")

# Drop rows with NaN values
data.dropna(inplace=True)

# Calculate the difference between y1 and y2
data["y_diff"] = data["y1"] - data["y2"]

# Define the specific time values
time_values = [
    2815,
    2869,
    2886,
    2946,
    2973,
    3008,
    3023,
    3049,
    3062,
    3089,
    3099,
    3119,
    3131,
    3160,
    3175,
    3201,
    3217,
    3254,
    3272,
    3337,
    3353,
    3463,
    3487,
    3597,
    3616,
    3683,
    3705,
    3742,
    3758,
    3783,
    3796,
    3821,
    3835,
    3852,
    3874,
    3890,
    3911,
    3933,
    3955,
    3989,
    4003,
    4075,
    4098,
    4202,
    4210,
]

# Find the indices of the specific times
time_indices = [data[data["time"] == time].index[0] for time in time_values]

# Create the figure
fig = go.Figure()

# Add the segments of the line trace with alternating colors
for i in range(len(time_indices) - 1):
    color = "green" if i % 2 != 0 else "blue"  # Alternating colors
    fig.add_trace(
        go.Scatter(
            x=data["time"][time_indices[i] : time_indices[i + 1] + 1],
            y=data["y_diff"][time_indices[i] : time_indices[i + 1] + 1],
            mode="lines",
            name=(
                f"Unloaded" if i == 1 else ""
            ),  # Only show legend for the first Unloaded segment
            showlegend=i == 1,
            line=dict(color=color),
        )
    )

# Add vertical lines to partition time frames
for time in time_values:
    fig.add_shape(
        dict(
            type="line",
            x0=time,
            y0=data["y_diff"].min(),
            x1=time,
            y1=data["y_diff"].max(),
            line=dict(color="black", width=1, dash="dashdot"),
        )
    )

# Define the sequence of labels
load_labels = [
    "10 second load",
    "5 second load",
    "2.5 second load",
    "1 second load",
    "0.5 second load",
    "0.25 second load",
    "0.5 second load",
    "1 second load",
    "2.5 second load",
    "5 second load",
    "10 second load",
]

# Define y_shifts for odd and even labels
y_shifts_odd = [80, 30, 60, 0, 15, 75, 45]
y_shifts_even = -80

# Add distinct labels within each line partition
for i in range(len(time_values) - 1):
    midpoint = (time_values[i] + time_values[i + 1]) / 2
    label = "Unloaded" if i % 2 == 1 else load_labels[(i // 2) % len(load_labels)]
    if i % 2 == 0:
        y_shift = y_shifts_odd[i // 2 % len(y_shifts_odd)]
    else:
        y_shift = y_shifts_even
    fig.add_annotation(
        x=midpoint,
        y=(data["y_diff"].min() + data["y_diff"].max())
        / 2,  # Placing in the middle of y-axis range
        text=label,
        showarrow=False,
        yshift=y_shift,
        font=dict(color="black", size=12),
    )

# Following lines of code are for the 200N force Segment
# Descending First
# Add the 10 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[0] : time_indices[1] + 1],
        y=data["y_diff"][time_indices[0] : time_indices[1] + 1],
        mode="lines+text",
        text=[f"10 Second Load"],
        textposition="bottom center",
        name="10 Second Load",
        showlegend=True,
        line=dict(color="red"),
    )
)
# Add the 5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[2] : time_indices[3] + 1],
        y=data["y_diff"][time_indices[2] : time_indices[3] + 1],
        mode="lines",
        name="5 Second Load",
        showlegend=True,
        line=dict(color="orange"),
    )
)
# Add the 2.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[4] : time_indices[5] + 1],
        y=data["y_diff"][time_indices[4] : time_indices[5] + 1],
        mode="lines",
        name="2.5 Second Load",
        showlegend=True,
        line=dict(color="yellow"),
    )
)
# Add the 1 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[6] : time_indices[7] + 1],
        y=data["y_diff"][time_indices[6] : time_indices[7] + 1],
        mode="lines",
        name="1 Second Load",
        showlegend=True,
        line=dict(color="purple"),
    )
)
# Add the 0.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[8] : time_indices[9] + 1],
        y=data["y_diff"][time_indices[8] : time_indices[9] + 1],
        mode="lines",
        name="0.5 Second Load",
        showlegend=True,
        line=dict(color="blue"),
    )
)
# Add the 0.25 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[10] : time_indices[11] + 1],
        y=data["y_diff"][time_indices[10] : time_indices[11] + 1],
        mode="lines",
        name="0.25 Second Load",
        showlegend=True,
        line=dict(color="black"),
    )
)
# Ascending Next,
# Add the 0.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[12] : time_indices[13] + 1],
        y=data["y_diff"][time_indices[12] : time_indices[13] + 1],
        mode="lines",
        name="0.5 Second Load",
        showlegend=False,
        line=dict(color="blue"),
    )
)
# Add the 1 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[14] : time_indices[15] + 1],
        y=data["y_diff"][time_indices[14] : time_indices[15] + 1],
        mode="lines",
        name="1 Second Load",
        showlegend=False,
        line=dict(color="purple"),
    )
)
# Add the 2.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[16] : time_indices[17] + 1],
        y=data["y_diff"][time_indices[16] : time_indices[17] + 1],
        mode="lines",
        name="2.5 Second Load",
        showlegend=False,
        line=dict(color="yellow"),
    )
)
# Add the 5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[18] : time_indices[19] + 1],
        y=data["y_diff"][time_indices[18] : time_indices[19] + 1],
        mode="lines",
        name="5 Second Load",
        showlegend=False,
        line=dict(color="orange"),
    )
)
# Add the 10 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[20] : time_indices[21] + 1],
        y=data["y_diff"][time_indices[20] : time_indices[21] + 1],
        mode="lines",
        name="10 Second Load",
        showlegend=False,
        line=dict(color="red"),
    )
)


# Following lines of code are for the 400N force Segment
# Descending First
# Add the 10 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[22] : time_indices[23] + 1],
        y=data["y_diff"][time_indices[22] : time_indices[23] + 1],
        mode="lines+text",
        text=[f"10 Second Load"],
        textposition="bottom center",
        name="10 Second Load",
        showlegend=False,
        line=dict(color="red"),
    )
)
# Add the 5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[24] : time_indices[25] + 1],
        y=data["y_diff"][time_indices[24] : time_indices[25] + 1],
        mode="lines",
        name="5 Second Load",
        showlegend=False,
        line=dict(color="orange"),
    )
)
# Add the 2.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[26] : time_indices[27] + 1],
        y=data["y_diff"][time_indices[26] : time_indices[27] + 1],
        mode="lines",
        name="2.5 Second Load",
        showlegend=False,
        line=dict(color="yellow"),
    )
)
# Add the 1 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[28] : time_indices[29] + 1],
        y=data["y_diff"][time_indices[28] : time_indices[29] + 1],
        mode="lines",
        name="1 Second Load",
        showlegend=False,
        line=dict(color="purple"),
    )
)
# Add the 0.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[30] : time_indices[31] + 1],
        y=data["y_diff"][time_indices[30] : time_indices[31] + 1],
        mode="lines",
        name="0.5 Second Load",
        showlegend=False,
        line=dict(color="blue"),
    )
)
# Add the 0.25 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[32] : time_indices[33] + 1],
        y=data["y_diff"][time_indices[32] : time_indices[33] + 1],
        mode="lines",
        name="0.25 Second Load",
        showlegend=False,
        line=dict(color="black"),
    )
)
# Ascending Next,
# Add the 0.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[34] : time_indices[35] + 1],
        y=data["y_diff"][time_indices[34] : time_indices[35] + 1],
        mode="lines",
        name="0.5 Second Load",
        showlegend=False,
        line=dict(color="blue"),
    )
)
# Add the 1 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[36] : time_indices[37] + 1],
        y=data["y_diff"][time_indices[36] : time_indices[37] + 1],
        mode="lines",
        name="1 Second Load",
        showlegend=False,
        line=dict(color="purple"),
    )
)
# Add the 2.5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[38] : time_indices[39] + 1],
        y=data["y_diff"][time_indices[38] : time_indices[39] + 1],
        mode="lines",
        name="2.5 Second Load",
        showlegend=False,
        line=dict(color="yellow"),
    )
)
# Add the 5 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[40] : time_indices[41] + 1],
        y=data["y_diff"][time_indices[40] : time_indices[41] + 1],
        mode="lines",
        name="5 Second Load",
        showlegend=False,
        line=dict(color="orange"),
    )
)
# Add the 10 second load segment of the line trace
fig.add_trace(
    go.Scatter(
        x=data["time"][time_indices[42] : time_indices[43]],
        y=data["y_diff"][time_indices[42] : time_indices[43]],
        mode="lines",
        name="10 Second Load",
        showlegend=False,
        line=dict(color="red"),
    )
)

# Update the layout for the title and labels
fig.update_layout(
    title="Difference between y1 and y2 over Time, Dynamic1.1",
    xaxis_title="Time",
    yaxis_title="Difference (y1 - y2)",
    legend_title="Legend",
)

fig.show()
