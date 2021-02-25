# Web-Scrapping 
# Download Youtube entire playlist video files or single video files
# Getting Started
These instructions will get idea of the project up and running on your local machine for development and Execution purposes. See deployment for notes on how to deploy the project on a live system.

# How it works

This script to download youtube videos with high definaton and high speed x50times accuracy.  
Download files in same folder where you run script.  
If youtube url link has 'watch' - word it means single file like:https://www.youtube.com/watch?v=d07SayjuLJk   
        or  
If youtube url link has 'Playlist' - word it means multiple file in that playlist like : https://www.youtube.com/playlist?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG  
all files Download in same folder  

# Prerequisites

What things you need to install the software and how to install them  

1. Python2/Python3  
2. Pytube - The Web site pytube 8.0.2  
3. Urllib - The Web site urllib  
4. bs4 - The Web site beautifulsoup4 4.6.0  

# Installing

A step by step have to get a development env running  

step 1.  python2 or python3  
step 2.  pip install pytube  
step 3.  pip install urllib  
step 4.  pip install bs4  

# Running the Script

Enter terminal or console windows/Linux/mac.  

Like : python filename youtube-urlpath  

Example 1 Single video : python youtubeDownloader.py https://www.youtube.com/watch?v=d07SayjuLJk   

Example 2 Playlist : python youtubeDownloader.py https://www.youtube.com/playlist?list=PLx0sYbCqOb8TBPRdmBHs5Iftvv9TPboYG  
