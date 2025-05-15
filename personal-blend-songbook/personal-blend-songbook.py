import os
import json
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("personal-blend-songbook"),
    autoescape=select_autoescape()
)

def generate_index(song_list):
    index = env.get_template("index.html")
    index_html = index.render(song_list=song_list)
    with open("index.html", 'w') as new_html:
        new_html.write(index_html)
    new_html.close()



if __name__ == "__main__":
    song_list = sorted([x.split(".")[0] for x in os.listdir("songs") if x.endswith(".json")])
    for song_name in song_list:
        with open(os.path.join("songs", song_name + ".json"), 'r') as song_json:
            my_song = json.load(song_json)
        song_json.close()

        song = env.get_template("song.html")
        song_template = song.render(song=my_song)
        with open(os.path.join("html", song_name + ".html"), 'w') as new_html:
            new_html.write(song_template)
        new_html.close()

    generate_index(song_list=song_list)