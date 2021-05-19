from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from .models import Photo, Category, Comment
from .forms import CommentForm

# Create your views here.

def index(request, pk):
    User = get_user_model()
    host = User.objects.get(pk=pk)
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    page = int(request.GET.get('page', default='1')) # page 매개변수가 없을 경우 1 이 되게, GET방식으로 page 변수를 받음
    paginator = Paginator(categories, 3, allow_empty_first_page = True) # Paginator(자료목록, 몇개씩출력할지)
    photo = paginator.get_page(page) # 현재 페이지에 대한 자료를 가져옴

    all_page_list = paginator.page_range # 전체 페이지 리스트 가져오기
    alpha= beta = 0 # 항상 목록에 5개만 나오게 하기 위한 임시변수

    if page -2 <= 0 : 
        alpha = 3 - page
    elif page +2 > len(all_page_list) :
        beta = 2 + page - len(all_page_list) 
    page_list = all_page_list[max((page-1)-2-beta, 0)  : min((page-1)+3+alpha, len(all_page_list))] # paginator에서 쓸 페이지 리스트

    context = {
        'host':host,
        'categories':categories,
        'photos':photos,
        'page_list':page_list,
    }

    return render(request, 'albums/index.html', context)


def create(request, pk):
    User = get_user_model()
    host = User.objects.get(pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])

        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                content=data['content'],
                image=image,
            )

        return redirect('albums:photo', photo.pk)

    context = {
        'host':host,
        'categories': categories,
        }
    return render(request, 'albums/create.html', context)


def photo(request, pk):
    User = get_user_model()
    host = User.objects.get(pk=pk)

    categories = Category.objects.all()
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = photo.comment_set.all()
    context = {
        'categories':categories,
        'photo':photo,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'albums/photo.html', context)


def delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    
    if request.method == 'POST':
        photo.delete()
        return redirect('albums:index')
    else:
        return redirect('albums:photo', photo.pk)



def comments_create(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.photo = photo
        comment.save()
        return redirect('albums:photo', photo.pk)

    context = {
        'comment_form': comment_form,
        'photo': photo,
    }
    return render(request, 'photos/photo.html', context)


# def category(request):
#     categories = Category.objects.all()

#     if request.method == 'POST':
#         data = request.POST

#         if data['category'] != 'none':
#             category = Category.objects.get(id=data['category'])

#         elif data['category_new'] != '':
#             category, created = Category.objects.get_or_create(
#                 name=data['category_new'])

#         else:
#             category = None
#         return redirect('albums:index')

#     context = {
#         'categories': categories,
#         }
#     return render(request, 'albums/category.html', context)