# import xml.etree.ElementTree as ET
# import os
# import discord
# from dotenv import load_dotenv
# from discord.ext import commands
#
# load_dotenv()  # load all the variables from the env file
#
# # Load XML data
# tree = ET.parse('./data/pythongeneralAug2020.xml.out')
# root = tree.getroot()
#
# # Set up Discord bot
# intents = discord.Intents.default()
# intents.messages = True
#
# bot = commands.Bot(command_prefix='!', intents=intents)
#
#
# async def send_messages():
#     # Assuming you have a dictionary mapping channel names in XML to Discord channel IDs
#     channel_mapping = {
#         'python-general': '1308646814492266496',
#         'programming-help': '1308646835425902682',
#         'share-your-setup': '1308646876890927176',
#         'web-development': '1308646907802943498',
#         'new-ideas': '1308648685277548594',
#     }
#
#     # Limit to the first 1000 messages
#     max_messages = 1000
#     message_count = 0
#
#     # Extract and send messages
#     for message in root.findall('message'):
#         if message_count >= max_messages:
#             break
#
#         user = message.find('user').text
#         text = message.find('text').text
#         channel_name = root.find('channel_name').text
#
#         # Get the Discord channel
#         discord_channel_id = channel_mapping.get(channel_name)
#
#         if discord_channel_id:
#             discord_channel = bot.get_channel(int(discord_channel_id))
#
#             if discord_channel:
#                 await discord_channel.send(f'{user}: {text}')
#                 message_count += 1
#
#     # Close the bot after messages are sent
#     await bot.close()
#
#
# @bot.event
# async def on_ready():
#     print(f'{bot.user} is ready to import data')
#     await send_messages()
#
#
# bot.run(os.getenv('TOKEN'))
