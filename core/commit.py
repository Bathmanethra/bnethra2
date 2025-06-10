import os
import json
import hashlib
from datetime import datetime

def create_commit(message):
    if not os.path.exists(".vcs"):
        print("❌ Run 'init' first.")
        return

    snapshot = {}

    for file in os.listdir():
        if file in [".vcs", "cli.py"]:
            continue

        if os.path.isfile(file):
            try:
                # Try reading with UTF-8
                with open(file, "r", encoding="utf-8") as f:
                    snapshot[file] = f.read()
            except UnicodeDecodeError:
                try:
                    # Fallback for Windows encoding
                    with open(file, "r", encoding="cp1252") as f:
                        snapshot[file] = f.read()
                except Exception as e:
                    print(f"⚠️ Skipped {file} (unreadable: {e})")
            except Exception as e:
                print(f"⚠️ Skipped {file} (unexpected error: {e})")

    if not snapshot:
        print("⚠️ No valid text files to commit.")
        return

    content = json.dumps(snapshot, sort_keys=True)
    commit_id = hashlib.sha256((content + message).encode()).hexdigest()

    commit_data = {
        "id": commit_id,
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "files": snapshot
    }

    os.makedirs(".vcs/commits", exist_ok=True)

    with open(f".vcs/commits/{commit_id}.json", "w", encoding="utf-8") as f:
        json.dump(commit_data, f)

    log_path = ".vcs/log.json"
    try:
        with open(log_path, "r", encoding="utf-8") as f:
            log = json.load(f)
    except:
        log = []

    log.append(commit_id)

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, indent=2)

    print(f"✅ Commit saved: {commit_id[:7]}")
