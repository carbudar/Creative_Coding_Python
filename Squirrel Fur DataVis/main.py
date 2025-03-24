import pandas as pd
import plotly.graph_objects as go

# Load dataset from https://data.cityofnewyork.us/Environment/2018-Squirrel-Census-Fur-Color-Map/fak5-wcft
df = pd.read_csv("2018CPSquirrel.csv")

# colors for each color class
fur_color_palette = {
    "Gray": "#A9A9A9",
    "Cinnamon": "#D2691E",
    "Black": "#000000"
}

# Filter data to include X coordinate, Y coordinate, and color
filtered_df = df.dropna(subset=["X", "Y", "Primary Fur Color"])

# Create scatter plot
fig = go.Figure()

for color in fur_color_palette.keys():
    subset = filtered_df[filtered_df["Primary Fur Color"] == color]
    fig.add_trace(go.Scattergl(
        x=subset["X"],
        y=subset["Y"],
        mode="markers",
        marker=dict(color=fur_color_palette[color], size=5, opacity=0.7),
        name=color
    ))

# Update layout
fig.update_layout(
    title="Squirrel Locations by Primary Fur Color",
    xaxis_title="Longitude (X)",
    yaxis_title="Latitude (Y)",
    legend_title="Primary Fur Color",
    template="plotly_white"
)

# Show plot
fig.show()
