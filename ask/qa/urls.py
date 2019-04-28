from django.conf.urls import url
from qa.view import test

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'^$', test)
 ]