#!/usr/bin/env python 
from datetime import date, datetime, timedelta
import argparse
import json
import os

from evernote.api.client import EvernoteClient
from dotenv import load_dotenv


WEEK_DAYS = {
    1: u'понедельник',
    2: u'вторник',
    3: u'среда',
    4: u'четверг',
    5: u'пятница',
    6: u'суббота',
    7: u'воскресенье',
}


def is_valid_date(text):
    text = text.strip()
    if text.startswith('-') or text.startswith('+') or text.isdigit():
        return date.today() + timedelta(days=int(text))
    try:

        return datetime.strptime(text, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(text)
        raise argparse.ArgumentTypeError(msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=u'Adds note to notebook "Дневник", uses template note')
    parser.add_argument('date',
                        nargs='?',
                        type=is_valid_date,
                        help='date in format "YYYY-MM-DD"')
    args = parser.parse_args()

    load_dotenv()
    evernote_personal_token = os.getenv('EVERNOTE_PERSONAL_TOKEN')
    journal_template_note_guid = os.getenv('JOURNAL_TEMPLATE_NOTE_GUID')
    journal_notebook_guid = os.getenv('JOURNAL_NOTEBOOK_GUID')

    client = EvernoteClient(
        token=evernote_personal_token,
        sandbox=False # Default: True
    )
    noteStore = client.get_note_store()

    day = args.date or date.today()
    context = {
        'date': day.isoformat(),
        'dow': WEEK_DAYS[day.isoweekday()],
    }
    print('Title Context is:')
    print(json.dumps(context, ensure_ascii=False, indent=4))

    new_note = noteStore.copyNote(journal_template_note_guid, journal_notebook_guid)
    utitle_without_comment = new_note.title.decode('utf8').split('#', 1)[0]
    utitle = utitle_without_comment.strip().format(**context)
    new_note.title = utitle.encode('utf8')
    noteStore.updateNote(new_note)
    
    print(u'Note created: %s' % utitle)
    print('Done')
