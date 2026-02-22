import streamlit as st
import requests
import urllib.parse
import random
import re

st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- تنسيق ChatGPT الاحترافي مع مسافات أمان كاملة ---
st.markdown("""
<style>
    .main .block-container { max-width: 800px; padding: 2rem; }
    .stApp { background-color: #1e1e1e; direction: rtl; }
    
    /* فقاعة الرد: ChatGPT Style */
    .ai-bubble {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 25px 35px;
        margin-top: 20px;
        color: #e0e0e0;
        line-height: 1.8;
        text-align: right;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .ai-bubble h2, .ai-bubble h3 { color: #f59e0b; margin-bottom: 15px; }
    
    /* تظبيط القوائم عشان النقط متبقاش لازقة في الطرف */
    .ai-bubble ul, .ai-bubble ol {
        padding-right: 35px !important;
        direction: rtl !important;
    }

    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white; border-radius: 10px; border: 1px solid #555;
    }

    .stButton>button {
        width: 100%; background-color: #f59e0b; color: white; border-radius: 10px; font-weight: bold; height: 3.5em; border: none;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر (صورة المعلم اللي بتدي هيبة)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        # تأكد إن ملف logo.png موجود بنفس الاسم ده على GitHub
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>👨‍🍳</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🧑‍🍳 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #f59e0b; font-size: 1.1rem; font-weight: bold; font-style: italic;'>أشطر من حماتك في المطبخ.. ومن غير تدخل في شؤونك الخاصة 😉🥘</p>", unsafe_allow_html=True)
st.divider()

# مكان عرض الرد
chat_placeholder = st.empty()

user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: بيض، جبنة، فول...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ترويض الشيف.. ادعي يطلع أكلة عدلة! 🍳🧑‍🍳"):
                try:
                    prompt = f"Recipes for {user_input}. Reply ONLY in Arabic. No JSON. No reasoning."
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,9999)}"
                    
                    response = requests.get(url, timeout=25)
                    
                    if response.status_code == 200:
                        res_text = response.text
                        
                        # تنظيف الرد لو السيرفر استهبل وبعت JSON
                        if 'content":"' in res_text:
                            matches = re.findall(r'"content":"(.*?)"', res_text, re.DOTALL)
                            if matches:
                                res_text = matches[-1].encode().decode('unicode_escape')
                        
                        # مسح أي بقايا كود إنجليزي
                        res_text = re.sub(r'\{.*\}', '', res_text, flags=re.DOTALL)
                        res_text = res_text.replace('reasoning_content', '').replace('assistant', '')

                        # عرض الرد داخل الفقاعة الشيك
                        st.markdown(f'<div class="ai-bubble">{res_text.strip()}</div>', unsafe_allow_html=True)
                        
                                              # عرض الرد داخل الفقاعة الشيك
                        st.markdown(f'<div class="ai-bubble">{res_text.strip()}</div>', unsafe_allow_html=True)
                        
                        # رجعنا للبلالين المضمونة عشان الشكل يبقى نضيف 🎈
                        st.balloons()

                    else:
                        st.error("السيرفر زحمة.. جرب تضغط تاني.")
                except:
                    st.error("مشكلة في الإنترنت.")
