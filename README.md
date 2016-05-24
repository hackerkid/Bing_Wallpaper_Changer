##Bing Wallpaper Changer
This is a python script that changes the wallpaper of ubuntu desktop to the bing's photo of the day.
Tested successfully on ubuntu 14.04.

###Check for new Wallpaper every 30 Minutes

```
git clone https://github.com/praneelrathore/Bing_Wallpaper_Changer
cd Bing_Wallpaper_Changer
crontab -e
```

Now add this line to the file

```
24 */30 * * * * python Bing_Wallpaper_Changer/wallpaper.py
```

Save the crontab file and exit. Your script would now check for new wallpaper every 30 minutes and update. 


