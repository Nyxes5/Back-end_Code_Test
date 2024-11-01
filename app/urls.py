from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"persons", views.PersonViewSet, basename="person")

urlpatterns = router.urls
