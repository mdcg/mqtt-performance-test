start/publisher-worker:
	poetry run python -m src.application.workers.publisher_worker

start/subscriber-worker:
	poetry run python -m src.application.workers.subscriber_worker
