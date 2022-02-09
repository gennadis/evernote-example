import os

from evernote.api.client import EvernoteClient
from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv()
    evernote_personal_token = os.getenv("EVERNOTE_PERSONAL_TOKEN")

    client = EvernoteClient(token=evernote_personal_token, sandbox=True)
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print(f"{notebook.guid} - {notebook.name}")
