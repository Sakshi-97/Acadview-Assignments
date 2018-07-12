# Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
#The access token is a authority that can be used by an application to acess an API.
#its purose is to inform the API that the bearer o this token has ben authorised and can perform specific actions.

#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
# Google:- 172.217.9.164
#Facebook:- 157.240.18.35

#Q.3- Using Tweepy library try to extract tweets from Twitter.

#Q.4- What is a difference between library and API . Figure it out with examples.
An architect (read application developer) wanted to build a house(read application), so he prepared for all its
aspects including structure, plumbing, wiring, decors etc(read different libraries). He cant do all of the stuff
himself so he took help from various experts in those fields, who are really good at doing what they do. But he needed
communicate his needs and requirements face to face or via mail (read invoking API )so that they can cater to his need
and provide the asked service.  After some time a fellow Architect came and wanted to accomplish a similar task but with
a few add on features like swimming pool (a new library). He can conveniently use the framework provided by our
architect and add new features invoking any new service.

Carefully lets review-

A library is a collection of functions / objects that serves one particular purpose. you could use a library in a
variety of projects. (Various specialized services in our case)

An API is an interface for other programs to interact with your program or library  without having direct access.
( giving specifications for our need to various vendors in our case)

eg- Angular js- a JS framework may use many libraries like iniline editing of text using an exposed API of that library

#Q.5- Try to access Spotify API . Find out some library for it and play some music.
import sys
import os
import spotify
import spotify.util as util
if len(sys.argv)>2:
    user = sys.argv[1]
    playlist = sys.argv[2]
else:
    sys.exit()
token = util.prompt_for_user(user)
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlists = sp.user_playlist_create(user,playlist)
else:
    print("cannot get token.")

