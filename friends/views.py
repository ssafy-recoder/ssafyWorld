from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from accounts.models import User
from .models import Location

# Create your views here.
def index(request, username):
    host = get_object_or_404(get_user_model(), username=username)
    all_users = User.objects.all()
    
    list_friends = []
    for user in all_users:
        if user.followers.filter(pk=host.pk).exists():
            list_friends.append(user)

    context = {
        'host': host,
        'all_users': all_users,
        'list_friends': list_friends,
    }
    
    return render(request, 'friends/index.html', context)


def recommend(request, username):
    host = get_object_or_404(get_user_model(), username=username)
    
    users = User.objects.all()
    list_friends = []
    for user in users:
        if user.followers.filter(pk=host.pk).exists():
            list_friends.append(user)
    list_recommend = {}
    for friend in list_friends:
        for user in users:
            if user != host and user not in list_friends:
                if user.followers.filter(pk=friend.pk).exists():
                    if user not in list_recommend:
                        list_recommend[user] = 1
                    else:
                        list_recommend[user] += 1 
    sdict = sorted(list_recommend.items(), key=lambda x: x[1], reverse=True)
    sdict = dict(sdict)
    context = {
        'host': host,
        'this_user': host,
        'list_friends': list_friends,
        'list_recommend': sdict,
    }
    return render(request, 'friends/recommend.html', context)


def location(request, username):
    host = get_object_or_404(get_user_model(), username=username)
    key_js = 'cf38b368117baa7591dbe1e159585d8c'
    loca = Location.objects.all()
    context = {
        'key_js': key_js,
        'this_user': host,
        'loca': loca,
    }
    return render(request, 'friends/location.html', context)


def save_location(request, username):
    host = get_object_or_404(get_user_model(), username=username)
    key_js = 'cf38b368117baa7591dbe1e159585d8c'
    latitude_submit = request.POST.get('latitude_submit')
    longitude_submit = request.POST.get('longitude_submit')
    print(latitude_submit, longitude_submit)
    location = Location(user=host, latitude=latitude_submit, longitude=longitude_submit)
    location.save()
    context = {
        'key_js': key_js,
        'this_user': host,
    }
    return render(request, 'friends/location.html', context)