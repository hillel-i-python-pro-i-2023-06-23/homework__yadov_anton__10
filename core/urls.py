from django.urls import path, include


# Add routes instead of using decorators in views
urlpatterns = [
    path("generate/", include("apps.generate_users.urls")),
]
