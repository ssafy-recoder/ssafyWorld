from django.shortcuts import render, redirect, get_object_or_404
from .forms import guestForm
from accounts.models import User
from .models import Guest
from django.core.paginator import Paginator
from django.views.generic.list import ListView

# Create your views here.
# pk: 해당 미니홈피 주인
def index(request, pk):
    global mini_host
    host = User.objects.get(pk=pk)
    mini_host = host

    guest_articles = Guest.objects.filter(host_id=pk)[::-1]
    paginator = Paginator(guest_articles, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # page_obj.paginator.num_pages
    if page_obj.number > 2 and page_obj.number+2 <= page_obj.paginator.num_pages:
        pages_count = list(range(page_obj.number-2,  page_obj.number+2))
    elif page_obj.number > 2 and page_obj.number+2 > page_obj.paginator.num_pages:
        pages_count = list(range(page_obj.number-2,  page_obj.paginator.num_pages+1))
    else:
        pages_count = list(range(page_obj.number,  page_obj.number+1))
    
    # 방명록 글 등록
    if request.method == 'POST':
        form = guestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.user = request.user
            guest.host = host
            guest.save()
        return redirect('guest:index', pk)
    else:
        form = guestForm()
    context = {
        'form': form,
        'host': host,
        'page_obj': page_obj,
        'pages_count': pages_count,
    }
    return render(request, 'guest/index.html', context)


# 작성된 방명록 수정
def update(request, pk, article_pk):
    host = User.objects.get(pk=pk)
    article = Guest.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = guestForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('guest:index', pk)
    else:
        form = guestForm(instance=article)
    context = {
        'form': form,
        'pk': pk,
        'article_pk': article_pk,
        'host': host
    }
    return render(request, 'guest/update.html', context)


def delete(request, pk, article_pk):
    guest = get_object_or_404(Guest, pk=article_pk)
    if request.user.is_authenticated:
        if request.user == guest.user:
            guest.delete()
    return redirect('guest:index', pk)
