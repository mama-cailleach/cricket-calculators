import streamlit as st
from calculators import net_run_rate, required_run_rate

st.set_page_config(page_title="Cricket Calculators", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Calculators")
st.markdown("""
Quickly calculate Net Run Rate, Required Run Rate, and more for your cricket matches!
""")

calculator = st.sidebar.selectbox(
    "Choose Calculator",
    ("Net Run Rate", "Required Run Rate")
)

if calculator == "Net Run Rate":
    st.header("Net Run Rate Calculator")
    runs_scored = st.number_input("Runs Scored", min_value=0)
    overs_faced = st.number_input("Overs Faced", min_value=0.1, step=0.1, format="%.1f")
    runs_conceded = st.number_input("Runs Conceded", min_value=0)
    overs_bowled = st.number_input("Overs Bowled", min_value=0.1, step=0.1, format="%.1f")
    if st.button("Calculate NRR"):
        nrr = net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled)
        st.success(f"Net Run Rate: {nrr:.2f}")

elif calculator == "Required Run Rate":
    st.header("Required Run Rate Calculator")
    runs_needed = st.number_input("Runs Needed", min_value=0)
    overs_left = st.number_input("Overs Left", min_value=0.1, step=0.1, format="%.1f")
    if st.button("Calculate Required Run Rate"):
        rrr = required_run_rate(runs_needed, overs_left)
        st.success(f"Required Run Rate: {rrr:.2f}")
