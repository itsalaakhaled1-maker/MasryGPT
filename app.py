import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- تنسيق "نفس عميق" للكلام (ChatGPT RTL) ---
st.markdown("""
<style>
    .main .block-container {
        max-width: 800px;
        padding: 2rem;
    }
    .stApp { background-color: #1e1e1e; direction: rtl; }

    /* فقاعة الرد مع مساحة أمان للأرقام والنقاط */
    .ai-response {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 25px 40px 25px 20px; /* زودنا اليمين لـ 40 عشان الأرقام تظهر */
        margin-bottom: 20px;
        color: #e0e0e0;
        line-height: 1.8;
        text-align: right;
    }

    /* إجبار القوائم تبعد عن الحافة اليمين */
    .ai-response ul, .ai-response ol {
        padding-right: 30px !important;
        margin-right: 10px !important;
        direction: rtl !important;
    }

    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white; border-radius: 10px; padding: 10px;
    }

    .stButton>button {
        width: 100%; background-color: #f59e0b; color: white; border-radius: 10px; font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# تظبيط اللوجو والعنوان
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # رجعنا اللوجو وبنأكد عليه
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>🧑‍🍳</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>مساعدك الشخصي لابتكار أشهى الوصفات العربية</p>", unsafe_allow_html=True)

st.divider()

chat_placeholder = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ابتكار وصفاتك... 🪄"):
                try:
                    # طلب بسيط ومباشر
                    prompt = f"Recipes for {user_input}. Reply in Arabic. Use clear headers and bullet points."
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,999)}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        # عرض الرد داخل الفقاعة المتظبطة
                        st.markdown(f'<div class="ai-response">{response.text}</div>', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، جرب تضغط تاني.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
