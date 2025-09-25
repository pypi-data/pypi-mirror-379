import os
from typing import Dict, Optional

from ..bot import slack_bot


def configure_slack(users_mapping: Dict[str, str], token: Optional[str] = None):
    if token:
        os.environ['SLACK_BOT_TOKEN'] = token
        slack_bot.connect(token=token)
    else:
        slack_bot.connect()

    for user_name, channel_id in users_mapping.items():
        slack_bot.add_user_channel_id(user_name, channel_id)

    return slack_bot
