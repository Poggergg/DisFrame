from os import environ as env
from discord.ext import commands

bot = commands.Bot(
	command_prefix="$",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

extensions = [
	'cogs.cog'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.


bot.run(env['token'])  # Starts the bot