# Passel Public Version
This is the public version of the passel discord bot. You can use the provided code and instructions to run the bot by yourself and use in your own server.

## Why passel is being removed
First of all, thank you for using the passel bot. The bot has been active for over 2 years, and I greately apprecitate those who have added and used the bot in their servers. Due to Discord's changing rules, I will not be able to host the passel public bot anymore. 

You can still use the bot by hosting it on your own by following the steps below. If you have *any* questions, feel free to reach out to me via the [discord support server](https://discord.gg/wmSsKCX).
***

# About
Passel is a discord bot that manages the number of pins in a server. Discord has a pin limit of 50 pins per channel. However, with passel, that limit can be bypassed. The following readme will explain how the bot works and how to add and set up the bot in a server.

## How it works
The bot works by unpinning one message and sending it to a different channel during setup. There are 2 modes the bot can be set up in. 

**Mode 1:** In mode 1, the most recent pinned message gets sent to a pins archive channel of your choice. This means that the most recent pin wont be viewable in the pins tab, but will be visible in the pins archive channel that you chose during setup

**Mode 2:** In mode 2, the oldest pinned message gets sent to a pins archive channel of your choice. This means that the most recent pin will be viewable in the pins tab, and the oldest pin will be unpinned and put into the pins archive channel

**Also, any channel that has 50 pins should have one message unpinned, and then repin that 1 message after the bot is setup.**

***Please keep in mind that the bot only pins messages that REACH and EXCEED the limit of 50 pins per channel in discord.***

***If you want to pin ALL messages, use the sendall feature, follow instructions below to set up***

***
# Setup
**Note: There will be a setup video uploaded by August 1 2022 so that you can follow the video step by step as well as having the instructions below to follow.**

Set up consists of the 3 following sections. Please follow each section carefully, if you run into issues reach out via the  [discord support server](https://discord.gg/wmSsKCX). It would be easy to do this setup if you are the server owner or have administrator permissions. You MUST do the setup on a laptop.

## 1. Create a Discord bot in the developer portal
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

You are done with this part. Please move onto the next section below. 
***
## 2. Edit the main.py file
This section, you will be editing the python code to fit your server's needs.  
1. Click on [this link](https://github.com/stoir/passel_public).
2. Click on the green Code button, then click on Download ZIP
3. Unzip the file, and open the unzipped folder.
4. Open the main.py file. You might need to install an editor like text edit to open the file. 

### 2.a. Once you open the File there are 5 places you MUST edit, and one place you may optionally edit.
When you open the file, you will see the python code. This section may be a bit overwhelming for anyone experienceing code for the first time. Please follow the steps carefully so you can do this easily.

**MUST DO THIS BEFORE PROCEEDING**
1. on your discord account, go to settings
2. then, on the side bar click on advanced
3. check Developer mode so its green

***
If you observe the main.py file, you notice that there are lines that start with #. If you look closer there are lines that start with `# TODO`. There are a total of 6 `# TODO` statements. The first `# TODO` is optional, the remaining 5 are REQUIRED.

**2.a.i) optional edit**

 1. This is the first `# TODO` statement which says 
>  `# TODO change command here if you want to use another command, replace p. with anything you want inside the single ('') quotes`

If you want to change the bot command from p. (for example p.settings) to something else like =, replace the p. to = so the bot responds when you type =settings. 

The p. can be replaced with anything that is 1 character or multiple characters. Normally for discord bots, do not replace this with anything that is more than 2 characters.

**2.a.ii) MUST edit**
1. The second `# TODO` says

> `# TODO change mode to 1 or 2 here`

Change the mode of the bot herre, by replacing the 1 in `mode = 1` to the mode you want. If you want mode 1, you can leave this as is, if you want mode 2, change `mode = 1` to `mode = 2`

*Modes:*

Mode 1: In mode 1, the most recent pinned message gets sent to a pins archive channel of your choice. This means that the most recent pin wont be viewable in the pins tab, but will be visible in the pins archive channel that you chose during setup

Mode 2: In mode 2, the oldest pinned message gets sent to a pins archive channel of your choice. This means that the most recent pin will be viewable in the pins tab, and the oldest pin will be unpinned and put into the pins archive channel
***
2. The third `# TODO` statement says

> `# TODO`
> `sendall is set to 0 by default, change to 1 if you want`
>  `the bot to send all pinned messages to the pins channel`

The sendall feature means that every pinned message (instead of the 50th pinned message) is sent to the pins channel which you will set up in the next step. Change `sendall = 0` to `sendall = 1` if you want the bot to send all pins to the pins channel
***
3. The fourth `# TODO` statement says

> `# TODO`
> `# replace the 0 with the pins channel ID for your sever`

1. If you do not have a channel where you want to forward your pinned messages, create one. 
2. In the sidebar of your discord server where the channels are listed right click on the channel and click on `COPY ID`. 
3. replace the 0 in `pins_channel = 0` to the channel ID you copied. After copying it should look something like this `pins_channel = 947931203858726952` (obviously, the sequence of numbers for the pins channel in your server will be different from the example).
4. please try to not delete the channel in the future if you want the bot to work
***
4. The fifth `# TODO` statement says

> `# TODO`
> `# add any black listed channel IDs as a list separated by a comma (,)`
> `# a good idea is to add admin channels to this`

Blacklisting means that pinned messages in those channels will not be sent to the pins channel. For example, if you have a mod channel, #mod-general, and if you do not want extra pinned messages from that channel being sent to #pins, copy the #mod-general ID andd put it in the `[ ]`

If you want to add blacklisted channels, copy their IDs and put them inside the `[ ]` sepearated by commas `,`. 

Adding one channel should look like: `blacklisted_channels  = [926958717696634901]`

More than one channel should look like: `blacklisted_channels  = [926958717696634901, 972685609040748584, 840372439824334888]`

Obviously, the sequence of numbers for the channels in your server will be different from the examples.

***
5. For the sixth `# TODO` statement, scroll all the way to the bottom. It should say

>   `# TODO Replace TOKEN with the token from discord developer portal`

The Bot token you got from the first step and saved in a safe space should be used here. Copy the token and replace the words `TOKEN` with the token inside the quotes, **DO NOT DELETE THE QUOTES ON BOTH ENDS**.

It should look something like `client.run('MTAwMTg3MDk1OTUzNzU2NTc1Ng.GZ6ikH.C_NRQfjO2oB1otGsRJZz5cpTRhKrIZ6twRnI4M')` 

Obviously, your token will be different from the one in the example.

If the token is posted anywhere online, your server may be in danger, please reset the token in the bot and update in the file and follow the steps in "Changing settings in the future after hosting" to update the hosting agent described in the section below.

***
## 3. Host the bot on heroku for free

Hosting is typically expensive, there are multiple ways to host for free. You can either use the method I describe below or another one you find online. For this method you need a credit card, but you will not be charged anything, it is only used for verifying your heroku account. 

Using Heroku to host your bot is complicated. You will need to use the command line/terminal feature on your laptop to use this. If you need help reach out or allow an expereinced member of your team to do this.

### Hosting the bot

1. go to [https://id.heroku.com/login](https://id.heroku.com/login)
2. create a new account and sign up, for primary development language select python. 
3. Verify your email and set a password. Set a complicated password for safety and note the password in a safe area. 
4. Log in with your password and click accept
5. Click on create new app
6. add an app name, keep it simple
7. choose a region, US works well most of the time
8. Use the heroku CLI to deploy, the heroku page shows steps on how to use the heroku CLI. You will need to run the heroku CLI commands on your windows command line or your mac terminal depending on your operating system. 
9. go to the heroku portal and click on resources, then toggle the worker python main.py on. To do this, click on the edit button then toggle on and click confirm.
10. Once you delpy successfully, you should see the bot online in your discord server with a green active bubble on the bot's profile.
11. click on more in the top right of the heroku portal, then click on view logs, you should also see your bot deployed successfully here. 
12. After following the steps above, **please set up 2FA if you add a credit card to your account so your accound is extra protected** [Follow this link to set up 2FA.](https://devcenter.heroku.com/articles/multi-factor-authentication#enabling-mfa-and-registering-verification-methods)

### Verifying your heroku account
If you want your bot to be online all the time, YOU MUST verify your account by providing a credit card.

By default, heroku gives you 555 hours free per month. This means that if want your bot to run 24x7 you will be able to host the bot for about 23 days per month before you run out of the 555 hours. 

**To get 450 more hours for free without any additional charge, you have to add a credit card to your account. To date, you will not be charged by heroku. *To avoid getting charged do not create any more heroku apps per account other than the discord bot.***

**Also enable 2FA, in case of a data leak, your account, password, and credit card details will be protected with 2FA**

Follow these steps to verify your account and get 450 hours free of charge. 
1. click on the user icon in the top corner, then click on Account Settings
2. click on billing
3. click add credit card
4. you should be all set!

**If you can use the bot now, you have successfully set up the bot and heroku account (with 2FA hopefully)! If you have any issues reach out in the support server or watch the setup video.**

***
## 4. Changing settings in the future after hosting

***
> # Thank you for using the code, if you need any help at all please reach out on the support server.
> ## I hope that the tutorial was informative and easy to follow.
> hyppytyynytyydytys#1010
