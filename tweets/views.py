from django.shortcuts import render
from django.http import Http404

from .models import Tweet


def home_view(request, *args, **kwargs):
    context = {
        'content': 'Hello World!',
    }
    return render(request, 'tweets/home.html', context)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        #raise Http404
        return render(request, 'tweets/home.html', context={'content': '404 Error'})

    context = {
        'content': obj.content,
    }
    return render(request, 'tweets/home.html', context)
