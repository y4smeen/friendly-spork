#
# import spotipy
#
#
# lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'
#
# spotify = spotipy.Spotify()
#
# # results = spotify.artist_top_tracks(lz_uri)
# def getPlaylist(mood):
#     results = spotify.search(mood, limit=10, offset=0, type='track')
#     for track in results['tracks'][:10]:
#         print('track    : ' + playlist['name'])
#         # print('audio    : ' + track['preview_url'])
#         # print('cover art: ' + track['album']['images'][0]['url'])
#         print()
#
# getPlaylist("happy")

#
#
# import spotipy
#



# spotify = spotipy.Spotify()
#
# # results = sp.search(q='happy', limit=20, category='moods')
# # for i, t in enumerate(results['tracks']['items']):
# #     print(' ', i, t['name'])
#
# def getPlaylists(category):
#     results = spotify.category_playlists(category_id=category, country=None, limit=5, offset=0)
#     print results
#
# getPlaylists("moods")




# shows a user's playlists (need to be authenticated via oauth)

# import sys
# import spotipy
# import spotipy.util as util

# export SPOTIPY_CLIENT_ID='c51ddb3a55044e5086181d9222239ae8'
# export SPOTIPY_CLIENT_SECRET='127a3b3aa6e146ff9aab53ae4ef6cbb1'
# export SPOTIPY_REDIRECT_URI='http://google.com'
#
# def show_tracks(tracks):
#     for i, item in enumerate(tracks['items']):
#         track = item['track']
#         print "   %d %32.32s %s" % (i, track['artists'][0]['name'],
#             track['name'])
#
#
# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         username = sys.argv[1]
#     else:
#         print "Whoops, need your username!"
#         print "usage: python user_playlists.py [username]"
#         sys.exit()
#
#     token = util.prompt_for_user_token(username)
#
#     if token:
#         sp = spotipy.Spotify(auth=token)
#         playlists = sp.user_playlists(username)
#         for playlist in playlists['items']:
#             if playlist['owner']['id'] == username:
#                 print
#                 print playlist['name']
#                 print '  total tracks', playlist['tracks']['total']
#                 results = sp.user_playlist(username, playlist['id'],
#                     fields="tracks,next")
#                 tracks = results['tracks']
#                 show_tracks(tracks)
#                 while tracks['next']:
#                     tracks = sp.next(tracks)
#                     show_tracks(tracks)
#     else:
#         print "Can't get token for", username

import sys
import spotipy
import spotipy.util as util

def userauth():
	scope = 'user-library-read'
	SPOTIPY_CLIENT_ID='c51ddb3a55044e5086181d9222239ae8'
	SPOTIPY_CLIENT_SECRET='127a3b3aa6e146ff9aab53ae4ef6cbb1'
	SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'
	username = 'swappro'
	token = util.prompt_for_user_token(username, scope,SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
	if token:
		sp = spotipy.Spotify(auth=token)
		results = sp.current_user_saved_tracks()
		for item in results['items']:
			track = item['track']
			print track['name'] + ' - ' + track['artists'][0]['name']
		else:
			print "Can't get token for", username

userauth()
