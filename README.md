# Viral Social Media Trends and Engagement Analysis

## Project Overview
This project analyzes engagement patterns in viral social media content across multiple platforms. The goal is to understand how factors such as platform choice, hashtags, and region influence views and audience interaction (likes, comments, and shares).

## Viral Social Media Trends Dataset
The dataset is stored in data/Viral_Social_Media_Trends.csv and contains the following key columns:

- Platform
- Hashtag
- Region: Geographical region where the trend gained traction.
- Views
- Likes
- Comments
- Shares
- Engagement Level: Categorized as Low, Medium, or High

The [dataset](https://www.kaggle.com/datasets/atharvasoundankar/viral-social-media-trends-and-engagement-analysis/discussion/567523) is included in the repo and is open license. 

# Methodology

## Data Preprocessing
- Checked dataset structure, missing values, and duplicates.
- Converted Engagement Level from categorical to numerical (Low: 1, Medium: 2, High: 3).

## Platform-Based Analysis
- Calculated average views and engagement rates per post for each platform.
- Identified the most active region and most popular hashtag per platform.

## Hashtag-Based Analysis
- Measured average views and engagement rates per post per hashtag.
- Determined the most active region and most popular platform for each hashtag.

## Engagement Analysis
- Ranked platforms and hashtags based on interactions to views ratio (Likes/Views, Comments/Views, Shares/Views).
- Created bar chart visualizations of engagement patterns.
