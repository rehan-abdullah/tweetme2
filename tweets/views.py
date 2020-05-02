from django.shortcuts import render
from django.http import Http404, JsonResponse

from .models import Tweet


def home_view(request, *args, **kwargs):
    context = {
        'content': 'Hello World!',
    }
    return render(request, 'tweets/home.html', context)


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
