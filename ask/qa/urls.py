from django.conf.urls import url, path
from qa.views import question

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    path('/', question)
 ]