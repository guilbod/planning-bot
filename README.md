# planning-bot

A python bot to notify about a planning change.


Principle :
- the bot connects to planning website and takes a screenshot of the planning
- if 2 screenshots in /images/ directory
	- compare pixels between the older screen and the newer
	- notify about an added, removed or substituted lecture
		- note : each lecture has a specific color, an empty slot is grey
- else
	- launch manually the bot to have 2 screenshots


Usage :
- if you already have 2 screenshots (stored in ./images/), launch image.py
- otherwise, launch the bot twice to have 2 screenshots, then, launch image.py


Directory :
- images/ : it contains planning screenshots


Files :
- requirements.txt : all the modules needed
- credentials.py : where you store your username and password
- image.py : used to deal with screenshots
- hyperplanning_bot.py : the bot itself
- planning.py : it contains all pixel positions of planning days and hours


History : 
- version 1 : connect to the planning website and take a screenshot
- version 2 (now) : pixel comparison for notifying


Upgrades :
- image.py and bot.py need to be launched manually. These 2 files are not linked for now
- make a cron to automatically run the program
