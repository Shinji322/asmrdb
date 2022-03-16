from asmrdb import db, app
from asmrdb.database import Audio, Performer

p = Performer(
    username="rp_asmrtist",
    platform="YouTube",
    primary_audience="F4A",
    primary_language='en',
    gender="Female", 
    description="""
    I like to make roleplay asmr
    """
)
a = Audio(
    asmrtist_id=1,
    tags="[ASMR Roleplay], [F4A]",
    title="Getting you ready for a battle in 1330 AD",
    performer_gender="Female",
    audience="Any",
    variant="Roleplay",
    source="87askfdz8",
    description="""
    We are going to war, brother
    """
)
p1 = Performer(
    username="rain_noises",
    platform="YouTube",
    description="""
    Rain noises are cool
    """
)
a1 = Audio(
    asmrtist_id=2,
    tags="[Rain Noises]",
    title="Epic Rain noises for relaxing and studying",
    variant="White Noise",
    source="53lhjfa9",
    description="""
    I like rain
    """
)
a2 = Audio(
    asmrtist_id=2,
    tags="(No Talking)",
    title="ASMR Umbrella ☔️ Water Spritzing all Around & On You, Brushing, Tapping & Rain Sounds (No Talking)",
    variant="White Noise",
    source="f8a8ahru",
    description="""
    I also like rain
    """
)

with app.test_request_context():
    db.create_all()
    db.session.add(p)
    db.session.add(p1)
    db.session.add(a)
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()

