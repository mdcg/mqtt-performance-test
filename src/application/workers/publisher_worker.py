import random
from time import sleep

from src.application.services.publisher import Publisher
from src.infrastructure.logging import Logger

logger = Logger("Publisher Worker")


def main():
    pub = Publisher()
    pub.run()

    try:
        while True:
            sleep(1)
            for i in range(random.randrange(500, 999)):
                pub.publish(f"Hello, {i}")
    except KeyboardInterrupt:
        pub.stop()


if __name__ == "__main__":
    main()
