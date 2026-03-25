import mlflow
import sys

mlflow.set_tracking_uri("file:./mlruns")

with open("model_info.txt", "r") as f:
    run_id = f.read().strip()

run = mlflow.get_run(run_id)
accuracy = float(run.data.metrics["accuracy"])

print(f"Accuracy: {accuracy}")

if accuracy < 0.85:
    print("❌ Accuracy below threshold")
    sys.exit(1)
else:
    print("✅ Accuracy OK")
    