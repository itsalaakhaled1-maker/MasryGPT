import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- تنسيق الـ RTL والدارك مود ---
st.markdown("""
<style>
    .stApp { direction: rtl; text-align: right; background-color: #1a1a1a; }
    h1, h2, h3, h4, p, li, div, span, label { text-align: right !important; direction: rtl !important; color: #ffffff !important; }
    ul, ol { padding-right: 1.5rem; list-style-position: inside; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3.5em; }
</style>
""", unsafe_allow_html=True)

# عرض اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>👨‍🍳🥘</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.divider()

chat_box = st.empty()
user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: فول، زيت، ليمون")

if st.button("اكتشف الوصفات 🚀"):
    if user_ingredients.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # أمر مباشر جداً للموديل المستقر
                    prompt = f"Ingredients: {user_ingredients}. Suggest 2 simple Arab recipes. Reply ONLY in Arabic text. No JSON, No English."
                    safe_prompt = urllib.parse.quote(prompt)
                    
                    # رجعنا للموديل mistral الأسطوري في السرعة
                    seed = random.randint(1, 5000)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=mistral&seed={seed}"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        # تنظيف الرد من أي إعلانات أو كود
                        clean_text = response.text
                        if "{" in clean_text: clean_text = clean_text.split("{")[0]
                        if "Powered by" in clean_text: clean_text = clean_text.split("Powered by")[0]
                        
                        st.markdown(clean_text.strip())
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول شوية، اضغط 'اكتشف الوصفات' مرة تانية.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
