import discord
from discord import Intents, Client, Message
from discord.ext import tasks, commands
import asyncio
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN =  os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.typing = False
intents.presences =False
intents.voice_states=True
intents.guilds=True

client: Client = Client(intents=intents)
class VCmaker:
    @client.event
    async def on_ready():
        print(f'{client.user} join to Discord!')
        
    @client.event
    async def on_voice_state_update(member,before,after):
        now = datetime.now()
        time = now.strftime("%H:%M:%S:")
        
        if after.channel is not None:
            if after.channel and after.channel.name == 'create':
                new_channel = await after.channel.clone(name = f'new channel name')
                print(time, f'{member} create vc')
                await member.move_to(new_channel)
                print(time, f'{member} moved in vc')
                
                while len(new_channel.members)!=0:
                    await asyncio.sleep(1)
                    if len(new_channel.members)==0:
                        await new_channel.delete()
                        print(time, f'The Voice channel{new_channel.name} deleted')

    def main() -> None:
        client.run(token=TOKEN)
    main()
