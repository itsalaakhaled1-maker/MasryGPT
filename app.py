import streamlit as st
import requests
import urllib.parse
import random
import re

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- التنسيق العربي الـ RTL والدارك مود ---
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] { direction: rtl; text-align: right; background-color: #1a1a1a; }
    .stMarkdown, p, li, h1, h2, h3, h4 { direction: rtl !important; text-align: right !important; color: #ffffff !important; }
    ul, ol { padding-right: 1.5rem !important; list-style-position: inside !important; }
    .stTextInput>div>div>input { direction: rtl; text-align: right; background-color: #2d2d2d; color: white; border-radius: 12px; }
    .stButton>button { width: 100%; background-color: #f59e0b; color: white; border-radius: 12px; font-weight: bold; height: 3.5em; }
</style>
""", unsafe_allow_html=True)

# اللوجو
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
            with st.spinner("جاري ترويض السيرفر واستخراج الوصفة... 🧑‍🍳"):
                try:
                    # نستخدم موديل searchgpt لأنه الأكثر هدوءاً واستقراراً
                    prompt = f"Recipes for {user_input}. Reply ONLY in Arabic text. Use bullet points."
                    safe_prompt = urllib.parse.quote(prompt)
                    seed = random.randint(1, 10000)
                    url = f"https://text.pollinations.ai/{safe_prompt}?seed={seed}&model=searchgpt"
                    
                    response = requests.get(url, timeout=25)
                    
                    if response.status_code == 200:
                        res_text = response.text
                        
                        # --- تنظيف جراحي لمنع "الهيروغليفي" ---
                        # مسح أي JSON أو Reasoning Content
                        res_text = re.sub(r'\{.*\}', '', res_text, flags=re.DOTALL)
                        res_text = res_text.replace('reasoning_content', '').replace('assistant', '').replace('role', '').replace('content', '')
                        
                        # لو الرد لسه فيه بقايا إنجليزي أو أقواس
                        clean_text = res_text.strip().strip('"').strip("'")
                        
                        st.markdown(clean_text)
                        st.balloons()
                    else:
                        # تم إصلاح علامات التنصيص هنا عشان ميعملش SyntaxError
                        st.error('السيرفر لسه "ابن كلب" ومشغول 😂.. جرب تضغط تاني الآن.')
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
