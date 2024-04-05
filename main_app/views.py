from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Comic, Character
from .forms import RatingForm
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def comics_index(request):
  comics = Comic.objects.all()
  return render(request, 'comics/index.html', {
    'comics': comics
  })

def comics_detail(request, comic_id):
  comic = Comic.objects.get(id=comic_id)
  id_list = comic.characters.all().values_list('id')
  characters_comic_doesnt_have = Character.objects.exclude(id__in=id_list)
  rating_form = RatingForm()
  return render(request, 'comics/detail.html', { 'comic': comic, 
  'rating_form': rating_form,
  'characters': characters_comic_doesnt_have
  })

class ComicCreate(CreateView):
  model = Comic
  fields = ['title', 'description', 'creator', 'first_appearance', 'publisher']

class ComicUpdate(UpdateView):
  model = Comic
  fields = ['description', 'creator', 'first_appearance', 'publisher']

class ComicDelete(DeleteView):
  model = Comic
  success_url = '/comics'

def add_rating(request, comic_id):
  form = RatingForm(request.POST)
  if form.is_valid():
    new_rating = form.save(commit=False)
    new_rating.comic_id = comic_id
    new_rating.save()
  return redirect('detail', comic_id=comic_id)

class CharacterList(ListView):
  model = Character

class CharacterDetail(DetailView):
  model = Character

class CharacterCreate(CreateView):
  model = Character
  fields = '__all__'

class CharacterUpdate(UpdateView):
  model = Character
  fields = ['name', 'superpower']

class CharacterDelete(DeleteView):
  model = Character
  success_url = '/characters'

def assoc_character(request, comic_id, character_id):
  Comic.objects.get(id=comic_id).characters.add(character_id)
  return redirect('detail', comic_id=comic_id)

def unassoc_character(request, comic_id, character_id):
  Comic.objects.get(id=comic_id).characters.remove(character_id)
  return redirect('detail', comic_id=comic_id)