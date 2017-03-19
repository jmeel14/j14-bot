import os
import re

init_arr = []
init_cmd = {}

for path_file in os.listdir(os.path.dirname(__file__)):
    if re.search('^cmd\_(.*)\.py', path_file):
        file_ref = path_file[:-3]
        init_arr.append(file_ref)
        init_cmd[file_ref] = path_file
__all__ = init_arr

class Command:
    def __init__(self, admin_only, disc_client, msg_obj):
        self.admin_only = admin_only
        self.disc_client = disc_client
        self.msg_obj = msg_obj

    def warn_not_admin(self, admin_only, admin_id):
        if self.msg_obj.author.id != admin_id:
            self.disc_client.send_message(
                self.msg_obj.channel,
                '```py\n\'Error:\' This command is an admin-only feature.```'
)