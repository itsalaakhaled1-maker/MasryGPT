import streamlit as st
import requests
import urllib.parse
import random

# إعداد الصفحة مع عنوان أيقونة
st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- سحر التصميم (ChatGPT & Gemini Look) ---
st.markdown("""
<style>
    /* الحاوية الرئيسية: نحدد العرض ونسيب مسافات من الجناب */
    .main .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem; /* مسافة أمان من اليمين عشان البوردر يظهر */
    }
    
    /* خلفية التطبيق بالكامل */
    .stApp {
        background-color: #1e1e1e;
        direction: rtl;
    }

    /* تنسيق فقاعة الرد (AI Bubble) */
    .ai-response {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        color: #e0e0e0;
        line-height: 1.6;
        text-align: right;
    }

    /* تنسيق العناوين داخل الرد */
    .ai-response h3 { color: #f59e0b; margin-top: 0; }
    .ai-response h4 { color: #fbbf24; }

    /* تنسيق مربع الإدخال والزرار */
    .stTextInput>div>div>input {
        background-color: #2d2d2d;
        color: white;
        border-radius: 10px;
        border: 1px solid #555;
        padding: 10px;
    }

    .stButton>button {
        width: 100%;
        background-color: #f59e0b;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px;
        font-weight: bold;
    }
    
    /* منع النصوص من الالتصاق التام بالحافة اليمنى */
    p, li, div, h1, h2, h3, h4 {
        margin-right: 5px;
    }
</style>
""", unsafe_allow_html=True)

# الجزء العلوي (الهيدر)
st.markdown("<h1 style='text-align: center; color: white;'>🧑‍🍳 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #aaa;'>مساعدك الشخصي لابتكار أشهى الوصفات العربية</p>", unsafe_allow_html=True)

st.divider()

# مكان عرض الرد (شات بوكس)
chat_placeholder = st.empty()

# مدخل البيانات
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز، بصل...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ابتكار وصفاتك... 🪄"):
                try:
                    # طلب بسيط ومباشر للسيرفر
                    prompt = f"Recipes for {user_input}. Use Arabic only. Clear headers."
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,999)}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        # عرض الرد داخل "فقاعة" AI شيك
                        st.markdown(f"""
                        <div class="ai-response">
                            {response.text}
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، جرب تضغط تاني.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
