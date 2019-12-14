from django.urls import include, path

urlpatterns = [
    path('', IndexView.as_view(), name="index")
]