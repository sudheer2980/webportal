from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$','webapp.views.index'),
    url(r'^webapp/', include('webapp.urls')),
    # url(r'^user/', include('django.contrib.auth.urls')),

    url(r'^contributor/profile/edit/$', 'webapp.views.contributor_profile_edit',),
    
    # this takes us to contributor profile
    url(r'^contributor/profile/$','webapp.views.contributor_profile'), 
    url(r'^contributor/upload/$','webapp.views.contributor_upload'),
    url(r'^contributor/profile/(?P<class_num>\d+)/$','webapp.views.contributor_profile_subject'), 
    url(r'^contributor/profile/(?P<class_num>\d+)/(?P<sub>.+)/$','webapp.views.contributor_profile_topic'),
    url(r'^contributor/profile/(?P<class_num>\d+)/(?P<sub>.+)/(?P<topics>.+)/(?P<id>\d+)/$','webapp.views.contributor_profile_comment'),
    url(r'^contributor/profile/(?P<class_num>\d+)/(?P<sub>.+)/(?P<topics>.+)/(?P<id>\d+)/detail/$','webapp.views.contributor_profile_topic_detail'),
    
    url(r'^reviewer/profile/edit/$', 'webapp.views.reviewer_profile_edit'),


    # this takes us to reviewer profile
    url(r'^reviewer/profile/$','webapp.views.reviewer_profile'),
    url(r'^reviewer/profile/(?P<class_num>\d+)/$','webapp.views.reviewer_profile_subject'), 
    url(r'^reviewer/profile/(?P<class_num>\d+)/(?P<sub>.+)/$','webapp.views.reviewer_profile_topic'),
    url(r'^reviewer/profile/(?P<class_num>\d+)/(?P<sub>.+)/(?P<topics>.+)/(?P<id>\d+)/$','webapp.views.reviewer_profile_comment'),
    
    
    
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

    # this is used to display the content page of either the contributor or the reviewer
    url(r'^content/$','webapp.views.content'),
    

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^search/','webapp.views.search'),

)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
