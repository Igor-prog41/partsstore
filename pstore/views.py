from symtable import Class

from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {'page_name': 'Home page', 'page_address': 'home'},
    {'page_name': 'Found parts', 'page_address': 'found_parts'},
    {'page_name': 'About', 'page_address': 'about'},
    {'page_name': 'Feedbacks', 'page_address': 'feedback'},
    {'page_name': 'Cart', 'page_address': 'cart' },
    {'page_name': 'Personal account', 'page_address': 'account' },
]

data_db = [
    {'id': 1,'title': 'nut', 'description': '<h1> HEX NUT </h1>, 5/16-24 THREAD, ½ IN HEX W, 17/64 IN HEX H, STEEL, GRADE 5, ZINC PLATED, 100 PK', 'is_published': True},
    {'id': 2,'title': 'bolt', 'description': 'bolt 1/2 by 1.5 inch', 'is_published': False},
    {'id': 3, 'title': 'screw', 'description': 'screw  1.5 inch', 'is_published': True},
    {'id': 4, 'title': 'heater', 'description': 'H-2000', 'is_published': True},
    {'id': 5, 'title': 'fitting', 'description': 'fitting  3/4 to 1 inch', 'is_published': True},
]

cats_db =[
    {'id': 1, 'name': 'Fasteners'},
    {'id': 2, 'name': 'Filter'},
    {'id': 3, 'name': 'Hydraulic hoses'},
]


def index(request): # HttpRequest

    data = {'title': 'main page',
            'menu': menu,
            'post': data_db,
            }

    return render(request, 'pstore/index.html', context=data)


def about(request):
    data = {'title': 'About',
            'menu': menu}
    return render(request, 'pstore/about.html', context=data)


def part(request,part_id,):
    data = {'title': 'Part',
            'menu': menu,
            'part_detail': data_db[part_id-1]
            }
    return render(request, 'pstore/part.html', context=data)


def show_category(request,cat_id,):
    data = {'title': 'main page for show category',
            'menu': menu,
            'post': data_db,
            }
    return render(request, 'pstore/index.html', context=data)



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")




# views for example and test

def categories(request,cat_id): # HttpRequest
    return HttpResponse(f'<H1>Parts by categories</H1> <p>id : {cat_id}</p>')


def categories_by_slug(request,cat_slug): # HttpRequest
    return HttpResponse(f'<H1>Parts by categories</H1> <p>slug : {cat_slug}</p>')


def year_archive(request,year): # HttpRequest
    if year > 2025:
        uri = reverse('cats',args=('heater',))
        return HttpResponsePermanentRedirect(uri)
    print(request.POST)
    return HttpResponse(f'<H1>Archive by year</H1> <p>year : {year}</p><hr>')
