# boboselenium

Modules:

I'd recommend using a virtual environment so your modules don't get messy.
To create a virtual environment in vscode: 
Run python -m venv venv in the terminal
Then press 'CTRL+SHIFT+P' then go to Python select interepter and select the venv.
This means any modules installed stay in this project and you won't get clashing ones with other projects.

pip installs:
pip install selenium
pip install os-sys
pip install python-time



First things first you've got to install a chromedriver to access the website:

Head to https://chromedriver.chromium.org/downloads and download the driver for your chrome version.

If you're curious about what chrome you have: click the three dots in the top right of chrome, go to the help
tab at the bottom and then click 'About Google Chrome'.

After downloading the chromedriver (don't worry if you're on win64, win32 is the only one available 
but it works fine) put it into the directory of your project.


The script itself has very heavy commenting to walk you through it hopefully clearly, mind the tame swearing.

You'll see me call to a config file a lot - so I've included an example of what it looks like so you can do 
it yourself. I've written it into the gitignore file so you can't see my private information, I'd reccomend you 
do the same if you ever make a repo of a similiar project