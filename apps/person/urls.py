from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"person", views.PersonViewSet, basename="person")

urlpatterns = router.urls + [
    path('person/by_name/<str:name>', views.PersonByNameView.as_view())
]
