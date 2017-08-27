from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^coffee/', include('coffee.urls', namespace="coffee")),
	url(r'^cart/', include('cart.urls', namespace="cart")),
	url(r'^payment/', include('payment.urls', namespace="payment")),
]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)