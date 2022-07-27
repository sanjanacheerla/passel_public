# Passel Public Version
This is the public version of the passel discord bot. You can use the provided code and instructions to run the bot by yourself and use in your own server.

## Why passel is being removed
First of all, thank you for using the passel bot. The bot has been active for over 2 years, and I greately apprecitate those who have added and used the bot in their servers. Due to Discord's changing rules, I will not be able to host the passel public bot anymore. 

You can still use the bot by hosting it on your own by following the steps below. If you have *any* questions, feel free to reach out to me via the [discord support server](https://discord.gg/wmSsKCX).
***

# Setup
Set up consists of the 3 following sections. Please follow each section carefully, if you run into issues reach out via the  [discord support server](https://discord.gg/wmSsKCX). It would be easy to do this setup if you are the server owner or have administrator permissions.

## Create a Discord bot in the developer portal
You must first create a discord bot account in the [discord developer portal](https://discord.com/developers/applications). 

 1. log in to the portal using your discord account
 2. click on new application
 3. give the bot a name, you can name it anything you want, does not have to be passel
 4. optional: under settings > general information, add a profile photo for the bot
 5. optional: under settings > general information, add a description for the bot
 6. under settings > bot, click on add bot, click on "yes, do it!" 
 7. click on reset token, **when you see the token copy it and store in a safe place.** DO NOT EVER post this token anywhere. If you do go back to the portal and reset the token and update it the main.py file in the section below. The token should look something like this `MTAwMTg3MDk1OTUzNzU2NTc1Ng.GZ6ikH.C_NRQfjO2oB1otGsRJZz5cpTRhKrIZ6twRnI4M`, a random generation of characters.
 8. uncheck PUBLIC BOT and REQUIRES OAUTH2 CODE GRANT
 9. under Privileged Gateway Intents, check PRESENCE INTENT, SERVER MEMBERS INTENT, and MESSAGE CONTENT INTENT
 10. save your changes
 11. under BOT PERMISSIONS, check Administrator, the first one. 

The page should look like this: 
![enter image description here](https://github.com/stoir/passel_public/blob/main/Images/intents.png)
![enter image description here](https://github.com/stoir/passel_public/blob/main/Images/bot_perms.png)


## Edit the main.py file

## Host the bot on heroku for free
