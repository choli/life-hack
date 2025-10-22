import os
import subprocess

def test_update_feed():
    # Ensure the feed file exists
    feed_file = "docs/feed.xml"
    assert os.path.exists(feed_file), "Feed file does not exist."

    # Ensure the podcast folder exists
    podcast_folder = "docs/assets/podcast"
    assert os.path.exists(podcast_folder), "Podcast folder does not exist."

    # Ensure the posts folder exists
    posts_folder = "docs/_posts"
    assert os.path.exists(posts_folder), "Posts folder does not exist."

    # Run the update_feed script
    result = subprocess.run(["python", "scripts/update_feed.py"], capture_output=True, text=True)
    assert result.returncode == 0, f"Script failed with error: {result.stderr}"

    # Check if the feed file was updated
    with open(feed_file, "r") as f:
        feed_content = f.read()
        assert "<item>" in feed_content, "No items found in the feed."

    print("All tests passed.")

if __name__ == "__main__":
    test_update_feed()