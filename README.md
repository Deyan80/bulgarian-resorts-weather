🌊⛷️ Български Курорти: Времето Преди Година
Това е проста уеб апликация за туристи, която показва историческото време на този ден преди година в популярни български курорти. Полезна за планиране на почивки – виж дали е било слънчево, дъждовно или снежно!
Функции

Избор от 10 курорта: Sunny Beach, Golden Sands, Sozopol, Albena, Burgas, Nessebar, Varna, Bansko, Borovets, Pamporovo.
Данни за: макс/мин температура, валежи, вятър.
Туристически съвети базирани на времето.
Безплатно: Използва Open-Meteo API (open-source).

Инсталация и Стартиране

Клонирай репото: git clone https://github.com/yourusername/bulgarian-resorts-weather.git
Инсталирай dependencies: pip install streamlit requests pandas
Стартирай: streamlit run app.py
Отвори в браузъра: http://localhost:8501

Хостинг

Локално: Като по-горе.
Онлайн (Render):
Качи app.py, README.md и requirements.txt в GitHub.
В Render, създай нов Web Service.
Свържи GitHub repo, задай:
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
Instance Type: Free


Deploy и вземи URL (напр. https://resorts-weather-app.onrender.com).



Данни

Източник: Open-Meteo Historical API (данни от ERA5, покритие за България от 1940 г.).
Координати на курортите: Използвани са стандартни GPS точки за точност.

Разширения

Добави още курорти в resorts dictionary.
Интегрирай карти с Folium.
Добави прогнози за бъдещи дати.

Ако имаш въпроси или искаш промени – пиши! 😊
Автор: [Твоето име] | Лиценз: MIT