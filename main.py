
'''
Discord Invite Auto Joiner - Self Bot!
RKuangDev
'''

import discord
import datetime
import requests

token = "Token" #Replace with discord token
client = discord.Client()

print('''
==================================================================================================
______ _                       _   _____           _ _           ___       _                 
|  _  (_)                     | | |_   _|         (_) |         |_  |     (_)                
| | | |_ ___  ___ ___  _ __ __| |   | | _ ____   ___| |_ ___      | | ___  _ _ __   ___ _ __ 
| | | | / __|/ __/ _ \| '__/ _` |   | || '_ \ \ / / | __/ _ \     | |/ _ \| | '_ \ / _ \ '__|
| |/ /| \__ \ (_| (_) | | | (_| |  _| || | | \ V /| | ||  __/ /\__/ / (_) | | | | |  __/ |   
|___/ |_|___/\___\___/|_|  \__,_|  \___/_| |_|\_/ |_|\__\___| \____/ \___/|_|_| |_|\___|_|   

By: RockyLogic
==================================================================================================
''')


input("""
I've Read The ReadMe File, And I Choose to Continue:
Press Any 'Enter' To Continue: """)

print ("\nMonitoring... \n")

@client.event
async def on_message(message):
    if "discord.gg/" in message.content:
        print("[{}]".format(datetime.datetime.now()),"[Server: {0.guild.name}][{0.channel}][{0.author}]:'{0.content}'".format(message))
        print("[{}] Found Invite".format(datetime.datetime.now()))
        indexNum = message.content.find("discord.gg/")
        indexNum += 11
        # Valid for standard 6 character invite codes
        inviteCode = message.content[indexNum:indexNum+6]
        print("[{}] Invite Code: ".format(datetime.datetime.now()), inviteCode)

        URL = "https://discordapp.com/api/v6/invites/" + inviteCode
        headers = {
            "authorization": "{}".format(token),
        }
        print(f"[{datetime.datetime.now()}] Attempting to Join Discord")
        requestResponse = requests.post(url=URL, data="", headers=headers)

        if requestResponse.status_code == 200:
            print(f"[{datetime.datetime.now()}] Successfully Attempted To Join Discord Invite")
        else:
            print(f"[{datetime.datetime.now()}] Failed To Join Discord Invite")

client.run(token, bot=False)