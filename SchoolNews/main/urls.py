from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('create', views.create, name='create'),
    path('article/edit/<int:id>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:id>/', views.delete_article, name='delete_article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
