import os
import requests
import streamlit as st
from dotenv import load_dotenv

# ----------------------------
# Load Environment Variables
# ----------------------------
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.railradar.in/v1/trains"

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="🚆 Live Train Tracker",
    page_icon="🚆",
    layout="wide"
)

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
<style>

.main-title{
    font-size:40px;
    font-weight:bold;
    color:#ff4b4b;
    text-align:center;
}

.subtitle{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

.card{
    background:#262730;
    padding:20px;
    border-radius:12px;
    border:1px solid #444;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🚆 Live Train Tracker</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Track Indian Railways in Real Time</p>', unsafe_allow_html=True)

# ----------------------------
# User Input
# ----------------------------
col1, col2 = st.columns([2,1])

with col1:
    train_number = st.text_input(
        "Train Number",
        placeholder="Example: 13009"
    )

with col2:
    journey_date = st.date_input("Journey Date")

# ----------------------------
# Search Button
# ----------------------------
if st.button("🚆 Track Train", use_container_width=True):

    if not train_number.isdigit() or len(train_number) != 5:
        st.error("Please enter a valid 5-digit train number.")
        st.stop()

    url = f"{BASE_URL}/{train_number}/live"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json"
    }

    params = {
        "date": str(journey_date)
    }

    with st.spinner("Fetching Live Train Status..."):

        try:

            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=20
            )

            if response.status_code != 200:
                st.error(f"API Error : {response.status_code}")
                st.code(response.text)
                st.stop()

            result = response.json()

            if not result.get("success"):
                st.error("Unable to fetch train information.")
                st.stop()

            data = result["data"]
            train = data["train"]

            # ----------------------------
            # Header
            # ----------------------------

            st.success("Train Found Successfully")

            st.markdown("---")

            st.header(f"🚆 {train['name']}")

            st.caption(f"Train Number : {train['number']}")

            # ----------------------------
            # Metrics
            # ----------------------------

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Running Status",
                data["status"].title()
            )

            c2.metric(
                "Current Station",
                data["currentLocation"]["stationCode"]
            )

            c3.metric(
                "Delay",
                f"{data['delayMinutes']} min"
            )

            st.markdown("---")

            c4, c5, c6 = st.columns(3)

            c4.metric(
                "Average Speed",
                f"{train['avgSpeed']} km/h"
            )

            c5.metric(
                "Maximum Speed",
                f"{train['maxSpeed']} km/h"
            )

            c6.metric(
                "Distance",
                f"{train['distance']} km"
            )

            st.markdown("---")

            # ----------------------------
            # Source & Destination
            # ----------------------------

            left, right = st.columns(2)

            with left:

                st.info(f"""
### 🚉 Source

**{train['source']['name']}**

Station Code : **{train['source']['code']}**
""")

            with right:

                st.info(f"""
### 🏁 Destination

**{train['destination']['name']}**

Station Code : **{train['destination']['code']}**
""")

            st.markdown("---")

            # ----------------------------
            # Journey Details
            # ----------------------------

            st.subheader("📅 Journey Details")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Journey Date:**", data["startDate"])
                st.write("**Train Type:**", train["type"])
                st.write("**Category:**", train["category"])
                st.write("**Total Halts:**", train["totalHalts"])

            with col2:
                st.write("**Previous Halt:**", data["previousHalt"]["stationName"])
                st.write("**Next Halt:**", data["nextHalt"]["stationName"])
                st.write("**Last Updated:**", data["lastUpdatedAt"])

            st.markdown("---")

            # ----------------------------
            # Route
            # ----------------------------

            with st.expander("🛤 Train Route", expanded=False):

                route = data.get("route", [])

                if route:

                    for station in route:

                        st.write(
                            f"**{station['sequence']}**. "
                            f"{station['stationName']} "
                            f"({station['stationCode']})"
                        )

                else:

                    st.info("Route information not available.")

            # ----------------------------
            # Debug JSON
            # ----------------------------

            with st.expander("🔍 Raw API Response"):

                st.json(result)

        except requests.exceptions.Timeout:
            st.error("Request Timed Out.")

        except requests.exceptions.ConnectionError:
            st.error("Unable to connect to RailRadar API.")

        except Exception as e:
            st.error(e)