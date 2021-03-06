import os
from .models import *
from .db_builder import remove_escape_char
from socket import gethostname, gethostbyname
from image_server import IMAGES_PORT
from re import match

URL_IMAGES_SERVER = f'http://{gethostbyname(gethostname())}:{IMAGES_PORT}/'
NOT_FOUND_IMG = "TODO"


def get_first_pic_path(doujin_obj):
    if os.path.exists(doujin_obj.dir_path):
        img_paths = os.listdir(doujin_obj.dir_path)
        img_paths.sort()
        return remove_escape_char(os.path.join(doujin_obj.dir_path, img_paths[0]))
    return '.'


def path_to_link(url: str , path: str):
    p = path.split('/')
    if len(p) >= 2:
        return url + '/' + p[-2] + '/' + p[-1]
    return url + NOT_FOUND_IMG


def get_first_pic_url(doujin):
    return path_to_link(URL_IMAGES_SERVER, get_first_pic_path(doujin))


def get_all_img_links(doujin_id):
    doujin_obj = Doujinshi.objects.get(pk=doujin_id)
    if os.path.exists(doujin_obj.dir_path):
        _paths = os.listdir(doujin_obj.dir_path)
        img_paths = []
        for _path in _paths:
            if match(r'\d+(\.jpg|\.png|\.jpeg)', _path):
                img_paths.append(_path)
        img_paths.sort()
        img_paths_escaped = [path_to_link(URL_IMAGES_SERVER, remove_escape_char(os.path.join(doujin_obj.dir_path, p))) for p in img_paths]
        return img_paths_escaped


def get_doujin_tags_str(doujin_id):
    tags = Tags.objects.filter(doujinshi=doujin_id)
    tag_str = [tag.tag.name for tag in tags]
    tag_str.sort()
    return tag_str


def get_all_tags_str():
    all_tags = Tag.objects.all()
    all_tags_str = [tag.name for tag in all_tags]
    all_tags_str.sort()
    return all_tags_str


def get_doujins_with_tag(tag_str):
    tag_obj = Tag.objects.get(name=tag_str)
    tags_obj = Tags.objects.filter(tag=tag_obj.id)
    doujins = [tag.doujinshi for tag in tags_obj]
    return doujins
