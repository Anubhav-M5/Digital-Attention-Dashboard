import streamlit as st
import pandas as pd
import plotly.express as px

# Set up page configurations
st.set_page_config(page_title="Digital Attention Economy Dashboard", layout="wide")

st.title("📊 My Digital Attention Economy Dashboard")
st.markdown("---")

# 1. Load the cleaned datasets
@st.cache_data
def load_data():
    watches = pd.read_csv('cleaned_youtube_watches.csv')
    searches = pd.read_csv('cleaned_youtube_searches.csv')
    return watches, searches

try:
    df_watches, df_searches = load_data()
    
    # 2. Key Metrics Row
    total_videos = len(df_watches)
    edu_videos = len(df_watches[df_watches['focus_category'].isin(['Data Science & Tech', 'Education & Exam Prep'])])
    focus_percentage = (edu_videos / total_videos) * 100 if total_videos > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Videos Tracked", f"{total_videos:,}")
    col2.metric("Educational Content Logged", f"{edu_videos:,}")
    col3.metric("Productive Focus Score", f"{focus_percentage:.1f}%")
    
    st.markdown("---")
    
    # 3. Dynamic Charts Layout
    left_col, right_col = st.columns(2)
    
    with left_col:
        st.subheader("🎯 Attention Investment Breakdowns")
        fig_pie = px.pie(df_watches, names='focus_category', hole=0.4,
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with right_col:
        st.subheader("⏰ Hourly Focus Profile")
        hourly_data = pd.crosstab(df_watches['hour'], df_watches['focus_category']).reset_index()
        fig_bar = px.bar(hourly_data, x='hour', y=hourly_data.columns[1:], 
                         labels={'value': 'Count', 'hour': 'Hour of Day (24h)'},
                         barmode='stack')
        st.plotly_chart(fig_bar, use_container_width=True)
        
    # 4. Search Intent Table
    st.subheader("🔍 Top Academic/Technical Search Intent Queries")
    edu_searches = df_searches[df_searches['is_edu_search'] == 1]['query'].value_counts().reset_index()
    edu_searches.columns = ['Search Query Keyword', 'Frequency Count']
    st.dataframe(edu_searches.head(10), use_container_width=True)

except FileNotFoundError:
    st.error("Missing cleaned data files! Make sure you successfully ran the export cell in your Jupyter Notebook.")
