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
                # --- السحر هنا: حقن الشخصية المصرية ---
                persona = "أنت مساعد ذكي مصري، دمك خفيف جداً. ردك دايماً لازم يكون باللهجة المصرية العامية 100%. ابدأ كلامك دايماً بإفيه أو تريقة خفيفة أو هزار، وبعدين جاوب على السؤال. ممنوع تتكلم لغة عربية فصحى نهائياً. إليك سؤال المستخدم: "
                
                # لزقنا الشخصية في السؤال بتاعك
                full_message = persona + user_input
                safe_prompt = urllib.parse.quote(full_message)
                
                url = f"https://text.pollinations.ai/{safe_prompt}"
                
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
