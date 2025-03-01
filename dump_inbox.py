import argparse
import os

from evernote.api.client import EvernoteClient
from evernote.api.client import NoteStore
from bs4 import BeautifulSoup
from dotenv import load_dotenv


def get_notebook_list(note_store, notebook_guid, number=10, offset=0):
    _filter = NoteStore.NoteFilter(notebookGuid=notebook_guid)
    resultSpec = NoteStore.NotesMetadataResultSpec(
        includeTitle=True,
        includeContentLength=True,
        includeCreated=True,
        includeUpdated=True,
        includeDeleted=False,
        includeUpdateSequenceNum=True,
        includeNotebookGuid=False,
        includeTagGuids=True,
        includeAttributes=True,
        includeLargestResourceMime=True,
        includeLargestResourceSize=True,
    )

    # this determines which info you'll get for each note
    return note_store.findNotesMetadata(_filter, offset, number, resultSpec)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dumps notes from Evernote inbox to console"
    )
    parser.add_argument(
        dest="number",
        nargs="?",
        type=int,
        default=10,
        help="number of records to dump",
    )
    args = parser.parse_args()

    load_dotenv()
    evernote_personal_token = os.getenv("EVERNOTE_PERSONAL_TOKEN")
    inbox_notebook_guid = os.getenv("INBOX_NOTEBOOK_GUID")

    client = EvernoteClient(token=evernote_personal_token, sandbox=True)
    note_store = client.get_note_store()

    notes = get_notebook_list(note_store, inbox_notebook_guid, args.number).notes

    for counter, note in enumerate(notes, start=1):
        print(f"\n--------- {counter} ---------")
        content = note_store.getNoteContent(
            note.guid
        )  # kwargs will be skipped by api because of bug
        soup = BeautifulSoup(content, "html.parser")
        print(soup.get_text())
