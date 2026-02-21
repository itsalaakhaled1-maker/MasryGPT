import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="العالم المصري", page_icon="🧠", layout="centered")

st.markdown("""
<style>
    .stApp {
        background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton>button {
        background-color: #2e7bcf;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1b5b9e;
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #2e7bcf;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True) 

st.markdown("<h1 style='text-align: center; color: #1e293b;'>مصري عارف كل حاجه 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #2e7bcf;'>اسألني في أي حاجة.. أنا متصل بسيرفر مصري صاروخي ومجاني!</h4>", unsafe_allow_html=True)

st.divider() 

user_input = st.text_input("كيف يمكنني مساعدتك اليوم؟ (مثلاً: نصيحة سريعة للنجاح)")

if st.button("إرسال السؤال 🚀"):
    if user_input.strip() == "":
        st.warning("الرجاء كتابة سؤالك أولاً.")
    else:
        with st.spinner("جاري التفكير وكتابة الرد... 🧠"):
            try:
                                # غرفة العمليات السرية (شخصية الشات بوت مفصولة عن السؤال)
                # أمر صارم جداً بعدم استخدام أي رموز أو حروف غير عربية
                system_prompt = "You are a normal Egyptian guy. Reply ONLY in everyday Egyptian Arabic. CRITICAL RULE: You MUST ONLY output standard Arabic letters. DO NOT output any English letters, symbols, HTML, or weird codes. Just clean Arabic text."
                
                # تشفير الأوامر والسؤال كل واحد لوحده
                safe_system = urllib.parse.quote(system_prompt)
                safe_prompt = urllib.parse.quote(user_input)
                
                # الرابط الجديد اللي بيفهم الأوامر صح
                url = f"https://text.pollinations.ai/{safe_prompt}?system={safe_system}"

                response = requests.get(url, timeout=30)
                
                if response.status_code == 200:
                    st.success("الرد:")
                    st.write(response.text)
                else:
                    st.error("السيرفر بياخد نفسه، جرب تدوس إرسال كمان ثواني.")
                    
            except requests.exceptions.Timeout:
                st.error("السيرفر خد وقت طويل، جرب مرة تانية.")
            except Exception as e:
                st.error("تأكد من اتصالك بالإنترنت.")
