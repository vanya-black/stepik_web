from django.conf.urls import url
from qa.views import question

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'^$', question)
 ]