import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='sendmessage')
@has_permissions(administrator=True)
async def send_message(ctx, channel: discord.TextChannel, role: discord.Role = None, *, message: str):
    message_link = await channel.send(f"{role.mention} {message}" if role else message)

    await ctx.send(f"Zpráva byla odeslána na kanál {channel.mention} s rolí {role.mention if role else 'bez role'}. Odkaz na zprávu: {message_link.jump_url}")

bot.run('TOKEN')
