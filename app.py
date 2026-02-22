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
        width: 100%;
        background: linear-gradient(90deg, #f59e0b, #fbbf24); /* تدرج ذهبي */
        color: white;
        border-radius: 12px;
        font-weight: bold;
        height: 3.8em;
        border: none;
        transition: 0.3s ease-in-out;
        font-size: 1.2rem;
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.4);
    }
    /* تصميم الزرار الأسطوري */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); /* تدرج لوني فخم */
        color: white !important;
        border-radius: 15px; /* زوايا أنعم */
        font-weight: 800;
        height: 4em;
        border: none;
        font-size: 1.2rem;
        letter-spacing: 1px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); /* حركة مطاطية شيك */
        box-shadow: 0 10px 20px -10px rgba(245, 158, 11, 0.5);
        cursor: pointer;
    }

    /* تأثير عند الوقوف بالماوس أو اللمس */
    .stButton>button:hover {
        transform: translateY(-5px); /* يرتفع لفوق سنة */
        box-shadow: 0 15px 25px -5px rgba(245, 158, 11, 0.6);
        background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%);
        color: white !important;
    }

    /* تأثير عند الضغط */
    .stButton>button:active {
        transform: scale(0.95); /* ينضغط لجوه */
    }

        /* إخفاء قائمة المطورين والفوتر المزعج */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;} /* وده عشان يخفي الشريط اللي فوق لو ظهر */
    .stAppDeployButton {display: none;} /* وده عشان يخفي زرار Manage App تحديداً */

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

if st.button("أبهِر حماتك بالطبخة! 😉🥘"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري ترويض الشيف وتجهيز الأكلة... 🍳😂"):
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

                        # العرض النهائي الشيك
                        st.markdown(f'<div class="ai-bubble">{res_text.strip()}</div>', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("السيرفر زحمة.. جرب تضغط تاني.")
                except:
                    st.error("مشكلة في الإنترنت.")
