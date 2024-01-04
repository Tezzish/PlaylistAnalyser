from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlaylistSerializer
from .playlist_handler import PlaylistHandler

# instantiates a playlist handler outside the functions
# so there is no need to create a new one every time
playlist_handler = PlaylistHandler()


class AnalysisView(APIView):
    def post(self, request):
        print(request.POST)
        playlist_link = request.POST.get('playlist_link')

        # if no link was provided, return an error
        if playlist_link is None:
            return Response(
                {'error': 'No playlist link provided'},
                status=status.HTTP_400_BAD_REQUEST
                )

        try:
            playlist = playlist_handler.get_playlist(playlist_link)

        except Exception as e:
            print(e)
            return Response(
                {'error': 'Failed to get playlist'},
                status=status.HTTP_400_BAD_REQUEST
                )

        # serialize the playlist object
        serializer = PlaylistSerializer(playlist)
        
        context = {
            'playlist': serializer.data,
            'avg_values': playlist.get_avg_attributes(),
            'max_values': playlist.get_max_attributes(),
        }

        return Response(context, status=status.HTTP_200_OK)
