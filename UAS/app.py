import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# CONFIG
st.set_page_config(
    page_title="Dashboard Kinerja Media Sosial",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CUSTOM CSS
st.markdown("""
<style>
.metric-card {
    background-color: #1f2933;
    padding: 18px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 0 8px rgba(0,0,0,0.3);
}
.metric-title {
    font-size: 14px;
    color: #9ca3af;
}
.metric-value {
    font-size: 24px;
    font-weight: bold;
    color: white;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #0e1117;
    color: #9ca3af;
    text-align: center;
    padding: 10px;
    font-size: 13px;
    border-top: 1px solid #333;
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# LOAD DATA
@st.cache_data
def load_data():
    return pd.read_csv("dataset_transformed.csv")

df = load_data()

# SIDEBAR FILTER
st.sidebar.title("Filter")

platform_filter = st.sidebar.multiselect(
    "Platform",
    options=df["platform"].unique(),
    default=df["platform"].unique()
)

follower_cat_filter = st.sidebar.multiselect(
    "Kategori Follower",
    options=df["follower_category"].unique(),
    default=df["follower_category"].unique()
)

# Slider filters
follower_min, follower_max = int(df["follower_count"].min()), int(df["follower_count"].max())
eng_min, eng_max = float(df["engagement_rate"].min()), float(df["engagement_rate"].max())
post_min, post_max = int(df["posts_per_week"].min()), int(df["posts_per_week"].max())

follower_range = st.sidebar.slider(
    "Rentang Jumlah Follower",
    follower_min, follower_max,
    (follower_min, follower_max)
)

engagement_range = st.sidebar.slider(
    "Rentang Engagement Rate",
    eng_min, eng_max,
    (eng_min, eng_max)
)

posting_range = st.sidebar.slider(
    "Rentang Post per Minggu",
    post_min, post_max,
    (post_min, post_max)
)

# APPLY FILTER
filtered_df = df[
    (df["platform"].isin(platform_filter)) &
    (df["follower_category"].isin(follower_cat_filter)) &
    (df["follower_count"].between(follower_range[0], follower_range[1])) &
    (df["engagement_rate"].between(engagement_range[0], engagement_range[1])) &
    (df["posts_per_week"].between(posting_range[0], posting_range[1]))
]

# TITLE
st.title("Kinerja Media Sosial")
st.markdown("Analisis performa media sosial berdasarkan engagement dan aktivitas konten")
st.markdown("---")

# KPI CARDS
st.subheader("Ringkasan Data")

col1, col2, col3, col4, col5 = st.columns(5)

def kpi_card(title, value):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">{title}</div>
        <div class="metric-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

with col1:
    kpi_card("Total Akun", len(filtered_df))

with col2:
    kpi_card("Rata-rata Engagement", f"{filtered_df['engagement_rate'].mean():.2f}%")

with col3:
    kpi_card("Rata-rata Conversion", f"{filtered_df['conversion_rate'].mean():.2f}%")

with col4:
    kpi_card("Rata-rata Follower", f"{int(filtered_df['follower_count'].mean()):,}")

with col5:
    kpi_card("Total Jangkauan", f"{int(filtered_df['campaign_reach'].sum()):,}")

st.markdown("---")

# Helper
def dominant_text(series):
    return series.value_counts().idxmax(), series.value_counts(normalize=True).max() * 100

# ROW 1
col1, col2 = st.columns(2)

with col1:
    df_eng = filtered_df.groupby("platform")["engagement_rate"].mean().reset_index()
    fig1 = px.bar(df_eng, x="platform", y="engagement_rate",
                  title="Rata-rata Engagement per Platform",
                  labels={"platform": "Platform", "engagement_rate": "Engagement Rate"})
    st.plotly_chart(fig1, use_container_width=True)

    dom = df_eng.sort_values("engagement_rate", ascending=False).iloc[0]["platform"]
    st.caption(f"Platform dengan engagement rata-rata tertinggi adalah **{dom}**. Grafik ini digunakan untuk membandingkan tingkat engagement antar platform.")

with col2:
    df_conv = filtered_df.groupby("platform")["conversion_rate"].mean().reset_index()
    fig2 = px.bar(df_conv, x="platform", y="conversion_rate",
                  title="Rata-rata Conversion Rate per Platform",
                  labels={"platform": "Platform", "conversion_rate": "Conversion Rate"})
    st.plotly_chart(fig2, use_container_width=True)

    dom = df_conv.sort_values("conversion_rate", ascending=False).iloc[0]["platform"]
    st.caption(f"Platform dengan conversion rate tertinggi adalah **{dom}**. Grafik ini digunakan untuk melihat efektivitas platform dalam mendorong tindakan pengguna.")

# ROW 2
col1, col2 = st.columns(2)

with col1:
    fig3 = px.pie(filtered_df, names="follower_category",
                  title="Distribusi Kategori Follower", hole=0.4)
    st.plotly_chart(fig3, use_container_width=True)

    dom, pct = dominant_text(filtered_df["follower_category"])
    st.caption(f"Kategori follower yang paling dominan adalah **{dom}**, dengan proporsi sekitar **{pct:.1f}%** dari total akun. Grafik ini menunjukkan distribusi akun berdasarkan ukuran jumlah follower.")

with col2:
    fig4 = px.box(filtered_df, x="follower_category", y="engagement_rate",
                  title="Engagement Berdasarkan Kategori Follower",
                  labels={"follower_category": "Kategori Follower", "engagement_rate": "Engagement Rate"})
    st.plotly_chart(fig4, use_container_width=True)
    st.caption("Grafik ini digunakan untuk melihat sebaran engagement pada setiap kategori follower dan mengidentifikasi adanya perbedaan pola interaksi.")

# ROW 3
col1, col2 = st.columns(2)

with col1:
    fig5 = px.scatter(filtered_df, x="follower_count", y="engagement_rate",
                      title="Hubungan Jumlah Follower dan Engagement",
                      labels={"follower_count": "Jumlah Follower", "engagement_rate": "Engagement Rate"})
    st.plotly_chart(fig5, use_container_width=True)
    st.caption("Grafik ini digunakan untuk melihat hubungan antara jumlah follower dengan tingkat engagement yang dihasilkan.")

with col2:
    fig6 = px.histogram(filtered_df, x="posts_per_week", nbins=20,
                        title="Distribusi Jumlah Post per Minggu",
                        labels={"posts_per_week": "Jumlah Post per Minggu"})
    st.plotly_chart(fig6, use_container_width=True)

    dom = filtered_df["posts_per_week"].mode()[0]
    st.caption(f"Frekuensi posting yang paling sering muncul adalah sekitar **{dom} post per minggu**. Grafik ini digunakan untuk melihat pola aktivitas posting akun.")

# HEATMAP
st.subheader("Korelasi Antar Variabel")

corr_cols = [
    "follower_count",
    "posts_per_week",
    "engagement_rate",
    "ad_spend_(usd)",
    "conversion_rate",
    "campaign_reach"
]

corr = filtered_df[corr_cols].corr()

fig7 = px.imshow(
    corr,
    text_auto=".2f",
    aspect="auto",
    title="Heatmap Korelasi Variabel"
)

fig7.update_layout(width=700, height=500, title_x=0.5)
fig7.update_traces(textfont_size=10)

st.plotly_chart(fig7, use_container_width=False)
st.caption("Grafik ini digunakan untuk melihat kekuatan hubungan antar variabel dalam dataset.")

# FOOTER
st.markdown(
    """
    <div class='footer'>
        Dashboard Visualisasi Data |
        Kelompok 2 | 
        Faiz Abdullah Hanif Firmansyah • 
        Jamilatun Khoerunnisa • 
        Alim Rifai
    </div>
    """,
    unsafe_allow_html=True
)