#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:04:46 2018

@author: chrisbuetti
"""


import requests, json
from bs4 import BeautifulSoup


class igFollowerCount():
    
    
    def __init__(self, username):
        self.username = username
        url_user = 'https://www.instagram.com/{}'.format(self.username)

        s = requests.Session()
        r = s.get(url_user)
        text = r.text
    
        finder_text_start = ('<script type="text/javascript">'
                             'window._sharedData = ')
        finder_text_start_len = len(finder_text_start)-1
        finder_text_end = ';</script>'
    
        all_data_start = text.find(finder_text_start)
        all_data_end = text.find(finder_text_end, all_data_start + 1)
        json_str = text[(all_data_start + finder_text_start_len + 1) \
                       : all_data_end]
        user_info = json.loads(json_str)
    
        self.followers = user_info['entry_data']['ProfilePage'][0]['graphql']['user']['edge_followed_by']['count']
        self.following = user_info['entry_data']['ProfilePage'][0]['graphql']['user']['edge_follow']['count']


                
   
    def __str__(self):
        return "Platform: Instagram, Account: {}, Followers: {}, Following: {}".format(self.username, self.followers, self.following)
        
 

class twitFollowerCount():
    
    platform = "twitter"
    
    def __init__(self, username):
        self.username = username
        url = "https://www.twitter.com/{}".format(username)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'lxml')

        x = soup.find('li', class_="ProfileNav-item--followers")
        followers = x.find('a')['title']
        self.followers = int(followers.split(' ')[0].replace(',',''))


        y = soup.find('li', class_="ProfileNav-item--following")
        following = y.find('a')['title']
        self.following = int(following.split(' ')[0].replace(',',''))


    def __str__(self):
        return "Platform: Twitter, Account: {}, Followers: {}, Following: {}".format(self.username, self.followers, self.following)
        

 
    
#### Example
def main():
    print('Instagram Example: ')
    print("Using Bruno Mars for example, @BrunoMars")
    BrunoMarsInsta = igFollowerCount('brunomars')
    followers = BrunoMarsInsta.followers
    print("Bruno Mars Followers: " + str(followers))
    following = BrunoMarsInsta.following
    print("Bruno Mars Following: " + str(following))
    print(BrunoMarsInsta)
    
    print('\n')
    
    print('Twitter Example: ')
    print('Using Kanye West for example, @KanyeWest')
    KanyeTwitter = twitFollowerCount('kanyewest')
    followers = KanyeTwitter.followers
    print("Kanye West Followers: " + str(followers))
    following = KanyeTwitter.following
    print("Kanye Following: " + str(following))
    print(KanyeTwitter)
    
    
if __name__ == '__main__':    
    main()   
    
