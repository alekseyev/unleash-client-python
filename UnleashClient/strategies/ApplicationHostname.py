import platform
from UnleashClient.strategies.Strategy import Strategy


class ApplicationHostname(Strategy):
    def load_provisioning(self):
        return [x.strip() for x in self.parameters["hostNames"].split(',')]

    def apply(self, context=None):
        """
        Returns true if userId is a member of id list.

        :return:
        """
        return platform.node() in self.parsed_provisioning
