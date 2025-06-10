import argparse
from core import init, commit, log

def main():
    parser = argparse.ArgumentParser(description="Simple VCS")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("init", help="Initialize VCS")

    commit_parser = subparsers.add_parser("commit", help="Create a commit")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")

    subparsers.add_parser("log", help="Show commit logs")

    args = parser.parse_args()

    if args.command == "init":
        init.init_repo()
    elif args.command == "commit":
        commit.create_commit(args.message)
    elif args.command == "log":
        log.show_log()
    else:
        print("❌ Invalid command")

if __name__ == "__main__":
    main()
