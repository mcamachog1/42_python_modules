#!/usr/bin/env python3

from typing import (
    Any,
    List,
    Tuple,
    Union,
    Dict,
    Protocol,
    runtime_checkable
)
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


@runtime_checkable
class ExportPlugin(Protocol):

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        ...


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
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            print(f"{proc.__class__.__name__}: "
                  f"total {proc.counter} items processed, "
                  f"remaining {len(proc.data_store)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        output_data: List[Tuple[int, str]] = []
        for proc in self.processors:
            for _ in range(min(nb, len(proc.data_store))):
                output_data.append(proc.output())
            plugin.process_output(output_data)
            output_data.clear()


# PLUGINS
class JSONPlugin():

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        json_data: Dict[str, str] = {}
        print("JSON Output:")
        for item in data:
            id: str = f"item_{item[0]}"
            json_data[id] = item[1]
        print(json_data)


class CSVPlugin():

    def process_output(self, data: List[Tuple[int, str]]) -> None:
        csv_data: List[str] = []
        print("CSV Output:")
        for item in data:
            csv_data.append(item[1])
        print(",".join(csv_data))


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors")
    data_stream.register_processor(NumericProcessor())
    data_stream.register_processor(TextProcessor())
    data_stream.register_processor(LogProcessor())

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
    print(f"\nSend first batch of data on stream: {first_batch}")
    data_stream.process_stream(first_batch)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin")
    data_stream.output_pipeline(3, CSVPlugin())
    data_stream.print_processors_stats()

    second_batch: List[Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR', 'log_message': '500 server crash'},
            {
                'log_level': 'NOTICE',
                'log_message': 'Certificate expires in 10 days'
            }
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]
    print(f"\nSend another batch of data: {second_batch}")
    data_stream.process_stream(second_batch)
    data_stream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin")
    data_stream.output_pipeline(5, JSONPlugin())
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
