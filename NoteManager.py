import json
import os

from Note import Note


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        note = Note(note_id, title, body)
        self.notes.append(note)
        return note

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note.update(title, body)
            return True
        return False

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            return True
        return False

    def list_notes(self):
        return [note.to_dict() for note in self.notes]

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.list_notes(), file, indent=2)

    def load_from_json(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.notes = [Note(
                    note['note_id'],
                    note['title'],
                    note['body']
                ) for note in data]