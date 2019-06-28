from castervoice.lib.dfplus.ccrmerging2.validation.base_validator import BaseRuleValidator

class HasContextValidator(BaseRuleValidator):
    def _is_valid(self, rule, params):
        return rule.get_context() is not None
    def _invalid_message(self):
        return "must have a Context"