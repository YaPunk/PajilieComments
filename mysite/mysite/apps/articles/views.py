from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse

from .models import Article, Comment

def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')
	return render(request, 'articles/list.html', {'latest_articles_list':latest_articles_list})


def detail(request, article_id):
	try: 
		a = Article.objects.get( id = article_id)
	except: 
		raise Http404('Статьи нет, но вы держитес')

	latest_comments_list=a.comment_set.order_by('-id')

	return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list' : latest_comments_list})	

def lc(request, article_id):
	try: 
		a = Article.objects.get( id = article_id)
	except: 
		raise Http404('Статьи нет, но вы держитес')

	a.comment_set.create(author_name = request.POST['name'], text = request.POST['text'], pub_date=timezone.now())

	return HttpResponseRedirect( reverse('articles:detail', args=(a.id,)) )