import streamlit as st
import base64

# 폰트 로딩 함수
def load_font(font_path):
    with open(font_path, "rb") as f:
        font_data = f.read()
    return base64.b64encode(font_data).decode()

# 폰트 파일 경로
font_regular = "fonts/NanumGothic-Regular.ttf"
font_bold = "fonts/NanumGothic-Bold.ttf"
font_extrabold = "fonts/NanumGothic-ExtraBold.ttf"

# CSS 스타일 적용
st.markdown(f"""
<style>
@font-face {{
    font-family: 'NanumGothic';
    src: url(data:font/ttf;base64,{load_font(font_regular)}) format('truetype');
    font-weight: normal;
}}
@font-face {{
    font-family: 'NanumGothic';
    src: url(data:font/ttf;base64,{load_font(font_bold)}) format('truetype');
    font-weight: bold;
}}
@font-face {{
    font-family: 'NanumGothic';
    src: url(data:font/ttf;base64,{load_font(font_extrabold)}) format('truetype');
    font-weight: 800;
}}
body {{
    font-family: 'NanumGothic', sans-serif;
}}
</style>
""", unsafe_allow_html=True)

# 페이지 설정
st.set_page_config(page_title="자기소개", page_icon="👤", layout="wide")

# 사이드바
st.sidebar.title("목차")
st.sidebar.markdown("---")
st.sidebar.write("📧 이메일: example@email.com")
st.sidebar.write("🔗 LinkedIn: [링크](https://linkedin.com)")
st.sidebar.write("🐙 GitHub: [링크](https://github.com)")

# 메인 콘텐츠
st.title("👋 안녕하세요! 자기소개 페이지입니다")

# 소개 섹션
st.markdown("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/150", caption="프로필 사진")
with col2:
    st.header("📖 소개")
    st.write("여기에 간단한 자기소개를 작성하세요. 예를 들어, 이름, 나이, 관심사 등을 적어보세요.")

# 경력 섹션
st.markdown("---")
st.header("💼 경력")
st.write("• 회사 A에서 개발자로 근무 (2020-현재)")
st.write("• 회사 B에서 인턴십 (2019)")

# 기술 섹션
st.markdown("---")
st.header("🛠️ 기술")
tech_col1, tech_col2 = st.columns(2)
with tech_col1:
    st.subheader("프로그래밍 언어")
    st.write("• Python")
    st.write("• JavaScript")
with tech_col2:
    st.subheader("도구 및 프레임워크")
    st.write("• Streamlit")
    st.write("• React")

# 연락처 섹션
st.markdown("---")
st.header("📞 연락처")
st.write("📧 이메일: example@email.com")
st.write("📱 전화: 010-1234-5678")
st.write("🏠 주소: 서울시 강남구")

# 푸터
st.markdown("---")
st.write("© 2023 자기소개 페이지. 모든 권리 보유.")
