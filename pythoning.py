"""System module."""
import sys

print("Hello World from Python")

if len(sys.argv) > 1:
    arg = sys.argv[1]
    print(f"Received arg: {arg}")
