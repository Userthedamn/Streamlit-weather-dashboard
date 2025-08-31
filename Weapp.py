import streamlit as st
import requests
locations = {
    'Colombo':(6.927079, 79.861244),
    'Jaffna':(9.661498, 80.025543),
    'Batticaloa':(7.707880, 81.701736),
    'Trincomalee':(8.569000, 81.233002),
    "Kandy":(7.284440, 80.637466)
}
cities = list(locations.keys())
dropdown = st.sidebar.selectbox("Select you Loactions:", cities)
latitude, longitude = locations[dropdown]
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weather_code,uv_index_max&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,dew_point_2m,weather_code,pressure_msl,surface_pressure,visibility,wind_speed_10m,wind_gusts_10m,soil_temperature_0cm,uv_index,uv_index_clear_sky,soil_moisture_0_to_1cm&current=temperature_2m,wind_speed_10m,relative_humidity_2m,weather_code,surface_pressure,pressure_msl"

res = requests.get(API_URL)

data = res.json()


st.title(f"{dropdown} Weather Dashboard")

# Initialize states for each button
for section in ["Tempreture", "section2", "section3", "section4", "section5", "section6"]:
    if section not in st.session_state:
        st.session_state[section] = False

# Toggle functions
def toggle_section1():
    st.session_state["Tempreture"] = not st.session_state["Tempreture"]

def toggle_section2():
    st.session_state["section2"] = not st.session_state["section2"]

def toggle_section3():
    st.session_state["section3"] = not st.session_state["section3"]

def toggle_section4():
    st.session_state["section4"] = not st.session_state["section4"]

def toggle_section5():
    st.session_state["section5"] = not st.session_state["section5"]

def toggle_section6():
    st.session_state["section6"] = not st.session_state["section6"]

# Buttons
st.sidebar.button("Temperature", on_click=toggle_section1)
if st.session_state["Tempreture"]:
    st.subheader("Tempreture")
    st.write(data["current"]["temperature_2m"], "°C")
    st.line_chart(data["hourly"]["temperature_2m"], x_label="time(hours)", y_label="Tempreture(°C)")
st.sidebar.button("Humidity", on_click=toggle_section2)
st.sidebar.button("Wind Speed", on_click=toggle_section3)
st.sidebar.button("Weather code", on_click=toggle_section4)
st.sidebar.button("Surface Pressure", on_click=toggle_section5)
st.sidebar.button("Pressure MSL", on_click=toggle_section6)

# Sections


if st.session_state["section2"]:
    st.subheader("Humidity")
    st.write(data["current"]["relative_humidity_2m"], "%")
    st.line_chart(data["hourly"]["relative_humidity_2m"], x_label="time(hours)", y_label="Humidity(%)")
    st.line_chart(data["hourly"]["visibility"], x_label="time(hours)", y_label="Visibility(m)")


if st.session_state["section3"]:
    st.subheader("Wind Speed")
    st.write(data["current"]["wind_speed_10m"], "km/h")
    st.line_chart(data["hourly"]["wind_speed_10m"], x_label="time(hours)", y_label="Wind Speed(Km/h)")

if st.session_state["section4"]:
    st.subheader("Weather code")
    st.write(data["current"]["weather_code"], "wmo code")

if st.session_state["section5"]:
    st.subheader("Surface Pressure")
    st.write(data["current"]["surface_pressure"], "hPa")
    st.line_chart(data["hourly"]["surface_pressure"], x_label="time(hours)", y_label="Surface pressure(hPa))")


if st.session_state["section6"]:
    st.subheader("Pressure MSL")
    st.write(data["current"]["pressure_msl"], "hPa")
    st.line_chart(data["hourly"]["pressure_msl"], x_label="time(hours)", y_label="pressure(msl)")
