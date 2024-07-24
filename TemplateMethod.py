from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self):
        self._read_data()
        self._process_data()
        self._save_data()

    @abstractmethod
    def _read_data(self):
        print("//////1//////")

    @abstractmethod
    def _process_data(self):
        print("//////2//////")

    @abstractmethod
    def _save_data(self):
        print("//////3//////")

class JsonProcessor(DataProcessor):
    def _read_data(self):
        print("Json Processor read data")

    def _process_data(self):
        print("Json Processor processed data")

    def _save_data(self):
        print("Json Processor saved data")


class CSVProcessor(DataProcessor):
    def _read_data(self):
        print("CSV Processor read data")

    def _process_data(self):
        print("CSV Processor processed data")

    def _save_data(self):
        print("CSV Processor saved data")


processor = JsonProcessor()
processor.process()
