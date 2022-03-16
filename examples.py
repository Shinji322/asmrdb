from asmrdb import db
from asmrdb.db import Audio, Performer

p = Performer(
    username="strawberrylia_VA",
    platform="YouTube",
    primary_audience="F4A",
    primary_language='en',
    gender="Female", 
    description="""
    hi! i make ASMR roleplay videos :) i hope you have a great day ahead of you!

    english isn't my first language so please excuse my,,, lisp/accent (??) hehe

    everything on my channel is gender neutral btw !! (o´▽`o)

    ₍՞◌′ᵕ‵ू◌₎♡

    thank you so much for stopping by! (´｡• ᵕ •｡`) ♡
    """
)
a = Audio(
    asmrtist_id=1,
    tags="[ASMR Roleplay], [F4A], [Late Night Conversation], [Strangers To Lovers]",
    title="strawberrylia_VA - 20220130 - Stay With Me, Forever [ASMR Roleplay] [F4A] [Late Night Conversation] [Strangers To Lovers] [6CbP48JlejA]",
    performer_gender="Female",
    audience="Any",
    variant="Roleplay",
    source="youtube.com/watch?v=6CbP48JlejA",
    description="""
    Yes, person at the other side of the balcony, i’m talking to you. Let’s sneak out.

    woooo !! if you watched my Before Your Eyes livestream, chat was loving the idea of the neighbour girl X MC so I wanted to remake that except as an audio roleplay! was thinking of making this into a short series especially since part 2 of this is already ready to go （*´▽｀*) well, regardless, hope you guys like this one !!

    also, the Lunar New Year is really close to this upload, so i wish to those celebrating a Happy Lunar New Year !! may you be blessed with prosperity !!

    Art by: @muninshiki on twitter
    https://twitter.com/muninshiki/status/1461620269982920704

    if you liked the video, i hope you consider liking, commenting or subscribing but it's totally cool if you're here just to listen! thanks for stopping by ^^ have a great day ahead of you ! (๑°꒵°๑)･*♡

    join the discord, would love to see you there !! - https://discord.com/invite/hxm4AQJZtG

    if you’d like to donate/support me, no pressure !!
    ♡ ko-fi !! - https://ko-fi.com/strawberrylia_va

    if you’d like to follow me on social media !!
    ♡ twitter !! - https:// twitter.com/strawberryliaVA
    """
)


# Add info to database
from asmrdb import db

def add_performer(p:Performer):
    db.session.add(p)

def add_audio(a:Audio):
    db.session.add(a)

# Examples on how to query a database
def query_db():
    search = "straw"

    # match only title and receive title
    title_q = Audio.query.with_entities(Audio.title).\
        filter(Audio.title.ilike(f"%{search}%")).all()

    # match description only
    desc_q = Audio.query.\
        filter(Audio.description.ilike(f"%{search}%")).all()
