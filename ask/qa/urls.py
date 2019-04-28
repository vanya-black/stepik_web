from django.conf.urls import url
from view import test

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'^$', test)
 ]