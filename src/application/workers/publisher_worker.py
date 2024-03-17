import uuid
from random import randint
from time import sleep

from src.application.services.publisher import Publisher
from src.infrastructure.common.csv import CSV
from src.infrastructure.logging import Logger

logger = Logger("Publisher Worker")


def main():
    csv = CSV(file_path="/home/mdcg/Development/Projects/mqtt-performance-test/payload.csv")
    pub = Publisher()
    pub.run()

    try:
        while True:
            sleep(randint(1, 5))
            pub.publish(str(uuid.uuid4()))
    except KeyboardInterrupt:
        pub.stop()


if __name__ == "__main__":
    main()
