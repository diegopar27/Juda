"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from leader.routers import router_Leader
from voter.routers import router_Voter
from candidate.routers import router_Candidate
from neighborhood.routers import router_Neighborhood_leader, router_Neighborhood
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'docs/', schema_view.with_ui('swagger',
                                       cache_timeout=0), name='schema-swagger-ui'),
    path(r'redocs/', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('api/Leader/', include(router_Leader.urls)),
    path('api/Voter/', include(router_Voter.urls)),
    path('api/Candidate', include(router_Candidate.urls)),
    path('api/Neighborhood', include(router_Neighborhood.urls)),
    path('api/Neighborhood_leader', include(router_Neighborhood_leader.urls)),

]
