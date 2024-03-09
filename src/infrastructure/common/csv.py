from csv import DictReader


class CSV:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, "r") as file:
            csv_reader = DictReader(file)
            for row in csv_reader:
                yield row
