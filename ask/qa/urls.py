from django.conf.urls import url
from qa.views import test

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'^$', test)
 ]