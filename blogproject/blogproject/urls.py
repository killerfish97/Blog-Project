from django.contrib import admin
from django.conf.urls import url,include
from myApp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home/',views.home_view),
    #url(r'home1/',views.home1_view),
    url(r'about/',views.about_view),
    url(r'contact/',views.contact_view),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r'logout/',views.logout_view),
    url(r'^$',views.post_list_view),
    url(r'(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)',views.post_detail_view,name='post_detail'),
    url(r'^(?P<id>\d+)/share',views.mail_send_view),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_list_view,name='post_list_by_tag_name')
]