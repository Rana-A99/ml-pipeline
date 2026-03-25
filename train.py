import mlflow
import random

mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    accuracy = random.uniform(0.7, 0.95)

    mlflow.log_metric("accuracy", accuracy)

    print(f"Accuracy: {accuracy}")
    print(f"RUN_ID={run.info.run_id}")