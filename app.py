import streamlit as st
from calculators import net_run_rate, required_run_rate

def cricket_over_input(label, key=None):
    """Custom input for cricket overs that automatically handles 6-ball system."""
    col1, col2 = st.columns([3, 1])
    
    with col1:
        overs = st.number_input(f"{label} - Overs", min_value=0, value=0, key=f"{key}_overs" if key else None)
    
    with col2:
        balls = st.number_input("Balls", min_value=0, max_value=5, value=0, key=f"{key}_balls" if key else None)
    
    return overs + (balls / 6.0)

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
    overs_faced = cricket_over_input("Overs Faced", key="faced")
    runs_conceded = st.number_input("Runs Conceded", min_value=0)
    overs_bowled = cricket_over_input("Overs Bowled", key="bowled")
    
    if st.button("Calculate NRR"):
        nrr = net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled)
        st.success(f"Net Run Rate: {nrr:.2f}")

elif calculator == "Required Run Rate":
    st.header("Required Run Rate Calculator")
    runs_needed = st.number_input("Runs Needed", min_value=0)
    overs_left = cricket_over_input("Overs Left", key="left")
    
    if st.button("Calculate Required Run Rate"):
        rrr = required_run_rate(runs_needed, overs_left)
        st.success(f"Required Run Rate: {rrr:.2f}")