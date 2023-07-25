from django.urls import path
from .views import post_list_view, post_create_form_view, post_update_view,post_detail_view, post_confirm_delete_view


app_name ='posts'
urlpatterns =[
    path('', post_list_view, name='post-list'),
    #path('create/', post_create_view, name = 'post-create'),
    path('create/', post_create_form_view, name = 'post-create'),
    path('<int:id>/edit/',post_update_view ),
    path('<int:id>/', post_detail_view),
    path('<int:id>/delete/',post_confirm_delete_view),
]
