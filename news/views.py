from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import News,Cat
from django.db.models import Q
from .forms import CreateNews

def home(request):
    context={}
    template = 'home.html'
    return render(request,template,context)

def create_news(request):
    form = CreateNews(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Post successfully created")
        return redirect('news:news_list')
    context = {'form':form}
    template = 'create_news.html'
    return render(request,template,context)


def news_detail(request,id=None):
    n = get_object_or_404(News, id = id)
    context = {'news':n}
    template = 'news_detail.html'
    return render(request,template,context)

# list of all news
def news_list(request):
    n = News.objects.all().order_by("-timestamp")
    ctb = Cat.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(n,12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    query = request.GET.get('q')
    if query:
        n = n.filter(
            Q(title__icontains = query)|
            Q(content__icontains = query)
              )
    context = {'users':users, 'ct':ctb}
    template = 'news_list.html'
    return render(request,template,context)


def update_news(request,id=None):
    d = get_object_or_404(News, id=id)
    form = CreateNews(request.POST or None,request.FILES or None, instance=d)
    if form.is_valid():
        d = form.save(commit=False)
        d.save()
        messages.success(request, "Post successfully updated.")
        return redirect('news:news_list')
    template = 'create_news.html'
    context = {'d':d,
               'form':form}
    return render(request,template,context)



def delete_news(request,id=None):
    n = get_object_or_404(News, id=id)
    n.delete()
    messages.success(request, "Post successfully deleted")
    return redirect('news:news_list')