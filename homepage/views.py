from django.shortcuts import render, redirect, get_object_or_404
from .forms import HomeCommentForm
from .models import HomeComment, Homepage
from django.contrib.auth import get_user_model

# Create your views here.
def index(request, pk):
    User = get_user_model()
    host = User.objects.get(pk=pk)
    comment_form = HomeCommentForm()
    comments = host.homecomment_set.all()
    home_info = host.homepage_set.all()
    users = User.objects.all()
    list_friends = []
    for user in users:
        if user.followers.filter(pk=host.pk).exists():
            list_friends.append(user)
    context = {
        'host': host,
        'comment_form': comment_form,
        'comments': comments,
        'home_info': home_info,
        'list_friends': list_friends,
    }
    return render(request, 'homepage/index.html', context)


def test(request):
    return render(request, 'homepage/test.html')


def comments_create(request, pk):
    if request.user.is_authenticated:
        host = get_object_or_404(get_user_model(), pk=pk)
        comment_form = HomeCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.host = host
            comment.writer = request.user
            comment.save()
            return redirect('homepage:index', host.pk)
        context = {
            'comment_form': comment_form,
            'host': host,
        }
        return render(request, 'homepage/index.html', context)
    return redirect('accounts:login')

        


