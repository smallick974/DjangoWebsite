from .models import Album, Songs
from django.shortcuts import render,get_object_or_404

def index(request):
    all_albums = Album.objects.all()
    return render(request,'music/index.html',{'all_albums' : all_albums})

def detail(request,album_id):
    '''try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album Does Not Exist")'''

    #instead of above code this can be used
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    try:
        selected_song = album.songs_set.get(pk = request.POST['song'])
    except (KeyError, Songs.DoesNotExist):
        return render(request, 'music/detail.html',{
            'album' : album,
            'error_message' : "You did not select a valid song",
        })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
