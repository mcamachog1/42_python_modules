#!/usr/bin/env python3


def exist_file(file_name: str) -> bool:
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        return False
    f.close()
    return True


def create_file(file_name: str) -> None:
    if exist_file(file_name):
        print(
            f"The file '{file_name}' already exists,"
            "it will be overwritten.")
    print(f"Initializing new storage unit: {file_name}")
    try:
        f = open(file_name, "w")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        return
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    message_list = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]
    try:
        for message in message_list:
            print(message)
            f.write(message + "\n")
        print(
            "\nData inscription complete. Storage unit sealed.\n"
            f"Archive '{file_name}' ready for long-term preservation.")
    except Exception as e:
        print(f"An error occurred during data inscription: {e}")
    finally:
        f.close()
        return


def main() -> None:
    file_name = "../new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_file(file_name)


if __name__ == "__main__":
    main()
