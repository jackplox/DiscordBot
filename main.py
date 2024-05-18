import settings
import discord
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
import csv
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    x = datetime.now()
    
    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

    @bot.command()
    async def getKPM(ctx):
        try:
            kpmSum=0
            with open("stats/%s-KPM.csv" % ctx.message.author.id, mode="rU") as file:
                csvFile = csv.reader(file)
                count = 0
                for line in csvFile:
                    count += 1
                    kpmSum += line[0]
                    if count == 1:
                        oldest = line[1]
                
                kpmAvg = kpmSum / count
                await discord.InteractionResponse.send_message(content="Since %s, your average KPM is : %d!" % (oldest, kpmAvg), ephemeral = True)
        except:
            await discord.InteractionResponse.send_message(content="You dont have any stats yet! Use `!addKPM <YOUR KPM>` to start tracking your stats!", ephemeral = True)
            return

    @bot.command(
            help="Add a KPM stat to your spreadsheet.",
            description="Add a new KPM to your average."
    )
    async def addKPM(ctx, kpm):
        """ Adds stats to your spreadsheet """
        try:
            kpm = float(kpm)

        except:
            await discord.InteractionResponse.send_message(content="Invalid input -- please enter a NUMBER!", ephemeral = True)
            return
        
        if kpm > 120:
                await discord.InteractionResponse.send_message(content="...Are you sure you're being honest?  You got a KPM of %d on Aimbotz?\n...wow, ok." % kpm, ephemeral = True)

        date = "%s/%s/%s" % (x.month, x.day, x.year)
                        
        with open("stats/%s-KPM.csv" % ctx.message.author.id, mode="a") as file:
            file.write("%d,%s\n" % (kpm, date))


        #await discord.InteractionResponse.send_message(content=discord.Interaction.id)
        logger.info(f"Added stat for User: {ctx.message.author}")       
        await discord.InteractionResponse.send_message(content="Your KPM stats have been updated!", ephemeral = True)

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

    
if __name__ == "__main__":
    run()