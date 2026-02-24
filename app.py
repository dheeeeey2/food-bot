import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="사내 맛집 추천 봇", page_icon="🍽️")
st.title("🍽️ 사내 맛집/회식 추천 AI")
st.markdown("양재역/강남역 근처 맛집이나 회식 장소를 물어보세요!")

# Streamlit 비밀 금고(Secrets)에서 API 키를 몰래 가져와서 세팅합니다.
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.5-flash') 

# 사용자 입력창 (API 키 입력창은 사라짐!)
user_input = st.text_input("어떤 맛집을 찾으시나요? (예: 강남역 가성비 좋은 점심 맛집 알려줘)")

if st.button("추천 받기"):
    if user_input:
        prompt = f"""
        너는 센스있는 사내 맛집 추천 전문가야. 
        사용자의 요청에 맞춰 3~4곳의 식당을 추천해줘.
        형식:
        ### 1. 식당 이름
        * **추천 메뉴:** * **추천 이유:** 사용자 요청: {user_input}
        """
        with st.spinner('맛집 데이터를 분석 중입니다... 🧐'):
            try:
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
    else:
        st.warning("질문을 먼저 입력해주세요!")
