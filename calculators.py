def convert_overs_to_decimal(overs, balls):
    """Convert overs and balls to decimal format for calculations."""
    return overs + (balls / 6.0)

def validate_over_input(over_input):
    """Validate and convert over input to proper cricket format."""
    if over_input < 0:
        return 0.0
    
    overs = int(over_input)
    balls = round((over_input - overs) * 10)
    
    # If balls >= 6, convert to additional overs
    if balls >= 6:
        additional_overs = balls // 6
        remaining_balls = balls % 6
        overs += additional_overs
        balls = remaining_balls
    
    return overs + (balls / 6.0)

def net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled):
    """Calculate Net Run Rate (NRR)."""
    try:
        # Validate over inputs
        overs_faced = validate_over_input(overs_faced)
        overs_bowled = validate_over_input(overs_bowled)
        
        return (runs_scored / overs_faced) - (runs_conceded / overs_bowled)
    except ZeroDivisionError:
        return 0.0

def required_run_rate(runs_needed, overs_left):
    """Calculate Required Run Rate (RRR)."""
    try:
        # Validate over input
        overs_left = validate_over_input(overs_left)
        
        return runs_needed / overs_left
    except ZeroDivisionError:
        return 0.0