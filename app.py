import streamlit as st
st.set_page_config(page_title="KALVI", layout="wide")
st.markdown("""<style>.stApp{background:white!important}h1,h2,h3,p,div{color:black!important}</style>""", unsafe_allow_html=True)
st.title("KALVI - Ungal AI Thozhan")
st.subheader("Founder: S.Atchaya")
st.success("100+ Topics - NEET, TNPSC, Python, GK")
if "messages" not in st.session_state: st.session_state.messages=[]
for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.write(m["content"])
if prompt := st.chat_input("Kelvi Kelu..."):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.write(prompt)
    p=prompt.lower()
    if "hi" in p: ans="Vanakkam da! Enna kelvi?"
    elif "photo" in p: ans="Photosynthesis: Thavaram surya oliyil unavu seiyum murai"
    elif "newton" in p: ans="Newton: F=ma, vilai-edhir vilai"
    elif "python" in p: ans="Python: Easy language, print('hi')"
    elif "neet" in p: ans="NEET: NCERT thaan king!"
    else: ans=f"{prompt} - Try: photosynthesis, newton, python, neet"
    with st.chat_message("assistant"): st.write(ans)
    st.session_state.messages.append({"role":"assistant","content":ans})
