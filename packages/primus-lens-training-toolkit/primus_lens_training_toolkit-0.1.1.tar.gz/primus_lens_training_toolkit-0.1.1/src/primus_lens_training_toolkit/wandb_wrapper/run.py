import os
import json
import wandb


RANK = int(os.environ.get("RANK", "0"))
DUMP_FLAG = os.environ.get("PRIMUS_LENS_WANDB_DUMP", "0") == "1"
LOG_DIR = "/training/log"
LOG_PATH = os.path.join(LOG_DIR, f"{RANK}.jsonl")


ARTIFACT_DIR = "/training/artifact"

ARTIFACT_PATH = os.path.join(ARTIFACT_DIR, f"{RANK}.json")




def apply_patch():

    _original_log = wandb.sdk.wandb_run.Run.log
    _original_log_artifact = wandb.sdk.wandb_run.Run.log_artifact

    try:
        os.makedirs(ARTIFACT_DIR, exist_ok=True)
    except OSError as e:
        print("[PrimusLens][Wandb Wrapper]Failed to create artifact directory")

    try:
        os.makedirs(LOG_DIR, exist_ok=True)
    except OSError as e:
        print("[PrimusLens][Wandb Wrapper]Failed to create log directory")

    def log_with_local_dump(self, *args, **kwargs):
        result = _original_log(self, *args, **kwargs)

        if DUMP_FLAG:
            step = kwargs.get("step")
            data = args[0] if args else kwargs.get("data", {})

            if not isinstance(data, dict):
                data = {"value": data}

            record = {"step": step, **data}

            with open(LOG_PATH, "a", encoding="utf-8") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        return result


    def log_artifact_with_local_dump(self, artifact, *args, **kwargs):
        result = _original_log_artifact(self, artifact, *args, **kwargs)

        if DUMP_FLAG:
            try:
                # 获取 artifact 信息
                record = {
                    "name": getattr(artifact, "name", None),
                    "type": getattr(artifact, "type", None),
                    "metadata": getattr(artifact, "metadata", None),
                    "description": getattr(artifact, "description", None),
                    "aliases": getattr(artifact, "aliases", None),
                }

                # 如果文件存在，先读
                if os.path.exists(ARTIFACT_PATH):
                    with open(ARTIFACT_PATH, "r", encoding="utf-8") as f:
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError:
                            data = []
                else:
                    data = []

                # 追加
                data.append(record)

                # 覆盖写入
                with open(ARTIFACT_PATH, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

            except Exception as e:
                print(f"[PrimusLens] Failed to dump artifact: {e}")

        return result
    wandb.sdk.wandb_run.Run.log_artifact = log_artifact_with_local_dump
    wandb.sdk.wandb_run.Run.log = log_with_local_dump