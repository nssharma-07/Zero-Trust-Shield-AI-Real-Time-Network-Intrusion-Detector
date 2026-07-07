import streamlit as st
import joblib
import numpy as np

st.title("🛡️ Zero-Trust Shield AI")
st.subheader("Real-Time Network Intrusion Detector")

model = joblib.load("intrusion_model.pkl")

packet = st.number_input("Packet Size",100,5000,500)
time = st.number_input("Connection Time",1,100,20)
login = st.number_input("Failed Login Attempts",0,100,0)
rate = st.number_input("Request Rate",10,10000,100)
port = st.number_input("Port Number",1,65535,80)

if st.button("Analyze Traffic"):

    result = model.predict(np.array([[
        packet,time,login,rate,port
    ]]))[0]

    if result:
        st.error("🚨 Threat Detected - High Risk Traffic")
        st.warning("Recommended Action: Block connection and investigate.")
    else:
        st.success("✅ Normal Network Activity")