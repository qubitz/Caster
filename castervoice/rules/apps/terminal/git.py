from dragonfly import Mimic, Function, MappingRule, Choice, Dictation

from castervoice.rules.apps.terminal import command_support

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.actions import Key, Text
from castervoice.lib import commandline
from castervoice.lib.merge.state.short import R


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class GitCommandRule(MappingRule):
    GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"
    mapping = {
        "(git|get) add existing":
            R(Key("g, i, t, space, a, d, d, space, dot")),
        "(git|get) commit short":
            R(Key(GIT_COMMIT)),
        "(git|get) bug fix commit <n>":
            R(Mimic("get", "commit") + Text("fixes #%(n)d ") + Key("backspace")),
        "(git|get) reference commit <n>":
            R(Mimic("get", "commit") + Text("refs #%(n)d ") + Key("backspace")),
        "(git|get) checkout":
            R(Text("git checkout ")),
        "(git|get) remote":
            R(Text("git remote ")),
        "(git|get) merge tool":
            R(Text("git mergetool")),
        "(git|get) push force":
            R(Text("git push -f ")),
        "(git|get) push gentle":
            R(Text("git push --force-with-lease")),
        "undo [last] commit | (git|get) reset soft head":
            R(Text("git reset --soft HEAD~1")),
        "(undo changes | (git|get) reset hard)":
            R(Text("git reset --hard")),
        "stop tracking [file] | (git|get) remove":
            R(Text("git rm --cached ")),
        "preview remove untracked | (git|get) clean preview":
            R(Text("git clean -nd")),
        "remove untracked | (git|get) clean untracked":
            R(Text("git clean -fd")),
        "(git|get) visualize":
            R(Text("gitk")),
        "(git|get) visualize file":
            R(Text("gitk -- PATH")),
        "(git|get) visualize all":
            R(Text("gitk --all")),
        "(git|get) history":
            R(Text("git ls")),
        "(git|get) log one":
            R(Text("git log --pretty=oneline ")),
        "(git|get) stash apply [<n>]":
            R(Text("git stash apply") + Function(_apply)),
        "(git|get) stash list":
            R(Text("git stash list")),
        "(git|get) stash branch":
            R(Text("git stash branch ")),
        "(git|get) cherry pick":
            R(Text("git cherry-pick ")),
        "(git|get) (abort cherry pick | cherry pick abort)":
            R(Text("git cherry-pick --abort")),
        "(git|get) (GUI | gooey)":
            R(Text("git gui")),
        "(git|get) blame":
            R(Text("git blame PATH -L FIRSTLINE,LASTLINE")),
        "(git|get) gooey blame":
            R(Text("git gui blame PATH")),

        "(git|get) <argument> [<shock>]": R(Function(commandline.input, command="git"))
    }

    custom_args = {
        "add all": "add -A"
    }
    verbose_args = command_support.mirrored([
        "clone",
        "add",
        "restore",
        "diff",
        "grep",
        "log",
        "show",
        "status",
        "branch",
        "commit",
        "merge",
        "rebase",
        "switch",
        "tag",
        "fetch",
        "pull",
        "push",
        "stash",
        "checkout"
    ])
    arguments = {
        "base": "",
        "initialize": "init",
        "move": "mv",
        "remove": "rm"
    }
    arguments.update(verbose_args)
    arguments.update(custom_args)

    extras = [
        Choice("argument", arguments),
        Choice("shock", {
            "shock": "true"
        }),
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {
        "shock": "false",
        "n": 0
    }


def get_rule():
    return GitCommandRule, RuleDetails(name="git")

