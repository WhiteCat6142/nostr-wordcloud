from pynostr.relay_manager import RelayManager
from pynostr.filters import FiltersList, Filters
from pynostr.event import EventKind
import time
import uuid

def fetch(relay,ban_list,limit,author):
    contents=[]
    relay_manager = RelayManager(timeout=2)
    relay_manager.add_relay(relay)
    if author is None:
        filters = FiltersList([Filters(kinds=[EventKind.TEXT_NOTE], limit=limit)])
    else:
        filters = FiltersList([Filters(kinds=[EventKind.TEXT_NOTE], limit=limit, authors=[author])])
    subscription_id = uuid.uuid1().hex
    relay_manager.add_subscription_on_all_relays(subscription_id, filters)
    relay_manager.run_sync()
    while relay_manager.message_pool.has_notices():
        notice_msg = relay_manager.message_pool.get_notice()
        print(notice_msg.content)
    while relay_manager.message_pool.has_events():
        event_msg = relay_manager.message_pool.get_event()
        if event_msg.event.pubkey in ban_list:
            continue
        warning=False
        if event_msg.event.tags is not None:
            for t in event_msg.event.tags:
                if t[0]=="content-warning":
                    warning=True
                    break
        if warning:
            continue
        contents.append(event_msg.event.content)
    relay_manager.close_all_relay_connections()
    return contents
