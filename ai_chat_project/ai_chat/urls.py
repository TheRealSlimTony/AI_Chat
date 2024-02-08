from django.urls import path
from .views import MensajeListCreate
from .views import home, SearchQuestion

urlpatterns = [
    path("mensajes/", MensajeListCreate.as_view(), name="mensaje-list-create"),
    path("search_question/", SearchQuestion.as_view(), name="search-question"),
    path("", home, name="home"),
]
