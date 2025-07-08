# Battle Chess
# # Chess variant to demonstrate using the LiChess api
# # How to run the web version:
- Download caddy to ui/web/server/caddy.exe
- Copy env_sample to .env and add your token to the file
- Create a virtual environment
- - python -m venv ./venv
- Install libraries
- - pip install -r requirements.txt
- Start caddy in a bash terminal
- - cd ui/web/server
- - ./caddy.exe start
- Run waitress in a second bash terminal
- - cd ui/web
- - waitress-serve app:app
- Visit https://localhost