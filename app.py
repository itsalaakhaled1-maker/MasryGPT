import streamlit as st
import requests
import urllib.parse
import random
import re

st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- التنسيق الاحترافي النهائى (ChatGPT Style) ---
st.markdown("""
<style>
    .main .block-container { max-width: 800px; padding: 2rem; }
    .stApp { background-color: #1e1e1e; direction: rtl; }
    
    .ai-bubble {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 25px 35px;
        margin-top: 20px;
        color: #e0e0e0;
        line-height: 1.8;
        text-align: right;
    }

    .ai-bubble h1, .ai-bubble h2, .ai-bubble h3 { color: #f59e0b; margin-bottom: 15px; }

    /* إجبار القوائم (المكونات) تظهر تحت بعضها بوضوح */
    .ai-bubble ul, .ai-bubble ol {
        padding-right: 40px !important;
        display: block !important;
    }
    
    .ai-bubble li { margin-bottom: 10px; display: list-item !important; }

    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white; border-radius: 10px; padding: 12px;
    }

    .stButton>button {
        width: 100%; background-color: #f59e0b; color: white; border-radius: 10px; font-weight: bold; height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>🧑‍🍳</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🧑‍🍳 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #f59e0b; font-weight: bold;'>أشطر من حماتك في المطبخ.. ومن غير تدخل في شؤونك الخاصة 😉🥘</p>", unsafe_allow_html=True)
st.divider()

chat_placeholder = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: بيض، جبنة، فول...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ترويض الشيف.. بلاش تضغط عليه عشان ميقلبش عليك! 😉🪄"):
                try:
                    # طلب صارم جداً للتنسيق الرأسي
                    prompt = f"Recipe for {user_input}. Arabic ONLY. VERTICAL ingredients list with bullet points. Clear steps."
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,9999)}"
                    
                    response = requests.get(url, timeout=25)
                    
                    if response.status_code == 200:
                        res_text = response.text
                        
                        # تنظيف الرد من أي JSON أو Reasoning
                        if 'content":"' in res_text:
                            matches = re.findall(r'"content":"(.*?)"', res_text, re.DOTALL)
                            if matches: res_text = matches[-1].encode().decode('unicode_escape')
                        
                        res_text = re.sub(r'\{.*\}', '', res_text, flags=re.DOTALL)
                        
                        # إصلاح مشكلة المكونات العرضية: تحويل الشرطات "-" لسطور جديدة
                        clean_text = res_text.replace(" - ", "\n- ").replace(" * ", "\n* ")

                        st.markdown(f'<div class="ai-bubble">{clean_text.strip()}</div>', unsafe_allow_html=True)
                        st.balloons() # رجعنا للبلالين النظيفة المضمونة
                    else:
                        st.error("السيرفر مشغول، جرب تاني.")
                except:
                    st.error("مشكلة في الإنترنت.")
