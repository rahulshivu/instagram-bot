from __future__ import print_function
from self_info import self_info
from get_user_info import get_user_info
from like_a_post import like_a_post
from get_user_post import get_user_post
from post_comment import post_comment
from get_own_post import get_own_post
from new_obj import *

# from objective import get_hash_tag
import time
# def fuction for start instabot


def init_bot():
    # this list cotain users options
    option_list = ['\t\t\t\t*************************Welcome to instabot*****************************',
                   'A.Get your own details', 'B..Get details of user by username', 'C..get your own recent post',
                   'D..get recent post of user by username ', 'E..Like most recent user post',
                   'F..make comment on user recent post ','G..YOUR FRIND ANANLYSIS BASIC BY Hasttag','...write exit to leave instabot']

    instabot = True

    while instabot:
        # loop for print the option and time delay for each option is .200 microsecond
        for x in range(0,len(option_list)):
            print(option_list[x],end='\n\n')
            time.sleep(.100)

        select_option = raw_input("Enter your choice::")
        try:
            # enter the choice

            select_option=select_option.upper()
            if select_option == 'A':
                self_info()

            elif select_option == 'B':
                insta_username = raw_input("Enter username: ")
                get_user_info(insta_username)

            elif select_option == 'C':
                get_own_post()

            elif select_option == 'D':
                insta_username = raw_input("Enter username::")
                get_user_post(insta_username)

            elif select_option == 'E':
                insta_username = raw_input("Enter username::")
                like_a_post(insta_username)

            elif select_option == 'F':
                insta_username = raw_input("Enter username::")
                post_comment(insta_username)

            elif select_option == 'G':
                objective()


            elif select_option =='EXIT':
                 instabot=False

        except:
            print ("This is not valid option")
        raw_input("Press enter to continue:\n\n\n ")

# calling insta bot function
init_bot()


