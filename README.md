🌊⛷️ Bulgarian Resorts: Weather One Year Ago
This is a simple web app for tourists, showing the weather for this day last year in popular Bulgarian resorts. Perfect for planning vacations – check if it was sunny, rainy, or snowy! Now with multilingual support, background music, and Facebook sharing.
Features

Choose from 10 resorts: Sunny Beach, Golden Sands, Sozopol, Albena, Burgas, Nessebar, Varna, Bansko, Borovets, Pamporovo.
Displays: max/min temperature, precipitation, wind speed.
Tourist tips based on weather (e.g., "Perfect for the beach!").
New: Switch between Bulgarian and English.
New: Play/stop tourist-themed background music.
New: Share results on Facebook with a resort image.
Free: Uses Open-Meteo API (open-source).

Installation and Running Locally

Clone the repo: git clone https://github.com/Deyan80/bulgarian-resorts-weather.git
Install dependencies: pip install -r requirements.txt
Run: streamlit run app.py
Open in browser: http://localhost:8501

Hosting on Render

Upload app.py, README.md, requirements.txt, audio/tourist_music.mp3, and images/*.jpg to GitHub.
In Render, create a new Web Service.
Connect GitHub repo, set:
Build Command: pip install -r requirements.txt
Start Command: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
Instance Type: Free


Deploy and access at URL (e.g., https://bulgarian-resorts-weather.onrender.com).

Data

Source: Open-Meteo Historical API (ERA5 data, covers Bulgaria since 1940).
Resort coordinates: Standard GPS points for accuracy.
Images: Free Unsplash images for each resort, hosted in GitHub.
Music: Free tourist-themed MP3, hosted in GitHub.

Setup for Images and Music

Download free images (e.g., from Unsplash) for each resort (Sunny Beach, Bansko, etc.).
Place them in an images/ folder in the repo (e.g., images/sunny_beach.jpg).
Download a free MP3 (e.g., from Free Music Archive) and place it in audio/tourist_music.mp3.
Update image_urls and music_url in app.py if you host files elsewhere.

Extensions

Add more resorts to resorts dictionary.
Integrate maps with Folium.
Add weather forecasts for future dates.

Questions or improvements? Let me know! 😊
Author: Deyan80 | License: MIT