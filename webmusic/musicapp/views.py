from django.contrib.messages.api import success
from django.shortcuts import render
from musicapp.models import Song ,watchlater , History
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login, logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import Createuserform
from django.db.models import Case, When, query

def index(request):
    song = Song.objects.all()
    return render(request ,"index.html", {'song':song})


def allsongs(request):
    song = Song.objects.all()
    return render(request , "allsongs.html", {'song':song})


def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request , "songpost.html", {'song':song})

def signup(request):
    form = Createuserform()
    if request.method =="POST":
        form=Createuserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request , 'Account Created')
            return redirect('login')

    return render(request , "signup.html" ,{'form': form})

def loginpage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)
        if user is not None:
            login(request , user)
            return redirect('/')

        else:
            messages.info(request ,'username or password is incorect')
            return render(request , 'login.html')
    return render(request , 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/')

def listenlater(request):
    if request.method == 'POST':
        user = request.user
        vedio_id =request.POST['vedio_id']
        listen = watchlater.objects.filter(user=user)

        for i in listen:
            if vedio_id == i.vedio_id:
                message = "Your song is already added"
                break
        else:
            Watchlater = watchlater(user=user, vedio_id=vedio_id)
            Watchlater.save()
            message = "Song added"
        songs =  Song.objects.filter(song_id = vedio_id).first()
        return render(request, 'songpost.html',{'songs':songs , 'message':message})
    wl = watchlater.objects.filter(user = request.user)
    ids= []
    for i in wl:
        ids.append(i.vedio_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in = ids).order_by(preserved)
    return render(request , 'listenlater.html', {'song':song})

def history(request):
    if request.method =="POST":
        user = request.user
        music_id = request.POST['music_id']
        history  = History(user = user , music_id = music_id)
        history.save()

        
        return redirect(f'allsongs/{music_id}')

    history = History.objects.filter(user= request.user)
    ids= []
    for i in history:
        ids.append(i.music_id)

    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in = ids).order_by(preserved)
    return render(request , 'history.html', {'history': song})


def search(request):
    query = request.GET.get('query')
    song = Song.objects.all()
    qs = song.filter(name__icontains = query)

    return render(request, 'search.html', {'songs':qs, 'query':query})