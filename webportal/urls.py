from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','webapp.views.index'),
    url(r'^webapp/', include('webapp.urls')),
    # url(r'^user/', include('django.contrib.auth.urls')),


    # this takes us to contributor profile
    url(r'^contributor/profile/$','webapp.views.contributor_profile'), 
    # this takes us to reviewer profile
    url(r'^reviewer/profile/$','webapp.views.reviewer_profile'),


    url(r'^login/$','webapp.views.userlogin'),
    # this is used for logging out the respective user    
    url(r'^logout/$','webapp.views.user_logout'),


    # this is for changing password, and for confirmation of that change
    url(r'^user/password/change/$','django.contrib.auth.views.password_change'),
    url(r'^user/password/change/done/$','django.contrib.auth.views.password_change_done'),


    url(r'^contributor/signup/$','webapp.views.contributor_signup'),
    url(r'^reviewer/signup/$','webapp.views.reviewer_signup'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
