import argparse
import os


class FileSynchronizer:
    def __init__(self, source_path, target_path, log_path, interval):
        self.source_path = source_path
        self.target_path = target_path
        self.log_path = log_path
        self.interval = interval


def main():
    parser = argparse.ArgumentParser(description="Program requires 4 arguments")

    parser.add_argument("-s", "--source_path", type=str,
                        help="Select the absolute path to the folder you want to back up.", required=True)
    parser.add_argument("-t", "--target_path", default=os.path.abspath(__file__), type=str,
                        help="Select the absolute path to the folder where you want to store backups.", required=False)
    parser.add_argument("-l", "--log_path", default=os.path.abspath(__file__), type=str,
                        help="Select the absolute path to the folder in which you want to store the log.", required=False)
    parser.add_argument("-i", "--interval", default=5, type=int,
                        help="Specify the time interval at which backups will be created (in seconds).", required=False)

    args = parser.parse_args()

    fs = FileSynchronizer(args.source_path, args.target_path, args.log_path, args.interval)
    fs.test()

if __name__ == "__main__":
    main()