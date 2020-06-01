from dragonfly import MappingRule, Choice
from castervoice.lib.actions import Key, Text


def input(argument, shock, command):
    commandline = Text(command) + Key("space") + Text(argument)
    if argument != "":
        commandline += Key("space")
    if shock == "true":
        commandline += Key("enter")
    commandline.execute()
