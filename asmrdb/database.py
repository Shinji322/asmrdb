from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re
# imports the db variable from init in this current directory
# from __init__ import db, ROOT, LANG
from . import db, ROOT, LANG


# IMPORTANT NOTE:
# flask_sqlalchemy defines table names from descriptive base models
# if a model name is e.g. CamelCase, 
# it sets the table name as camel_case, not camelcase.
class Performer(db.Model):
    __tablename__ = 'performer'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    platform = db.Column(db.String)
    primary_audience = db.Column(db.String, default="All")
    primary_language = db.Column(db.String, default=LANG)
    # this is an additional query running in the background
    # as such, it doesn't appear in an sql client
    # "Audio" refers to class name
    # Despite layout, this actually adds a column to "Audio"
    audios = db.relationship('Audio', backref='performer', lazy=True)

    favorite = db.Column(db.Boolean, default=False)

    gender = db.Column(db.String, default='N/A')
    description = db.Column(db.String)

    first_archive_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_archive_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"""
        Performer(
            id='{self.id}'
            username='{self.username}', 
            platform='{self.platform}', 
            primary_audience='{self.primary_audience}', 
            favorite='{self.favorite}'
            gender='{self.gender}', 
            description='{self.description}'
            first_archive_date='{self.first_archive_date}', 
            last_archive_date='{self.last_archive_date}'
        )
        """


class Audio(db.Model):
    __tablename__ = 'audio'

    id = db.Column(db.Integer, primary_key=True)
    # 0 if no asmrtist was found
    # asmrtist is common letters since we're actually referring to the table and column
    # SQLAlchemy, by default, always sets this to lowercase
    asmrtist_id = db.Column(db.Integer, db.ForeignKey('performer.id'), default=0)

    # Info relevant to the audio file
    tags = db.Column(db.String)
    # The title of the file
    title = db.Column(db.String)
    # Some audios may be peformed by someone of a specific gender
    performer_gender = db.Column(db.String)
    # Some audios may have an intended audience 
    audience = db.Column(db.String)
    # Roleplay | Rain | Vacuum etc.; if multiple apply, 
    variant = db.Column(db.String) 
    # Where the file was downloaded from
    source = db.Column(db.String)
    # Description of the file
    description = db.Column(db.String)

    # Personal stuff
    # Date the file was created (uploaded to whatever site)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    # Date the file was archived by the user
    date_downloaded = db.Column(db.DateTime, default=datetime.utcnow)

    times_viewed = db.Column(db.Integer, default=0)
    # If the user has marked this audio as a favorite
    favorite = db.Column(db.Boolean, default=False)
    # The path to the file on the hard drive
    path = db.Column(db.String, default=ROOT)
    # optional image
    img_path = db.Column(db.String, default=None)
    # language of audio
    language = db.Column(db.String, default='en')

    def __repr__(self) -> str:
        return f"""audios(
            id='{self.id}'
            asmrtist_id={self.asmrtist_id}, 
            tags='{self.tags}',
            title='{self.title}', 
            audience='{self.audience}',
            variant='{self.variant}', 
            source='{self.source}',
            source='{self.source}',
            description={self.description}, 
            date_created='{self.date_created}', 
            date_downloaded='{self.date_downloaded}',
            times_viewed={self.times_viewed}, 
            favorite={self.favorite},
            path={self.path},
            img_path={self.img_path},
            language={self.language}
        )"""
