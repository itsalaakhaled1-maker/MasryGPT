import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="العالم المصري", page_icon="🧠", layout="centered")

# --- بداية سحر الدارك مود ---
st.markdown("""
<style>
    /* لون الخلفية أسود/رمادي غامق شيك زي شات جي بي تي */
    .stApp {
        background-color: #212121;
    }
    
    /* تجميل زر الإرسال */
    .stButton>button {
        background-color: #3b82f6; /* أزرق هادي */
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
    
    /* تجميل مربع النص عشان يليق مع الأسود */
    .stTextInput>div>div>input {
        background-color: #2f2f2f; /* خلفية المربع رمادي غامق */
        color: white; /* لون الكتابة أبيض */
        border-radius: 12px;
        border: 1px solid #555;
    }
    
    /* تلوين النصوص العادية والرسائل عشان تظهر بوضوح */
    p, div, span, label {
        color: #e0e0e0 !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("logo.png", use_container_width=True) 

# غيرنا ألوان العناوين عشان تنور في الخلفية الغامقة
st.markdown("<h1 style='text-align: center; color: #ffffff;'>مصري عارف كل حاجه 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #a0aec0;'>اسألني في أي حاجة.. أنا متصل بسيرفر مصري صاروخي ومجاني!</h4>", unsafe_allow_html=True)

st.divider() # خط فاصل أنيق

# --- الحيلة الذكية: حجز مكان فاضي للرد عشان يظهر فوق ---
chat_box = st.empty()

# مربع إدخال النص (بقى تحت المكان الفاضي)
user_input = st.text_input("كيف يمكنني مساعدتك اليوم؟ (مثلاً: نصيحة سريعة للنجاح)")

if st.button("إرسال السؤال 🚀"):
    if user_input.strip() == "":
        st.warning("الرجاء كتابة سؤالك أولاً.")
    else:
        # هنخلي التحميل والرد يظهروا جوه المكان الفاضي اللي حجزناه فوق
        with chat_box.container():
            with st.spinner("جاري التفكير وكتابة الرد... 🧠"):
                try:
                    # أوامر السيستم الصارمة عشان ميهلوسش
                    # أمر سيستم هادي وبسيط عشان السيرفر ميتجننش
                    system_prompt = "رد كأنك شاب مصري جدع وبسيط. استخدم عامية مصرية خفيفة جداً ومفهومة للكل. الرد لازم يكون قصير ومباشر وبدون أي مقدمات أو أكواد أو حروف إنجليزية."
                    
                    safe_system = urllib.parse.quote(system_prompt)
                    safe_prompt = urllib.parse.quote(user_input)
                    
                    # الرابط الجديد: أجبرنا السيرفر يستخدم مخ OpenAI الذكي
                    url = f"https://text.pollinations.ai/{safe_prompt}?system={safe_system}&model=openai"
                    
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
