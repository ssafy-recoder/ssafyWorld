from django.shortcuts import render
from accounts.models import User

# Create your views here.
def index(request, pk):
    user = User.objects.get(pk=pk)
    context = {
        'this_user': user,
    }
    return render(request, 'homepage/index.html', context)

def test(request):
    return render(request, 'homepage/test.html')