from rich.console import Console
import csv
from collections import Counter
import yt_dlp
from os import path


class Channel:

    def __init__(self, channel_url):
        self.channel_url = channel_url
        self.videos_info = self.get_videos_info()
        self.video_titles = [entry["title"] for entry in self.videos_info["entries"]]

    def get_videos_info(self):
        ydl_opts = {
            "extract_flat": True,  # don't download videos
            "dump_single_json": True,
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(self.channel_url, download=False)

        titles = [entry["title"] for entry in info["entries"]]
        substring = self.find_frequent_substring(titles=titles)
        for indx, entry in enumerate(info["entries"]):
            # self.titles[indx] = title.replace(substring, "").strip()
            if substring in entry["title"]:
                info["entries"][indx]["substring"] = substring

        return info

    def find_frequent_substring(self, titles, min_len=3, threshold=0.8):
        substr_counts = Counter()
        n_titles = len(titles)

        # Build substring frequency counts
        for title in titles:
            words = title.split()
            for i in range(len(words)):
                for j in range(
                    i + 1, min(i + 4, len(words) + 1)
                ):  # up to 3-word substrings
                    phrase = " ".join(words[i:j])
                    if len(phrase) >= min_len:
                        substr_counts[phrase] += 1

        # Pick the most frequent substring over threshold
        for phrase, freq in substr_counts.most_common():
            if freq >= threshold * n_titles:
                return phrase
        return ""


def compare_titles(main_channel_info, theft_channel_info):
    rows = []
    for original_entry in main_channel_info["entries"]:
        for theft_entry in theft_channel_info["entries"]:
            try:
                theft_video_name = (
                    theft_entry["title"].replace(theft_entry["substring"], "").strip()
                )
            except KeyError:
                theft_video_name = theft_entry["title"].strip()
            if original_entry["title"] == theft_video_name:
                rows.append(
                    {
                        "Original Video Title": original_entry["title"],
                        "Original Video Link": original_entry["url"],
                        "Imposter Video Title": theft_entry["title"],
                        "Imposter Video Link": theft_entry["url"],
                    }
                )

    return rows


def main():
    console = Console()
    main_channel_url = console.input("Please enter the video url of your channel: ")
    theft_channel_url = console.input(
        "Please enter the video url of the channel that stole your content: "
    )

    console.print("Fetching your video titles...")
    main_channel = Channel(channel_url=main_channel_url)

    console.print("Fetching thief's video titles...")
    theft_channel = Channel(channel_url=theft_channel_url)

    console.print("Comparing titles...")
    rows = compare_titles(
        main_channel_info=main_channel.videos_info,
        theft_channel_info=theft_channel.videos_info,
    )
    csv_file = "theft_documentation.csv"
    with open(csv_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Original Video Title",
                "Original Video Link",
                "Imposter Video Title",
                "Imposter Video Link",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    console.print(f"Finished! Your file is saved at {path.abspath(csv_file)}")


if __name__ == "__main__":
    main()
