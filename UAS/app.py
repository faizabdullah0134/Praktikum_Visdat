import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# CONFIG
st.set_page_config(page_title="Dashboard Media Sosial", layout="wide")

# LOAD DATA
df = pd.read_csv("dataset_transformed.csv")
platform_summary = pd.read_csv("platform_summary.csv")

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

# HEADER
st.title("Visualisasi Kinerja Media Sosial")
st.markdown("Analisis performa media sosial berdasarkan engagement, aktivitas konten, dan efektivitas iklan.")

# SIDEBAR FILTER
st.sidebar.header("🎛 Filter Data")

platform_filter = st.sidebar.multiselect(
    "Platform",
    options=df["platform"].unique(),
    default=df["platform"].unique()
)

follower_min, follower_max = st.sidebar.slider(
    "Rentang Jumlah Follower",
    int(df["follower_count"].min()),
    int(df["follower_count"].max()),
    (int(df["follower_count"].min()), int(df["follower_count"].max()))
)

engagement_filter = st.sidebar.multiselect(
    "Tingkat Engagement",
    options=df["engagement_level"].unique(),
    default=df["engagement_level"].unique()
)

posting_filter = st.sidebar.multiselect(
    "Intensitas Posting",
    options=df["posting_intensity"].unique(),
    default=df["posting_intensity"].unique()
)

follower_category_filter = st.sidebar.multiselect(
    "Kategori Follower",
    options=df["follower_category"].unique(),
    default=df["follower_category"].unique()
)

ad_min, ad_max = st.sidebar.slider(
    "Rentang Biaya Iklan (USD)",
    float(df["ad_spend_(usd)"].min()),
    float(df["ad_spend_(usd)"].max()),
    (float(df["ad_spend_(usd)"].min()), float(df["ad_spend_(usd)"].max()))
)

# APPLY FILTER
filtered_df = df[
    (df["platform"].isin(platform_filter)) &
    (df["follower_count"] >= follower_min) &
    (df["follower_count"] <= follower_max) &
    (df["engagement_level"].isin(engagement_filter)) &
    (df["posting_intensity"].isin(posting_filter)) &
    (df["follower_category"].isin(follower_category_filter)) &
    (df["ad_spend_(usd)"] >= ad_min) &
    (df["ad_spend_(usd)"] <= ad_max)
]

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

# OVERVIEW
st.markdown("Komposisi Kategori Follower")

follower_dist = filtered_df["follower_category"].value_counts().reset_index()
follower_dist.columns = ["Kategori", "Jumlah"]

fig_donut = px.pie(follower_dist, names="Kategori", values="Jumlah", hole=0.5)
st.plotly_chart(fig_donut, use_container_width=True)

if not follower_dist.empty:
    top_cat = follower_dist.iloc[0]["Kategori"]
    top_val = follower_dist.iloc[0]["Jumlah"]
    total = follower_dist["Jumlah"].sum()
    perc = (top_val / total) * 100

st.markdown(f"""
Kategori follower yang paling dominan adalah **{top_cat}**, dengan proporsi sekitar **{perc:.1f}%** dari total akun yang dianalisis.
""")

# PLATFORM PERFORMANCE
st.subheader("Performa Platform")

col8, col9 = st.columns(2)

with col8:
    fig_bar1 = px.bar(
        platform_summary,
        x="platform",
        y="avg_engagement_rate",
        labels={"platform": "Platform", "avg_engagement_rate": "Rata-rata Engagement (%)"},
        title="Rata-rata Engagement per Platform"
    )
    fig_bar1.update_layout(height=330)
    st.plotly_chart(fig_bar1, use_container_width=True)

    top_eng = platform_summary.sort_values("avg_engagement_rate", ascending=False).iloc[0]
    st.caption(f"Platform dengan engagement tertinggi adalah **{top_eng['platform']}** ({top_eng['avg_engagement_rate']:.2f}%).")

with col9:
    fig_bar2 = px.bar(
        platform_summary,
        x="platform",
        y="avg_conversion_rate",
        labels={"platform": "Platform", "avg_conversion_rate": "Rata-rata Conversion (%)"},
        title="Rata-rata Conversion Rate per Platform"
    )
    fig_bar2.update_layout(height=330)
    st.plotly_chart(fig_bar2, use_container_width=True)

    top_conv = platform_summary.sort_values("avg_conversion_rate", ascending=False).iloc[0]
    st.caption(f"Platform dengan conversion rate tertinggi adalah **{top_conv['platform']}** ({top_conv['avg_conversion_rate']:.2f}%).")

# SCATTER
st.markdown("Hubungan Jumlah Follower dan Engagement")

fig_scatter = px.scatter(
    filtered_df,
    x="follower_count",
    y="engagement_rate",
    color="platform",
    labels={"follower_count": "Jumlah Follower", "engagement_rate": "Engagement (%)"}
)
fig_scatter.update_layout(height=350)
st.plotly_chart(fig_scatter, use_container_width=True)

corr_val = filtered_df["follower_count"].corr(filtered_df["engagement_rate"])
st.caption(f"Nilai korelasi antara jumlah follower dan engagement adalah **{corr_val:.2f}**, menunjukkan hubungan yang relatif lemah.")

# DISTRIBUTION
st.markdown("Distribusi Data")

col10, col11 = st.columns(2)

with col10:
    fig_box = px.box(
        filtered_df,
        x="platform",
        y="engagement_rate",
        labels={"platform": "Platform", "engagement_rate": "Engagement (%)"},
        title="Distribusi Engagement per Platform"
    )
    fig_box.update_layout(height=330)
    st.plotly_chart(fig_box, use_container_width=True)

    st.caption("Terdapat perbedaan sebaran engagement antar platform.")

with col11:
    fig_hist = px.histogram(
        filtered_df,
        x="follower_count",
        nbins=30,
        labels={"follower_count": "Jumlah Follower"},
        title="Distribusi Jumlah Follower"
    )
    fig_hist.update_layout(height=330)
    st.plotly_chart(fig_hist, use_container_width=True)

    median_val = filtered_df["follower_count"].median()
    st.caption(f"Sebagian besar akun memiliki jumlah follower di sekitar atau di bawah median ({int(median_val):,}).")

# HEATMAP
st.markdown("Korelasi Antar Variabel")

col_corr1, col_corr2, col_corr3 = st.columns([1,2,1])

with col_corr2:
    numeric_cols = [
        "follower_count", "posts_per_week", "engagement_rate",
        "ad_spend_(usd)", "conversion_rate", "campaign_reach"
    ]

    corr = filtered_df[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(3.8,2.8))
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax,
        annot_kws={"size": 7},
        cbar_kws={"shrink": 0.6}
    )
    ax.tick_params(axis='x', labelsize=7)
    ax.tick_params(axis='y', labelsize=7)

    st.pyplot(fig)

    corr_abs = corr.abs()
    corr_abs.values[[range(len(corr_abs))]*2] = 0
    max_pair = corr_abs.unstack().idxmax()
    max_val = corr_abs.unstack().max()

    st.caption(f"Hubungan terkuat terdapat antara **{max_pair[0]}** dan **{max_pair[1]}** dengan nilai korelasi sebesar **{max_val:.2f}**.")

# CONCLUSION
st.markdown("Kesimpulan")

st.markdown("""
Berdasarkan hasil visualisasi, dapat disimpulkan bahwa performa media sosial tidak hanya
dipengaruhi oleh jumlah follower, tetapi juga oleh tingkat engagement, konsistensi posting,
serta efektivitas kampanye iklan. Oleh karena itu, strategi pemasaran digital perlu
difokuskan pada peningkatan kualitas interaksi, bukan hanya pada pertumbuhan jumlah pengikut.
""")

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