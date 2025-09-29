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
        'beach_weather': '🕶️ Миналата година е било идеално за плаж! Слънчево и топло.',
        'rainy_weather': '☔ Било е дъждовно – по-добре планирай вътрешни активности.',
        'error': 'Грешка при зареждане на данните. Провери връзката си с интернет.',
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
        'beach_weather': '🕶️ Last year was perfect for the beach! Sunny and warm.',
        'rainy_weather': '☔ It was rainy – better plan indoor activities.',
        'error': 'Error loading data. Please check your internet connection.',
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

# Задаване на Open Graph мета тагове в head
def set_open_graph_tags(resort, date):
    og_image = image_urls.get(resort, "")
    og_title = translations[st.session_state.language]['title']
    og_description = translations[st.session_state.language]['weather_success'].format(date, resort)
    components.html(f"""
        <script>
            document.head.innerHTML += `
                <meta property="og:title" content="{og_title}">
                <meta property="og:description" content="{og_description}">
                <meta property="og:image" content="{og_image}">
                <meta property="og:url" content="https://bulgarian-resorts-weather.onrender.com">
            `;
        </script>
    """, height=0)

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
st.image(image_urls[resort], caption=resort, use_column_width=True)

# Задаване на Open Graph мета тагове за избрания курорт
set_open_graph_tags(resort, (datetime.now().date() - timedelta(days=365)).strftime("%Y-%m-%d"))

# Бутон за музика
if 'playing' not in st.session_state:
    st.session_state.playing = False

if st.button(translations[st.session_state.language]['play_music' if not st.session_state.playing else 'stop_music']):
    st.session_state.playing = not st.session_state.playing

if st.session_state.playing:
    st.audio(music_url, format="audio/mp3", start_time=0)

lat, lon = resorts[resort]

# Изчисляване на датата преди година
today = datetime.now().date()
last_year = today - timedelta(days=365)
start_date = last_year.strftime("%Y-%m-%d")
end_date = last_year.strftime("%Y-%m-%d")

# API URL за Open-Meteo
url = f"https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max&timezone=Europe/Sofia"

# Изпращане на заявка
if st.button(translations[st.session_state.language]['show_weather']):
    with st.spinner(translations[st.session_state.language]['loading']):
        response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        daily = data['daily']
        
        # Създаване на DataFrame
        df = pd.DataFrame({
            'Date' if st.session_state.language == 'en' else 'Дата': pd.to_datetime(daily['time']),
            'Max Temp (°C)' if st.session_state.language == 'en' else 'Макс. Темп. (°C)': daily['temperature_2m_max'],
            'Min Temp (°C)' if st.session_state.language == 'en' else 'Мин. Темп. (°C)': daily['temperature_2m_min'],
            'Precipitation (mm)' if st.session_state.language == 'en' else 'Валежи (mm)': daily['precipitation_sum'],
            'Max Wind Speed (km/h)' if st.session_state.language == 'en' else 'Макс. Вятър (km/h)': daily['wind_speed_10m_max'],
        })
        
        st.success(translations[st.session_state.language]['weather_success'].format(last_year, resort))
        st.dataframe(df, use_container_width=True)
        
        # Туристически съвет
        max_temp = daily['temperature_2m_max'][0]
        precip = daily['precipitation_sum'][0]
        if max_temp > 25 and precip < 1:
            st.balloons()
            st.info(translations[st.session_state.language]['beach_weather'])
        elif precip > 5:
            st.warning(translations[st.session_state.language]['rainy_weather'])
        
        # Бутон за споделяне във Facebook
        share_to_facebook(resort, last_year)
    else:
        st.error(translations[st.session_state.language]['error'])