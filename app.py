import streamlit as st
import requests
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components

# Инициализация на session_state за език
if 'language' not in st.session_state:
    st.session_state.language = 'bg'

# Речници за преводи
translations = {
    'bg': {
        'title': '🌞⛷️ Български Курорти: Времето Преди Година',
        'description': 'Избери курорт и виж какво е било времето на **този ден преди година**. Идеално за планиране на почивка! 🇧🇬🏖️🏔️',
        'select_resort': 'Избери курорт:',
        'show_weather': 'Покажи времето',
        'loading': 'Зареждам историческите данни...',
        'weather_success': 'Времето на {} в {}:',
        'forecast_success': 'Прогноза за времето днес ({}) в {}:',
        'beach_weather': '🕶️ Миналата година е било идеално за плаж! Слънчево и топло.',
        'rainy_weather': '☔ Било е дъждовно – по-добре планирай вътрешни активности.',
        'beach_forecast': '🕶️ Днес се очаква идеално за плаж! Слънчево и топло.',
        'rainy_forecast': '☔ Очаква се дъжд – по-добре планирай вътрешни активности.',
        'error': 'Грешка при зареждане на данните. Провери връзката си с интернет.',
        'detailed_error': 'Грешка: {}',
        'play_music': 'Пусни музика 🎶',
        'stop_music': 'Спри музика',
        'share_facebook': 'Сподели във Facebook',
        'language': 'Смени език: Английски'
    },
    'en': {
        'title': '🌞⛷️ Bulgarian Resorts: Weather One Year Ago',
        'description': 'Choose a resort and see what the weather was like **this day last year**. Perfect for planning a vacation! 🇧🇬🏖️🏔️',
        'select_resort': 'Select a resort:',
        'show_weather': 'Show Weather',
        'loading': 'Loading historical weather data...',
        'weather_success': 'Weather on {} in {}:',
        'forecast_success': 'Weather Forecast for today ({}) in {}:',
        'beach_weather': '🕶️ Last year was perfect for the beach! Sunny and warm.',
        'rainy_weather': '☔ It was rainy – better plan indoor activities.',
        'beach_forecast': '🕶️ Today is expected to be perfect for the beach! Sunny and warm.',
        'rainy_forecast': '☔ Rain expected – better plan indoor activities.',
        'error': 'Error loading data. Please check your internet connection.',
        'detailed_error': 'Error: {}',
        'play_music': 'Play Music 🎶',
        'stop_music': 'Stop Music',
        'share_facebook': 'Share on Facebook',
        'language': 'Switch Language: Bulgarian'
    }
}

# Списък с курорти и координати
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

# URL за снимки и музика
image_urls = {
    "Sunny Beach": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/sunny_beach.jpg",
    "Golden Sands": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/golden_sands.jpg",
    "Sozopol": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/sozopol.jpg",
    "Albena": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/albena.jpg",
    "Burgas": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/burgas.jpg",
    "Nessebar": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/nessebar.jpg",
    "Varna": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/varna.jpg",
    "Bansko": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/bansko.jpg",
    "Borovets": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/borovets.jpg",
    "Pamporovo": "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/images/pamporovo.jpg",
}
music_url = "https://raw.githubusercontent.com/Deyan80/bulgarian-resorts-weather/main/audio/tourist_music.mp3"

# Функция за споделяне във Facebook
def share_to_facebook(resort, date):
    share_url = "https://bulgarian-resorts-weather.onrender.com"
    st.markdown(f"""
        <a href="https://www.facebook.com/sharer/sharer.php?u={share_url}" target="_blank">
            <button>{translations[st.session_state.language]['share_facebook']}</button>
        </a>
    """, unsafe_allow_html=True)

# Заглавие и описание
st.title(translations[st.session_state.language]['title'])
st.markdown(translations[st.session_state.language]['description'])

# Бутон за смяна на език
if st.button(translations[st.session_state.language]['language']):
    st.session_state.language = 'en' if st.session_state.language == 'bg' else 'bg'

# Избор на курорт
resort = st.selectbox(translations[st.session_state.language]['select_resort'], list(resorts.keys()))

# Показване на снимка за избрания курорт
st.image(image_urls[resort], caption=resort, width="stretch")

# Бутон за музика
if 'playing' not in st.session_state:
    st.session_state.playing = False

if st.button(translations[st.session_state.language]['play_music' if not st.session_state.playing else 'stop_music']):
    st.session_state.playing = not st.session_state.playing

if st.session_state.playing:
    st.audio(music_url, format="audio/mp3", start_time=0)

lat, lon = resorts[resort]

# Изчисляване на датите
today = datetime.now().date()
last_year = today - timedelta(days=365)
start_date = last_year.strftime("%Y-%m-%d")
end_date = last_year.strftime("%Y-%m-%d")
today_str = today.strftime("%Y-%m-%d")

# API URL за исторически данни (Open-Meteo archive)
url_historical = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe/Sofia"

# API URL за прогноза (Open-Meteo forecast, за днес)
url_forecast = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe/Sofia"

# Изпращане на заявка
if st.button(translations[st.session_state.language]['show_weather']):
    with st.spinner(translations[st.session_state.language]['loading']):
        try:
            response_h = requests.get(url_historical)
            response_f = requests.get(url_forecast)
        except Exception as e:
            st.error(translations[st.session_state.language]['detailed_error'].format(str(e)))
            st.stop()

    if response_h.status_code == 200 and response_f.status_code == 200:
        data_h = response_h.json()
        daily_h = data_h['daily']
        
        # DataFrame за исторически
        df_h = pd.DataFrame({
            'Date' if st.session_state.language == 'en' else 'Дата': pd.to_datetime(daily_h['time']),
            'Max Temp (°C)' if st.session_state.language == 'en' else 'Макс. Темп. (°C)': daily_h['temperature_2m_max'],
            'Min Temp (°C)' if st.session_state.language == 'en' else 'Мин. Темп. (°C)': daily_h['temperature_2m_min'],
            'Precipitation (mm)' if st.session_state.language == 'en' else 'Валежи (mm)': daily_h['precipitation_sum'],
            'Max Wind Speed (km/h)' if st.session_state.language == 'en' else 'Макс. Вятър (km/h)': daily_h['wind_speed_10m_max'],
        })
        
        st.success(translations[st.session_state.language]['weather_success'].format(last_year, resort))
        st.dataframe(df_h, width="stretch")
        
        # Туристически съвет за миналата година
        max_temp_h = daily_h['temperature_2m_max'][0]
        precip_h = daily_h['precipitation_sum'][0]
        if max_temp_h > 25 and precip_h < 1:
            st.balloons()
            st.info(translations[st.session_state.language]['beach_weather'])
        elif precip_h > 5:
            st.warning(translations[st.session_state.language]['rainy_weather'])
        
        # Прогнозни данни (взимаме първия ден - днес)
        data_f = response_f.json()
        daily_f = data_f['daily']
        
        # DataFrame за прогноза
        df_f = pd.DataFrame({
            'Date' if st.session_state.language == 'en' else 'Дата': pd.to_datetime(daily_f['time'][0:1]),
            'Max Temp (°C)' if st.session_state.language == 'en' else 'Макс. Темп. (°C)': daily_f['temperature_2m_max'][0:1],
            'Min Temp (°C)' if st.session_state.language == 'en' else 'Мин. Темп. (°C)': daily_f['temperature_2m_min'][0:1],
            'Precipitation (mm)' if st.session_state.language == 'en' else 'Валежи (mm)': daily_f['precipitation_sum'][0:1],
            'Max Wind Speed (km/h)' if st.session_state.language == 'en' else 'Макс. Вятър (km/h)': daily_f['wind_speed_10m_max'][0:1],
        })
        
        st.success(translations[st.session_state.language]['forecast_success'].format(today_str, resort))
        st.dataframe(df_f, width="stretch")
        
        # Туристически съвет за прогнозата
        max_temp_f = daily_f['temperature_2m_max'][0]
        precip_f = daily_f['precipitation_sum'][0]
        if max_temp_f > 25 and precip_f < 1:
            st.balloons()
            st.info(translations[st.session_state.language]['beach_forecast'])
        elif precip_f > 5:
            st.warning(translations[st.session_state.language]['rainy_forecast'])
        
        # Бутон за споделяне във Facebook
        share_to_facebook(resort, last_year)
    else:
        st.error(translations[st.session_state.language]['error'])

