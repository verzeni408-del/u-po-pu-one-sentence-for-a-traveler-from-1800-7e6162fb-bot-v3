"""One sentence for a traveler from 1800, in the tongue of his own century.

The internet, as a traveler from 1800 would grasp it: one great post
office with no walls, where any letter finds any door before the ink
dries, and every book ever written waits to be read. Writes the entry
text to /output/entry.txt with no trailing newline.
"""

from pathlib import Path

entry_sentence = "It is one great post office with no walls, where any letter finds any door before the ink dries, and every book ever written waits to be read."

output_path = Path("/output/entry.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(entry_sentence, encoding="utf-8")
