# make a fucntion to read a config file
from .database import Audio, Performer
import json
import re

# extrapalates information from a .info.json file
def read_json(json_file:str, path:str=".") -> tuple[Performer, Audio]:
# matches: [f4m] (f4a) (mf4a), etc.
# audiences_reg = re.compile("[\[\(]?([fFmMaA]+)4([fFmMaA]+)[\]|\)]?")
    gender_reg = "([fFmMaA(nB|NB|nb|Nb)]+)"
    audiences_reg = re.compile(f"[\[\(]?{gender_reg}4{gender_reg}[\]|\)]?")
    tags_reg = re.compile("[\[\(](\w+|\d+)[\]\)]")
# a case insensitive regex to determine if whitenoise or roleplay
    roleplay_reg  = re.compile("roleplay", re.I)


    with open(json_file) as f:
        info = json.load(f)

        title:str = info["title"]
        description:str = info["description"]
        uploader:str = info["uploader"]
        upload_date = info["upload_date"]
        source = "{}".format(info["id"])

    performers = []
    audiences = []
    tags = []
    variant = "White Noise" # default

    # these are lists of tuples where the first part is the performer
    # the second part is the audience 
    audience_title_matches:list = audiences_reg.findall(title)
    audience_description_matches:list = audiences_reg.findall(description)

    # if no matches
    if not audience_title_matches and not audience_description_matches:
        audiences.append(None)
    else:
        for tmatch in audience_title_matches:
            # first regex group
            if tmatch[0] not in performers:
                performers.append(f"{tmatch[0]}")
            # second regex group
            if tmatch[1] not in audiences:
                audiences.append(f"{tmatch[1]}")
        for dmatch in audience_description_matches:
            if dmatch[0] not in performers:
                performers.append(f"{dmatch[0]}")
            if dmatch[1] not in audiences:
                audiences.append(f"{dmatch[1]}")

    # finding tags
    tags_title_matches:list = tags_reg.findall(title)
    description_title_matches:list = tags_reg.findall(description)

    if tags_title_matches:
        for tmatch in tags_title_matches:
            if tmatch not in tags:
                tags.append(tmatch)
    if description_title_matches:
        for dmatch in description_title_matches:
            if dmatch not in tags:
                tags.append(dmatch)

    # if roleplay
    rp_matches:list = roleplay_reg.findall(title) + roleplay_reg.findall(description)
    if rp_matches:
        variant = "Roleplay"

    # Check if performer doesn't exist in db. If not, create one, otherwise, just use the first one
    results = Performer.query.filter_by(username=uploader)
    if not results:
        performer = Performer(
            username=uploader,
            gender=performers[0],
        )
    else:
        performer = results[0]

    audio = Audio(
        username=uploader,
        performer=performers[0],
        audience=audiences[0],
        title=title,
        description=description,
        variant=variant,
        tags=str(tags),
        source=source,
        date_created=upload_date,
        path=path
    )

    return (performer, audio)


def read_data(form_data:list) -> tuple[Performer,Audio]:
    # matches: [f4a] (f4a) (mf4a), etc.
    # audiences_reg = re.compile("[\[\(]?([fFmMaA]+)4([fFmMaA]+)[\]|\)]?")
    gender_reg = "([fFmMaA(nB|NB|nb|Nb)]+)"
    audiences_reg = re.compile(f"[\[\(]?{gender_reg}4{gender_reg}[\]|\)]?")
    tags_reg = re.compile("[\[\(](\w+|\d+)[\]\)]")
    # a case insensitive regex to determine if whitenoise or roleplay
    roleplay_reg  = re.compile("roleplay", re.I)

    # form data
    title = form_data[0]
    description = form_data[1]
    username = form_data[2]
    source = form_data[3]
    favorite = form_data[4]

    performers = []
    audiences = []
    tags = []
    variant = "White Noise" # default

    # these are lists of tuples where the first part is the performer
    # the second part is the audience 
    audience_title_matches:list = audiences_reg.findall(title)
    audience_description_matches:list = audiences_reg.findall(description)

    # if no matches
    if not audience_title_matches and not audience_description_matches:
        audiences.append(None)
    else:
        for tmatch in audience_title_matches:
            # first regex group
            if tmatch[0] not in performers:
                performers.append(f"{tmatch[0]}")
            # second regex group
            if tmatch[1] not in audiences:
                audiences.append(f"{tmatch[1]}")
        for dmatch in audience_description_matches:
            if dmatch[0] not in performers:
                performers.append(f"{dmatch[0]}")
            if dmatch[1] not in audiences:
                audiences.append(f"{dmatch[1]}")
    if not performers:
        performers.append("N/A")

    # finding tags
    tags_title_matches:list = tags_reg.findall(title)
    description_title_matches:list = tags_reg.findall(description)

    if tags_title_matches:
        for tmatch in tags_title_matches:
            if tmatch not in tags:
                tags.append(tmatch)
    if description_title_matches:
        for dmatch in description_title_matches:
            if dmatch not in tags:
                tags.append(dmatch)

    # if roleplay
    rp_matches:list = roleplay_reg.findall(title) + roleplay_reg.findall(description)
    if rp_matches:
        variant = "Roleplay"

    # Check if performer doesn't exist in db. If not, create one, otherwise, just use the first one
    results = Performer.query.filter_by(username=username).all()
    print(results)
    if not results:
        performer = Performer(
            username=username,
            gender=performers[0],
        )
    else:
        performer = results[0]

    audio = Audio(
        performer_gender=performers[0],
        audience=audiences[0],
        title=title,
        description=description,
        variant=variant,
        tags=str( tags ),
        source=source
    )

    return (performer, audio)
