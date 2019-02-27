from json import dumps


def json_convert(duplicate_file_ls):
    """ convert duplicate_file_ls to json expression """
    return dumps(duplicate_file_ls, indent=4)