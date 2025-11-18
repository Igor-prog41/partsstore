from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, "yyyy4")

urlpatterns = [
    path('part/<int:part_id>/', views.part, name='part'),

    path('',views.index,name='home'),
    path('found/', views.about, name='found_parts'),
    path('about/', views.about, name='about'),
    path('feedback/', views.about, name='feedback'),
    path('cart/', views.about, name='cart'),
    path('account/', views.about, name='account'),
    path('category/<int:cat_id>/', views.show_category, name='category'),




    path('categories/<int:cat_id>/',views.categories, name='cats_id'),
    path('categories/<slug:cat_slug>/',views.categories_by_slug, name='cats'),
    path('archive/<yyyy4:year>/',views.year_archive, name='archive'),
]