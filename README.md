# Byte Detective Kids Edition 🕵️

A colourful, beginner-friendly Python debugging game for children and first-time coders.

## Run the game
1. Install Python 3.10 or newer.
2. Open this folder in VS Code or a terminal.
3. Install Flask: `pip install -r requirements.txt`
4. Start the game: `python app.py`
5. Open `http://127.0.0.1:5000` in your browser.

## What children learn
- `=` versus `==`
- Python lists and indexes
- `for` loops
- Reading clues, spotting mistakes, and trying again

## Project files
- `app.py` — Flask backend and safe answer checking
- `templates/index.html` — game screens
- `static/css/style.css` — colourful responsive design
- `static/js/game.js` — interactions and progress
- `static/images/` — original local SVG cartoon scenes

## Safety note
This is a learning game. The server checks the submitted code against the intended solution and does not execute arbitrary code entered by players.
