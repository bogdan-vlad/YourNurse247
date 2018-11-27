from django.conf.urls import url, include
from accounts.views import index, registration, profile, logout, login
from accounts import url_reset

urlpatterns = [
    url(r'^registration/$', registration, name='registration'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password_reset/', include(url_reset)),
]