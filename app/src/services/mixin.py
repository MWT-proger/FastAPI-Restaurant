from dataclasses import dataclass

from repositories.container import AbstractRepositoriesContainer


@dataclass
class ServiceMixin:
    container: AbstractRepositoriesContainer
