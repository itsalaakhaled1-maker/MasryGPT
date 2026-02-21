import streamlit as st
import requests
import urllib.parse

# 1. إعدادات الواجهة (يجب أن تكون أول سطر)
st.set_page_config(page_title="العالم المصري", page_icon="🧠", layout="centered")

# 2. إضافة الثيم المخصص (CSS) لتجميل التطبيق
st.markdown("""
<style>
    /* تغيير لون الخلفية لتدرج لوني أنيق */
    .stApp {
        background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* تجميل زر الإرسال */
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
        transform: scale(1.05); /* حركة تكبير بسيطة عند وقوف الماوس */
    }
    
    /* تجميل مربع النص */
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #2e7bcf;
    }
</style>
""", unsafe_allow_html=True)

# 3. عرض الصورة فوق (في المنتصف)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # الصورة اللي هتتعرض (لازم نرفعها على جيت هاب برضه)
    st.image("logo.png", use_container_width=True) 

# 4. العنوان الرئيسي والجملة الترحيبية (في المنتصف وبخطوط أكبر)
st.markdown("<h1 style='text-align: center; color: #1e293b;'>مصري عارف كل حاجه 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #2e7bcf;'>اسألني في أي حاجة.. أنا متصل بسيرفر مصري صاروخي ومجاني!</h4>", unsafe_allow_html=True)

st.divider() # خط فاصل أنيق

# 5. مربع إدخال النص
user_input = st.text_input("كيف يمكنني مساعدتك اليوم؟ (مثلاً: نصيحة سريعة للنجاح)")

if st.button("إرسال السؤال 🚀"):
    if user_input.strip() == "":
        st.warning("الرجاء كتابة سؤالك أولاً.")
    else:
        with st.spinner("جاري التفكير وكتابة الرد... 🧠"):
            try:
                # تشفير النص
                safe_prompt = urllib.parse.quote(user_input)
                # السيرفر المعتمد
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
