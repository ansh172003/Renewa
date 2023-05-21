from django.shortcuts import render
from .models import BlogModel
from django.contrib import messages
from .forms import Imageupload
from django.shortcuts import get_object_or_404
import openai

def askGPT(items):

    openai.api_key = "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"
    prompt = "Here is the list of my leftovers items, suggest me a indian easy to make recipe that I can make using these leftovers" + items
    chat = openai.Completion.create( engine = "text-davinci-003", prompt = prompt, max_tokens = 1024, n=1, stop=None, temperature=0.5)
    
    reply = chat.choices[0].text
    print(reply)
    return reply

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

def blog_detail(request, id):
    detail = get_object_or_404(BlogModel, pk = id)
    data = {
        'detail':detail,
    }
    return render(request,"mainsite/blog-solo.html",data)

    
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
    return render(request, 'mainsite/food.html')
    

def recipe(request):
    if request.method == 'POST':
        recipe = request.POST['recipe']
        print(recipe)
        if recipe:
            output = askGPT('garlic, onion, tomato')
            data = {
                'output':output
            }
            return render(request,'mainsite/recipe_output.html',data)
    
    return render(request,'mainsite/recipe.html')
    
def recipe_output(request):
    return render(request,'mainsite/recipe_output.html')

def food_card(request):
    return render(request,'mainsite/food_card.html')

def grocery(request):
    pass

def donate(request):
    return render(request, 'mainsite/donate.html')