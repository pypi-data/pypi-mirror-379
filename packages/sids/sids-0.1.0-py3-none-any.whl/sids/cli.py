"""SIDS Command Line Interface."""
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: sids <init|run>")
        return
    cmd = sys.argv[1]
    if cmd == "init":
        print("Initializing Tailwind config...")
    elif cmd == "run":
        print("Running SIDS demo app...")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
