from django.http import HttpResponse, Http404
from django.template import loader
from django.utils.encoding import smart_str

from .models import Doujinshi
from .db_builder import generate_db, remove_escape_char
from .helpers import *


def index(request):
    latest_doujin_list = Doujinshi.objects.order_by('-upload_date')[:10]
    data = [[get_first_pic_url(doujao), doujao.id] for doujao in latest_doujin_list]
    data = dict(latest_doujin_list=data)
    template = loader.get_template('nhentai/index.html')
    return HttpResponse(template.render(data, request))


def details(request, doujin_id):
    try:
        doujin = Doujinshi.objects.get(pk=doujin_id)
    except Doujinshi.DoesNotExist:
        raise Http404("doujin does not exist")
    tags = get_doujin_tags_str(doujin.id)
    doujao = {  'tags': tags, 
                'title': doujin.title, 
                'coverlink': get_first_pic_url(doujin),
                'id': doujin.id,
                'gallery_list': get_all_img_links(doujin.id)
            }
    template = loader.get_template('nhentai/details.html')
    return HttpResponse(template.render(dict(doujin=doujao), request))


def reader(request, doujin_id, page_number):
    img_links = get_all_img_links(doujin_id)
    if page_number <= 0 or page_number > len(img_links):
        page_number = 1
    data = dict(img_links=img_links,
                page_number=page_number)
    template = loader.get_template('nhentai/reader.html')
    return HttpResponse(template.render(data, request))


def search(request):
    return HttpResponse("You're searching for \"%s\"." % request.POST['keywords'])


def get_tags(request):
    all_tags = get_all_tags_str()
    data = dict(tags=all_tags)
    template = loader.get_template('nhentai/all_tags.html')
    return HttpResponse(template.render(data, request))


def doujins_with_tag(request, tag):
    doujaos = get_doujins_with_tag(tag)
    doujins = [[get_first_pic_url(doujao), doujao] for doujao in doujaos]
    data = dict(doujins=doujins, tag=tag)
    template = loader.get_template('nhentai/get_doujins_with_tag.html')
    return HttpResponse(template.render(data, request))


def init(request):
    template = loader.get_template('nhentai/initialize.html')
    return HttpResponse(template.render({}, request))


def init_db(request):
    data = generate_db(remove_escape_char(str(request.POST['doujins_path'])))
    template = loader.get_template('nhentai/initdb_result.html')
    return HttpResponse(template.render(data, request))
