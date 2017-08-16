from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.usersignup, name="signup"),
	url(r'^login/$', views.userlogin, name="login"),
	url(r'^logout/$', views.userlogout, name="logout"),
	url(r'^bean/$', views.bean_create, name="bean"),
	url(r'^powder/$', views.powder_create, name="powder"),
	url(r'^syrup/$', views.syrup_create, name="syrup"),
	url(r'^roast/$', views.roast_create, name="roast"),
	url(r'^coffee/$', views.coffee_create, name="coffee"),
	url(r'^beanupdate/(?P<post_id>\d+)/$', views.bean_update, name="beanupdate"),
]