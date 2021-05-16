from django.shortcuts import render, redirect
from .forms import guestForm
from accounts.models import User
from .models import Guest
from django.core.paginator import Paginator
from django.views.generic.list import ListView

# Create your views here.
# pk: 해당 미니홈피 주인
def index(request, pk):
    person = User.objects.get(pk=pk)
    guest_articles = Guest.objects.filter(person_id=pk)[::-1]
    paginator = Paginator(guest_articles, 1) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # 방명록 글 등록
    if request.method == 'POST':
        form = guestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.user = request.user
            guest.person = person
            guest.save()
        return redirect('guest:index', pk)
    else:
        form = guestForm()
    context = {
        'form': form,
        'person': person,
        'page_obj': page_obj,
    }
    return render(request, 'guest/guest_list.html', context)


# 작성된 방명록 수정
def update(request, pk, article_pk):
    article = Guest.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = guestForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('guest:index', pk)

