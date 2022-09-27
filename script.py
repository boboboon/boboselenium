from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC

import config

import os

import time

# This just grabs what directory you're in automatically which I like
directory= os. getcwd()


# And this tells us where our chromedriver is
DRIVER_PATH = directory + '\\chromedriver.exe'

# This is whatever directory we're interested in, we'll use Reddit as an example
url=r'https://www.reddit.com/login/'

# These allow some options for our chrome driver.
chrome_options = Options()

# You can include these arguments so you don't actually see the chromedriver window however
# I'd recommend only doing this after getting everything set up and it's all nicely automated.
# (It's hard to see what you're doing if there's nothing to see right?)

#chrome_options.add_argument("--headless")
#chrome_options.add_argument('--disable-gpu') 

# This chooses the level of messages that will get output to the terminal, with 'log-level=3' being the 
# the smallest amount. I like living in ignorance of errors so I like to keep this on.
chrome_options.add_argument('log-level=3')

# Chrome will also be annoying and ask to show notifications and stuff so just disable these

chrome_options.add_argument("--disable-notifications")

# This starts our driver
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=DRIVER_PATH)

# This gets our driver to go to our requested URL
driver.get(url)

# Now you can access some websites like Reddit directly without an account but we'll take a look
# at how to handle logins as this is pretty common.

# Once you're on the login page, we want to type into the boxes our login information.
# To do this, we gotta find where we're typing so on the chromedriver page that's opened up
# right click the screen, go to inspect and you'll get the dev console. Now click the top left in the console
# which is a tool that allows you to hover over elements on the page and find them in the HTML directly.

# A lot of this process is opening the driver, finding elements you're interested in and then interacting with
# them and then rinse and repeat.

# There's different ways to find elements, for most logins they'll have an ID such as 'loginUsername' which
# will show up in the developer console when you click the top left search tool and then the login box.
# The IDs will be different for pages so you gotta check this yourself again with the search tool.

# To 'type' in this box we'll use our driver to send keys there as seen below:

#Login:
username = driver.find_element('id', 'loginUsername').send_keys(config.username)
password= driver.find_element('id', 'loginPassword').send_keys(config.password)




# Great! Now you should see your details in the appropiate boxes, now you need to submit them either
# by clicking submit or hitting enter. We'll just hit enter to save us some time.

enter= driver.find_element('id', 'loginPassword').send_keys(Keys.RETURN)

# If you are returning an error that these IDs or classes (if that's how you're searching for something) then
# it'll likely be an iframe issue that we'll look into in a bit.


#


# I often personally like refreshing a page as soon as I log onto it as this can get rid of issues like
# chrome asking you to change some options + some websites occasionally get stuck and refreshing before
# interacting with them can sometimes fix this. You want to make sure this doesn't happen before you've
# logged in though or else you'll be stuck at the login page. But you can wait until an element shows
# up on the main Reddit page, and refresh when we find it just to get a nice clean page. Waiting is pretty
# important or you'll often do an incomplete and inconsistent search

# Refreshing can be done with the below code.

#driver.refresh()

# We are going to wait 15 seconds for anything to load in
wait= WebDriverWait(driver, 15)


# The main content of the page is held by this ID so we wait till this loads in
wait.until(EC.presence_of_element_located((By.ID, 'AppRouter-main-content')))


# Let's say we want to create a post. First we click the area that says create a post after waiting for it
# to load in. To find the class name you can just hover over it.

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'zgT5MfUrDMC54cpiCpZFu')))


# Now notice that we are finding multiple elements and I've chosen the first one. This is because this stuff
# can be a bit finnicky so it turns out there's multiple classes with this class_name. Largely so the HTML
# can update how it looks on the website. However we're just going to choose the first one as that happens
# to be the correct one, find_elements will return a list of them!
create= driver.find_elements(By.CLASS_NAME, 'zgT5MfUrDMC54cpiCpZFu')[0].click()



# Now we're on the create page so we wait again for it to load in, it happens to have the same ID as before.



wait.until(EC.presence_of_element_located((By.ID, 'AppRouter-main-content')))



# Anyway! We're going to wait until this iframe loads in and then switch to it. If your search for something
# is returning 0, 'CTRL+F' in the dev console and look for where the iframes are, there's most likely one above
# the element you're looking for hiding it away from you like some cruel monster.

# Now our code couldn't find the below class on the website: class="notranslate public-DraftEditor-content"
# I thought we needed to switch into the iframe that has these buttons, because otherwise our code won't find it.
# If I'm being perfectly honest, I was here for 20 minutes wondering why I couldn't find the cookies buttons
# anywhere but hey here we are. Think of iframes as different templates of a drawing that all layer together
# to make a final image. I should also mention I know nothing about them so that might be a terrible analogy.
# Turns out I was wrong! The class name is not notranslate public-DraftEditor-content but rather two classes
# notranslate and public-DraftEditor-content. The latter there is only one of so it's a good way to choose
# this textbox. There's lots of classes that the textbox is contained in (classes that contain other classes)
# but the role tells us this is the textbox, you can see if you hover over:
                                                                            
# <div class="notranslate public-DraftEditor-content" contenteditable="true" role="textbox" spellcheck="true" 
# style="outline: none; user-select: text; white-space: pre-wrap; overflow-wrap: break-word;"><div 
# data-contents="true"><div data-offset-key="6285d6_initial-0-0" class="_3LuG0YVLLHE2azRNVaKz7O">
# <div class="" data-block="true" data-editor="6285d6" data-offset-key="6285d6_initial-0-0">
# <div data-offset-key="6285d6_initial-0-0" class="public-DraftStyleDefault-block 
# public-DraftStyleDefault-ltr"><span data-offset-key="6285d6_initial-0-0"><br 
# data-text="true"></span></div></div></div></div></div>

# The role let me know this is where we're going to put out text.



# Make sure our textbox loads in

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'public-DraftEditor-content')))


# Let our driver find it
type = driver.find_element(By.CLASS_NAME, 'public-DraftEditor-content')


# Then let our driver click it and type something in. I've chosen the opening lines to the novel
# 'Do Androids Dream of Electric Sheep?' more commonly known for the film blade runner. 
type.click()

type.send_keys('“A merry little surge of electricity piped by automatic alarm from the mood organ beside his bed awakened Rick Deckard.”')

# We can do the same to choose which community we want to post to and the title of the post.

community= driver.find_element(By.CLASS_NAME, '_1MHSX9NVr4C2QxH2dMcg4M')

# We can post to our own reddit by using our username.

self_post='u/'+config.username

community.click()

community.send_keys(self_post)

# And again for the title



title= driver.find_element(By.CLASS_NAME,'PqYQ3WC15KaceZuKcFI02')

title.click()

title.send_keys('Humble Beginnings')


# We've now got an issue. The 'do you want to accept cookies tab' is messing us up
# as it is covering our post button. We can either scroll down to get past it but I think it's best to just
# click on accept cookies and move on to the post button. Only annoying thing is the button for post and 
# the button for accept cookies have the same classes. Thankfully all but one.

cookies=   driver.find_element(By.CLASS_NAME,'_1tI68pPnLBjR1iHcL7vsee')

cookies.click()

# Just making sure we have enough time for our accept cookies part to bugger off
time.sleep(1.5)

post = driver.find_element(By.CLASS_NAME,'_18Bo5Wuo3tMV-RDB8-kh8Z ')

post.click()

# And we have officially just done our first post to Reddit!




