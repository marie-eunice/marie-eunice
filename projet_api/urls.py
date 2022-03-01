from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'projets', views.ProjetViewSet)

#routage automatique des URL de l' API. 
#URL de connexion pour l'API navigable
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

