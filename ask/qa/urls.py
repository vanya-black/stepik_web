from django.conf.urls import url
from django.urls import path
from qa.views import question

urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    path('/', question)
 ]