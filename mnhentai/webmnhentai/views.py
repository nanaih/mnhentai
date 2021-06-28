from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from django.utils.encoding import smart_str

from .models import Doujinshi
from .utils.db_builder import generate_db




def init(request):
    template = loader.get_template('nhentai/initialize.html')
    return HttpResponse(template.render({}, request))

def init_db(request):
    data = generate_db(request.POST['doujins_path'])
    template = loader.get_template('nhentai/initdb_result.html')
    return HttpResponse(template.render(data, request))
