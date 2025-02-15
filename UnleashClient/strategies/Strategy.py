# pylint: disable=dangerous-default-value
import warnings
from UnleashClient.constraints import Constraint


class Strategy:
    """
    The parent class for default and custom strategies.

    In general, default & custom classes should only need to override:
    * __init__() - Depending on the parameters your feature needs
    * apply() - Your feature provisioning
    """
    def __init__(self,
                 constraints=[],
                 parameters={},
                 ):
        """
        A generic strategy objects.

        :param constraints: List of 'constraints' objects derived from strategy section (...from feature section) of
        /api/clients/features response
        :param parameters: The 'parameter' objects from the strategy section (...from feature section) of
        /api/clients/features response
        """
        self.parameters = parameters
        self.constraints = constraints
        self.parsed_constraints = self.load_constraints(constraints)
        self.parsed_provisioning = self.load_provisioning()

    def __call__(self, context=None):
        warnings.warn(
            "unleash-client-python v3.x.x requires overriding the execute() method instead of the __call__() method.",
            DeprecationWarning
        )

    def execute(self, context=None):
        """
        Executes the strategies by:
        - Checking constraints
        - Applying the strategy

        :param context: Context information
        :return:
        """
        flag_state = False

        if all([constraint.apply(context) for constraint in self.parsed_constraints]):
            flag_state = self.apply(context)

        return flag_state

    def load_constraints(self, constraints_list):  #pylint: disable=R0201
        """
        Loads constraints from provisioning.

        :return:
        """
        parsed_constraints_list = []

        for constraint_dict in constraints_list:
            parsed_constraints_list.append(Constraint(constraint_dict=constraint_dict))

        return parsed_constraints_list

    # pylint: disable=no-self-use
    def load_provisioning(self):
        """
        Method to load data on object initialization, if desired.

        This should parse the raw values in self.parameters into format Python can comprehend.
        """
        return []

    def apply(self, context=None):  #pylint: disable=W0613,R0201
        """
        Strategy implementation goes here.

        :param context:
        :return:
        """
        return False
