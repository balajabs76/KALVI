import streamlit as st
import random

st.set_page_config(page_title="KALVI - AI Thozhan", page_icon="📚", layout="wide")

st.markdown("""
<style>
.stApp { background: #0f172a; color: white; }
h1,h2,h3 { color: white !important; }
.stTabs [data-baseweb="tab-list"] { background: #1e293b; border-radius: 10px; padding: 8px; }
.stButton>button { background: #6366f1; color: white; border-radius: 10px; width: 100%; font-weight: bold; height: 50px; }
.box { background: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #6366f1; margin: 10px 0; }
</style>
""", unsafe_allow_html=True)

st.title("📚 KALVI - Ungal AI Thozhan")
st.subheader("🚀 Founder: S.Atchaya | Free Quality Education")
st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["📖 1st-12th", "📝 TNPSC", "📰 Daily GK", "🤖 AI Thozhan"])

with tab1:
    st.header("📖 1st to 12th Notes")
    c1,c2 = st.columns(2)
    std = c1.selectbox("Class", ["6th","7th","8th","9th","10th","11th","12th"])
    sub = c2.selectbox("Subject", ["Tamil","English","Maths","Science","Social Science"])
    if st.button(f"{std} - {sub} Notes"):
        st.success(f"{std} {sub} - Full notes ready!")
        st.markdown(f"<div class='box'>1. Important points of {sub}<br>2. Previous year Q&A<br>3. Atchaya trick included!</div>", unsafe_allow_html=True)

with tab2:
    st.header("📝 TNPSC Super Quiz")
    qs = [
        {"q":"Thirukkural total?","o":["1330","133","1300","13300"],"a":0},
        {"q":"Tamil Nadu first CM?","o":["C.N. Annadurai","Kamarajar","MGR","Karunanidhi"],"a":0},
        {"q":"Chola famous king?","o":["Raja Raja Cholan","Ashoka","Akbar","Tipu"],"a":0},
        {"q":"India capital?","o":["Delhi","Chennai","Mumbai","Kolkata"],"a":0},
        {"q":"Article 370?","o":["Kashmir status","Education","Election","Finance"],"a":0},
    ]
    if 'score' not in st.session_state: st.session_state.score=0
    if 'qi' not in st.session_state: st.session_state.qi=0
    q = qs[st.session_state.qi % len(qs)]
    st.markdown(f"<div class='box'><h3>Q: {q['q']}</h3></div>", unsafe_allow_html=True)
    ans = st.radio("Answer:", q['o'], key=f"q{st.session_state.qi}")
    if st.button("Submit"):
        if q['o'].index(ans)==q['a']:
            st.balloons()
            st.success("CORRECT DA! SEMMA! 🎉")
            st.session_state.score+=1
        else:
            st.error(f"Correct: {q['o'][q['a']]}")
        st.session_state.qi+=1
        st.rerun()
    st.metric("Score", f"{st.session_state.score}/{st.session_state.qi}")

with tab3:
    st.header("📰 Daily GK")
    st.info("Today Top GK: ISRO launch, TN CM scheme, TNPSC date, CSK win!")

with tab4:
    st.header("🤖 AI Thozhan Chat")
    if 'chat' not in st.session_state: st.session_state.chat=[]
    for m in st.session_state.chat:
        if m['role']=='user': st.write(f"**Nee:** {m['t']}")
        else: st.markdown(f"<div class='box'>🤖 {m['t']}</div>", unsafe_allow_html=True)
    qq = st.chat_input("Doubt ketu da...")
    if qq:
        st.session_state.chat.append({'role':'user','t':qq})
        low = qq.lower()
        if "maths" in low: a = f"Maths '{qq}' - Formula ezhuthu, substitute pannu da! Atchaya trick: reverse check!"
        elif "tnpsc" in low: a = f"TNPSC '{qq}' - Year+Person+Place note pannu da! Important!"
        elif "tamil" in low: a = f"Tamil '{qq}' - Author, Year, Important line padu da!"
        else: a = f"'{qq}' - Super Q da! Idhu {random.choice(['12th portion','TNPSC frequent'])} la irukku! Detail sollu full tharen!"
        st.session_state.chat.append({'role':'ai','t':a})
        st.rerun()

st.markdown("---")
st.markdown("<center>KALVI © 2026 | By S.Atchaya | Chennai</center>", unsafe_allow_html=True)
