from telegram.ext import BaseFilter

from castle_files.work_materials.filters.general_filters import filter_is_chat_wars_forward, filter_is_pm

import re


class FilterIsHero(BaseFilter):
    def filter(self, message):
        return filter_is_chat_wars_forward(message) and re.match("[🍆🍁☘🌹🐢🦇🖤]+", message.text) is not None and \
               re.search("🎒Рюкзак:", message.text) is not None


filter_is_hero = FilterIsHero()


class FilterIsProfile(BaseFilter):
    def filter(self, message):
        return filter_is_pm(message) and filter_is_chat_wars_forward(message) \
               and "Битва семи замков через" in message.text and \
               "Состояние:" in message.text and "Подробнее: /hero" in message.text


filter_is_profile = FilterIsProfile()


class FilterViewHero(BaseFilter):
    def filter(self, message):
        return filter_is_pm(message) and message.text.startswith("👀 Посмотреть в зеркало")


filter_view_hero = FilterViewHero()


class FilterViewProfile(BaseFilter):
    def filter(self, message):
        return filter_is_pm(message) and message.text.startswith("/view_profile_")


filter_view_profile = FilterViewProfile()
