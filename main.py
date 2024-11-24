import discord
import os # default module
from dotenv import load_dotenv
from datetime import datetime
from agents.historian import HistorianAgent

load_dotenv() # load all the variables from the env file
bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    # Add the following lines to send a message to a specific channel
    channel_id = 1301367723514921081  # Replace with your channel ID
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Hello, this is a message from the bot!")


@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("Hey!")


def clean_message(message: discord.Message) -> dict:
    # Extract relevant information
    content = message.content
    author_name = message.author.name
    timestamp = message.created_at

    # Format the timestamp to a concise string
    # Example format: "2023-12-31 23:59"
    timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M")

    cleaned_message = {
        "content": content,
        "author": author_name,
        "timestamp": timestamp_str
    }
    return cleaned_message


@bot.slash_command(name="message_history", description="fetches the message history of the current channel")
async def message_history(ctx: discord.ApplicationContext):
    channel = ctx.channel
    messages = await channel.history(limit=2).flatten()

    cleaned_messages = [clean_message(message) for message in messages]

    for message in cleaned_messages:
        print(message)

    await ctx.respond("fetching message history")


@bot.slash_command(name="summarize_channel", description="summarizes the message history of the current channel")
async def summarize_channel(ctx: discord.ApplicationContext):
    channel = ctx.channel
    history = await channel.history(limit=100).flatten()
    agent = HistorianAgent(channel_history=history)

    summary = agent.summarize()
    await ctx.respond(summary)


bot.run(os.getenv('TOKEN'))  # run the bot with the token
