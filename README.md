# swgoh-salvage-tracker
## What is the Salvage Tracker?
Salvage Tracker is a spreadsheet developed to help players of SWGOH to determine how much "extra" gear is available for relic scrapping.
## How does it work?
In short terms, the user fills out the "Gear Need Scrape" sheet with the gear needed for characters not yet fully geared, and the user fills out the "Gear Have Scrape" sheet with all the gear they currently have in their inventory. Once all the data is entered, then the Gear Main applies a top down recipe filter to determine how much lower gear is needed to fulfill any higher order recipes. The end result is then pushed to the Gear Salvage sheet. The Gear Salvage sheet has a column named "Have" which is the total number of pieces of that particular gear you have in inventory. The Gear Salvage sheet has a column named "Salvage" which is the amount of gear you have in inventory above needed. According to the gear you inputed on the Gear Need sheet and the Gear Have sheet, the "Salvage" column is the amount of that particular gear that is completely safe for scrapping.
## What is the script for?
The gearScrape.py script scrapes data from swgoh.gg Gear Needed page for Gear Need and hotutils.com (Player -> Salvage) page for Gear Have. The script takes the data from those 2 pages and creates GearNeed.csv and GearHave.csv. These can then be imported into the "Gear Need Scrape" and "Gear Have Scrape" sheets respectively. This drastically reduces the time needed to fill out the 2 sheets and gets you to scrapping faster.
## If I have HotUtils already and they have a Salvage tool, why use this?
In the past (not sure if they fixed it) their need algorithm seems to doesn't take fully crafted pieces in to account when determining lower tier gear pieces. Take the follwing recipe for example:
Mk 2 Merr-Sonn Thermal Detonator
-- 1 Mk 3 BioTech Implant
-- 1 Mk 3 BlasTech Weapon Mod 
Now if the need was 30 Mk 2 Merr-Sonn Thermal Detonator and there were currently 5 in inventory. Their algorithm would determine the need at:  
-- 25 Mk 2 Merr-Sonn Thermal Detonator  
-- 30 Mk 3 BioTech Implant  
-- 30 Mk 3 BlasTech Weapon Mod  
So the need value would be 5 over for BioTech and BlasTech pieces, and this is compounded for any other recipes that require those same pieces.
## How to use the script?
This script was written in python using the Selenium Webdriver for Google Chrome. It requires having both Google Chrome and the Selenium Webdriver that matches the Google Chrome version. https://www.selenium.dev/documentation/webdriver/  
If a different browser or scraper is desired, feel free to change or use whatever pieces of the script as needed.  
Once Selenium is set up, the script must be editted by putting your ally code in wherever the <allycode> appears in the script.  
 Second, you must get a session key from HotUtils and put the session key in the wherever the <sessionkey> appears in the script.  
 To get the session key, log in to HotUtils, and in Chrome press Ctrl-Shift-j to bring up the Developer Tools.![DevToolsNetwork](https://user-images.githubusercontent.com/5667248/203377530-4e148b75-e0e8-4a4b-995f-602ae72e6397.png)
Select the Network tab, and hit Ctrl-r to reload the page.Select the "hotutils" on the left, and select the "Headers" tab on the right. In the "Requests Headers", scroll down to the cookie. It should look like this "cookie: hotUtilsSession=<sessionkey>; hotUtilsAllyCode=<allycode>". Everything between the = and the ; is the session key.![RequestHeaders](https://user-images.githubusercontent.com/5667248/203379503-6e3882dc-4c46-4555-9dee-f1372f240ed6.png)

 Running the script (python gearScrape.ph) will create the 2 csv files which need to be imported into the spreadsheet.  
 On the "Gear Need Scrape", I suggest deleting all the information on the sheet before importing the new data to make sure there is only the current information in the sheet.
 On the "Gear Have Scrape", I suggest deleting all the information above the red:"Gear below has to be manually entered" for the same reason. Everything below has to be entered manually so just adjust the values as needed for those.
