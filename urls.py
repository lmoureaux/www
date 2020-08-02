from django.conf.urls import *
from django.contrib import admin
from longturn.game.views import nations_v
from longturn.views import *

admin.autodiscover()

urlpatterns = [
	url(r'^nations/$',			nations_v, name='nations'),
	url(r'^account/',			include('longturn.player.urls')),
	url(r'^game/',				include('longturn.game.urls')),
	url(r'^admin/',				admin.site.urls),
	url(r'^',						include('cms.urls')),
]
