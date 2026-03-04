from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('api/', include('tasks.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

schema_view = get_schema_view(
    openapi.Info(title="Task API", default_version='v1'),
    public=True,
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger')),
]