# road_trip_planner.py
# pip install streamlit folium streamlit-folium requests geopy

import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
import requests
import json

# ----------------- API KEYS -----------------
ORS_API_KEY = "your_openrouteservice_api_key"  # https://openrouteservice.org/dev/#/signup

# ----------------- Helper Functions -----------------
def get_coordinates(place):
    geolocator = Nominatim(user_agent="road_trip_planner")
    location = geolocator.geocode(place)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None

def fetch_route(start, end, mode="driving-car"):
    url = f"https://api.openrouteservice.org/v2/directions/{mode}"
    headers = {"Authorization": ORS_API_KEY, "Content-Type": "application/json"}
    body = {"coordinates": [[start[1], start[0]], [end[1], end[0]]]}  # (lon, lat)
    resp = requests.post(url, headers=headers, json=body)

    if resp.status_code == 200:
        return resp.json()
    else:
        st.error(f"Route API failed: {resp.text}")
        return None

def show_route(route_data, start, end):
    m = folium.Map(location=start, zoom_start=10)

    # Start & end markers
    folium.Marker(start, popup="Start", icon=folium.Icon(color="green")).add_to(m)
    folium.Marker(end, popup="End", icon=folium.Icon(color="red")).add_to(m)

    # Draw route
    coords = route_data["features"][0]["geometry"]["coordinates"]
    coords_latlon = [(c[1], c[0]) for c in coords]  # swap lon,lat → lat,lon
    folium.PolyLine(coords_latlon, color="blue", weight=5).add_to(m)

    st_folium(m, width=700, height=500)

# ----------------- Streamlit UI -----------------
st.title("🗺️ Road Trip Planner")

start_location = st.text_input("Enter start location (e.g., Los Angeles, CA)")
end_location = st.text_input("Enter destination (e.g., San Francisco, CA)")

mode = st.selectbox(
    "Select travel mode",
    {
        "Car (Driving)": "driving-car",
        "Walking": "foot-walking",
        "Biking": "cycling-regular",
        "Bus (Public Transport)": "driving-hgv",  # ORS doesn’t have direct bus but can approximate
        "Train": "cycling-electric"  # placeholder, ORS doesn’t support train directly
    }
)

if st.button("Plan Route"):
    if start_location and end_location:
        start = get_coordinates(start_location)
        end = get_coordinates(end_location)

        if start and end:
            route_data = fetch_route(start, end, mode)
            if route_data:
                show_route(route_data, start, end)
