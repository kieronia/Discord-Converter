import os
import logging
import asyncio
import discord
import requests

from discord.ext import commands
TOKEN = "put token here"
os.system("title lets have some fun!")
bot = commands.Bot(description="Discord self-bot" , command_prefix="!")



listeningchannel = 123123123
webhookurl = "https://discord.com/api/webhooks/76417996123/abceef"

@bot.event
async def on_connect():
	print(f"Connected to {bot.user.name} :)" )
	
	
@bot.event
async def on_ready():
	print(f"Ready on {bot.user.name} :)" )
    



@bot.event
async def on_message(message):
    if message.channel.id == listeningchannel:
        if message.author.discriminator != "0000":
            print(f"[!]{message.content}\n[!]{message.author.name}\n[!]{message.author.avatar_url}")
            print("[+] Got Data,Deleting message.")
            try:
                await message.delete()
                print("[+] Message Deleted, Sending Out Data Through Webhook.")
            except:
                print("[-] Error - Check Delete Message Permissions?")
            try:
                message.content = message.content.replace("@","at ") #stops ping attempts
                dataaa = {
                    "content" : f"{message.content}", #webhook message
                    "username" : f"{message.author.name}", #webhook username
                    "avatar_url" : f"{message.author.avatar_url}", #webhook pfp
                }
                requests.post(webhookurl, data=dataaa)
                print("[+] Success!")
            except:
                print("[-] Webhook Problem - Check Validity/Ratelimits")


    

bot.run(TOKEN, bot = False)
