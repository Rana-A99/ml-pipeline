import mlflow

mlflow.set_tracking_uri("file:./mlruns")

with mlflow.start_run() as run:
    accuracy = 0.7  

    mlflow.log_metric("accuracy", accuracy)

    with open("accuracy.txt", "w") as f:
        f.write(str(accuracy))

    print(f"RUN_ID={run.info.run_id}")