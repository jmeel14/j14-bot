import re

def get_prefix():
    regex_str = "\{\s\'bot_prefix\'\:\s\'(.*)'\s\}"

    config_file = open('bot_settings.txt', 'r')
    config_file_read = config_file.read()
    config_file.close()

    for read_line in config_file_read:
        if re.search(regex_str, read_line):
            return re.search(regex_str, read_line).groups()[0]
        else:
            return 'j14.'
