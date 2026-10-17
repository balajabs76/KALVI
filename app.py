import streamlit as st

st.set_page_config(page_title="KALVI - Ungal AI Thozhan", page_icon="📚", layout="wide")

st.markdown("""
<style>
body { background: #0f172a; }
.main { background: #0f172a; }
</style>
""", unsafe_allow_html=True)

st.title("📚 KALVI - Ungal AI Thozhan")
st.subheader("AI Powered Learning Platform for Students")

st.markdown("### 🚀 Founder: S.Atchaya")
st.markdown("**Mission: Free Quality Education For All**")

tab1, tab2, tab3, tab4 = st.tabs(["📖 1st-12th Std", "📝 TNPSC & GK", "📰 Daily News", "🤖 AI Chat"])

with tab1:
    st.header("1st to 12th Standard - All Subjects")
    std = st.selectbox("Class Select Pannu", ["6th", "7th", "8th", "9th", "10th", "11th", "12th"])
    subject = st.selectbox("Subject", ["Tamil", "English", "Maths", "Science", "Social"])
    st.info(f"{std} - {subject} notes & lessons soon coming!")

with tab2:
    st.header("TNPSC, GK, General Knowledge")
    st.write("TNPSC Group 1,2,4 questions, GK quizzes daily!")

with tab3:
    st.header("Daily News & Current Affairs")
    st.write("Today news updates...")

with tab4:
    st.header("AI Thozhan Chat")
    user_q = st.text_input("Enna doubt? Ketu parunga!")
    if user_q:
        st.success(f"Ungal kelvi: {user_q}")
        st.write("AI Thozhan answer: Idhu KALVI AI chat - full feature soon varum da!")

st.markdown("---")
st.markdown("**KALVI © 2026 | Made with ❤️ by Atchaya**")
