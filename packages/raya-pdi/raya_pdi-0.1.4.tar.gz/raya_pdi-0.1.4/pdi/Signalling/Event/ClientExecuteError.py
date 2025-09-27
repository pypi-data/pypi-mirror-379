class ClientExecuteError:
    def __init__(self, exception: Exception):
        self.exception = exception

    @classmethod
    def getName(cls) -> str:
        return 'client:execute:error'
