from django.conf.urls import url

from . import views

app_name = "posts"
urlpatterns = [
    url(
        r'^search/$',
        views.PostSearchListView.as_view(),
        name='post_search_list_view',
    ),
]
