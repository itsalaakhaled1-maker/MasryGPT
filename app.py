import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="شيف العرب الذكي", page_icon="🥘", layout="centered")

# --- التنسيق الليلي الفخم ---
st.markdown("""
<style>
    .stApp { background-color: #1a1a1a; }
    .stButton>button {
        background-color: #f59e0b;
        color: white; border-radius: 12px; border: none;
        padding: 12px 28px; font-weight: bold; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #d97706; transform: scale(1.05); }
    .stTextInput>div>div>input {
        background-color: #2d2d2d; color: white;
        border-radius: 12px; border: 1px solid #444;
    }
    p, div, span, label, h1, h4 { color: #ffffff !important; }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True) 

st.markdown("<h1 style='text-align: center;'>🥘 شيف العرب الذكي</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; opacity: 0.8;'>أدخل المكونات وسأقترح عليك أشهى الأطباق العربية فوراً</h4>", unsafe_allow_html=True)

st.divider()

chat_box = st.empty()

user_ingredients = st.text_input("ماذا يوجد في مطبخك؟", placeholder="مثلاً: فول، طماطم، بيض")

if st.button("اقترح وصفات شهية 🚀"):
    if user_ingredients.strip() == "":
        st.warning("فضلاً، اكتب المكونات أولاً.")
    else:
        with chat_box.container():
            with st.spinner("جاري ابتكار وصفة سريعة... 🧑‍🍳"):
                try:
                    # استخدمنا موديل p1 السريع والطلقة 🚀
                    instruction = f"I have: {user_ingredients}. Suggest 2 simple Arab recipes. Reply in short Arabic. No English."
                    safe_prompt = urllib.parse.quote(instruction)
                    
                    # الرابط المحدث مع الموديل السريع
                    url = f"https://text.pollinations.ai/{safe_prompt}?model=p1"
                    
                    response = requests.get(url, timeout=20)
                    
                    if response.status_code == 200:
                        st.success("وصفات الشيف السريعة:")
                        st.write(response.text)
                    else:
                        st.error("السيرفر لسه مزدحم، جرب تضغط مرة تانية الآن.")
                except:
                    st.error("مشكلة في الاتصال، حاول مرة أخرى.")
