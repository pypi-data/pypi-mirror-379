from pdi.Signalling.Event.AbstractEvent import Event


class ClientExecuteError(Event):
    def __init__(self, exception: Exception):
        self.exception = exception

    @classmethod
    def getName(cls) -> str:
        return 'client:execute:error'
