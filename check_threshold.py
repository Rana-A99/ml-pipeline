import sys

with open("accuracy.txt", "r") as f:
    accuracy = float(f.read())

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    print(" Failed")
    sys.exit(1)
else:
    print(" Passed")