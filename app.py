import streamlit as st
import datetime

st.set_page_config(page_title="Health AI Agent", page_icon="🏥", layout="centered")

st.title("🏥 Health AI Agent")
st.write("Build a simple daily health routine (hydration, movement, meds).")

with st.form("health_form"):
    habit = st.text_input("Health habit", placeholder="e.g., Drink water, 15-min walk")
    frequency = st.selectbox("Frequency", ["Every hour", "3× per day", "Morning only", "Evening only"])
    time_pick = st.time_input("Preferred time", datetime.time(7, 0))
    submitted = st.form_submit_button("Create Routine")

if submitted:
    plan = f"""
🏥 **Health Routine**
- Habit: {habit or "Your habit"}
- Frequency: {frequency}
- Preferred time: {time_pick.strftime('%H:%M')}

**Tip**
Stack this habit with an existing one (after brushing teeth, take a 250ml glass of water).
"""
    st.success("Routine ready!")
    st.code(plan, language="markdown")
