from django.urls import path

from apps.generate_users import views

app_name = "generate_users"

# Add routes instead of using decorators in views
urlpatterns = [
    path("", views.generator, name="value"),
]
