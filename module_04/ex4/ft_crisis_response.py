#!/usr/bin/env python3

def crisis_response(file_name: str) -> None:

    print(f"Attempting access to {file_name}...")
    try:
        with open(file_name, "r") as f:
            content = f.read()
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE:  Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as e:
        print(
            f"RESPONSE:  Unexpected error: {e}"
            f"- Type: {type(e).__name__}")
        print("STATUS: Crisis handled")


def main() -> None:
    files = [
        "../standard_archive.txt",
        "../lost_archive.txt",
        "../security_protocols.txt",
        "../is_not_an_archive.txt"
    ]
    for file in files:
        crisis_response(file)
        print()


if __name__ == "__main__":
    main()
