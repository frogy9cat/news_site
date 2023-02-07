from django.shortcuts import render, redirect
from .models import News, Category1

from .forms import *
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from django.db.models import Q


class HomeNews(ListView):
    model = News
    template_name = 'new/news_list.html'
    context_object_name = "news"

    def get_queryset(self):
        return News.objects.filter(is_bool=True)


class CreateNews(CreateView):
    form_class = News_form
    template_name = 'new/add_news.html'
    success_url = reverse_lazy('home')


class GetNew(DetailView):
    model = News
    context_object_name = 'item'
    pk_url_kwarg = 'news_id'
    template_name = 'new/new.html'


def delete_new(request, new_id):
    new = News.objects.get(pk=new_id)
    new.delete()
    return redirect('home')


def get_category(request, category_id):
    news = News.objects.filter(category1=category_id)
    categories = Category1.objects.all()
    content = {
        "news": news,
        "title": "Ma'lumatlar",
        "categories": categories,

    }
    return render(request, "new/category.html", context=content)


def delete(request):
    news = News.objects.all()
    categories = Category1.objects.all()

    content = {
        "news": news,
        "title": "Ma'lumatlar",
        "categories": categories
    }
    return render(request, 'new/delete.html', context=content)




def search_field_title(request):
    print("yes")
    if request.method == "GET":
        title = News(request.GET)
        if title.is_valid():
            News.objects.create(**title.cleaned_data)
            print("ok")
            content = News.objects.filter(title=title)
            contents = {'contents':content}
            return render(request, 'new/sr.html', context=contents)
    else:
        title = News_form()
    content = {
        "title": title
    }

    return render(request, 'new/sr.html', context=content)




def post_search(request):
    categories = Category1.objects.all()
    search_post = request.GET.get('search')
    print(search_post)
    news_title = News.objects.filter(title__contains=search_post)
    news_info = News.objects.filter(info__icontains=search_post)
    if not search_post:
        return render(request, 'new/news_list.html')
    elif search_post: 
        if news_title:
            content = {'news': news_title, 'categories': categories}
            return render(request, 'new/search.html', context=content)
        elif news_info:
            content = {'news': news_info, 'categories': categories}
            return render(request, 'new/search.html', context=content)
        else:
            print(request, 'ниче не нашел')





def search(request):
    
    categories=Category1.objects.all()
    # search = request.POST['search']
    search_post = request.GET.get('search')
    
    if search_post:
        posts = News.objects.filter(Q(title__icontains=search_post)|Q(info_icontains=search_post))
    else:    # If not searched, return default posts    
        posts = News.objects.all().order_by("-created_at")

    content={
        'searchs':posts,
        "title":"Ma'lumotlar",
        "categories":categories,
        # "news":news,  
    }
    if len(posts)==0:
        return render(request,'new/return_null.html')
    else:
        return render(request,'new/search.html',context=content)




def login(request):
    render(request, 'new/login_page.html')



# def login_writed(request, login, password):






# def searchh(request):
#     languages = News.objects.all()
#     return render(request,'inc/nav.html',{"languages":languages})


# def search(request):
#     search_post = request.GET.get('search')
    
#     if search_post:
#         posts = News.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))
#     else:    # If not searched, return default posts    
#         posts = News.objects.all().order_by("-created_at")
    
#     return render(request,{'posts':posts})


