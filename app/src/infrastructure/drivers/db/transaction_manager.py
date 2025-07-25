from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.transaction_manager import ITransactionManager


class TransactionManager(ITransactionManager):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def commit(self) -> None:
        await self.session.commit()

    async def flush(self) -> None:
        await self.session.flush()

    async def rollback(self) -> None:
        await self.session.rollback()
