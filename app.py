import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="العالم المصري", page_icon="🧠", layout="centered")

# --- بداية سحر الدارك مود ---
st.markdown("""
<style>
    .stApp {
        background-color: #212121;
    }
    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        background-color: #2f2f2f;
        color: white;
        border-radius: 12px;
        border: 1px solid #555;
    }
    p, div, span, label {
        color: #e0e0e0 !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True) 

st.markdown("<h1 style='text-align: center; color: #ffffff;'>مصري عارف كل حاجه 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #a0aec0;'>اسألني في أي حاجة.. أنا متصل بسيرفر مصري صاروخي ومجاني!</h4>", unsafe_allow_html=True)

st.divider()

chat_box = st.empty()

user_input = st.text_input("كيف يمكنني مساعدتك اليوم؟")

if st.button("إرسال السؤال 🚀"):
    if user_input.strip() == "":
        st.warning("الرجاء كتابة سؤالك أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري التفكير... 🧠"):
                try:
                    # أوامر صارمة ومختصرة جداً
                    magic_prompt = f"Reply ONLY in funny Egyptian Arabic slang. Short and natural response to: {user_input}"
                    safe_prompt = urllib.parse.quote(magic_prompt)
                    
                    # استخدمنا موديل mistral عشان نلغي الرغي الإنجليزي
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=mistral"
                    
                    response = requests.get(url, timeout=30)
                    
                    if response.status_code == 200:
                        st.success("الرد:")
                        st.write(response.text)
                    else:
                        st.error("السيرفر مهنج ثواني، جرب تاني.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
