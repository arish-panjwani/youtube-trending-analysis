import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ✅ Must be the first Streamlit command
st.set_page_config(layout="wide", page_title="YouTube Trending Dashboard", page_icon="📺")

# 🎨 Apply custom CSS to style the dashboard like YouTube
st.markdown("""
<style>
    body {
        background-color: #0f0f0f;
        color: white;
    }
    .css-1d391kg, .css-1v0mbdj, .stApp {
        background-color: #0f0f0f;
        color: white;
    }
    .css-1cpxqw2, .css-ffhzg2, .css-1v3fvcr {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Title with YouTube logo
st.markdown("""
<h1 style="display: flex; align-items: center; color: #ffffff;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg" height="40" style="margin-right: 10px;">
    Trending Video Dashboard
</h1>
""", unsafe_allow_html=True)

# Load the processed CSV file exported from the EDA notebook
df = pd.read_csv("processed_youtube_data.csv")

# Ensure 'days_to_trend' column exists (fallback for dashboards)
if 'publish_time' in df.columns and 'trending_date' in df.columns:
    df['trending_date'] = pd.to_datetime(df['trending_date'])
    df['publish_time'] = pd.to_datetime(df['publish_time']).dt.tz_localize(None)
    df['days_to_trend'] = (df['trending_date'] - df['publish_time']).dt.days
    df = df[df['days_to_trend'] >= 0]

# Category ID to Name mapping based on YouTube Data API
category_map = {
    1: 'Film & Animation',
    2: 'Autos & Vehicles',
    10: 'Music',
    15: 'Pets & Animals',
    17: 'Sports',
    19: 'Travel & Events',
    20: 'Gaming',
    22: 'People & Blogs',
    23: 'Comedy',
    24: 'Entertainment',
    25: 'News & Politics',
    26: 'Howto & Style',
    27: 'Education',
    28: 'Science & Technology',
    29: 'Nonprofits & Activism'
}

# Sidebar filters for interactivity
st.sidebar.header("🔍 Filter Options")
categories = df['category_id'].unique()
category_names = [category_map.get(cat, f"Unknown ({cat})") for cat in categories]
selected_name = st.sidebar.selectbox("Select Category", category_names)

# Only try to match if the category is known
matching_categories = [k for k, v in category_map.items() if v == selected_name]
if matching_categories:
    selected_category = matching_categories[0]
    filtered_df = df[df['category_id'] == selected_category]

    # Section: Top 10 channels by number of trending videos
    st.subheader("Top 10 Channels in Selected Category")
    top_channels = filtered_df['channel_title'].value_counts().head(10)
    st.bar_chart(top_channels)

    # Section: Distribution of views for selected category
    st.subheader("Distribution of Views")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['views'], bins=30, ax=ax)
    st.pyplot(fig)

    # Section: Word cloud of video titles
    st.subheader("📄 Word Cloud of Video Titles")
    text = " ".join(filtered_df['title'].astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig_wc, ax_wc = plt.subplots(figsize=(10, 5))
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis('off')
    st.pyplot(fig_wc)

    # Section: Sentiment analysis of video titles
    st.subheader("📈 Sentiment Analysis of Titles")
    sentiment_counts = filtered_df['sentiment'].value_counts()
    st.bar_chart(sentiment_counts)

    # Section: Distribution of days it took for a video to trend
    if 'days_to_trend' in filtered_df.columns:
        st.subheader("📅 Days to Trend Distribution")
        fig2, ax2 = plt.subplots()
        sns.histplot(filtered_df['days_to_trend'], bins=20, kde=True, ax=ax2)
        st.pyplot(fig2)
    else:
        st.warning("'days_to_trend' column is missing. Please check the processed dataset.")
else:
    st.warning("The selected category is not recognized in the mapping. Please choose another.")

# Section: Summary of findings
st.subheader("📌 Summary")
st.markdown("""
- **Entertainment** and **Music** are the most frequent trending categories.
- Most trending videos appear within **1–3 days** of being uploaded.
- Titles with **positive or neutral sentiment** are more common.
- A few top creators have many trending videos, suggesting strong brand power.
- **High view counts** are strongly correlated with **likes** and **comment counts**.
""")

# Footer section
st.markdown("---")

import streamlit as st

col1, col2 = st.columns([1, 0.4])  # Adjust width ratio as needed

with col1:
    st.markdown("Made with ❤️ using Streamlit")

with col2:
    st.markdown("""
        <a href="https://github.com/arish-panjwani/youtube-trending-analysis" target="_blank" style="text-decoration: none;">
            <div style="display: flex; align-items: center;">
                <span style="color: #ffffff; font-size: 16px; margin-right: 8px;">View Project on GitHub</span>
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"
                     width="24"
                     style="filter: brightness(0) invert(1);">
            </div>
        </a>
    """, unsafe_allow_html=True)
