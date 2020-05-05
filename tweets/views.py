import random as r
from django.shortcuts import render
from django.http import Http404, JsonResponse

from .models import Tweet


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html')


def tweet_list_view(request,*args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or React/React Native/VueJS//IOS/Android
    return JSON data
    """
    # Query string
    qs = Tweet.objects.all()
    # List comprehension
    tweets_list = [{"id": obj.id, "content": obj.content, "likes": r.randint(0, 1000)} for obj in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or React/React Native/VueJS//IOS/Android
    return JSON data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404

    return JsonResponse(data, status=status)
