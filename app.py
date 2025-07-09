import streamlit as st
from calculators import net_run_rate, required_run_rate

st.set_page_config(page_title="Cricket Calculators", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Calculators")
st.markdown("""
Quickly calculate Net Run Rate, Required Run Rate, and more for your cricket matches!
""")

# Add explanation for over format
st.sidebar.markdown("""
**Over Format Guide:**
- Enter overs as: `overs.balls`
- Examples: 
  - 5.2 = 5 overs 2 balls
  - 10.4 = 10 overs 4 balls
  - 0.3 = 0 overs 3 balls
- Valid balls: 0-5 (6 balls = 1 over)
""")

calculator = st.sidebar.selectbox(
    "Choose Calculator",
    ("Net Run Rate", "Required Run Rate")
)

if calculator == "Net Run Rate":
    st.header("Net Run Rate Calculator")
    runs_scored = st.number_input("Runs Scored", min_value=0)
    overs_faced = st.number_input("Overs Faced (e.g., 5.2)", min_value=0.1, step=0.1, format="%.1f")
    runs_conceded = st.number_input("Runs Conceded", min_value=0)
    overs_bowled = st.number_input("Overs Bowled (e.g., 5.2)", min_value=0.1, step=0.1, format="%.1f")
    
    # Show warning for invalid ball counts
    if overs_faced > 0:
        balls = round((overs_faced - int(overs_faced)) * 10)
        if balls > 5:
            st.warning(f"⚠️ Invalid ball count in 'Overs Faced': {balls}. Valid range is 0-5 balls.")
    
    if overs_bowled > 0:
        balls = round((overs_bowled - int(overs_bowled)) * 10)
        if balls > 5:
            st.warning(f"⚠️ Invalid ball count in 'Overs Bowled': {balls}. Valid range is 0-5 balls.")
    
    if st.button("Calculate NRR"):
        nrr = net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled)
        st.success(f"Net Run Rate: {nrr:.2f}")

elif calculator == "Required Run Rate":
    st.header("Required Run Rate Calculator")
    runs_needed = st.number_input("Runs Needed", min_value=0)
    overs_left = st.number_input("Overs Left (e.g., 5.2)", min_value=0.1, step=0.1, format="%.1f")
    
    # Show warning for invalid ball counts
    if overs_left > 0:
        balls = round((overs_left - int(overs_left)) * 10)
        if balls > 5:
            st.warning(f"⚠️ Invalid ball count: {balls}. Valid range is 0-5 balls.")
    
    if st.button("Calculate Required Run Rate"):
        rrr = required_run_rate(runs_needed, overs_left)
        st.success(f"Required Run Rate: {rrr:.2f}")