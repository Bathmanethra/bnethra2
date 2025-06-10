import os
import json

def show_log():
    log_path = ".vcs/log.json"
    if not os.path.exists(log_path):
        print("❌ No commits yet.")
        return

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            log = json.load(f)
    except:
        print("❌ Couldn't read log.")
        return

    if not log:
        print("📭 No commits found.")
        return

    for commit_id in log:
        try:
            with open(f".vcs/commits/{commit_id}.json", "r", encoding="utf-8") as f:
                commit = json.load(f)
            print(f"🔹 Commit: {commit['id'][:7]}")
            print(f"📅 Date:   {commit['timestamp']}")
            print(f"📝 Msg:    {commit['message']}")
            print("-" * 30)
        except:
            print(f"⚠️ Failed to read commit: {commit_id}")
