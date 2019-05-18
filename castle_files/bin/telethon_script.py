from telethon import TelegramClient, events
from telethon.utils import PeerChannel

from castle_files.work_materials.globals import RESULTS_PARSE_CHANNEL_ID

try:
    from config import phone, username, password, api_id, api_hash
except ImportError:
    pass

from multiprocessing import Queue

castles_stats_queue = Queue()

TEST_CHANNEL_ID = 1353017829


def script_work():
    global client
    admin_client = TelegramClient(username, api_id, api_hash, update_workers=1, spawn_read_thread=False)
    admin_client.start(phone, password)

    client = admin_client
    admin_client.get_entity("ChatWarsBot")
    client.add_event_handler(stats_handler, event=events.NewMessage)
    print("telegram script launched")

    admin_client.idle()


def stats_handler(event):
    text = event.message.message
    if event.message.to_id == PeerChannel(RESULTS_PARSE_CHANNEL_ID) and 'Результаты сражений:' in text:
        print("put stats in queue")
        castles_stats_queue.put(text)
        return