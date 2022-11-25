import time
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
import linecache
import re
import discord
tk.Tk().withdraw()


CheckSettings = False
Main_Folder = os.path.dirname(os.path.realpath(__file__))
DataBase_Folder = Main_Folder + "\Database"




try:
    import Settings
except ModuleNotFoundError:
    CheckSettings = True
    print("Detected No Settings File")
    print("Running SettingEditor")
    time.sleep(3)
    Settings = open("Settings.py", "a")
    tokenbot = input("Insert Bot Token(Insert nothing if undecided)")
    delay_message = input("Insert time delay per bot message(Insert nothing if undecided)")
    channel_id = input("Insert channel ID(Insert nothing if undecided)")
    Settings.write("BotToken = '" + tokenbot + "'")
    Settings.write("\nMessage_Delay = '" + delay_message + "'")
    Settings.write("\nChannelID = '" + channel_id + "'")
    Settings.close()


def countlines(file):
    with open(file, 'r') as fp:
        num_lines = sum(1 for line in fp if line.rstrip())
        return num_lines

def Text_Filtration():
    print("Please Open a Text File")
    fn = askopenfilename()
    fntxtstrip = fn.rstrip(".txt")
    databasefile = open(fntxtstrip + "(FilteredIn).txt", "a")
    print("Filter In or out?(out/in)")
    out_or_in = input()
    line = 1
    if out_or_in == "out":
        print("HI")
    elif out_or_in == "in":
        print("What to Filter In?:")
        filterin = input()
        linecount = countlines(fn)
        while line <= linecount:
            oo = linecache.getline(r"" + fn, line)
            if re.search("Embed", oo):
                line = line + 3
            else:
                if re.search(filterin, oo):
                    line = line + 1
                    databasefile.write(oo)
                else:
                    line = line + 1
        databasefile.close()
        print("Filtration has finished")
        time.sleep(1)
        print("Exitting program")
        time.sleep(0.5)
        quit()
    else:
        print("Invalid Input")
        time.sleep(2)
        print("Ending Program")
        time.sleep(2)
        quit()
def Message_Sending():
    print("Please Open a Text File")
    fn = askopenfilename()
    client = discord.Client(intents=discord.Intents.default())
    databasefile = open(fn, "r")
    @client.event
    async def on_ready():
        print("Bot is ready")
        channel = client.get_channel(int(Settings.ChannelID))
        while True:
            time.sleep(float(Settings.Message_Delay))
            try:
                await channel.send(databasefile.readline())
            except discord.errors.HTTPException:
                print("Done Sending all Messages")
                break
            # msg = await channel.send(databasefile.readline())
            # time.sleep(5)
            # await msg.publish()
    client.run(Settings.BotToken)



if CheckSettings == False:
    print("Welcome to Communiqué Discord Orchestrater Bot")
    time.sleep(1)
    print("What program would you like to use")
    print("[1] Text Filtration Bot")
    print("[2] Message Sending bot")
    Select_Program = input()
    if Select_Program == "1":
       Text_Filtration()
    elif Select_Program == "2":
      Message_Sending()