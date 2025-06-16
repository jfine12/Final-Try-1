import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
user = None
if 'user' in st.session_state:
    user = st.session_state['user']
user = None  # default user state; set this during login/signup
import datetime
import random

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(page_title="Stablewatch", layout="wide")

# -----------------------------
# GLOBAL STYLING INJECTION
st.markdown("""
    
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    html, body, .block-container {
        font-family: 'Inter', sans-serif;
        background-color: #f9fafb;
        color: #1f2937;
    }

    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 2px solid #e2e8f0;
        margin-bottom: 1rem;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        padding: 0.75rem 1.25rem;
        border-radius: 8px 8px 0 0;
        background-color: #e5e7eb;
        margin-right: 0.5rem;
    }

    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        border-bottom: 2px solid #3b82f6 !important;
        color: #1d4ed8;
    }

    .stButton>button {
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }

    .stButton>button:hover {
        background-color: #2563eb;
    }

    .stTextInput>div>div>input {
        padding: 0.5rem;
        border-radius: 6px;
        border: 1px solid #d1d5db;
    }

    .element-container:has(.stTable), .stDataFrame {
        border: 1px solid #e5e7eb;
        border-radius: 10px;
        padding: 1rem;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }

    h1, h2, h3 {
        color: #111827;
    }
</style>

""", unsafe_allow_html=True)

# Sidebar Guidance



# -----------------------------
# Tabs
# -----------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Homepage",
    "📊 Dashboard",
    "🔍 Price Drivers",
    "📰 News & AI Insights",
    "🔐 Account / Watchlist"
])


# HOMEPAGE TAB




with tab1:
    st.markdown(
        "<div style='background-color: #0f172a; padding: 4rem 2rem; border-radius: 12px; text-align: center;'>"
        "<h1 style='color: white; font-size: 2.5rem;'>AI-powered insights into<br>stablecoin transparency, risk, and stability</h1>"
        "<p style='color: #cbd5e1; font-size: 1.1rem;'>Built for investors, analysts, and institutions.</p>"
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown("### 🌟 Why Stablewatch?")
    colA, colB = st.columns(2)
    with colA:
        st.markdown("- Real-time Peg Tracking")
        st.markdown("- AI-Powered Risk Scores")
        st.markdown("- Daily Updated Metrics")
    with colB:
        st.markdown("- Collateralization & Volume Signals")
        st.markdown("- Watchlists & Reports")
        st.markdown("- Premium Token Alerts")

    st.markdown("### 💳 Subscription Plans")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Starter")
        st.markdown("**Free**")
        st.markdown("""- Live dashboard  
- 5 tokens  
- 7-day charts""")
        if st.button("Start Free", key="starter_plan"):
            st.success("Starter Plan Activated")
    with col2:
        st.markdown("#### Pro")
        st.markdown("**$19/mo**")
        st.markdown("""- Full AI analysis  
- 10+ tokens  
- Alerts & Reports""")
        if st.button("Subscribe to Pro", key="pro_plan"):
            st.success("Pro Plan Selected")
    with col3:
        st.markdown("#### Enterprise")
        st.markdown("**Custom**")
        st.markdown("""- API access  
- Team logins  
- White-label dashboards""")
        if st.button("Contact Sales", key="enterprise_plan"):
            st.success("We'll contact you soon")

    st.markdown("### 📬 Stay Updated")
    email = st.text_input("Email")
    if st.button("Notify Me", key="notify_btn_native"):
        st.success("You're on the list ✅")
with tab2:
    st.title("📊 Stablecoin Risk Dashboard")
    coins = {
        "USDC": "✅ Very Safe",
        "USDT": "🟡 Moderate Risk",
        "DAI": "✅ Very Safe",
        "FRAX": "🟠 Caution",
        "TUSD": "🔴 High Risk"
    }

    st.markdown("### Select a stablecoin to view")
    selected_coin = st.selectbox("Stablecoin", list(coins.keys()))
    safety_label = coins[selected_coin]

    today = datetime.datetime.today()
    dates = [today - datetime.timedelta(days=i) for i in reversed(range(7))]
    prices = [1 + random.uniform(-0.005, 0.005) for _ in dates]

    delta = round(prices[-1] - 1.0, 4)
    score = round(100 - abs(delta * 1000), 1)

    st.markdown(f"### {selected_coin} — {safety_label}")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("AI Risk Score", f"{score}/100", delta=f"{delta:+.4f}")
        st.write("**Status:**", safety_label)
        st.write("**Volatility:**", f"{round(max(prices)-min(prices), 5)}")
        st.caption("Risk score is AI-generated based on price deviations and volatility.")
    with col2:
        fig, ax = plt.subplots()
        ax.plot(dates, prices, marker='o')
        ax.axhline(1.0, color='gray', linestyle='--', linewidth=1)
        ax.set_title(f"{selected_coin} 7-Day Peg Trend")
        ax.set_ylabel("USD Price")
        ax.set_xlabel("Date")
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%y'))
        fig.autofmt_xdate(rotation=45)
        st.pyplot(fig)
    st.caption("Last updated: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# PRICE DRIVERS TAB

with tab3:
    st.title("🔍 Stablecoin Price Drivers & Hypotheticals")
    st.markdown("""
    ### 💡 What Moves a Stablecoin Off-Peg?
    - **Loss of confidence or insolvency** of the issuing platform
    - **Redemptions exceeding reserves**
    - **Regulatory restrictions**
    - **Market-wide liquidity crunch**
    """)

    st.markdown("### ✏️ Simulate Hypothetical Scenario")

    scenario_options = {
        "USDT fails audit": {"impact": "Peg drops to $0.95", "risk": -25},
        "USDC blacklisted in 2 countries": {"impact": "Peg drops to $0.985", "risk": -10},
        "DAI adds more ETH collateral": {"impact": "Peg stable, confidence up", "risk": +5},
        "Binance delists FRAX": {"impact": "Peg volatility rises", "risk": -15},
        "TUSD depegs 5%": {"impact": "High sell-off risk", "risk": -30}
    }

    selected_event = st.selectbox("Select Event", list(scenario_options.keys()))
    scenario_data = scenario_options[selected_event]

    impact = scenario_data["impact"]
    risk_delta = scenario_data["risk"]

    st.markdown("### 🔮 Outcome")
    st.table(pd.DataFrame([{
        "Event": selected_event,
        "Expected Impact": impact,
        "Risk Score Δ": f"{risk_delta:+} pts"
    }]))

    st.markdown("### ✏️ Customize Hypothetical Scenario")

    colA, colB, colC = st.columns(3)
    with colA:
        event = st.text_input("Scenario", "USDT fails audit", key='text_2')
    with colB:
        effect = st.text_input("Expected Impact", "Peg drops to $0.95", key='text_3')
    with colC:
        risk_delta_custom = st.slider("Risk Score Change", -50, 50, -25)

    st.markdown("### 🔮 Generated Table")
    st.table(pd.DataFrame([{
        "Event": event,
        "Expected Impact": effect,
        "Risk Score Δ": f"{risk_delta_custom:+} pts"
    }]))


with tab4:
    st.title("📰 Stablecoin News & AI Insights")
    st.markdown("""
    ### 🗞️ Latest Headlines
    - **Circle (USDC) announces new real-time reserve dashboard**
    - **Tether increases transparency amid audit pressure**
    - **SEC investigates algorithmic stablecoins**

    ### 🤖 AI-Generated Observations
    > _"DAI has maintained a strong peg despite volatility in ETH. Collateralization ratio trending positive."_
    > _"USDT score dropped 3 points due to large redemptions and exchange delistings."_

    ### 📌 Recommendations
    - ✅ **DAI** appears resilient and well-collateralized — *Low Risk*
    - ⚠️ **USDT** transparency still limited — *Monitor closely*
    - ❗ **TUSD** shows reduced trust metrics — *Consider alternatives*

    These insights are updated regularly and curated by Stablewatch AI.
    """)


import firebase_admin
from firebase_admin import credentials, auth

# Initialize Firebase Admin SDK (make sure to add your credentials file when deploying)
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_service_account.json")  # upload this JSON file securely
    firebase_admin.initialize_app(cred)



# Firebase config removed for firebase-admin setup
auth = firebase.auth()

with tab5:
    
    st.title("🔐 Account / Watchlist")

    if user is None:
        st.subheader("🔐 Sign In or Create Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sign In", key='button_1'):
                try:
                    user = auth.sign_in_with_email_and_password(email, password)
                    user['email'] = email
                    st.session_state['user'] = user
                    st.success("Signed in successfully!")
                except Exception as e:
                    st.error("Login failed.")
        with col2:
            if st.button("Sign Up", key='button_2'):
                try:
                    user = auth.create_user_with_email_and_password(email, password)
                    user['email'] = email
                    st.session_state['user'] = user
                    st.success("Account created and signed in!")
                except Exception as e:
                    st.error("Signup failed.")
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                user['email'] = email
                st.session_state['user'] = user
                st.success("Signed in successfully!")
            except Exception as e:
                st.error("Login failed.")
            try:
                user = auth.create_user_with_email_and_password(email, password)
                user['email'] = email
                st.session_state['user'] = user
                st.success("Account created and signed in!")
            except Exception as e:
                st.error("Signup failed.")
    if user:
        st.markdown(f"**Signed in as:** `{user['email']}`")
    st.markdown("### 📈 Your Watchlist")
    coin_choices = ["USDC", "USDT", "DAI", "FRAX", "TUSD"]
    selected = st.multiselect("Select coins to add to your portfolio:", coin_choices)
    if selected:
        st.write("#### Your AI Risk Overview")
        data = []
        for coin in selected:
            score = round(100 - random.uniform(0, 10), 1)
            label = "✅ Low Risk" if score > 95 else "🟡 Moderate Risk" if score > 90 else "🔴 High Risk"
            data.append({"Coin": coin, "AI Risk Score": score, "Status": label})
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Select stablecoins to add to your watchlist.")

        st.markdown("### 📈 Watchlist AI Risk Trend")


# Payment Option Buttons

