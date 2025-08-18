import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Netflix TV Shows and Movies.csv')
clean_df = df

st.title("🎬 Netflix Movies & TV Shows Analysis")

st.markdown("Explore Netflix data: movies, shows, ratings, and more.")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Filter by Type
content_type = st.sidebar.selectbox("Select Content Type", ["All"] + df['type'].unique().tolist())
if content_type != "All":
    df = df[df['type'] == content_type]

# Filter by Age Certification
rating = st.sidebar.selectbox("Select Age Certification", ["All"] + sorted(clean_df['age_certification'].dropna().unique().tolist()))
if rating != "All":
    df = df[df['age_certification'] == rating]

# Filter by Release Year
year = st.sidebar.selectbox("Select Release Year", ["All"] + sorted(clean_df['release_year'].dropna().unique().tolist()))
if year != "All":
    df = df[df['release_year'] == year]

st.write(f"### 📊 Filtered Dataset ({len(df)} entries)")
st.dataframe(df.head(20))

# --- Analysis 1: Count of Movies vs Shows ---
st.subheader("1. Movies vs TV Shows")
type_counts = df['type'].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(type_counts.index, type_counts.values)
ax1.set_title("Movies vs TV Shows")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# --- Analysis 2: Age Certification Distribution ---
st.subheader("2. Age Certification Distribution")
cert_counts = df['age_certification'].value_counts()

fig2, ax2 = plt.subplots()
ax2.bar(cert_counts.index, cert_counts.values, color="orange")
ax2.set_title("Age Certification Distribution")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# --- Analysis 3: Releases Over Time ---
st.subheader("3. Content Releases Over Time")
year_counts = df['release_year'].value_counts().sort_index()

fig3, ax3 = plt.subplots()
ax3.plot(year_counts.index, year_counts.values, marker="o")
ax3.set_title("Number of Releases per Year")
ax3.set_xlabel("Year")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# --- Analysis 4: IMDB Score Distribution ---
st.subheader("4. IMDB Score Distribution")
fig4, ax4 = plt.subplots()
ax4.hist(df['imdb_score'].dropna(), bins=20, color="green", edgecolor="black")
ax4.set_title("IMDB Score Distribution")
ax4.set_xlabel("Score")
ax4.set_ylabel("Frequency")
st.pyplot(fig4)

# --- Analysis 5: Top 10 Movies/Shows by IMDB Votes ---
st.subheader("5. Top 10 by IMDB Votes")
top10 = clean_df[['title', 'type', 'imdb_score', 'imdb_votes']].dropna().sort_values(by="imdb_votes", ascending=False).head(10)
st.dataframe(top10)

# --- Analysis 6: Average IMDb Score by Type ---
st.subheader("6. Average IMDb Score by Type")
avg_scores = df.groupby('type')['imdb_score'].mean()

fig, ax = plt.subplots()
avg_scores.plot(kind="bar", ax=ax, color=["purple", "skyblue"])
ax.set_ylabel("Average Score")
ax.set_title("Average IMDb Score: Movies vs Shows")
st.pyplot(fig)

# --- Analysis 7: Top 10 Longest Movies/Shows ---
st.subheader("7. Top 10 Longest Movies/Shows")
longest = clean_df[['title', 'type', 'runtime']].dropna().sort_values(by="runtime", ascending=False).head(10)
st.dataframe(longest)

# --- Analysis 8: IMDb Score vs Votes ---
st.subheader("8. IMDb Score vs Votes")
fig, ax = plt.subplots()
ax.scatter(df['imdb_votes'], df['imdb_score'], alpha=0.5)
ax.set_xlabel("IMDb Votes (Popularity)")
ax.set_ylabel("IMDb Score (Quality)")
ax.set_title("Popularity vs Quality")
st.pyplot(fig)

# --- Analysis 9: Most Common Age Certifications ---
st.subheader("9. Most Common Age Certifications")
age_counts = df['age_certification'].value_counts()

fig, ax = plt.subplots()
age_counts.plot(kind="barh", ax=ax, color="teal")
ax.set_xlabel("Count")
ax.set_title("Age Certification Breakdown")
st.pyplot(fig)

# --- Analysis 10: IMDb Score Trend Over Time ---
st.subheader("10. IMDb Score Trend Over Time")
avg_per_year = df.groupby('release_year')['imdb_score'].mean()

fig, ax = plt.subplots()
ax.plot(avg_per_year.index, avg_per_year.values, marker="o", color="red")
ax.set_ylabel("Average IMDb Score")
ax.set_xlabel("Release Year")
ax.set_title("Average IMDb Score Over Time")
st.pyplot(fig)

# --- Analysis 11: Correlation Heatmap ---
st.subheader("11. Correlation Heatmap")
numeric_df = df[['release_year', 'runtime', 'imdb_score', 'imdb_votes']].dropna()

fig, ax = plt.subplots()
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# --- Analysis 12: Boxplot of IMDb Scores by Type ---
st.subheader("12. Boxplot of IMDb Scores by Type")

fig, ax = plt.subplots(figsize=(6,4))
sns.boxplot(data=df, x="type", y="imdb_score", ax=ax, palette="Set2")
ax.set_title("IMDb Score Distribution by Type")
ax.set_xlabel("Content Type")
ax.set_ylabel("IMDb Score")
st.pyplot(fig)

# --- Analysis 13: Boxplot of Runtime by Age Certification ---
st.subheader("13. Boxplot of Runtime by Age Certification")

fig, ax = plt.subplots(figsize=(8,5))
sns.boxplot(data=df, x="age_certification", y="runtime", ax=ax, palette="coolwarm")
ax.set_title("Runtime Distribution by Age Certification")
ax.set_xlabel("Age Certification")
ax.set_ylabel("Runtime (minutes)")
st.pyplot(fig)

# -------------------- Download Button --------------------
st.subheader("⬇️ Download Dataset")
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="Download dataset as CSV",
    data=csv,
    file_name="Netflix TV Shows and Movies.csv",
    mime="text/csv",
)


# --- Conclusion ---
st.subheader("Conclusion")
st.markdown("""This analysis provides insights into Netflix's content, showing trends in releases, age certifications, and IMDb scores. The data reveals the popularity of movies vs shows, the distribution of age certifications, and how IMDb scores vary over time.
The top-rated content and longest titles highlight the diversity of Netflix's offerings. This analysis can help users understand the platform's content better and make informed viewing choices.""")

st.markdown("Created by [Susan kihara]❤️")
# --- End of app.py ---




