from .views import (
    TodosListViewset,
    TodosViewset,
)
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.SimpleRouter(trailing_slash=False)
router.register(r"todoslist", TodosListViewset, basename="todoslist")
router.register(r"todos", TodosViewset, basename="todos")

urlpatterns = []

urlpatterns += router.urls
urlpatterns = format_suffix_patterns(urlpatterns)