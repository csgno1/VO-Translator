# Before running this script...
# pip3 install langdetect googletrans==4.0.0-rc1
#

from langdetect import detect
from googletrans import Translator
import time

log_file = "chat.log"
out_file = "chat_translated.log"

translator = Translator()
seen_lines = set()

while True:
    with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    with open(out_file, "a", encoding="utf-8") as out:
        for line in lines:
            if line in seen_lines or not line.strip():
                continue

            seen_lines.add(line)

            try:
                lang = detect(line)
            except:
                continue

            if lang != "en":
                translation = translator.translate(line, dest="en")
                out.write(f"[{lang}] {line.strip()}\n")
                out.write(f"→ {translation.text}\n\n")

    time.sleep(2)  # check every 2 seconds
