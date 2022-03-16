# Running

```bash
python run.py
```

# SQLAlchemy Stuff

Run this in the python shell in the `./asmrdb` directory

```python
from __init__ import db
from db import Audio, Performer
db.create_all()
p = Performer(...)
db.session.add(p)
db.session.commit()
```

## Querying

```python
Performer.query.all()
```

## Checking if everything works
```bash
python
```
```python
from __init__ import db; from db import Audio, Performer
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
db.session.add(p)
db.session.commit()
Performer.query.all()
Performer.query.filter_by(gender="Female").all()
```
>Before re-editing the database, you may need to delete and recreate the database

# Variables

`asmr_db` -> the database file
`app` -> the flask application
