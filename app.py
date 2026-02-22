import streamlit as st
import requests
import urllib.parse
import random
import re

st.set_page_config(page_title="شيف العرب AI", page_icon="🧑‍🍳", layout="centered")

# --- التنسيق الاحترافي (ChatGPT Style) مع مسافات أمان ---
st.markdown("""
<style>
    .main .block-container { max-width: 800px; padding: 2rem; }
    .stApp { background-color: #1e1e1e; direction: rtl; }
    
    .ai-response {
        background-color: #2d2d2d;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 30px;
        margin-bottom: 20px;
        color: #e0e0e0;
        line-height: 1.8;
        text-align: right;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    /* تظبيط القوائم عشان متتحشرش في اليمين */
    .ai-response ul, .ai-response ol {
        padding-right: 45px !important;
        margin-top: 10px;
        list-style-position: outside !important;
    }

    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white; border-radius: 10px; padding: 12px;
    }

    .stButton>button {
        width: 100%; background-color: #f59e0b; color: white; border-radius: 10px; font-weight: bold; height: 3.5em;
    }
</style>
""", unsafe_allow_html=True)

# الهيدر واللوجو (ثبتنا الصورة)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h1 style='text-align:center;'>🧑‍🍳🥘</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.divider()

chat_placeholder = st.empty()
user_input = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: بيض، جبنة، طماطم...")

if st.button("اكتشف الوصفات 🚀"):
    if not user_input.strip():
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_placeholder.container():
            with st.spinner("جاري تنظيف الرد من الهيروغليفي... 🪄"):
                try:
                    # أمر صارم جداً لمنع الرغي الإنجليزي
                    prompt = f"Recipes for {user_input}. Reply ONLY in Arabic text. No JSON. No reasoning."
                    safe_prompt = urllib.parse.quote(prompt)
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=openai&seed={random.randint(1,9999)}"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        raw_text = response.text
                        
                        # --- سحر الفلترة الجراحية ---
                        # لو الرد فيه كود (JSON) هنسحب منه النص العربي بس
                        if 'content":"' in raw_text:
                            # محاولة استخراج الكلام اللي بين "content":" و "
                            matches = re.findall(r'"content":"(.*?)"', raw_text, re.DOTALL)
                            if matches:
                                # فك شفرات الـ Unicode زي \n و \u
                                clean_text = matches[-1].encode().decode('unicode_escape')
                            else:
                                clean_text = raw_text
                        else:
                            clean_text = raw_text
                        
                        # مسح أي بقايا كود إنجليزي لسه موجودة
                        clean_text = re.sub(r'\{.*\}', '', clean_text, flags=re.DOTALL)
                        clean_text = clean_text.replace('reasoning_content', '').replace('assistant', '').replace('role', '')

                        st.markdown(f'<div class="ai-response">{clean_text.strip()}</div>', unsafe_allow_html=True)
                        st.balloons()
                    else:
                        st.error("السيرفر لسه معاند.. جرب تضغط تاني الآن.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
