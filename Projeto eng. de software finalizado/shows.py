class Show:  # Renomeado para 'Show'
    def __init__(self, banda, data, local):
        self.banda = banda
        self.data = data
        self.local = local

class ListaDeShows:
    def __init__(self):
        self.shows = []

    def adicionar_show(self, show):
        self.shows.append(show)

    def listar_shows(self):
        return [(show.banda, show.data, show.local) for show in self.shows]
