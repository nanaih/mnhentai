import json
import os
from datetime import datetime
from .models import *


GENERIC_ENTRY_FIELDS = (
    (Parody, 'parody'),
    (Character, 'character'),
    (Tag, 'tag'),
    (Artist, 'artist'),
    (Group, 'group'),
    (Language, 'language'),
    (Category, 'category')
)
DT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


def remove_escape_char(path_escaped):
    return (((path_escaped.encode('unicode_escape')).replace(b'\\', b'/')).decode('utf-8')).replace('//', '/')


def get_id(url_str):
    """get id in url from 'https://nhentai.net/g/361286' format"""
    url_list = url_str.split('/')
    id_list = [x for x in url_list if x.isdecimal()]
    if len(id_list) == 1:
        return int(id_list[0])
    else:
        # (really bad) defaults to zero if it doesn't have a nhentai id 
        # or someday a bad url shows up
        return 0


def get_upload_date(date_str):
    return datetime.strptime(date_str, DT_FORMAT)


def get_language(lang_list):
    if len(lang_list) > 1 and 'translated' in lang_list:
        lang_list.remove('translated')
    return lang_list[0]


def create_generic_entry(doujin_dict, key, model_class):
    if key in doujin_dict:
        for entry_name in doujin_dict[key]:
            try:
                if model_class.objects.get(name=entry_name):
                    continue
            except model_class.DoesNotExist:
                model_object = model_class(name=entry_name)
                model_object.save()


def create_missing_entries(doujin):
    for entry in GENERIC_ENTRY_FIELDS:
        create_generic_entry(doujin, entry[1], entry[0])


def make_doujin_links(doujin, doujin_path):
    n_id = 0
    if 'URL' in doujin:
        n_id = get_id(doujin['URL'])
        if n_id != 0:
            try:
                Doujinshi.objects.get(nhentai_id=n_id)
                return False
            except Doujinshi.DoesNotExist:
                pass
    
    new_doujin = Doujinshi( nhentai_id = n_id,
                            title = doujin['title'],
                            subtitle = doujin['subtitle'],
                            upload_date = get_upload_date(doujin['upload_date']),
                            Pages = doujin['Pages'],
                            is_translated = 'translated' in doujin['language'],
                            dir_path = doujin_path)
    if 'language' in doujin:
        new_doujin.language = Language.objects.get(name=get_language(doujin['language']))
    if 'category' in doujin:
        new_doujin.category = Category.objects.get(name=doujin['category'][0])
    new_doujin.save()

    if 'parody' in doujin:
        for parody_name in doujin['parody']:
            parody_obj = Parody.objects.get(name=parody_name)
            new_link = Parodys(doujinshi=new_doujin, parody=parody_obj)
            new_link.save()
    if 'character' in doujin:
        for character_name in doujin['character']:
            character_obj = Character.objects.get(name=character_name)
            new_link = Characters(doujinshi=new_doujin, character=character_obj)
            new_link.save()
    if 'tag' in doujin:
        for tag_name in doujin['tag']:
            tag_obj = Tag.objects.get(name=tag_name)
            new_link = Tags(doujinshi=new_doujin, tag=tag_obj)
            new_link.save()
    if 'artist' in doujin:
        for artist_name in doujin['artist']:
            artist_obj = Artist.objects.get(name=artist_name)
            new_link = Artists(doujinshi=new_doujin, artist=artist_obj)
            new_link.save()
    if 'group' in doujin:
        for group_name in doujin['group']:
            group_obj = Group.objects.get(name=group_name)
            new_link = Groups(doujinshi=new_doujin, group=group_obj)
            new_link.save()
    return True

def generate_db(path_to_doujins):
    folders = os.listdir(path_to_doujins)
    doujins_added = 0
    for folder in folders:
        f_path = os.path.join(path_to_doujins, folder, 'metadata.json')
        if os.path.exists(f_path):
            with open(f_path) as doujin_meta:
                doujin_json = json.load(doujin_meta)
                doujin_meta.close()

            if 'category' in doujin_json:
                doujin_json['category'] = [doujin_json['category']]
            create_missing_entries(doujin_json)
            doujins_added += make_doujin_links(doujin_json, remove_escape_char(os.path.join(path_to_doujins, folder)))
        
    return dict(all_folders=len(folders), doujins_added=doujins_added)
