import os


def human_read_format(size):
    names = ["", "К", "М", "Г", "T"]
    step = 0
    while size >= 1024:
        step += 1
        size /= 1024
    return str(round(size)) + names[step] + "Б"


def get_files_sizes():
    return "\n".join(map(lambda el: f"{el} {human_read_format(os.path.getsize(el))}",
                         filter(os.path.isfile, os.listdir())))
