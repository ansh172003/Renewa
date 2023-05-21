from django.shortcuts import render, redirect
from .models import BlogModel, NightFood, Grocery, Donate
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
        return redirect('blog')
 
    return render(request, 'mainsite/blogwrite.html')

def food(request):
    return render(request, 'mainsite/food.html')
    
def congo(request):
    return render(request, 'mainsite/single-donation.html')

def recipe(request):
    if request.method == 'POST':
        recipe = request.POST['recipe']
        # print(recipe)
        if recipe:
            output = askGPT(recipe)
            data = {
                'output':output
            }
            return render(request,'mainsite/recipe_output.html',data)
    
    return render(request,'mainsite/recipe.html')
    
def recipe_output(request):
    return render(request,'mainsite/recipe_output.html')

def food_card(request):
    foods = NightFood.objects.all()
    data={
        'foods':foods,

    }
    return render(request,'mainsite/food_card.html',data)

def grocery_card(request):
    groceries = Grocery.objects.all()
    data={
        'groceries':groceries,

    }
    return render(request,'mainsite/grocery_card.html',data)

def singlegrocery(request, id):
    detail = get_object_or_404(Grocery, pk = id)
    data = {
        'detail':detail,
    }
    return render(request,"mainsite/single-grocery.html",data)



def singlefood(request, id):
    detail = get_object_or_404(NightFood, pk = id)
    data = {
        'detail':detail,
    }
    return render(request,"mainsite/single-food.html",data)


def grocery(request):
    pass

def donate(request):
    if request.method == 'POST':
        food_type = request.POST['food_type']
        address = request.POST['address']
        donate = Donate(food_type=food_type, address=address)
        donate.save()
        return redirect('congo')



    return render(request, 'mainsite/donate.html')

def user_choice(request):
    foodItems = []
    if request.method == 'POST':
        foodItems = request.POST.getlist('foodItem')
        print(foodItems)
    return render(request, 'mainsite/choices.html',{'foodItmes':foodItems})