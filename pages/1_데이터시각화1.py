import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# CSS 스타일 적용 (Google Fonts 사용)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&display=swap');
body {
    font-family: 'Nanum Gothic', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 데이터 시각화 예제")

st.markdown("이 페이지는 다양한 그래프를 그리는 예제를 보여줍니다.")

# 샘플 데이터 생성
np.random.seed(42)
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y1': np.random.randn(100).cumsum(),
    'y2': np.random.randn(100).cumsum() + 10,
    'category': np.random.choice(['A', 'B', 'C'], 100),
    'value': np.random.randint(1, 100, 100)
})

# 선 그래프
st.header("선 그래프 (Line Chart)")
fig_line = px.line(data, x='x', y=['y1', 'y2'], title="누적 랜덤 데이터")
st.plotly_chart(fig_line)

# 막대 그래프
st.header("막대 그래프 (Bar Chart)")
bar_data = data.groupby('category')['value'].mean().reset_index()
fig_bar = px.bar(bar_data, x='category', y='value', title="카테고리별 평균 값")
st.plotly_chart(fig_bar)

# 산점도
st.header("산점도 (Scatter Plot)")
fig_scatter = px.scatter(data, x='y1', y='y2', color='category', title="산점도 예제")
st.plotly_chart(fig_scatter)

# 히스토그램
st.header("히스토그램 (Histogram)")
fig_hist = px.histogram(data, x='value', nbins=20, title="값의 분포")
st.plotly_chart(fig_hist)

# 박스 플롯
st.header("박스 플롯 (Box Plot)")
fig_box = px.box(data, x='category', y='value', title="카테고리별 값의 분포")
st.plotly_chart(fig_box)
