#!/usr/bin/env python3

def read_ancient_text(file_name: str) -> None:
    try:
        f = open(file_name, "r")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' is missing.")
        return
    except PermissionError:
        print(
            f"Error: The file '{file_name}' "
            "does not have permission for reading.")
        return
    content = f.read()
    f.close()
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {file_name}")
    print("Connection established...\n")
    print(content, end="")
    print("\n\nData recovery complete. Storage unit disconnected.")


def main() -> None:
    file_name = "../ancient_fragment.txt"
    read_ancient_text(file_name)


if __name__ == "__main__":
    main()
