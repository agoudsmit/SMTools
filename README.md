# SMTools
This repository will include a number of Twitter and Instagram tools for automation/analytics in Python that I will be updating and adding to frequently. For any questions or suggestions, email crb4595@gmail.com

## FollowerCount

Simple scraper to easily get a follower or following count for any twitter/instagram account - public or private. The scraper does not require authentication/API connection. 
Suggested Use: The scraper can be used to automate the tracking of follower growth daily, monthly, yearly, etc.

It is very simple to use:

#### For Instagram:

```python
BrunoMarsInsta = igFollowerCount('brunomars')
followers = BrunoMarsInsta.followers; print(followers)
following = BrunoMarsInsta.following; print(following)
print(BrunoMarsInsta)
```

will return:

```python
19487405
37
Platform: Instagram, Account: brunomars, Followers: 19487405, Following: 37
```

#### For Twitter:

```python
KanyeTwitter = twitFollowerCount('kanyewest')
followers = KanyeTwitter.followers; print(followers)
following = KanyeTwitter.following; print(following)
print(KanyeTwitter)
```

will return:

```python
28158642
3
Platform: Twitter, Account: kanyewest, Followers: 28158642, Following: 3
```

###### Dependencies:
* requests
* json
* bs4 
