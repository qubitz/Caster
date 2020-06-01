from dragonfly import MappingRule, Choice, Function

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.rules.apps.terminal import command_support
from castervoice.lib import commandline
from castervoice.lib.actions import Key, Text
from castervoice.lib.merge.state.short import R


class DockerCommandRule(MappingRule):
    mapping = {
        "(docker|doctor) <argument> [<shock>]": R(Function(commandline.input, command="docker")),
    }

    verbose_args = command_support.mirrored([
        "attach",
        "build",
        "commit",
        "create",
        "diff",
        "export",
        "history",
        "import",
        "images",
        "info",
        "inspect",
        "kill",
        "load",
        "login",
        "logout",
        "logs",
        "pause",
        "port",
        "pull",
        "push",
        "rename",
        "restart",
        "run",
        "save",
        "search",
        "start",
        "stats",
        "stop",
        "tag",
        "top",
        "unpause",
        "update",
        "version",
        "wait"
    ])
    args = {
        "base": "",
        "copy": "cp",
        "execute": "exec",
        "list": "ps",
        "remove [container[s]]": "rm",
        "remove image[s]": "rmi"
    }
    args.update(verbose_args)

    extras = [
        Choice("argument", args),
        Choice("shock", {
            "shock": "true"
        })
    ]
    defaults = {
        "shock": "false"
    }


def get_rule():
    return DockerCommandRule, RuleDetails(name="Docker Commands")
