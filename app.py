import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- تنسيق الـ RTL الاحترافي الشامل ---
st.markdown("""
<style>
    /* إجبار التطبيق بالكامل على اتجاه اليمين */
    .stApp {
        direction: rtl;
        text-align: right;
        background-color: #1a1a1a;
    }
    
    /* محاذاة كل أنواع النصوص والعناوين لليمين */
    h1, h2, h3, h4, h5, h6, p, li, div, span, label {
        text-align: right !important;
        direction: rtl !important;
    }

    /* تظبيط القوائم (النقاط) لتظهر على اليمين بشكل صحيح */
    ul, ol {
        padding-right: 1.5rem;
        padding-left: 0;
        list-style-position: inside;
    }

    .stTextInput>div>div>input {
        direction: rtl;
        text-align: right;
        background-color: #2d2d2d;
        color: white;
        border-radius: 12px;
    }

    .stButton>button {
        width: 100%;
        background-color: #f59e0b;
        color: white;
        border-radius: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity: 0.8;'>وصفات عربية دقيقة ومجربة</h4>", unsafe_allow_html=True)

st.divider()
chat_box = st.empty()
user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: لحم، أرز، بهارات")

if st.button("اكتشف الوصفات 🚀"):
    if user_ingredients.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # الأمر المطور: الإيموجي على اليمين + منع الإعلانات + منع الرغي
                    instruction = (
                        f"Ingredients: {user_ingredients}. Suggest 2 professional Arab recipes. "
                        "CRITICAL RULES: "
                        "1. NO introductions, NO footers, NO 'Support Pollinations', NO advertisements. "
                        "2. Start titles with emoji on the RIGHT, like: '🥘 [اسم الأكلة]'. "
                        "3. Headers MUST be: '🥘 اسم الوصفة', '🛒 المقادير', '👨‍🍳 طريقة التحضير', '✨ سر الشيف'. "
                        "4. Reply in Arabic ONLY. NO English at all."
                    )
                    safe_prompt = urllib.parse.quote(instruction)
                    seed = random.randint(1, 1000)
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        # تنظيف الرد من أي جمل إنجليزية قد تتسرب
                        clean_text = response.text
                        if "Powered by" in clean_text:
                            clean_text = clean_text.split("Powered by")[0]
                        
                        st.markdown(clean_text)
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، حاول ثانية.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
