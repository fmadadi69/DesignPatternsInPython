class Operation:
    def execute(self):
        pass


class RequestHandler(Operation):
    def execute(self):
        print("Handling Requests")


class DataProcessor(Operation):
    def execute(self):
        print('Data is processed')


class LoggingDecorator:
    def __init__(self, wrapped_operation):
        self.__wrapped_operation = wrapped_operation

    def decorate(self):
        print(f'Logging Start time for {self.__wrapped_operation.__class__.__name__}')
        self.__wrapped_operation.execute()
        print(f'Logging End time for {self.__wrapped_operation.__class__.__name__}')


class RequestLoggingDecorator(LoggingDecorator):
    def decorate(self):
        super().decorate()
        

class DataLoggingDecorator(LoggingDecorator):
    def decorate(self):
        super().decorate()


request_handler = RequestHandler()
LoggingDecorator(request_handler).decorate()

RequestLoggingDecorator(request_handler).decorate()

DataLoggingDecorator(request_handler).decorate()



