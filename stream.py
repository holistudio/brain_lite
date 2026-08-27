import os

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


if __name__ == '__main__':
    main()
