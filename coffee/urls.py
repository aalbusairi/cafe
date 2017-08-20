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
	url(r'^beanlist/$', views.bean_list, name="beanlist"),
	url(r'^beanupdate/(?P<post_id>\d+)/$', views.bean_update, name="beanupdate"),
	url(r'^beandelete/(?P<post_id>\d+)/$', views.bean_delete, name="beandelete"),
	url(r'^powderlist/$', views.powder_list, name="powderlist"),
	url(r'^powderupdate/(?P<post_id>\d+)/$', views.powder_update, name="powderupdate"),
	url(r'^powderdelete/(?P<post_id>\d+)/$', views.powder_delete, name="powderdelete"),
	url(r'^roastlist/$', views.roast_list, name="roastlist"),
	url(r'^roastupdate/(?P<post_id>\d+)/$', views.roast_update, name="roastupdate"),
	url(r'^roastdelete/(?P<post_id>\d+)/$', views.roast_delete, name="roastdelete"),
	url(r'^syruplist/$', views.syrup_list, name="syruplist"),
	url(r'^syrupupdate/(?P<post_id>\d+)/$', views.syrup_update, name="syrupupdate"),
	url(r'^syrupdelete/(?P<post_id>\d+)/$', views.syrup_delete, name="syrupdelete"),
	url(r'^coffeelist/$', views.coffee_list, name="coffeelist"),
	url(r'^coffeeupdate/(?P<post_id>\d+)/$', views.coffee_update, name="coffeeupdate"),
	url(r'^coffeedelete/(?P<post_id>\d+)/$', views.coffee_delete, name="coffeedelete"),		
]