import streamlit as st
import requests
import json
from utils.config import BACKEND_URL

st.set_page_config(page_title="AI Trip Planner", page_icon="✈️", layout="wide")

st.title("Destination Planner")
st.markdown("Plan your next adventure with the help of AI!")

# User input form
with st.form("trip_plan_form"):
    user_query = st.text_area(
        "Tell me about your trip (e.g., 'Plan a trip to Paris from July 20, 2025 to July 25, 2025 for 2 people with a budget of 3000 USD. I want to convert USD to EUR.')",
        height=150,
        key="user_query_input"
    )
    submit_button = st.form_submit_button("Plan My Trip")

if submit_button and user_query:
    st.info("Planning your trip... This might take a moment.")
    
    try:
        response = requests.post(
            f"{BACKEND_URL}/plan_trip",
            json={"user_query": user_query}
        )
        response.raise_for_status() 
        trip_plan_data = response.json()

        st.success("Trip plan generated!")

        st.subheader("Your Trip Summary")
        
        if trip_plan_data.get("final_plan"):
            st.markdown(trip_plan_data["final_plan"])
        else:
            st.error("Could not generate a detailed trip plan.")
            st.json(trip_plan_data) 
        
        with st.expander("See Raw Data and Debug Messages"):
            st.json(trip_plan_data)
            st.subheader("Internal Messages")
            for msg in trip_plan_data.get("messages", []):
                st.write(f"**{msg['role'].capitalize()}**: {msg['content']}")

    except requests.exceptions.ConnectionError:
        st.error(f"Could not connect to the backend API at {BACKEND_URL}. Please ensure the FastAPI backend is running.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while calling the API: {e}")
        st.error(f"Response status code: {response.status_code}")
        st.error(f"Response content: {response.text}")
    except json.JSONDecodeError:
        st.error("Failed to decode JSON response from the API.")
        st.error(f"Raw response: {response.text}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

elif submit_button and not user_query:
    st.warning("Please enter your trip details to get a plan.")
