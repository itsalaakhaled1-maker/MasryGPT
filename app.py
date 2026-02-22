import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- التنسيق النهائي: مسافات واسعة وتنسيق قوائم احترافي ---
st.markdown("""
<style>
    .main .block-container { max-width: 800px; padding: 2rem; }
    .stApp { background-color: #1e1e1e; direction: rtl; }

    /* فقاعة الرد: ضفنا مساحة داخلية (Padding) مريحة جداً */
    .ai-response {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        color: #e0e0e0;
        line-height: 1.8;
        text-align: right;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    /* تنسيق القوائم لضمان ظهور النقط والأرقام بوضوح على اليمين */
    .ai-response ul, .ai-response ol {
        padding-right: 40px !important;
        margin-top: 10px;
        margin-bottom: 10px;
        list-style-position: outside !important;
    }
    
    .ai-response li { margin-bottom: 8px; }

    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white; border-radius: 10px; padding: 12px;
    }

    .stButton>button {
        width: 100%; background-color: #f59e0b; color: white; border-radius: 10px; font-weight: bold; height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر مع اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>🧑‍🍳🥘</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>وصفات عربية أصيلة بدون 'فروديت' ولا تعقيد 😂</p>", unsafe_allow_html=True)

st.divider()

chat_placeholder = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: فول، بيض، جبنة...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ترويض الشيف وتجهيز الوصفة... 🪄"):
                try:
                    # الأمر المحدث: منع الأسماء الغريبة وإجبار التنسيق الرأسي
                    prompt = (
                        f"Suggest 2 REAL Arab recipes for: {user_input}. "
                        "RULES: 1. Use standard Arab names only (NO myth names like Aphrodite). "
                        "2. List ingredients VERTICALLY with bullet points. "
                        "3. Reply in clear Arabic text only."
                    )
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,9999)}"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        # عرض الرد داخل الفقاعة المحسنة
                        st.markdown(f'<div class="ai-response">{response.text}</div>', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، جرب تضغط 'اكتشف الوصفات' مرة تانية.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
