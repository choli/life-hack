import os
import xml.etree.ElementTree as ET
from datetime import datetime
import markdown
import yaml

# Paths
PODCAST_FOLDER = "docs/assets/podcast"
FEED_FILE = "docs/feed.xml"
POSTS_DIR = "docs/_posts"

# Get the list of MP3 files
mp3_files = [f for f in os.listdir(PODCAST_FOLDER) if f.endswith(".mp3")]
print("MP3 files:", mp3_files)  # Debugging

# Parse the RSS feed
tree = ET.parse(FEED_FILE)
root = tree.getroot()
channel = root.find("channel")

# Get existing MP3 files in the feed
existing_items = {item.find("link").text for item in channel.findall("item")}

# Add new MP3 files to the feed
for mp3 in mp3_files:
    mp3_url = f"https://choli.github.io/life-hack/assets/podcast/{mp3}"
    if mp3_url not in existing_items:
        # Find the corresponding post
        post_files = os.listdir(POSTS_DIR)
        print("Post files:", post_files)  # Debugging
        post_file = next(
            (f for f in post_files if f.endswith(".markdown") and mp3 in open(os.path.join(POSTS_DIR, f)).read()),
            None,
        )
        if not post_file:
            print(f"No matching post found for {mp3}")
            continue

        # Read the post content
        with open(os.path.join(POSTS_DIR, post_file), "r") as f:
            content = f.read()
            front_matter, post_content = content.split("---", 2)[1:]
            front_matter = yaml.safe_load(front_matter)
            post_description = markdown.markdown(post_content.strip())

        # Create a new RSS item
        item = ET.Element("item")

        title = ET.SubElement(item, "title")
        title.text = front_matter.get("title", f"Episode: {mp3.replace('.mp3', '').title()}")

        description = ET.SubElement(item, "description")
        description.text = post_description

        link = ET.SubElement(item, "link")
        link.text = mp3_url

        guid = ET.SubElement(item, "guid")
        guid.text = mp3_url

        pub_date = ET.SubElement(item, "pubDate")
        pub_date.text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

        enclosure = ET.SubElement(item, "enclosure")
        enclosure.set("url", mp3_url)
        enclosure.set("length", str(os.path.getsize(os.path.join(PODCAST_FOLDER, mp3))))
        enclosure.set("type", "audio/mpeg")

        channel.append(item)

# Save the updated feed
tree.write(FEED_FILE, encoding="utf-8", xml_declaration=True)