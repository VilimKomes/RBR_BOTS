# RBR_BOTS
RBR discord bots

Hardware needed raspberry pi with wifi connection

Discord
https://discord.com/developers/

- Make a new application
- Name the bot
- Go to: BOT - give whatever permissions you need -> SAVE
- Go to: OAuth2-URL Generator - tick the bot box - then tick whatever permissions your bot is going to need - COPY THE LINK in GENERATED URL
- Go to the generated link and if you are admin of discord server invite the bot
- Go to BOT and RESET TOKEN - Copy that token that's  "Password"  for the program

NUMBER BOT
- NumberBot.py
- DownloadDrivers.py

- Register.csv
- Drivers.csv

Register has all the numbers that people have chosen to be their own
Drivers saves all registered drivers for GARC

setup DownloadDrivers with crontab to download it whenever you want (example is every 6 hours)
0 */6 * * * /usr/bin/python3 /home/pi/GARC/DownloadDrivers.py >> DOWNLOAD_DRIVERS_OUTPUT.txt 2>&1

DownloadDrivers link is rally championship entry list page
Example https://www.rallysimfans.hu/rbr/bajnoksag2.php?b=reszletek&bajnoksag_id=251&nevezes_list
