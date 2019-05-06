from django.conf.urls import url
from django.urls path
from qa.views import question

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    path('/', question)
 ]