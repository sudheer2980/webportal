from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'webportal.views.home', name='home'),
    url(r'^$', 'webapp.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^upload/$','webapp.views.contributor_upload'),
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/$','webapp.views.contributor_profile_subject'), 
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/$','webapp.views.contributor_profile_topic'),
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/(?P<topics>\w+)/(?P<id>\d+)/$','webapp.views.contributor_profile_comment'),
)
