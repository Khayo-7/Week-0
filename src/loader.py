import json
import argparse
import os
import glob

# Create wrapper classes for using slack_sdk in place of slacker


class SlackDataLoader:

    """
    Slack exported data IO class.

    When you open slack exported ZIP file, each channel or direct message
    will have its own folder. Each folder will contain messages from the
    conversation, organised by date in separate JSON files.

    You'll see reference files for different kinds of conversations:
    users.json files for all types of users that exist in the slack workspace
    channels.json files for public channels,

    These files contain metadata about the conversations, including their names and IDs.

    For secruity reason, we have annonymized names - the names you will see are generated using faker library.

    """

    def __init__(self, path):

        """
        path: path to the slack exported data folder
        """
        self.path = path

        # Should be removed
        # self.channels = self.get_channels()
        # self.users = self.get_users() # updated the get_ussers to get_users

    def get_users(self):

        """
        write a function to get all the users from the json file
        """
        with open(os.path.join(self.path, "users.json"), "r") as f:
            users = json.load(f)

        return users

    def get_channels(self):

        """
        write a function to get all the channels from the json file
        """
        with open(os.path.join(self.path, "channels.json"), "r") as f:
            channels = json.load(f)

        return channels

    def get_channel_messages(self, channel_name):

        """
        write a function to get all the messages from a channel

        """

        # specify path to get json files
        channel_path = os.path.join(self.path, channel_name)
        # updated
        # edited the path to have a trailing slash
        # for json_file in glob.glob(f"{path_channel}*.json"):
        channel_json_files = glob.glob(f"{channel_path}\\*.json")

        channel_msgs = [json.load(open(json_file)) for json_file in channel_json_files]

        return channel_msgs

    def get_all_channels_messages(self):

        """
        write a function to get all the channels from the json file
        """
        channels = self.get_channels()
        slack_data = {}

        for channel in channels:
            channel_name = channel["name"]
            channel_msgs = self.get_channel_messages(channel_name)
            slack_data[channel_name] = channel_msgs

        return slack_data


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Export Slack history")

    parser.add_argument("--zip", help="Name of a zip file to import")
    args = parser.parse_args()
