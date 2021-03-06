import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 5)
        self.guest = Guest("Carole Singer", 30.00)
        self.song = Song("You Can't Stop the Beat", "Hairspray")
    
    def test_room_has_room_number(self):
        self.assertEqual(1, self.room.room_number)
    
    def test_room_guests_list_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_can_check_in_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual(1, len(self.room.guests))
    
    def test_room_can_check_out_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_out_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))
    
    def test_room_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))
    
    def test_room_can_add_song_to_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.assertEqual(1, len(self.room.playlist))
    
    def test_room_can_remove_song_from_playlist(self):
        self.room.add_song_to_playlist(self.song)
        self.room.remove_song_from_playlist(self.song)
        self.assertEqual(0, len(self.room.playlist))
    
    def test_room_check_capacity(self):
        self.room.check_capacity()
        self.assertEqual(5, self.room.capacity)
    
    def test_room_can_check_number_guests_checked_in(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_occupancy()
        self.assertEqual(2, len(self.room.guests))

    def test_room_can_turn_down_guest(self):
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.room.check_in_guest(self.guest)
        self.assertEqual(f"Sorry, this room cannot accomodate more than {self.room.capacity} guests. Try another room.", self.room.check_in_guest(self.guest))
    
    def test_room_can_welcome_guest(self):
        self.room.check_in_guest(self.guest)
        self.assertEqual("Welcome! Enjoy your time.", self.room.check_in_guest(self.guest))
