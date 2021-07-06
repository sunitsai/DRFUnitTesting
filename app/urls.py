from django.urls import path
from . import views
urlpatterns = [
    path("puppies/<int:pk>",views.get_delete_update_puppy,name="get_delete_update_puppy"),
    path("puppies/",views.get_post_puppies,name="get_post_puppies"),
]
