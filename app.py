import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- تنسيق RTL والدارك مود ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { direction: rtl; text-align: right; background-color: #1a1a1a; }
    .stMarkdown, p, li, h1, h2, h3, h4 { direction: rtl !important; text-align: right !important; color: #ffffff !important; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3.5em; }
</style>
""", unsafe_allow_html=True)

# محاولة عرض اللوجو - لو مش موجود هيعرض إيموجي شيك
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # جرب تحط رابط صورة حقيقي هنا لو عندك، أو سيبه يحمل logo.png
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>👨‍🍳🥘</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.divider()

chat_box = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز، بصل")

if st.button("اكتشف الوصفات 🚀"):
    if user_input.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري الاتصال بالشيف... 🧑‍🍳"):
                try:
                    # طلب بسيط جداً عشان السيرفر ميهنجش
                    prompt = f"Suggest 2 simple Arab recipes with {user_input}. Reply in Arabic only. Use bullet points."
                    safe_prompt = urllib.parse.quote(prompt)
                    
                    # استخدمنا موديل openai وهو الأكثر استقراراً
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,1000)}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        # عرض الرد مباشرة
                        st.markdown(response.text)
                        st.balloons()
                    else:
                        st.error("السيرفر لسه مضغوط شوية.. جرب تضغط تاني بعد 5 ثواني.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
