from aiogram import Router
from commands import router as commands_router
from search_cmd import router as search_router
from info_cmd import router as info_router
from backend import searching_vac

router = Router(name=__name__)
router.include_routers(
    commands_router,
    search_router,
    info_router,
)

__all__ = (
    "router",
    "searching_vac"
)
print(searching_vac('Менеджер', 'all'))