"""
Здесь находятся тексты для квестов
"""


quest_texts = {"exploration": {
    "two_players": {0: {
        "first_begin":
"""На другой стороне ручья ты заметил соратника <b>{}</b>(@{}).
Очевидно, ему нужна помощь в переправе.
Ты схватил длинную палку, а в голове родился план:
"Проняну, он схватится - изи!"
Нажми "/protyanut" и жди, когда он схватится!""",

                     "second_begin":
"""На другой стороне ручья ты заметил соратника <b>{}</b>(@{}).
Очевидно, тебе нужна помощь в переправе на ту сторону.
Товарищь схватил длинную палку и машет тебе, а в твоей голове родился план:
"Он тянет, я хватаюсь - изи!"
Нажми "/shvatit" и жди, когда он потянет! Но помни, у вас 30 секунд на слаженные действия!""",
                     "first_success": """У вас получилось! Вместе вы успешно закончили разведку!""",
                     "first_fail": "Вы слишком долго копались. Сейчас уже не разобрать кто виноват, "
                             "вы оба мокрые до ниток и ни с чем вернулись в Замок."

                     }},
    "one_player": ["Побродив по окрестностям, ты отметил интересные места на карте и вернулся в замок."]
    },
    "pit": {
        "two_players": {},
        "one_player": ["Обычный рабочий день. Лопата, кирка, лопата."]
    }
}
