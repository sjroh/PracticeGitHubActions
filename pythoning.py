import sys

print("Hello World from Python")

if len(sys.argv) > 1:
    arg = sys.argv[1]
    print(f"Received arg: {arg}")

# TODO: Print out message when there is no argument to process
