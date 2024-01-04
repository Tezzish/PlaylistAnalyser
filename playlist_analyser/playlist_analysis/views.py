from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .playlist_handler import PlaylistHandler


# instantiates a playlist handler outside the functions
# so there is no need to create a new one every time
playlist_handler = PlaylistHandler()


# Create your views here.
def index(request):
    return render(request, 'index.html')


def analysis(request):
    playlist_link = request.POST.get('playlist_link')

    try:
        playlist = playlist_handler.get_playlist(playlist_link)
    except Exception as e:
        print(e)
        return render(request, 'error.html')

    context = {
        'playlist': playlist,
        'avg_values': playlist.get_avg_attributes(),
        'max_values': playlist.get_max_attributes(),
    }

    template = loader.get_template('analysis.html')
    return HttpResponse(template.render(context, request))
