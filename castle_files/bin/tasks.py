"""
Файл создан для планирования задач, которые реализованы в других файлах
"""

from castle_files.bin.castle import plan_roulette_games
from castle_files.bin.profile import plan_remember_exp
from castle_files.bin.guild_chats import arena_notify, top_notify, check_guilds_api_access
from castle_files.bin.service_functions import plan_work


# Запускается один раз при старте бота; осуществляет планирование всех рассылок, привязанных ко времени и
# прочие задания.
def plan_daily_tasks(bot=None, job=None):
    plan_arena_notify()
    plan_top_notify()
    plan_remember_exp()
    plan_guilds_api_players_update()
    plan_roulette_games()
    # plan_work(plan_daily_tasks, 0, 0, 10)


def plan_arena_notify():
    plan_work(arena_notify, 12, 0, 0)


def plan_top_notify():
    plan_work(top_notify, 19, 0, 0)


def plan_guilds_api_players_update():
    plan_work(check_guilds_api_access, 3, 0, 0, context={"reset": True})