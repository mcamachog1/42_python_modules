#!/usr/bin/env python3

def read_file(file_name: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    try:
        with open(file_name, "r+") as f:
            print("Vault connection established with failsafe protocols\n")
            content = f.read()
            if content:
                print("SECURE EXTRACTION:")
                print(content)
            else:
                print("[WARNING] Vault is empty. No data recovered.")
            print("\nSECURE PRESERVATION:")
            f.write("\n[CLASSIFIED] New security protocols archived")
            print("[CLASSIFIED] New security protocols archived")
            print("Vault automatically sealed upon completion\n")
    except FileNotFoundError:
        print(f"[ERROR] Vault {file_name} not found.")
    except Exception as e:
        print(f"Unexpected Error: {e}")
    print("All vault operations completed with maximum security.")


def main() -> None:
    file_name = "../classified_data.txt"
    read_file(file_name)


if __name__ == "__main__":
    main()
