# %% Import Dependencies
import pandas as pd
import matplotlib.pyplot as plt
import os

# %% Load dataset
file_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_dir, 'data', 'Viral_Social_Media_Trends.csv')
data = pd.read_csv(file_path)


# %% Display dataset structure and content
print(f"Dataset shape: {data.shape}\n\n")
print(f"Overview\n\n {data.head()}\n\n")
print(f"Dataset information\n")
data.info()
print("\n")
print(f"Missing value count: {data.isna().sum().sum()}")
print(f"Duplicate value count: {data.duplicated().sum()}\n\n")


# %% Change engagement level to numerical values
engagement_map = {'Low': 1, 'Medium': 2, 'High': 3}
data['Engagement_Level'] = data['Engagement_Level'].map(engagement_map)


# %% Analyze by Platform
platforms = data["Platform"].unique()

metrics = {
    "Average View Count": [],
    r"Likes/Views %": [],
    r"Comments/Views %": [], 
    r"Shares/Views %": [], 
    "Average Engagement Level": [],
    "Most Active Region": [],
    "Most Popular Hashtag": [],
}

for plat in platforms:
    platform_data = data[data["Platform"] == plat]
    metrics["Average View Count"].append(platform_data["Views"].mean())
    metrics[r"Likes/Views %"].append(platform_data["Likes"].sum()/platform_data["Views"].sum() * 100)
    metrics[r"Comments/Views %"].append(platform_data["Comments"].sum()/platform_data["Views"].sum() * 100)
    metrics[r"Shares/Views %"].append(platform_data["Shares"].sum()/platform_data["Views"].sum() * 100)
    metrics["Average Engagement Level"].append(platform_data["Engagement_Level"].mean())
    metrics["Most Active Region"].append(platform_data["Region"].mode().iat[0])
    metrics["Most Popular Hashtag"].append(platform_data["Hashtag"].mode().iat[0])

platform_metrics_df = pd.DataFrame(metrics, index=platforms)
platform_views_ranking = platform_metrics_df["Average View Count"].sort_values(ascending=False)


# %% Analyze by hashtag
hashtags = data["Hashtag"].unique()

metrics = {
    "Average View Count": [],
    r"Likes/Views %": [],
    r"Comments/Views %": [], 
    r"Shares/Views %": [], 
    "Average Engagement Level": [],
    "Most Active Region": [],
    "Most Popular Platform": [],
}

for tag in hashtags:
    hashtag_data = data[data["Hashtag"] == tag]
    metrics["Average View Count"].append(hashtag_data["Views"].mean())
    metrics[r"Likes/Views %"].append(hashtag_data["Likes"].sum()/hashtag_data["Views"].sum() * 100)
    metrics[r"Comments/Views %"].append(hashtag_data["Comments"].sum()/hashtag_data["Views"].sum() * 100)
    metrics[r"Shares/Views %"].append(hashtag_data["Shares"].sum()/hashtag_data["Views"].sum() * 100)
    metrics["Average Engagement Level"].append(hashtag_data["Engagement_Level"].mean())
    metrics["Most Active Region"].append(hashtag_data["Region"].mode().iat[0])
    metrics["Most Popular Platform"].append(hashtag_data["Platform"].mode().iat[0])

hashtag_metrics_df = pd.DataFrame(metrics, index=hashtags)
hashtag_views_ranking = hashtag_metrics_df["Average View Count"].sort_values(ascending=False)


# %% Analyze platforms and hashtags based on total interactions

platform_metrics_df.loc[:, 'Total Interactive %'] = platform_metrics_df[[r"Likes/Views %", r"Comments/Views %", r"Shares/Views %"]].sum(axis=1)

platform_interaction_ranking = (platform_metrics_df[
    ["Likes/Views %", "Comments/Views %", "Shares/Views %", "Total Interactive %"]]
    .copy()
    .sort_values("Total Interactive %", ascending=False)
)

hashtag_metrics_df.loc[:, 'Total Interactive %'] = hashtag_metrics_df[[r"Likes/Views %", r"Comments/Views %", r"Shares/Views %"]].sum(axis=1)

hashtag_interaction_ranking = (hashtag_metrics_df[
    ["Likes/Views %", "Comments/Views %", "Shares/Views %", "Total Interactive %"]]
    .copy()
    .sort_values("Total Interactive %", ascending=False)
)


# %% Display platform metrics
print(f"Platform-based engagement and view analysis: \n {platform_metrics_df} \n\n")
print(f"Ranking of platforms based on average view count: \n{platform_views_ranking}\n\n")
print(f"Ranking of platforms based on percentage of viewers interacting: \n{platform_interaction_ranking}\n\n")

# %% Display hashtag metrics
print(f"Hashtag-based engagement and view analysis: \n {hashtag_metrics_df} \n\n")
print(f"Ranking of hashtags based on average view count: \n{hashtag_views_ranking}\n\n")
print(f"Ranking of hashtags based on percentage of viewers interacting: \n{hashtag_interaction_ranking}\n\n")


# %% Plot bar chart for hashatag interaction metrics
plt.figure(figsize=(20, 15))

for i, col in enumerate(hashtag_interaction_ranking.columns):
    plt.subplot(2, 2, i+1) 
    
    # Plot bar chart
    plt.bar(hashtag_interaction_ranking.index, 
            hashtag_interaction_ranking[col], 
            color='skyblue',
            edgecolor='navy',
            linewidth=1)
    
    # Adjust y-axis limits for better visibility
    min_val = hashtag_interaction_ranking[col].min()
    max_val = hashtag_interaction_ranking[col].max()
    plt.ylim(min_val * 0.95, max_val * 1.05)  # Add 5% padding
    
    # Add value labels on bars
    for idx, value in enumerate(hashtag_interaction_ranking[col]):
        plt.text(idx, value, f'{value:.1f}%', 
                ha='center', va='bottom', 
                fontsize=8)
    
    plt.xlabel('Hashtags', fontsize=10)
    plt.ylabel(col, fontsize=10)
    plt.title(f'{col} by Hashtag', fontsize=12, pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout(pad=3.0)
