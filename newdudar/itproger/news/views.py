from django.shortcuts import render, redirect
from .models import Articles, Reviews
from django.core.paginator import Paginator
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView
import datetime

def news_home(request):
    news = Articles.objects.order_by('-date')
    paginator = Paginator(news, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_home.html', {'news': news, 'page_obj': page_obj})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'articles'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['datumo'] = Reviews.objects.filter(articles = Articles.objects.get(id=self.kwargs.get('pk'))).order_by('-timedate')
        return context

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticleForm

def newsdeleteview(request, pk):
    form = Articles.objects.get(id = pk)
    #if form != None:
    form.delete()
    return redirect('news_home')

def deletereview(request, pk):
    print('pk', pk)
    reviewk = Reviews.objects.get(id=pk)
    print(reviewk)
    return redirect('home')

def reviews(request, pk):
    now = datetime.datetime.now()
    nower = str(now)
    if request.method == "POST":
        user = str(request.user.username)
        text = request.POST.get('textfield', False)
        timedate = str(nower[:19])
        review = Reviews.objects.create(user=user, timedate=timedate, text=text, articles=Articles.objects.get(id=pk))
        review.save()
        return redirect('news-detail', pk=pk)
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Some error occured while posting your news. Please check your submition details.'
    form = ArticleForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)