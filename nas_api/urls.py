from django.conf.urls import patterns, include, url
from movie.scraper import Scraper
from api.systeminfo import SystemInfo
from views.views import IndexView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^$', IndexView.as_view(), name='index_view'),
    url('api/v1/movie/scraper', Scraper.as_view(), name='v1_movie_scraper'),
    url('api/v1/systeminfo', SystemInfo.as_view(), name="v1_systeminfo"),
    # Examples:
    # url(r'^$', 'nas_api.views.home', name='home'),
    # url(r'^nas_api/', include('nas_api.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
