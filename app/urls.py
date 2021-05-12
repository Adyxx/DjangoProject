from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    path('details/<int:pk>/', views.AnimalDetailView.as_view(), name='animal-detail'),

    path('', views.AnimalListView.as_view(), name='animals'),

    path('animal/add/', views.AddAnimal.as_view(), name='add-animal'),
    path('animal/<int:pk>/update/', views.UpdateAnimal.as_view(), name='update-animal'),
    path('animal/<int:pk>/delete/', views.DeleteAnimal.as_view(), name='delete-animal'),


    # WIP
    path('gallery', views.GalleryView.as_view(), name='gallery'),
    path('types', views.TypeListView.as_view(), name='animal-type'),
    
]