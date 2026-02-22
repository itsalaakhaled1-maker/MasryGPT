import streamlit as st
import requests
import urllib.parse
import random

# إعداد الصفحة
st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- التنسيق العربي الاحترافي (RTL) والدارك مود ---
st.markdown("""
<style>
    /* قلب اتجاه التطبيق بالكامل لليمين */
    .stApp {
        direction: rtl;
        text-align: right;
        background-color: #1a1a1a;
    }
    
    /* تظبيط أماكن العناوين والنصوص */
    h1, h4, p, div, span, label {
        text-align: right !important;
        color: #ffffff !important;
    }

    /* تظبيط مربع إدخال النص عشان المؤشر يبدأ من اليمين */
    .stTextInput>div>div>input {
        direction: rtl;
        text-align: right;
        background-color: #2d2d2d;
        color: white;
        border-radius: 12px;
        border: 1px solid #444;
    }

    /* تنسيق زر الإرسال */
    .stButton>button {
        width: 100%; /* الزرار بعرض الصفحة عشان السهولة */
        background-color: #f59e0b;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 12px 28px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #d97706;
        transform: scale(1.02);
    }
    
    /* تظبيط أيقونات التحميل والرسائل */
    .stSpinner, .stAlert {
        direction: rtl;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# محاذاة اللوجو
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity: 0.8;'>أدخل المكونات وسأقترح عليك أشهى الأطباق العربية</h4>", unsafe_allow_html=True)

st.divider()

# حجز مكان الرد فوق مربع النص
chat_box = st.empty()

# خانة الكتابة (بقت بتبدأ من اليمين دلوقتي)
user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز، بصل")

if st.button("اكتشف الوصفات 🚀"):
    if user_ingredients.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # الأمر المحدث لضمان الجودة ومنع الكلام الروبوتي
                    instruction = (
                        f"Suggest 2 delicious Arab recipes for: {user_ingredients}. "
                        "Rules: 1. Use natural Arabic culinary terms. "
                        "2. NO marketing fluff. "
                        "3. Use headers: '### 🥘 اسم الوصفة', '#### 🛒 المقادير', '#### 👨‍🍳 طريقة التحضير', '#### ✨ سر الشيف'. "
                        "4. Reply in Arabic only."
                    )
                    safe_prompt = urllib.parse.quote(instruction)
                    
                    seed = random.randint(1, 1000)
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        st.markdown(response.text)
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، حاول ثانية.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
