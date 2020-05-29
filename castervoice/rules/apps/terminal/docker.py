from dragonfly import MappingRule, Choice

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.rules.apps.vocabs import vocab_support
from castervoice.lib.actions import Key, Text
from castervoice.lib.merge.state.short import R


class DockerCommandRule(MappingRule):

    mapping = {
        "(docker|doctor) <command> [<shock>]": R(Text("docker %(command)s ") + Key("%(shock)s")),
        "(docker|doctor) <cmd> [<shock>]": R(Text("docker %(cmd)s ") + Key("%(shock)s")),
    }

    docker_verbose_commands = [
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
    ]

    extras = [
        Choice("command", vocab_support.map_to_mirror(docker_verbose_commands)),
        Choice("cmd", {
            "base": "",

            "copy": "cp",
            "execute": "exec",
            "list": "ps",
            "remove [container[s]]": "rm",
            "remove image[s]": "rmi",
        }),
        Choice("shock", {
            "shock": "enter"
        })
    ]
    defaults = {
        "shock": ""
    }


def get_rule():
    return DockerCommandRule, RuleDetails(name="Docker Commands")

