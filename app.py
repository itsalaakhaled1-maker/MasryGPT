import streamlit as st
import requests
import urllib.parse
import random
import re # مكتبة التنظيف الجراحي

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- التنسيق العربي العنيف (RTL) لضمان عدم الانحراف ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"], .stMarkdown, p, li {
        direction: rtl !important;
        text-align: right !important;
    }
    .stApp { background-color: #1a1a1a; }
    h1, h2, h3, h4, span, label { text-align: right !important; direction: rtl !important; color: #ffffff !important; }
    ul, ol { padding-right: 1.5rem !important; list-style-position: inside !important; direction: rtl !important; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3.5em; }
</style>
""", unsafe_allow_html=True)

# عرض اللوجو أو إيموجي بديل
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
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
            with st.spinner("جاري ابتكار وصفاتك... 🧑‍🍳"):
                try:
                    # طلب الوصفة بأمر إنجليزي لضمان دقة السيرفر
                    prompt = f"Suggest 2 professional Arab recipes for: {user_input}. Reply in Arabic only. Use headers: '### اسم الوصفة', '#### المقادير', '#### التحضير'."
                    safe_prompt = urllib.parse.quote(prompt)
                    
                    seed = random.randint(1, 9999)
                    # جربنا موديل searchgpt هنا لأنه أكثر استقراراً
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=searchgpt&seed={seed}"
                    
                    response = requests.get(url, timeout=25)
                    
                    if response.status_code == 200:
                        res_text = response.text
                        
                        # --- مرحلة التنظيف الجراحي ---
                        # 1. مسح أي JSON أو Reasoning content بيظهر في البداية أو النهاية
                        res_text = re.sub(r'\{.*?"content":\s*?"', '', res_text, flags=re.DOTALL)
                        res_text = re.sub(r'"\s*?,\s*?"reasoning_content".*?\}', '', res_text, flags=re.DOTALL)
                        res_text = re.sub(r'\{.*?\}', '', res_text, flags=re.DOTALL)
                        
                        # 2. مسح الكلمات الإنجليزية الشائعة اللي بتسربها السيرفرات
                        for word in ["assistant", "reasoning_content", "role", "content", "Powered by"]:
                            res_text = res_text.replace(word, "")
                        
                        # عرض النص النهائي النظيف
                        st.markdown(res_text.strip())
                        st.balloons()
                    else:
                        st.error("السيرفر زحمة جداً، اضغط مرة أخرى الآن.")
                except:
                    st.error("مشكلة في الاتصال، حاول مرة ثانية.")
