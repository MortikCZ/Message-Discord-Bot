import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='sendmessage')
async def send_message(ctx, channel: discord.TextChannel, role: discord.Role = None, *, message: str):
    # Získání odkazu na zprávu
    message_link = await channel.send(f"{role.mention} {message}" if role else message)

    await ctx.send(f"Zpráva byla odeslána na kanál {channel.mention} s rolí {role.mention if role else 'bez role'}. Odkaz na zprávu: {message_link.jump_url}")

# Spustí bota s tokenem vašeho bota
bot.run('MTIwODA0ODAzNTE2NzIxMTU4MQ.G__lMB.hSACpF7vlmBWo28LGSykA0ACnUvgAAkRdzx5bI')
