from dragonfly import Mimic

from castervoice.lib.actions import Text, Key
from castervoice.rules.ccr.standard import SymbolSpecs
from castervoice.lib.const import CCRType
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.mergerule import MergeRule
from castervoice.lib.merge.state.short import R


class CSharp(MergeRule):
    pronunciation = "C sharp"

    mapping = {
        SymbolSpecs.IF:
            R(Key("if")),
        SymbolSpecs.ELSE:
            R(Key("else")),
        #
        SymbolSpecs.SWITCH:
            R(Text("switch")),
        SymbolSpecs.CASE:
            R(Text("case :") + Key("left")),
        SymbolSpecs.BREAK:
            R(Text("break;")),
        SymbolSpecs.DEFAULT:
            R(Text("default: ")),
        #
        SymbolSpecs.DO_LOOP:
            R(Text("do")),
        SymbolSpecs.WHILE_LOOP:
            R(Text("while")),
        SymbolSpecs.FOR_LOOP:
            R(Text("for")),
        SymbolSpecs.FOR_EACH_LOOP:
            R(Text("foreach")),
        #
        SymbolSpecs.TO_INTEGER:
            R(Text("int.Parse()") + Key("left")),
        SymbolSpecs.TO_FLOAT:
            R(Text("float.Parse()") + Key("left")),
        SymbolSpecs.TO_STRING:
            R(Text("string.Parse()") + Key("left")),
        #
        SymbolSpecs.AND:
            R(Text("&&")),
        SymbolSpecs.OR:
            R(Text("||")),
        SymbolSpecs.NOT:
            R(Text("!")),
        #
        SymbolSpecs.SYSOUT:
            R(Text("Console.WriteLine()") + Key("left")),

        #
        SymbolSpecs.FUNCTION:
            R(Text("(){}") + Key("left, left, left")),
        SymbolSpecs.CLASS:
            R(Text("class ")),
        #
        SymbolSpecs.COMMENT:
            R(Text("// ")),
        SymbolSpecs.LONG_COMMENT:
            R(Text("/**/") + Key("left, left")),
        #
        SymbolSpecs.NULL:
            R(Text("null")),
        #
        SymbolSpecs.RETURN:
            R(Text("return ")),
        #
        SymbolSpecs.TRUE:
            R(Text("true")),
        SymbolSpecs.FALSE:
            R(Text("false")),

        # C# specific
        "using":
            R(Text("using ")),
        "enum":
            R(Text("enum ")),
        "struct":
            R(Text("struct ")),
        "interface":
            R(Text("interface ")),
        "public":
            R(Text("public ")),
        "internal":
            R(Text("internal ")),
        "protected":
            R(Text("protected ")),
        "private":
            R(Text("private ")),
        "static":
            R(Text("static ")),
        "void":
            R(Text("void ")),
        "read-only":
            R(Text("readonly ")),
        "cast integer":
            R(Text("(int)") + Key("left")),
        "cast double":
            R(Text("(double)") + Key("left")),
        "constant":
            R(Text("const ")),
        "variable":
            R(Text("var ")),
        "(lambda|goes to)":
            R(Text(" => ")),
        "new new":
            R(Text("new ")),
        "integer":
            R(Text("int ")),
        "double":
            R(Text("double ")),
        "character":
            R(Text("char ")),
        "boolean":
            R(Text("bool ")),
        "string":
            R(Text("string ")),
        "assign":
            R(Text(" = ")),
    }

    extras = []
    defaults = {}


def get_rule():
    return CSharp, RuleDetails(ccrtype=CCRType.GLOBAL)
