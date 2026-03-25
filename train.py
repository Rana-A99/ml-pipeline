import os
import mlflow

uri = os.environ.get("MLFLOW_TRACKING_URI", "file:./mlruns")
mlflow.set_tracking_uri(uri)

with mlflow.start_run() as run:
    accuracy = 0.9

    mlflow.log_metric("accuracy", accuracy)

    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)

    with open("accuracy.txt", "w") as f:
        f.write(str(accuracy))

    print(f"RUN_ID={run.info.run_id}")