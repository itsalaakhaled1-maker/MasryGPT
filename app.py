import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="شيف التلاجة الذكي", page_icon="🍳", layout="centered")

# --- تنسيق الدارك مود الفخم ---
st.markdown("""
<style>
    .stApp { background-color: #212121; }
    .stButton>button {
        background-color: #ef4444; /* لون أحمر فاتح للشهية */
        color: white; border-radius: 12px; border: none;
        padding: 10px 24px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #dc2626; transform: scale(1.05); }
    .stTextInput>div>div>input {
        background-color: #2f2f2f; color: white;
        border-radius: 12px; border: 1px solid #555;
    }
    p, div, span, label { color: #e0e0e0 !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True) 

st.markdown("<h1 style='text-align: center; color: #ffffff;'>شيف التلاجة الذكي 🍳</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #a0aec0;'>اكتبلي المكونات اللي عندك.. وهقولك تطبخ إيه في ثواني!</h4>", unsafe_allow_html=True)

st.divider()

# حجز مكان الرد فوق
chat_box = st.empty()

# مدخل البيانات
user_ingredients = st.text_input("إيه المكونات اللي في تلاجتك؟ (مثلاً: بيض، طماطم، فلفل)")

if st.button("اقترح عليا أكلة 🚀"):
    if user_ingredients.strip() == "":
        st.warning("قولي بس عندك إيه في التلاجة الأول.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفة مصرية... 🧑‍🍳"):
                try:
                    # أمر مخصص للمطبخ والموديل المستقر
                    instruction = f"I have these ingredients: {user_ingredients}. Suggest 2 simple Egyptian recipes I can make. Reply ONLY in Egyptian Arabic slang. Keep it short and organized with bullet points. No English."
                    safe_prompt = urllib.parse.quote(instruction)
                    
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=mistral"
                    
                    response = requests.get(url, timeout=30)
                    
                    if response.status_code == 200:
                        st.success("مقترحات الشيف:")
                        st.write(response.text)
                    else:
                        st.error("السيرفر بياخد نفسه، جرب كمان ثانية.")
                except:
                    st.error("تأكد من اتصالك بالإنترنت.")
