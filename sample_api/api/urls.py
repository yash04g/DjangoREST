from django.urls import path 
from api import views

urlpatterns = [
    path('users/',views.usersApi),
    path('articles/',views.articleApi),
    path('createArticle',views.createArticleApi)
    # path('createUsers/',views.createUserApi)
]

