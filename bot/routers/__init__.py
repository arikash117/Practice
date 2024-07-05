from aiogram import Router
from commands import router as commands_router
from search_cmd import router as search_router
from info_cmd import router as info_router

router = Router(name=__name__)
router.include_routers(
    commands_router,
    search_router,
    info_router,
)

__all__ = (
    "router",
)
