from castervoice.lib.dfplus.merge.mergerule import MergeRule

from castervoice.lib.dfplus.ccrmerging2.validation.base_validator import BaseRuleValidator

class IsMergeRuleValidator(BaseRuleValidator):
    def _is_valid(self, rule, params):
        return isinstance(rule, MergeRule)
    def _invalid_message(self):
        return "must be or inherit MergeRule"