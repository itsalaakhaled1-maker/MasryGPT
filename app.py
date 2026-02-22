import streamlit as st
import requests
import urllib.parse
import random
import re

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { direction: rtl; text-align: right; background-color: #1a1a1a; }
    .stMarkdown, p, li, h1, h2, h3, h4 { direction: rtl !important; text-align: right !important; color: #ffffff !important; }
    ul, ol { padding-right: 1.5rem !important; list-style-position: inside !important; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3.5em; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.divider()

chat_box = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟")

if st.button("اكتشف الوصفات 🚀"):
    if user_input.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري محاولة الاتصال بالشيف... 🧑‍🍳"):
                try:
                    prompt = f"Recipes for {user_input}. Reply in Arabic. Bullet points only."
                    safe_prompt = urllib.parse.quote(prompt)
                    seed = random.randint(1, 1000)
                    
                    # موديل unity.. خفيف ومحدش بيستخدمه كتير
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}&model=unity"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        # تنظيف أي كود برمجي JSON يظهر في الرد
                        clean_text = re.sub(r'\{.*\}', '', response.text, flags=re.DOTALL)
                        st.markdown(clean_text.strip())
                        st.balloons()
                    else:
                        st.error("السيرفر لسه مضغوط.. انتظر دقيقة وجرب مرة أخيرة.")
                except:
                    st.error("مشكلة في الإنترنت عندك.")
