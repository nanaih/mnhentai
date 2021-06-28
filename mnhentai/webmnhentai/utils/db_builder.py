import json
import os
from ..models import *


def create_missing_entries(doujin):
    if 'tag' in doujin:
        for tag_name in doujin['tag']:
            try:
                if Tag.objects.get(name=tag_name):
                    continue
            except Tag.DoesNotExist:
                t = Tag(name=tag_name)
                t.save()


def make_doujin_links():
    pass


def generate_db(path_to_doujins):
    folders = os.listdir(path_to_doujins)
    for folder in folders:
        if os.path.exists(path_to_doujins + '/' + folder + '/' + 'metadata.json'):
            with open(path_to_doujins + '/' + folder + '/' + 'metadata.json') as doujin_meta:
                doujin_json = json.load(doujin_meta)
            
            create_missing_entries(doujin_json)
            make_doujin_links()
