import json
import codecs
import datetime
import os
import logging
import argparse
import time
import random

from instagram_private_api import Client, MediaRatios, ClientError, ClientLoginError,ClientCookieExpiredError, ClientLoginRequiredError
from instagram_private_api_extensions import media, live

from savesettings_logincallback import *



settings_file = 'example.json'
username = 'exampleusername'
password = 'exampleusernamepassword'
users = [#list of nonstring userids]
try:
    device_id = None

    with open(settings_file) as file_data:
        cached_settings = json.load(file_data, object_hook=from_json)
    print('Reusing settings: {0!s}'.format(settings_file))

    device_id = cached_settings.get('device_id')
        # reuse auth settings
    api = Client(
        username, password,
        settings=cached_settings)
        
except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
    print('ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))
    print('run savesettings_logincallback')
    exit()

    
for user in users:
    time.sleep(random.randrange(3, 5))
    if api.user_broadcast(user) is not None:
        broadcast_id = api.user_story_feed(user).get('broadcast').get('id')
        time.sleep(random.randrange(3, 5))
        broadcast = api.broadcast_info(broadcast_id)
        time.sleep(random.randrange(3, 5))
        dl = live.Downloader(mpd=broadcast['dash_playback_url'], output_dir='output_{}/'.format(broadcast['id']), user_agent=api.user_agent)
        time.sleep(random.randrange(3, 5))
        try:
            dl.run()
        except KeyboardInterrupt:
            if not dl.is_aborted:
                dl.stop()
        finally:
            # combine the downloaded files
            # Requires ffmpeg installed. If you prefer to use avconv
            # for example, omit this step and do it manually
            dl.stitch('my_video' + broadcast.get(('username') + broadcast.get(('published_time') + '.mp4')))
