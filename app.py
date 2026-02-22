import streamlit as st
import requests
import urllib.parse
import random

# إعداد الصفحة بالاسم الجديد
st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# التنسيق الليلي الفخم (Dark Mode)
st.markdown("""
<style>
    .stApp { background-color: #1a1a1a; }
    .stButton>button {
        background-color: #f59e0b; /* لون برتقالي ملكي */
        color: white; border-radius: 12px; border: none;
        padding: 12px 28px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #d97706; transform: scale(1.05); }
    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white;
        border-radius: 12px; border: 1px solid #444;
    }
    p, div, span, label, h1, h4 { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

# محاذاة اللوجو والعناوين
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # تأكد أن ملف logo.png موجود في المشروع على GitHub أو امسح هذا السطر
    try:
        st.image("logo.png", use_container_width=True)
    except:
        pass

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity: 0.8;'>أدخل المكونات المتوفرة وسأعطيك وصفات عربية شهية</h4>", unsafe_allow_html=True)

st.divider()

# حجز مكان الرد فوق مربع النص كما طلبت
chat_box = st.empty()

user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز، بصل")

if st.button("اكتشف الوصفات 🚀"):
    if user_ingredients.strip() == "":
        st.warning("يرجى كتابة بعض المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # أوامر مختصرة لضمان السرعة وعدم التهنيج
                    # ده السطر الجديد اللي هيخلي الشيف بيفهم في الأصول
                    instruction = f"Suggest 2 delicious Arab recipes for: {user_ingredients}. Use natural Arabic cooking terms (like 'نصفّي الفول' not 'وسادة مرطبة'). Keep titles unique and steps clear. Reply in Arabic only."
                    safe_prompt = urllib.parse.quote(prompt)
                    
                    # استخدام seed عشوائي للهروب من ضغط السيرفر
                    seed = random.randint(1, 1000)
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}"
                    
                    response = requests.get(url, timeout=15)
                    
                    if response.status_code == 200:
                        st.success("إليك اقتراحات الشيف:")
                        st.write(response.text)
                    else:
                        st.error("السيرفر مشغول، حاول مرة أخرى بعد قليل.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
