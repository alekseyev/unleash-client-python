from UnleashClient.utils import LOGGER, get_identifier

class Constraint:
    def __init__(self, constraint_dict):
        """
        Represents a constraint on a strategy

        constraint_dict = From the strategy document.
        """
        self.context_name = constraint_dict['contextName']
        self.operator = constraint_dict['operator']
        self.values = constraint_dict['values']

    def apply(self, context=None):
        """
        Returns true/false depending on constraint provisioning and context.

        :param context: Context information
        :return:
        """
        constraint_check = False

        try:
            value = get_identifier(self.context_name, context)

            if value:
                if self.operator.upper() == "IN":
                    constraint_check = value in self.values
                elif self.operator.upper() == "NOT_IN":
                    constraint_check = value not in self.values
        except Exception as excep:  #pylint: disable=W0703
            LOGGER.info("Could not evaluate context %s!  Error: %s", self.context_name, excep)

        return constraint_check
