#import all need labraries and functions from files
from obj import *
from get_id import *

#  function which fetch the hash tag comment from users post


def get_hash_tag(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print "user not exist"
        exit()
    url=BASE_URL+'users/%s/media/recent/?access_token=%s' %(user_id,APP_ACCESS_TOKEN)
    print "GET requested url :%s" %url
    req_media=requests.get(url).json()

    # open a text file
    file = open("name.txt",'w')
    for posts in req_media['data']:

    # write the caption text or hashtag coments in text file in utf-8 encoding
        file.write(posts['caption']['text'].encode('utf-8'))
    # close the file
    file.close()


    # call wordcloud  function for making word cloud of hash tag comment in a activity


    #call the fuction
