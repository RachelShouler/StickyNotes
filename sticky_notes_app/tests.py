# sticky_notes_app/tests.py
from django.test import TestCase
from sticky_notes_app.models import StickyNotes


class AddNoteTest(TestCase):
    def setUp(self):
        # Create a Post object for testing
        StickyNotes.objects.create(title='Test', content='This is a test.')
        StickyNotes.objects.create(title='Test2', content='Second test.')

    def test_note_has_title(self):
        # Test that a Post object has the expected title
        note = StickyNotes.objects.get(id=1)
        self.assertEqual(note.title, 'Test')

    def test_note_has_content(self):
        # Test that a Post object has the expected content
        note = StickyNotes.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test.')

    def test_delete_note(self):
        # Test that post can be deleted
        note = StickyNotes.objects.get(id=1)
        note.delete()
        # Check if the post with ID 1 is deleted
        self.assertFalse(StickyNotes.objects.filter(id=1).exists())

    def test_view_note(self):
        # Test view of remaining posts
        notes = StickyNotes.objects.all()
        self.assertEqual(len(notes), 2)
