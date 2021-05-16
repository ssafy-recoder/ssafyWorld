from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import User
from .models import Location

# Create your views here.
def index(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    
    return render(request, 'friends/index.html', context)


def recommend(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    
    users = User.objects.all()
    list_friends = []
    for user in users:
        if user.followers.filter(pk=person.pk).exists():
            list_friends.append(user)
    list_recommend = {}
    for friend in list_friends:
        for user in users:
            if user != person and user not in list_friends:
                if user.followers.filter(pk=friend.pk).exists():
                    if user not in list_recommend:
                        list_recommend[user] = 1
                    else:
                        list_recommend[user] += 1 
    context = {
        'person': person,
        'list_friends': list_friends,
        'list_recommend': list_recommend,
    }
    return render(request, 'friends/recommend.html', context)


def location(request, username):
    key_js = 'cf38b368117baa7591dbe1e159585d8c'
    context = {
        'key_js': key_js,
    }
    return render(request, 'friends/location.html', context)


def save_location(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    key_js = 'cf38b368117baa7591dbe1e159585d8c'
    latitude_submit = request.POST.get('latitude_submit')
    longitude_submit = request.POST.get('longitude_submit')
    print(latitude_submit, longitude_submit)
    location = Location(user=person, latitude=latitude_submit, longitude=longitude_submit)
    location.save()
    context = {
        'key_js': key_js,
    }
    return render(request, 'friends/location.html', context)