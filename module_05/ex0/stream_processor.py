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


def test_numeric_processor() -> None:

    print("\nTesting Numeric Processor...")
    numeric_processor: NumericProcessor = NumericProcessor()
    input_int: int = 42
    print(
        f"Trying to validate input '{input_int}': "
        f"{numeric_processor.validate(input_int)}"
    )
    input_str: str = "Hello"
    print(
        f"Trying to validate input '{input_str}': "
        f"{numeric_processor.validate(input_str)}"
    )
    input_str_foo: str = "Foo"
    print(
        f"Test invalid ingestion of string '{input_str_foo}' "
        "without prior validation:"
    )
    try:
        numeric_processor.ingest(input_str_foo)
    except ValueError as e:
        print(f"Got exception: {e}")
    input_number_list: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {input_number_list}")
    numeric_processor.ingest(input_number_list)
    print("Extracting 3 values...")
    index: int
    value: str
    for _ in range(3):
        try:
            index, value = numeric_processor.output()
            print(f"Numeric value {index}: {value}")
        except ValueError as e:
            print(f"Got exception: {e}")
            break


def test_text_processor() -> None:

    print("\nTesting Text Processor...")
    text_processor: TextProcessor = TextProcessor()
    input_int: int = 42
    print(
        f"Trying to validate input '{input_int}': "
        f"{text_processor.validate(input_int)}"
    )
    input_string_list = ['Hello', 'Nexus', 'World']
    print(f"Processing data: {input_string_list}")
    try:
        text_processor.ingest(input_string_list)
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Extracting 1 value...")
    index: int
    value: str
    for _ in range(1):
        try:
            index, value = text_processor.output()
            print(f"Text value {index}: {value}")
        except ValueError as e:
            print(f"Got exception: {e}")
            break


def test_log_processor() -> None:

    print("\nTesting Log Processor...")
    log_processor: LogProcessor = LogProcessor()
    input_str: str = "Hello"
    print(
        f"Trying to validate input '{input_str}': "
        f"{log_processor.validate(input_str)}"
    )
    input_list_dict: List[Dict[str, str]] = [
            {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    try:
        log_processor.ingest(input_list_dict)
    except ValueError as e:
        print(f"Got exception: {e}")
    print(f"Processing data: {input_list_dict}")
    print("Extracting 2 values...")
    index: int
    value: str
    for _ in range(2):
        try:
            index, value = log_processor.output()
            print(f"Log entry {index}: {value}")
        except ValueError as e:
            print(f"Got exception: {e}")
            break


def main() -> None:
    print("== Code Nexus - Data Processor ===")
    test_numeric_processor()
    test_text_processor()
    test_log_processor()


if __name__ == "__main__":
    main()
