import praw
import requests
import time as t
import glob, pprint, os

start_time = t.time()
r = glob.glob('*.jpg')
file_path = 'C:/Users/Public/Wallpapers'
image_list = []

reddit = praw.Reddit('wallpaper_bot')
reddit_data = reddit.subreddit("Wallpaper").hot(limit=256)


def image_download(image_url):
    img = requests.get(image_url)

    try:
        img.raise_for_status()
    except Exception as exc:
        print('There was a problem... ' + exc)

    file = open(str(t.time()) + '.jpg', 'xb') #the filename here is just the time at which it was downloaded
    for chunk in img.iter_content(10000):
        file.write(chunk)

for files in r:
    os.remove(files)

print('Files removed\n')

for image in reddit_data:
    if len(image_list) > 9:
        print('Found ten wallpapers! Starting download...\n')
        break
    elif ('1080' in image.title or '1440' in image.title or '2160' in image.title) and (image.over_18 == False):
        image_list.append(image.url)

for image in image_list:
    image_download(image)
    print('Image '+ str(int(image_list.index(image) + 1)) +' downloaded!\n')

print('Program finished without errors! Runtime:' + str(int(t.time()) - start_time) + ' seconds')