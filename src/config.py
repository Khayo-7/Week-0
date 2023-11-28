from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description="cmdArgs")
parser.add_argument(
    "--output",
    type=str,
    default="slack_data.csv",
    help="filename to write analysis output in CSV format",
)
parser.add_argument(
    "--path", required=True, type=str, help="directory where slack data reside"
)
parser.add_argument("--channel", type=str, default="", help="which channel we parsing")
parser.add_argument(
    "--userfile", type=str, default="users.json", help="users profile information"
)

cfg = parser.parse_args()
# print(cfg)

# BASE_DIR = r"C:\Users\Frost\Videos\Git\10-Academy\Week-0"
# dataset_path = r"datasets\Anonymized_B6SlackExport_25Nov23\anonymized"
