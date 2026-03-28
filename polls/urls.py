from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("django_admin_site_yutomurao/", admin.site.urls),
    # /polls/ という URL がリクエストされたら main/urls.py を参照するよう指定
    path("polls/", include("main.urls")),
]
