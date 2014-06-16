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


    # this takes us to contributor profile
    url(r'^contributor/profile/(?P<contri_username>\w+)/$','webapp.views.contributor_profile'), 
    url(r'^contributor/upload/$','webapp.views.contributor_upload'),
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/$','webapp.views.contributor_profile_subject'), 
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/$','webapp.views.contributor_profile_topic'),
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/(?P<topics>\w+)/(?P<id>\d+)/$','webapp.views.contributor_profile_comment'),




    # this takes us to reviewer profile
    url(r'^reviewer/profile/$','webapp.views.reviewer_profile'),
    url(r'^reviewer/profile/comments/(?P<sub_id>\d+)/(?P<rev_id>\d+)/$',
        'webapp.views.reviewer_profile_comment', name="comments"),
    url(r'^reviewer/profile/(?P<rev_username>\w+)/$','webapp.views.reviewer_profile'),
    url(r'^reviewer/profile/(?P<rev_username>\w+)/(?P<class_num>\d+)/$','webapp.views.reviewer_profile_subject'), 
    url(r'^reviewer/profile/(?P<rev_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/$','webapp.views.reviewer_profile_topic'),
    url(r'^reviewer/profile/(?P<rev_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/(?P<topics>\w+)/(?P<id>\d+)/$','webapp.views.reviewer_profile_comment'),


    # url(r'^reviewer/profile/comments/(?P<sub_id>\d+)/(?P<rev_id>\d+)/$',
    #    'webapp.views.reviewer_comment', name="comments"),
    # this enables us to edit our profile
    url(r'^contributor/profile/edit/$', 'webapp.views.contributor_profile_edit',
        name='profile_edit'),
    url(r'^reviewer/profile/edit/$', 'webapp.views.reviewer_profile_edit',
        name='profile_edit'),

    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/$','webapp.views.contributor_profile_subject'), 
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/$','webapp.views.contributor_profile_topic'),
    url(r'^contributor/profile/(?P<contri_username>\w+)/(?P<class_num>\d+)/(?P<sub>\w+)/(?P<topics>\w+)/(?P<id>\d+)/$','webapp.views.contributor_profile_comment'),
    url(r'^login/$','webapp.views.userlogin'),
    # this is used for logging out the respective user    
    url(r'^logout/$','webapp.views.user_logout'),
    
   
    url(r'^reviewer/profile/edit_success/$','webapp.views.edit_success'),  
    url(r'^contributor/profile/edit_success/$','webapp.views.edit_success'),

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
