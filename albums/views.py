from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category, Comment
from .forms import CommentForm

# Create your views here.

def index(request):
    category = request.GET.get('category')

    if category == None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(cateogory__name=category)

    categories = Category.objects.all()

    context = {
        'categories':categories,
        'photos':photos,
    }

    return render(request, 'albums/index.html', context)


def create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                group=data['category_new'])

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
        'categories': categories,
        }
    return render(request, 'albums/create.html', context)


def photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = photo.comment_set.all()
    context = {
        'photo':photo,
        'comment_form':comment_form,
        'comments':comments,
    }
    return render(request, 'albums/photo.html', context)


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


def category(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])

        else:
            category = None
        return redirect('albums:index')

    context = {
        'categories': categories,
        }
    return render(request, 'albums/category.html', context)