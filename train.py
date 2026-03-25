import mlflow
import os
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"]) 

with mlflow.start_run() as run:
    accuracy = 0.9

    mlflow.log_metric("accuracy", accuracy)

    with open("model_info.txt", "w") as f:
        f.write(run.info.run_id)

    with open("accuracy.txt", "w") as f:
        f.write(str(accuracy))

    print(f"RUN_ID={run.info.run_id}")