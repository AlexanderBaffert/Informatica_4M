#Baffert Alexander 4M Es16


#Inizio delle Classi
class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    # def create_playlist(self):
    #     return print(f"The playlist, {} is created")
    def __str__ (self) -> str:
        return f"user: {self.username}, email: {self.email}"
    
class Subscription:
    def __init__(self,type,price):
        self.type=type
        self.price=price
        self.users=[]
    def add_users(self, user):
        self.users.append(user)
    def list_user(self):
        print(f"The users in {self.type}, paying {self.price}$/m are: ")
        for i in self.users:
            print(i)
class Playlist:
    def __init__(self,name) -> None:
        self.name=name
class Songs:
    def __init__(self,title,duration) -> None:
        self.title=title
        self.duration=duration
    def __str__(self) -> str:
        return f"title: {self.title}, duration:{self.duration}"
class Album:
    def __init__(self,title) -> None:
            self.title=title
            self.songs=[]
    def add_song(self,song):
        self.songs.append(song)
    def contains_songs(self):
        print(f"The songs in the Album are:")
        for i in self.songs:
            print(i)
    def __init__(self) -> None:
        return f"The Artist have "
class Artist:
    def __init__(self,name) -> None:
        self.name=name
    def create_album(self):
        return print(f"The Album, {self.name} is created")
class PremiumAlbum:
    def __init__(self,exlusive_content) -> None:
        self.exclusive_content=exlusive_content
#Main
#User -- Playlist
user1 = User("fade","@gmail.com")
#Album -- Songs
album1=Album("Ed sheeran")
song1=Songs("Shape of you",3.58)
song2=Songs("Shape of you",3.58)
song3=Songs("Shape of you",3.58)
album1.add_song(song1)
album1.contains_songs()
#User -- Subscription
sub=Subscription("Patreon",10)
sub.add_users(user1)
sub.list_user()
#Artist -- Album
