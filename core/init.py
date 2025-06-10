import os
import json

def init_repo():
    try:
        if not os.path.exists(".vcs"):
            os.makedirs(".vcs/commits", exist_ok=True)
            with open(".vcs/log.json", "w", encoding="utf-8") as f:
                json.dump([], f)
            print("✅ VCS initialized.")
        else:
            print("⚠️ VCS already initialized.")
    except Exception as e:
        print(f"❌ Init failed: {e}")
