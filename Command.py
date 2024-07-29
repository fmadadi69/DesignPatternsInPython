from abc import ABC, abstractmethod


class CustomerService:
    def __init__(self, name, age, sex):
        self._cname = name
        self._cage = age
        self._csex = sex

    def add_customer(self):
        return f'new customer: {self._cname}, age: {self._cage}, sex: {self._csex}'


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddCustomerCommand(Command):
    def __init__(self, customer_service: CustomerService):
        self._customer_service = customer_service

    def execute(self):
        return self._customer_service.add_customer()


class Button:
    def __init__(self, command: Command):
        self._command = command

    def click(self):
        return self._command.execute()


button = Button(AddCustomerCommand(CustomerService('faezeh', 34, 'Female')))
print(button.click())
