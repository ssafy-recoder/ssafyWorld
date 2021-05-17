from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from .forms import HomeCommentForm
from .models import HomeComment
from django.contrib.auth import get_user_model

# Create your views here.
def index(request, pk):
    host = User.objects.get(pk=pk)
    comment_form = HomeCommentForm()
    comments = host.homecomment_set.all()
    context = {
        'this_user': host,
        'comment_form': comment_form,
        'comments': comments,
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

        


