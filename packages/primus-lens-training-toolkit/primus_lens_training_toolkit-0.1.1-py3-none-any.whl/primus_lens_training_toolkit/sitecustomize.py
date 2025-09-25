
try:
    import primus_lens_training_toolkit.wandb_wrapper.run as wandb_patch
    wandb_patch.apply_patch()  # 你写一个函数来执行替换
    print("[PrimusLens] W&B hooks applied via sitecustomize")
except Exception as e:
    print(f"[PrimusLens] Failed to apply W&B hooks: {e}")