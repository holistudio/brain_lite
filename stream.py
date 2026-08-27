import os
import time

from dotenv import load_dotenv

from sub_data import Subcribe

load_dotenv()


def main():
    client_id = os.environ['EMOTIV_CLIENT_ID']
    client_secret = os.environ['EMOTIV_CLIENT_SECRET']
    headset_id = os.environ.get('EMOTIV_HEADSET_ID', '')

    s = Subcribe(client_id, client_secret)

    streams = ['met']
    s.start(streams, headset_id=headset_id)

    while True:
        metrics = s.latest_met
        # metrics is a dict like:
        # {'eng': 0.50, 'exc': 0.27, 'lex': 0.25, 'str': 0.29, 'rel': 0.23, 'int': 0.31, 'attn': 0.58}
        time.sleep(0.5)


if __name__ == '__main__':
    main()
