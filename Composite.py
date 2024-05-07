from abc import ABC, abstractmethod
from typing import List


class Employee(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_detail(self) -> str:
        pass


class IndividualContributor(Employee):
    def get_detail(self) -> str:
        return f'Individual Contributor:  {self.name}'


class Department(Employee):
    def __init__(self, name: str):
        super().__init__(name)
        self.members: List[Employee] = []

    def add_members(self, member: Employee) -> None:
        self.members.append(member)

    def get_detail(self) -> str:
        details = f'Department : {self.name}\n'
        for member in self.members:
            details += f' - {member.get_detail()} \n'

        return details


ali = IndividualContributor('ali')
zahra = IndividualContributor('zahra')
engineering = Department('Engineering')
engineering.add_members(ali)
engineering.add_members(zahra)
# print(engineering.get_detail())

marketing = Department('marketing')
marketing.add_members(IndividualContributor('mohsen'))
marketing.add_members(IndividualContributor('hassan'))

company = Department('Company')
company.add_members(engineering)
company.add_members(marketing)

print(company.get_detail())


