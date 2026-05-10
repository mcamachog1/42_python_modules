#!/usr/bin/env python3

from typing import Any, List, Tuple, Union, Dict
from abc import ABC, abstractmethod


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.data_store: list[Tuple[int, str]] = []
        self.counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data_store:
            raise ValueError("No data available")

        item = self.data_store.pop(0)  # FIFO
        return item


class NumericProcessor(DataProcessor):

    def validate(
            self,
            data: Union[int, float, List[int], List[float]]) -> bool:

        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            try:
                [float(item) for item in data]
                return True
            except (ValueError, TypeError):
                return False

        return False

    def ingest(
            self,
            data: Union[int, float, List[int], List[float]]) -> None:

        if self.validate(data):
            if isinstance(data, (int, float)):
                self.data_store.append((self.counter, str(data)))
                self.counter += 1
            if isinstance(data, list):
                for item in data:
                    self.data_store.append((self.counter, str(item)))
                    self.counter += 1
        else:
            raise ValueError(
                    "Improper numeric data"
            )


class TextProcessor(DataProcessor):
    def validate(
            self,
            data: Union[str, List[str]]) -> bool:

        if isinstance(data, str):
            return True

        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True

        return False

    def ingest(
            self,
            data: Union[str, List[str]]) -> None:

        if self.validate(data):
            if isinstance(data, (str)):
                self.data_store.append((self.counter, data))
                self.counter += 1
            if isinstance(data, list):
                for item in data:
                    self.data_store.append((self.counter, item))
                    self.counter += 1
        else:
            raise ValueError(
                    "Improper text data"
            )


class LogProcessor(DataProcessor):

    def validate(
            self,
            data: Union[Dict[str, str], List[Dict[str, str]]]) -> bool:

        result: bool = True

        # Auxiliar function
        def is_valid_dict(data: Dict[Any, Any]) -> bool:
            if isinstance(data, dict):
                return all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items()
                )
            else:
                return False

        if isinstance(data, list):
            try:
                for item in data:
                    if not is_valid_dict(item):
                        result = False
                        break
                return result
            except (ValueError, TypeError):
                return False

        if isinstance(data, dict):
            return is_valid_dict(data)

        return False

    def ingest(
            self,
            data: Union[Dict[str, str], List[Dict[str, str]]]) -> None:

        # Auxiliar function
        def ingest_dict(data: Dict[str, str]) -> None:
            list_items: List[str] = []
            for v in data.values():
                list_items.append(v)
            str_items: str = ": ".join(list_items)
            self.data_store.append((self.counter, str_items))
            self.counter += 1

        if self.validate(data):
            if isinstance(data, list):
                for item in data:
                    ingest_dict(item)

            if isinstance(data, dict):
                ingest_dict(data)
        else:
            raise ValueError("Improper log data")


class DataStream():
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for item in stream:
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    break
            else:
                print(
                    "DataStream error - Can't process element "
                    f"in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.__class__.__name__}: "
                  f"total {proc.counter} items processed, "
                  f"remaining {len(proc.data_store)} on processor")


def main() -> None:

    print("=== Code Nexus - Data Stream ===")

    print("\nInitialize Data Stream...")
    data_stream: DataStream = DataStream()
    data_stream.print_processors_stats()
    print("\nRegistering Numeric Processor\n")
    data_stream.register_processor(NumericProcessor())
    first_batch: List[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User wil is connected'
            }
        ],
        42,
        ['Hi', 'five']
    ]
    print(f"Send first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors\n")
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())
    print("Send the same batch again")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()
    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        data_stream.processors[0].output()
    for _ in range(2):
        data_stream.processors[1].output()
    data_stream.processors[2].output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
