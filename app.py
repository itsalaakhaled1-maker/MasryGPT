import streamlit as st
import requests
import urllib.parse
import random
import re # لمسح أي كود غريب

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- التنسيق العربي الاحترافي الشامل (RTL) ---
st.markdown("""
<style>
    .stApp { direction: rtl; text-align: right; background-color: #1a1a1a; }
    h1, h2, h3, h4, p, li, div, span, label { text-align: right !important; direction: rtl !important; color: #ffffff !important; }
    ul, ol { padding-right: 1.5rem; padding-left: 0; list-style-position: inside; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3em; }
</style>
""", unsafe_allow_html=True)

# عرض اللوجو (حاولنا نخليه يظهر بشكل مضمون)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align:center;'>👨‍🍳🥘</h2>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity: 0.8;'>وصفات عربية دقيقة ومجربة</h4>", unsafe_allow_html=True)

st.divider()
chat_box = st.empty()
user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: دجاج، أرز، بصل")

if st.button("اكتشف الوصفات 🚀"):
    if user_ingredients.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # أوامر صارمة جداً لمنع الردود البرمجية (JSON)
                    instruction = (
                        f"Suggest 2 professional Arab recipes for: {user_ingredients}. "
                        "Rules: Reply ONLY with the recipe text in Arabic. "
                        "NO JSON, NO reasoning_content, NO English letters. "
                        "Headers: '### 🥘 اسم الوصفة', '#### 🛒 المقادير', '#### 👨‍🍳 التحضير', '#### ✨ السر'."
                    )
                    safe_prompt = urllib.parse.quote(instruction)
                    seed = random.randint(1, 9999)
                    
                    # استخدمنا موديل p1 لأنه الأقل إنتاجاً للكود البرمجي
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}&model=p1"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        raw_text = response.text
                        
                        # سحر التنظيف: مسح أي نصوص برمجية (الهيروغليفي) لو ظهرت
                        clean_text = re.sub(r'\{.*\}', '', raw_text, flags=re.DOTALL) # مسح أي JSON
                        clean_text = clean_text.replace('role":"assistant"', '').replace('reasoning_content":', '')
                        
                        st.markdown(clean_text.strip())
                        st.balloons()
                    else:
                        st.error("السيرفر مشغول، حاول مرة أخرى.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
