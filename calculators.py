def net_run_rate(runs_scored, overs_faced, runs_conceded, overs_bowled):
    """Calculate Net Run Rate (NRR)."""
    try:
        return (runs_scored / overs_faced) - (runs_conceded / overs_bowled)
    except ZeroDivisionError:
        return 0.0

def required_run_rate(runs_needed, overs_left):
    """Calculate Required Run Rate (RRR)."""
    try:
        return runs_needed / overs_left
    except ZeroDivisionError:
        return 0.0
