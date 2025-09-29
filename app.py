import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd

# Списък с популярни български курорти и техните координати (lat, lon)
resorts = {
    "Sunny Beach": (42.695153, 27.710421),
    "Golden Sands": (43.2843, 28.0383),
    "Sozopol": (42.4167, 27.7),
    "Albena": (43.3682, 28.0801),
    "Burgas": (42.510578, 27.461014),
    "Nessebar": (42.659149, 27.736143),
    "Varna": (43.2167, 27.9167),
    "Bansko": (41.8373, 23.4857),
    "Borovets": (42.2667, 23.6),
    "Pamporovo": (41.6551, 24.6968),
}

st.title("🌞⛷️ Български Курорти: Времето Преди Година")
st.markdown("Избери курорт и виж какво е било времето на **този ден преди година**. Идеално за планиране на почивка! 🇧🇬🏖️🏔️")

# Избор на курорт
resort = st.selectbox("Избери курорт:", list(resorts.keys()))

lat, lon = resorts[resort]

# Изчисляване на датата преди година
today = datetime.now().date()
last_year = today - timedelta(days=365)
start_date = last_year.strftime("%Y-%m-%d")
end_date = last_year.strftime("%Y-%m-%d")  # Само един ден

# API URL за Open-Meteo (historical data)
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe/Sofia"

# Изпращане на заявка
if st.button("Покажи времето"):
    with st.spinner("Зареждам историческите данни..."):
        response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        daily = data['daily']
        
        # Създаване на DataFrame за таблица
        df = pd.DataFrame({
            'Дата': pd.to_datetime(daily['time']),
            'Макс. Темп. (°C)': daily['temperature_2m_max'],
            'Мин. Темп. (°C)': daily['temperature_2m_min'],
            'Валежи (mm)': daily['precipitation_sum'],
            'Макс. Вятър (km/h)': daily['wind_speed_10m_max'],
        })
        
        st.success(f"Времето на {last_year} в {resort}:")
        st.dataframe(df, use_container_width=True)
        
        # Туристически съвет
        max_temp = daily['temperature_2m_max'][0]
        precip = daily['precipitation_sum'][0]
        if max_temp > 25 and precip < 1:
            st.balloons()
            st.info("🕶️ Миналата година е било идеално за плаж! Слънчево и топло.")
        elif precip > 5:
            st.warning("☔ Било е дъждовно – по-добре планирай вътрешни активности.")
    else:
        st.error("Грешка при зареждане на данните. Провери връзката си с интернет.")