from .. import State


class ServerWaitEndOfEarlyData(State):
    can_send = True
    can_send_application_data = True

    def process(self, message):
        raise NotImplementedError  # TODO
