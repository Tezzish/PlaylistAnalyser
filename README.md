# Playlist Analyser
This is a full stack web application to analyse your spotify playlists
!!! Currently in Development !!!

## Currently deployed on http://www.playlistanalyser.com



## To run the backend:
- Run `cd playlist_analyser`
- Set up a python virtual environment with `python -m venv venv`
- Use pip to install the requirements in requirements.txt with `pip install -r requirements.txt`
- Get your Client ID and Secret from the Spotify developer console
- Add these to a .env file or export them as environment variables
- Run the application using `python manage.py runserver`
- To send requests to the backend running locally, you can use (you can change the link to whatever you want):
    curl --location 'http://localhost:8000/analysis/' \
    --header 'Content-Type: application/json' \
    --data '{
        "playlist_link":"https://open.spotify.com/playlist/0QmxADr9HXix6UbAlqvbGZ?si=d4966ff431fe4f69"
    }'

## To run the frontend:
- Run `cd frontend`
- Run `npm install`
- Run `npm run dev`
- Go to localhost:xxxx (xxxx is the port number) on your browser

### To get testing statistics, please visit [Playlist Analyser code coverage](https://app.codecov.io/gh/Tezzish/PlaylistAnalyser/)
