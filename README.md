# 🏏 Cricket Calculators Web App

A simple, mobile-friendly web app for cricket fans and players to calculate:
- Net Run Rate (NRR)
- Required Run Rate (RRR)
- Live Required Run Rate (with ball-by-ball counter)

Built with [Streamlit](https://streamlit.io/).

---

## 🚀 Try It Locally

1. **Clone this repo**
2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
3. **Run the app**
   ```
   streamlit run app.py
   ```
4. Visit [http://localhost:8501](http://localhost:8501) in your web browser.

---

## 🧮 Calculators

### Net Run Rate (NRR)
- Enter runs scored, runs conceded, overs faced, and overs bowled.
- Overs must be in `overs.balls` format (e.g., `5.3` for 5 overs 3 balls).
- If you enter an invalid number of balls (e.g., `5.7`), you'll get a warning.
- Result appears automatically when all fields are valid.

### Required Run Rate (RRR)
- Enter runs needed and overs left.
- Overs left must be in `overs.balls` format.
- Invalid balls (6-9) will show a warning.
- Result appears automatically when all fields are valid.

### Live Required Run Rate
- Enter runs needed.
- Set up the starting "Overs Left" using a manual input (must be valid cricket format).
- Click "Set Overs Left" to initialize the counter.
- Use the +/− buttons to adjust overs and balls as the game progresses (only valid cricket increments allowed).
- Click "Calculate Live Required Run Rate" to see the live RRR.

---

## 📦 File Structure

```
.
├── app.py            # Streamlit app UI and logic
├── calculators.py    # Calculator functions (NRR, RRR, validation, etc.)
├── requirements.txt  # Python dependencies
└── README.md         # Project info
```

---

## 📝 Add Your Own Calculators

- Add new functions to `calculators.py`
- Add new UI sections in `app.py` (copy/paste pattern)

---

## ⚠️ Notes

- All overs inputs must use the cricket format: `overs.balls` (balls: 0-5 only).
- The app will warn you if you enter an invalid number of balls.
- The "Live Required Run Rate" calculator uses a clickable counter for accurate ball-by-ball tracking.

---

Enjoy, and feel free to contribute!
