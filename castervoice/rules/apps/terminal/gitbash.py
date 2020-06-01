from dragonfly import Mimic, Function, MappingRule

from castervoice.lib.actions import Key, Text

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R


class GitBashRule(MappingRule):
    mapping = {
        "CD up":
            R(Text("cd ..")),
        "CD":
            R(Text("cd ")),
        "list":
            R(Text("ls ")),
        "make directory":
            R(Text("mkdir ")),
        "search recursive":
            R(Text("grep -rinH \"PATTERN\" *")),
        "search recursive count":
            R(Text("grep -rinH \"PATTERN\" * | wc -l")),
        "search recursive file type":
            R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;")),
        "to file":
            R(Text(" > FILENAME")),
    }


_executables = [
    "\\sh.exe",
    "\\bash.exe",
    "\\cmd.exe",
    "\\mintty.exe",
    "\\powershell.exe",
    "idea",
    "idea64",
    "studio64",
    "pycharm",
    "rider64",
    "code"
]


def get_rule():
    return GitBashRule, RuleDetails(name="git bash", executable=_executables)

