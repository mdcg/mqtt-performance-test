from src.application.services.subscriber import Subscriber
from src.infrastructure.logging import Logger

logger = Logger("Subscriber Worker")


def main():
    logger.info("Initializing...")
    Subscriber().run()


if __name__ == "__main__":
    main()
