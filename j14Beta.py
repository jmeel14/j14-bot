__title__ = 'j14_beta'
__author__ = 'Jmeel14'

import discord
import re

from bot_config import * as cfg
from bot_cmds import * as cmds

class Bot(discord.Client):
    """Discord bot class."""

    def __init__(self, ownerID, servID, logChnl):
        super(Bot, self).__init__()

        self.prefix = config_start.get_prefix()
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

            if msg_

j14_bot_beta = Bot(
    'ID_BOT_OWNNER',
    'ID_SERVER',
    'ID_LOG_CHANNEL'
)

j14_bot_beta.run('BOT_TOKEN')