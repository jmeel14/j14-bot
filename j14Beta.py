__title__ = 'j14_beta'
__author__ = 'Jmeel14'

import discord
import re

import config as cfg
import cmds as cmds

import cmds.commands as commands

class Bot(discord.Client):
    """Discord bot class."""

    def __init__(self, ownerID, servID, logChnl):
        super(Bot, self).__init__()

        self.prefix = cfg.config_start.get_prefix()
        self.ownerID = ownerID
        self.servID = servID
        self.logChnl = logChnl

    async def on_ready(self):
        out_string = "\n\nThe bot is ready with username {0}, and ID {1}"
        out_format_string = out_string.format(self.user.name, self.user.id)
        print(out_format_string)
        print(''.join(['_' for num in range(len(out_format_string) + 1)]))

    async def on_message(self, msg):
        """On message handler"""

        prefix_re = re.search('^' + self.prefix, msg.content)
        msg_cmd_re = '^' + self.prefix + '(.*)'

        if prefix_re:
            cmd_str = re.search(msg_cmd_re, msg.content).groups()[0]

            # Gain some arguments to use.
            args = msg.content.split(' ')
            channel = msg.channel

            # Assume the length, not sure how you want to do this.
            args[0] = str(args[0])[3:]

            # Printing the arguments. For debugging.
            # print(args)

            # Loop through all of our commands.
            for command in commands.defined:

                # Printing the commands names, for debugging.
                # print(command.name)

                if args[0] == command.name:

                    command.bot = j14_bot_beta
                    
                    if(command.process):
                        await command.process(args, channel)


j14_bot_beta = Bot(
    'ID_BOT_OWNER',
    'ID_SERVER',
    'ID_LOG_CHANNEL'
)

j14_bot_beta.run('BOT_TOKEN')