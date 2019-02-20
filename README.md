# python_wallpaper_bot
Fetches ten hot wallpapers from www.reddit.com/r/wallpaper and downloads them to a folder

# Walkthrough/Explanation
This code *specifically*, but simplly, does as follows in this order:
1. Logs into reddit and fetches the first 256 'hot' posts from /r/wallpapers
2. Deletes ALL .jpg files in folder it is placed in (Would reccomend making a separate folder for this script)
3. Checks that the posted pictures are at least 1080p and then puts their URLs in a list
4. Downloads all pictures from their URLs in the list

# How to Use:
-Download this file and put it in a NEW directory that you want to put 10 wallpapers into

-Create a praw.ini file with your reddit developer crudentials (Visit https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#praw-ini 
for more information)

-Set your wallpaper to be a slideshow of pictures from your directory and run the script!
