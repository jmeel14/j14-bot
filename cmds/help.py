import cmds.commands as commands

cmd = commands.Command('help')

async def processCommand(args, channel):

	await cmd.bot.send_message(channel, 'hello world')

	print('test')

cmd.process = processCommand