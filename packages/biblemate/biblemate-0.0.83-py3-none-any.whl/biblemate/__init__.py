from agentmake import AGENTMAKE_USER_DIR
from pathlib import Path
import os

AGENTMAKE_CONFIG = {
    "print_on_terminal": False,
    "word_wrap": False,
}
OLLAMA_NOT_FOUND = "`Ollama` is not found! BibleMate AI uses `Ollama` to generate embeddings for semantic searches. You may install it from https://ollama.com/ so that you can perform semantic searches of the Bible with BibleMate AI."
BIBLEMATEDATA = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "data")
if not os.path.isdir(BIBLEMATEDATA):
    Path(BIBLEMATEDATA).mkdir(parents=True, exist_ok=True)
def fix_string(content):
    return content.replace(" ", " ").replace("‑", "-")