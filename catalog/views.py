from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Game, Publisher, Genre, Comments
from .forms import  CommentForm
from django.utils import timezone
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm



def index(request):
    games = Game.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html',{'games': games})


class GameDetailView(generic.DetailView):
    	model = Game
        
def GamesListView(request):
    gamesList = Game.objects.filter(published_date__lte=timezone.now()).order_by('-release_date')
    return render(request, 'game_list.html',{'gamesList': gamesList})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Game , pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('game-detail', pk)
    else:
        form = CommentForm()
    return render(request, 'catalog/add_comment_to_post.html', {'form': form})


# Create your views here.
