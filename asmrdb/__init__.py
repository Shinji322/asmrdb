# this is the initialization file
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pathlib, json, os

# Read some configs
# a custom database path
DB_PATH="../db/test.db"
# Root audio dir
ROOT=str(pathlib.Path('.').absolute())
# Default lang
LANG = "en"
# Config file
if not os.path.exists("settings.json"):
    f = open("settings.json", 'a')
    # defaults
    f.write(json.dumps(
                {
                    "theme": "Cerulean",
                    "custom_css": "None",
                    "javascript": True
                }
            ))
    f.close()

with open("settings.json", "r+") as f:
    CONFIG = json.load(f)

# a list of valid themes
themes = [
    "Cerulean",
    "Cosmo",
    "Cyborg",
    "Darkly",
    "Flatly",
    "Journal",
    "Litera",
    "Lumen",
    "Lux",
    "Materia",
    "Minty",
    "Morph",
    "Pulse",
    "Quartz",
    "Sandstone",
    "Simplex",
    "Sketchy",
    "Slate",
    "Solar",
    "Spacelab",
    "Superhero",
    "United",
    "Vapor",
    "Yeti",
    "Zephyr"
]

# configuring the app
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
db = SQLAlchemy(app)

from . import routes
