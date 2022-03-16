# TODO: remove db import later
from . import app, themes, CONFIG, db
from .database import Audio, Performer
from .helpers import read_json, read_data
from flask import redirect, render_template, request, jsonify 
import os
# imports the app variable from init in this current directory

# on this page, we'll have a search function that will redirect to the search page
# it would be a YouTube like experience
@app.route("/")
def index():
    queries = Audio.query.limit(5).all()

    return render_template("index.html", 
                           theme=CONFIG["theme"],
                           queries=queries)


@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html", theme=CONFIG["theme"])


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        custom_theme = request.form.get("custom_theme")
        custom_css = request.form.get("custom_css")

        if custom_theme or custom_css:
            if custom_css:
                if not os.path.exists(custom_css):
                    return render_template("error.html", errno=403, errmsg="""
                        Custom CSS is not in a valid path
                    """, theme=CONFIG["theme"])

                return render_template("index.html", theme=CONFIG["theme"])
            if custom_theme:
                if custom_theme not in themes:
                    return render_template("error.html", errno=403, errmsg="""
                        Custom Theme is not a valid theme
                    """, theme=CONFIG["theme"])

                CONFIG["theme"] = custom_theme.lower()

                return render_template("index.html", theme=CONFIG["theme"])


        if not custom_theme:
            return render_template("error.html", errno=403, errmsg="""
                Custom Theme was not found 
            """, theme=CONFIG["theme"])
        if not custom_css:
            return render_template("error.html", errno=403, errmsg="""
                Custom CSS was not found 
            """, theme=CONFIG["theme"])

        return render_template("index.html", theme=CONFIG["theme"])
    else:
        return render_template("settings.html", themes=themes, theme=CONFIG["theme"])


@app.route("/results")
def results():
    search = request.args.get("search")
    plus_tags = request.args.get("plus_tags")
    min_tags = request.args.get("min_tags")
    perf_q = request.args.get("performer_query")
    audio_q = request.args.get("audio_query")

    # If this is fulfilled, then we just do a standard search
    if not plus_tags and not min_tags and not perf_q and not audio_q:
        title_results = []
        desc_results = []
        title_q = Audio.query.\
            filter(Audio.title.ilike(f"%{search}%"))
        desc_q = Audio.query.\
            filter(Audio.description.ilike(f"%{search}%"))

        # prefer title
        if title_q:
            title_results = title_q.all()
        if desc_q:
            desc_results = desc_q.all()

        return render_template("results.html", t_results=title_results, d_results=desc_results, theme=CONFIG["theme"])
    else: 
        results = []
        
        if plus_tags:
            results += Audio.query.filter(Audio.tags.ilike(f"%{plus_tags}%")).all() 
        if min_tags:
            results -= Audio.query.filter(Audio.tags.ilike(f"%{min_tags}%")).all() 
        if perf_q:
            results += Performer.query.filter(Performer.username.ilike(f"%{perf_q}%")).all() 
        if audio_q:
            results += Audio.query.filter(Audio.title.ilike(f"%{audio_q}%")).all() 

        return render_template("results.html", 
                               results=results,
                               theme=CONFIG["theme"])
        


@app.route("/update", methods=["POST", "GET"])
def update_db():
    add_options = [
        "Title",
        "Description",
        "ASMRtist",
        "Source",
        "Favorite"
    ]
    if request.method == "GET":
        return render_template("update.html",
                               add_options=add_options, theme=CONFIG["theme"])

    info_path = request.form.get("info_path")
    form_data = []
    for opt in add_options:
        form_data.append(request.form.get(opt)) 

    if info_path:
        if not os.path.exists(info_path) and not info_path.endswith("json"):
            return render_template("error.html", errno=403, errmsg="Invalid File Name/File does not exist")
        performer, audio = read_json(info_path) 
        with app.test_request_context():
            db.session.add(performer)
            db.session.add(audio)
            db.session.commit()
    if form_data:
        performer, audio = read_data(form_data)
        with app.test_request_context():
            db.session.add(performer)
            db.session.add(audio)
            db.session.commit()

    
    return render_template("update.html",
                           add_options=add_options, theme=CONFIG["theme"],
                           notification="Data added to db!")
