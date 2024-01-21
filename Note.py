from datetime import datetime


class Note:
    def __init__(self, note_id, title, body):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.creation_time = datetime.now()
        self.last_modified_time = datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.last_modified_time = datetime.now()

    def to_dict(self):
        return {
            'note_id': self.note_id,
            'title': self.title,
            'body': self.body,
            'creation_time': str(self.creation_time),
            'last_modified_time': str(self.last_modified_time)
        }