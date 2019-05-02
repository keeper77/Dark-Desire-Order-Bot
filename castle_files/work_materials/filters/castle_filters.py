"""
В этом модуле находятся фильтры для сообщений, относящихся к виртуальному замку
"""
from telegram.ext import BaseFilter
from castle_files.work_materials.filters.general_filters import filter_is_pm
from castle_files.work_materials.globals import dispatcher


class FilterBack(BaseFilter):
    def filter(self, message):
        return filter_is_pm and message.text.startswith("↩️ Назад")


filter_back = FilterBack()


# Далее идут фильтры для локаций замка
class FilterCentralSquare(BaseFilter):
    def filter(self, message):
        return filter_is_pm and message.text.startswith("⛲️ Центральная площадь")


filter_central_square = FilterCentralSquare()


class FilterCastleGates(BaseFilter):
    def filter(self, message):
        return filter_is_pm and message.text.startswith("⛩ Врата замка")


filter_castle_gates = FilterCastleGates()


class FilterBarracks(BaseFilter):
    def filter(self, message):
        user_data = dispatcher.user_data.get(message.from_user.id)
        if user_data is None:
            return False
        return filter_is_pm and message.text.startswith("🎪 Казарма") and user_data.get("status") == 'central_square'


filter_barracks = FilterBarracks()


