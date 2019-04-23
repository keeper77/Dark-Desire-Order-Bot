from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler


from order_files.work_materials.filters.pin_setup_filters import *
from order_files.work_materials.filters.service_filters import *
from order_files.work_materials.filters.pult_filters import filter_remove_order


from order_files.bin.pult_callback import pult, pult_callback
from order_files.bin.order import attackCommand, menu, remove_order, refill_deferred_orders

from order_files.bin.guild_chats import add_pin, pin_setup, recashe_order_chats, pindivision, pinmute, pinpin, pinset

from order_files.work_materials.globals import dispatcher, updater, conn


# ------------------------------------------------------------------------------------------------------


def inline_callback(bot, update):
    if update.callback_query.data.find("p") == 0:
        pult_callback(bot, update)
        return


def not_allowed(bot, update):
    mes = update.message
    title = update.message.chat.title
    if title is None:
        title = update.message.chat.username
    if (mes.text and '@Rock_Centre_Order_bot' in mes.text) or mes.chat_id > 0:
        bot.send_message(
            chat_id=admin_ids[0],
            text="Несанкционированная попытка доступа, от @{0}, telegram id = <b>{1}</b>,\n"
                    "Название чата - <b>{2}</b>, chat id = <b>{3}</b>".format(mes.from_user.username, mes.from_user.id,
                                                                             title, mes.chat_id), parse_mode='HTML')


def order_bot_processing():
    dispatcher.add_handler(CommandHandler('add_pin', add_pin, filters=filter_is_admin))
    dispatcher.add_handler(MessageHandler(~filter_super_admin & ~(filter_chat_allowed & filter_is_admin), not_allowed))
    dispatcher.add_handler(CommandHandler('⚔', attackCommand, filters=filter_is_admin))
    dispatcher.add_handler(CommandHandler('pult', pult, filters=filter_is_admin))
    dispatcher.add_handler(CommandHandler('menu', menu, filters=filter_is_admin))
    dispatcher.add_handler(CommandHandler('pin_setup', pin_setup, filters=filter_is_admin))
    dispatcher.add_handler(MessageHandler(Filters.command & filter_remove_order & filter_is_admin, remove_order))
    dispatcher.add_handler(MessageHandler(Filters.command & filter_pinset & filter_is_admin, pinset))
    dispatcher.add_handler(MessageHandler(Filters.command & filter_pinpin & filter_is_admin, pinpin))
    dispatcher.add_handler(MessageHandler(Filters.command & filter_pinmute & filter_is_admin, pinmute))
    dispatcher.add_handler(MessageHandler(Filters.command & filter_pindivision & filter_is_admin, pindivision))
    dispatcher.add_handler(CallbackQueryHandler(inline_callback, pass_update_queue=False, pass_user_data=False))


    recashe_order_chats()
    refill_deferred_orders()
    updater.start_polling(clean=False)


    # Останавливаем бота, если были нажаты Ctrl + C
    updater.idle()
    # Разрываем подключение.
    conn.close()
