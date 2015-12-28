from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import CHART
import EDS_WIND_MAP
from EDS_CHART import settings
from EDS_WIND_MAP import views
from CHART import views

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^EDS_CHART/', include('EDS_CHART.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^chart/', CHART.views.my_view),
                       url(r'^map/', EDS_WIND_MAP.views.map),
                       ) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()