class Track:

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def show(self):
        print(f'{self.name} - {self.duration} мин')

class Album:

    def __init__(self, groop_name, album_name):
        self.groop_name = groop_name
        self.album_name = album_name
        self.track_list = []

    def get_tracks(self):
        print(f'Группа {self.groop_name} альбом {self.album_name}:')
        for track in self.track_list:
            track.show()

    def add_track(self, Track):
        self.track_list.append(Track)

    def get_duration(self):
        album_duration = sum([track.duration for track in self.track_list])
        print(f'Длительность альбома {self.album_name}: {album_duration} мин')

enter_shikari = Track('Enter Shikari', 3)
mothership = Track('Mothership', 4)
labyrinth = Track('Labyrinth', 4)

nightbound = Track('Nightbound', 5)
lacrimosa = Track('Lacrimosa', 7)
purgatorio = Track('Purgatorio', 4)

numb = Track('Numb', 3)
faint = Track('Faint', 3)
dont_stay = Track('Don\'t Stay', 3)

take_to_the_skies = Album('Enter Shikari', 'Take to the Skies')
down_below = Album('Tribulation', 'Down Below')
meteora = Album('Linkin Park', 'Meteora')

take_to_the_skies.add_track(enter_shikari)
take_to_the_skies.add_track(mothership)
take_to_the_skies.add_track(labyrinth)

down_below.add_track(nightbound)
down_below.add_track(lacrimosa)
down_below.add_track(purgatorio)

meteora.add_track(numb)
meteora.add_track(faint)
meteora.add_track(dont_stay)

down_below.get_duration()
take_to_the_skies.get_duration()
meteora.get_duration()