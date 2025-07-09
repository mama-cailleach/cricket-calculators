import streamlit as st
from calculators import net_run_rate, required_run_rate

def cricket_over_input(label, key=None, value=0.0):
    """Manual input for cricket overs in overs.balls format (e.g., 5.3 = 5 overs 3 balls)."""
    over_value = st.number_input(
        label,
        min_value=0.0,
        value=value,
        step=0.1,
        format="%.1f",
        key=key,
        help="Enter overs in format: overs.balls (e.g., 5.3 = 5 overs 3 balls)"
    )
    # Only warn if balls > 5, do not auto-convert
    if over_value > 0:
        overs = int(over_value)
        balls = round((over_value - overs) * 10)
        if balls > 5:
            st.warning(f"⚠️ Invalid ball count: {balls}. Please use 0-5 balls (e.g., 5.3 not 5.{balls})")
    return over_value

def cricket_over_counter(label, key):
    """A clickable cricket over counter (0.0, 0.1, ..., 0.5, 1.0, ...)"""
    if key not in st.session_state:
        st.session_state[key] = 0.0

    overs = int(st.session_state[key])
    balls = int(round((st.session_state[key] - overs) * 10))

    col1, col2, col3 = st.columns([1,2,1])
    with col1:
        if st.button("−", key=f"{key}_minus"):
            if overs > 0 or balls > 0:
                if balls == 0:
                    if overs > 0:
                        overs -= 1
                        balls = 5
                else:
                    balls -= 1
                st.session_state[key] = overs + balls / 10
    with col2:
        st.markdown(f"<h3 style='text-align:center'>{label}: {overs}.{balls}</h3>", unsafe_allow_html=True)
    with col3:
        if st.button("\+", key=f"{key}_plus"):
            balls += 1
            if balls >= 6:
                overs += 1
                balls = 0
            st.session_state[key] = overs + balls / 10

    return st.session_state[key]

st.set_page_config(page_title="Cricket Calculators", page_icon="🏏", layout="centered")

st.title("🏏 Cricket Calculators")
st.markdown("""
Quickly calculate Net Run Rate, Required Run Rate, Live Required Run Rate, and more for your cricket matches!
""")

calculator = st.sidebar.selectbox(
    "Choose Calculator",
    ("Net Run Rate", "Required Run Rate", "Live Required Run Rate")
)

if calculator == "Net Run Rate":
    st.header("Net Run Rate Calculator")
    runs_scored = st.number_input("Runs Scored", min_value=0, format="%d")
    overs_faced = cricket_over_input("Overs Faced", key="faced")
    runs_conceded = st.number_input("Runs Conceded", min_value=0, format="%d")
    overs_bowled = cricket_over_input("Overs Bowled", key="bowled")

    # Only show result if all fields are valid (no invalid balls)
    valid_faced = int(overs_faced) >= 0 and 0 <= abs(round((overs_faced - int(overs_faced)) * 10)) <= 5
    valid_bowled = int(overs_bowled) >= 0 and 0 <= abs(round((overs_bowled - int(overs_bowled)) * 10)) <= 5

    if runs_scored > 0 and overs_faced > 0 and runs_conceded > 0 and overs_bowled > 0 and valid_faced and valid_bowled:
        nrr = net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled)
        st.success(f"Net Run Rate: {nrr:.2f}")

elif calculator == "Required Run Rate":
    st.header("Required Run Rate Calculator")
    runs_needed = st.number_input("Runs Needed", min_value=0, format="%d")
    overs_left = cricket_over_input("Overs Left", key="left")

    valid_left = int(overs_left) >= 0 and 0 <= abs(round((overs_left - int(overs_left)) * 10)) <= 5

    if runs_needed > 0 and overs_left > 0 and valid_left:
        rrr = required_run_rate(runs_needed, overs_left)
        st.success(f"Required Run Rate: {rrr:.2f}")

elif calculator == "Live Required Run Rate":
    st.header("Live Required Run Rate Calculator")
    runs_needed = st.number_input("Runs Needed", min_value=0, format="%d")
    
    # Manual setup field for overs left
    setup_overs = st.number_input(
        "Overs Left (setup)", 
        min_value=0.0, 
        value=20.0, 
        step=0.1, 
        format="%.1f", 
        key="live_left_setup",
        help="Set the starting overs left (e.g., 20.0, 15.3)"
    )
    # Error handling for balls > 5
    overs = int(setup_overs)
    balls = int(round((setup_overs - overs) * 10))
    if balls > 5:
        st.warning(f"⚠️ Invalid ball count: {balls}. Please use 0-5 balls (e.g., 5.3 not 5.{balls})")
    else:
        # Button to set the counter to the setup value
        if st.button("Set Overs Left"):
            st.session_state["live_left"] = setup_overs

    overs_left = cricket_over_counter("Overs Left", key="live_left")
    if st.button("Calculate Live Required Run Rate"):
        rrr = required_run_rate(runs_needed, overs_left)
        st.success(f"Live Required Run Rate: {rrr:.2f}")