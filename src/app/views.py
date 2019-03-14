from django.shortcuts import render, get_object_or_404, redirect
from .models import Source, ShortenerUrl
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return redirect("http://tiagoaguiar.co")


def redirection(request, slug):
    object = get_object_or_404(ShortenerUrl, shortcut=slug)
    object.count += 1
    object.save()

    refer = request.META.get('HTTP_USER_AGENT')
    context = { "obj": object, "refer": refer }
    return render(request, "index.html", context)


def gateway(request, slug):
    object = get_object_or_404(ShortenerUrl, shortcut=slug)
    max_page = 1
    host = object.link.split("?")
    rd_number = (settings.PAGE_INDEX % max_page)
    path = "{0}-{1}".format(host[0], rd_number)
    settings.PAGE_INDEX = settings.PAGE_INDEX + 1
    if (settings.PAGE_INDEX > 100):
        settings.PAGE_INDEX = 0

    total_path = len(host[0].split("/"))
    last_path = "{0}-{1}".format(host[0].split("/")[total_path - 1], rd_number)

    try:
        return redirect("{0}?utm_campaign=funnel-{1}&{2}".format(path, last_path, host[1]))
    except Exception:
            return redirect("/")
    return response
