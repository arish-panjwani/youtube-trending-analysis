# 📈 YouTube Trending Video Analysis & Dashboard

This project explores what makes YouTube videos trend using data from [Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new). It combines rich **exploratory data analysis (EDA)** with an interactive **Streamlit dashboard** that visualizes YouTube trends, sentiments, and performance metrics.

---

## 🚀 Project Highlights

- 📊 EDA of views, likes, comments, publish dates, etc.
- ☁️ WordClouds of trending video titles
- 🧠 Sentiment analysis using TextBlob
- 🔥 `days_to_trend` analysis to track how fast a video trends
- 🎯 Category-based filtering in dashboard
- 🌐 Live Streamlit dashboard for interactive insights

---

## 🔗 Live Dashboard

👉 [youtube-trends-analysis.streamlit.app](https://youtube-trends-analysis.streamlit.app/)

---

## 📁 File Structure

| File                              | Description                                       |
|-----------------------------------|---------------------------------------------------|
| `YouTube_Trending_Analysis.ipynb`| EDA and preprocessing notebook (Colab/Jupyter)    |
| `processed_youtube_data.csv`     | Cleaned CSV used by Streamlit app                 |
| `App.py`                          | Streamlit dashboard source code                   |
| `requirements.txt`               | Python dependencies for deployment                |
| `README.md`                       | You're reading it!                                |

---

## 📌 Project Summary

This dashboard analyzes trending YouTube videos in the US using a dataset from Kaggle. It includes visualizations of viewership patterns, title sentiment, top-performing channels, and how long videos take to trend. Use the sidebar to filter by category and explore meaningful insights interactively.

---

## 🧪 How to Run

### 🔬 Run Locally

```bash
git clone https://github.com/arish-panjwani/youtube-trending-analysis.git
cd youtube-trending-analysis
pip install -r requirements.txt
streamlit run app.py
```

Make sure `processed_youtube_data.csv` is in the same directory as `app.py`.

### ☁️ Deploy on Streamlit Cloud

1. Push your project (with `requirements.txt`) to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo and click **Deploy**

---

## 📊 Key Insights

- **Entertainment** and **Music** dominate trending categories.
- **Positive and neutral** sentiments are common in video titles.
- Top trending videos often surface within **1–3 days** of upload.
- Channels with consistent branding trend more frequently.
- **Views, likes, and comments** are strongly correlated.

---

## 🔧 Tech Stack

- **Python**
  - `pandas`, `matplotlib`, `seaborn`
  - `wordcloud`, `textblob`
- **Jupyter / Colab** for EDA
- **Streamlit** for dashboard

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [Kaggle Dataset by Data is Beautiful](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- [Streamlit](https://streamlit.io/)
- YouTube Data API (for category mapping)

---

Made with ❤️ by [Arish Panjwani](https://github.com/arish-panjwani)
