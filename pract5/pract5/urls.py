from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'pract5.paginas_estaticas.views.home', name='home'),
	 #url('^home', 'pract5.paginas_estaticas.views.home', name='home'),
	 url('^help', 'paginas_estaticas.views.help', name='help'),
	 url('^home', 'paginas_estaticas.views.home', name='home'),
	 url('^about', 'paginas_estaticas.views.about', name='about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
