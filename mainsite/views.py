from django.shortcuts import render
from .models import BlogModel
from django.contrib import messages
from .forms import Imageupload

# Create your views here.

def home(request):
    blogs = BlogModel.objects.all()
    data={
        'blogs':blogs,

    }
    return render(request,'mainsite/landing.html',data)

def blogs(request):
    blogs = BlogModel.objects.all()
    data={
        'blogs':blogs,

    }
    return render(request,'mainsite/blog_page.html',data)
    
def blogwrite(request):
    context = {}
    if request.method == 'POST':
        title = request.POST['title']

        content = request.POST['content']
        files = request.FILES.getlist('image')

        for file in files:
            new_file = BlogModel(
                title = title,
                content = content,
                image = file,
        )
        new_file.save()
        # form = Imageupload(request.FILES)
        
        # image = form.cleaned_data.get("image")
        
        # image = files.get("image")

        # blogmodel = BlogModel(title=title, content=content, image=image)
        # blogmodel.save()
        messages.success(request,'Thanks for reaching out! Will contact you soon.')

        # print(image)
    
    return render(request, 'mainsite/blogwrite.html')

def food(request):
    pass

def recipe(request):
    return render(request,'mainsite/recipe.html')
    

def grocery(request):
    pass

def donate(request):
    return render(request, 'mainsite/donate.html')