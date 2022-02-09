# Evernote API scripts

These scripts covers basic [Evernote](https://evernote.com/) API operations.

## Features
- Get notebooks name and GUID
- Print notes content to terminal
- Create new note from a template

## Getting Evernote API access
1. Sing up to Evernote Developer Sandbox [https://sandbox.evernote.com/](https://sandbox.evernote.com/)
2. Request an Evernote API Key [https://dev.evernote.com/#apikey](https://dev.evernote.com/#apikey)  
IMPORTANT! Select `Full Access` API permissions level to get these scripts working.
3. Get Developer token [https://sandbox.evernote.com/api/DeveloperToken.action](https://sandbox.evernote.com/api/DeveloperToken.action)


## Installation
1. Clone project
```bash
git clone https://github.com/gennadis/evernote-example.git
cd evernote-example
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Rename `.env.example` to `.env` and place your `EVERNOTE_PERSONAL_TOKEN` from step 2 of "Getting Evernote API access" section

## Examples
1. Get notebook names and GUIDs
```bash
python list_notebooks.py
aad4d2aa-4505-4f84-9b83-471e185d25ff - Default notebook
```

2. Dump notes from default notebook
```bash
python dump_inbox.py -- 2
--------- 1 ---------
note1 content

--------- 2 ---------
note2 content
```
Check help section for additional parameters
```bash
python dump_inbox.py --help
```

3. Create new note from a template
```bash
python add_note2journal.py
Title Context is:
{
    "date": "2022-02-09",
    "dow": "среда"
}
Note created: Note random 2121
Done
```
Check help section for additional parameters
```bash
python add_note2journal.py --help
```
