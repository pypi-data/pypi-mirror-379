# coding: utf-8
from django.urls import (
    re_path,
)

from .views import (
    test_view,
)


urlpatterns = [
    re_path(r'^test/$', test_view),
]
