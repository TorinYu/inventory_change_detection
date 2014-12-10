from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'compareImages.views.index',name='index'),

    url(r'^Compare$', 'compareImages.views.index',name='index'),

    url(r'^compare$', 'compareImages.views.index1',name='index1'),


    # url(r'^upload', 'compareImages.views.upload',name='upload'),

    url(r'^photo/(?P<id>\d+)$', 'compareImages.views.get_picture', name="photo"),

    url(r'^upload$', 'compareImages.views.upload',name='upload'),

    url(r'^upload1$', 'compareImages.views.upload1',name='upload1'),
)
