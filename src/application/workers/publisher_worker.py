from time import sleep

from src.application.services.publisher import Publisher
from src.infrastructure.logging import Logger
from src.infrastructure.common.csv import CSV
from json import dumps

logger = Logger("Publisher Worker")


def main():
    csv = CSV(file_path="/home/mdcg/Development/Projects/mqtt-performance-test/payload.csv")
    pub = Publisher()
    pub.run()

    try:
        while True:
            sleep(1)
            for row in csv.read():
                pub.publish(dumps(row))
    except KeyboardInterrupt:
        pub.stop()


if __name__ == "__main__":
    main()
