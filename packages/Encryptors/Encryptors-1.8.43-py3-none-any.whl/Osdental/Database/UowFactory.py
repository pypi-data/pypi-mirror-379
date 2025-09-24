from typing import Callable, Any, Dict
from Osdental.Database.UnitOfWork import UnitOfWork

class UowFactory:

    @staticmethod
    def uow_factory(session_factory: Callable[[], Any], repositories: Dict[str, Any]) -> Callable[[], Any]:
        return UnitOfWork(session_factory, repositories)