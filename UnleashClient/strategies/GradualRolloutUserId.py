from UnleashClient.utils import normalized_hash
from UnleashClient.strategies.Strategy import Strategy


class GradualRolloutUserId(Strategy):
    def apply(self, context=None):
        """
        Returns true if userId is a member of id list.

        :return:
        """
        percentage = int(self.parameters["percentage"])
        activation_group = self.parameters["groupId"]

        return percentage > 0 and normalized_hash(context["userId"], activation_group) <= percentage
