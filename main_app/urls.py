from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name= 'home'),
  path('about/', views.about, name='about'),
  path('comics/', views.comics_index, name='index'),
  path('comics/<int:comic_id>/', views.comics_detail, name='detail'),
  path('comics/create/', views.ComicCreate.as_view(), name='comics_create'),
  path('comics/<int:pk>/update/', views.ComicUpdate.as_view(), name='comics_update'),
  path('comics/<int:pk>/delete/', views.ComicDelete.as_view(), name='comics_delete'),
  path('comics/<int:comic_id>/add_rating/', views.add_rating, name='add_rating'),
  path('comics/<int:comic_id>/assoc_character/<int:character_id>/', views.assoc_character, name='assoc_character'),
  path('comics/<int:comic_id>/unassoc_character/<int:character_id>/', views.unassoc_character, name='unassoc_character'),
  path('characters/', views.CharacterList.as_view(), name='characters_index'),
  path('characters/<int:pk>/', views.CharacterDetail.as_view(), name='characters_detail'),
  path('characters/create/', views.CharacterCreate.as_view(), name='characters_create'),
  path('characters/<int:pk>/update/', views.CharacterUpdate.as_view(), name='characters_update'),
  path('characters/<int:pk>/delete/', views.CharacterDelete.as_view(), name='characters_delete'),
]