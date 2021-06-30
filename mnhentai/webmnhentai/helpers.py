import os
from .models import *
from .db_builder import remove_escape_char
from socket import gethostname, gethostbyname 


URL_IMAGES_SERVER = f'http://{gethostbyname(gethostname())}:6969/'


def get_first_pic_path(doujin_obj):
    if os.path.exists(doujin_obj.dir_path):
        img_paths = os.listdir(doujin_obj.dir_path)
        img_paths.sort()
        return remove_escape_char(os.path.join(doujin_obj.dir_path, img_paths[0]))
    return '.'


def path_to_link(url, path):
    p = path.split('/')
    return url + '/' + p[-2] + '/' + p[-1]


def get_first_pic_url(doujin):
    return path_to_link(URL_IMAGES_SERVER, get_first_pic_path(doujin))
