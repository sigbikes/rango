from django.conf.urls import url, include
from rango import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$',views.show_category, name = 'show_category'),
        url(r'^add_category/$', views.add_category, name = 'add_category'),

        ]
