# Facade
class EventManager:

    def __init__(self):
        print("Checking ... ")

    def arrange(self):
        self.presenter = Presenter()
        self.presenter.setPresentation()

        self.theaterGroup = TheaterGroup()
        self.theaterGroup.setTheater()

        self.services = Services()
        self.services.setService()


        self.lecturer = Lecturer()
        self.lecturer.setLecture()

        self.musicGroup = MusicGroup()
        self.musicGroup.setMusic()


# Subsystem (Systems)
class Presenter:

    def __init__(self):
        print("What day is your celebration ?")

    def setPresentation(self):
        print("Wednesday!")

class TheaterGroup:

    def __init__(self):
        print("Be serious or be fun ?")

    def setTheater(self):
        print("Fun!")

class Services:

    def __init__(self):
        print("What should the reception look like ?")

    def setService(self):
        print("Sweets, Orange juice!")


class Lecturer:

    def __init__(self):
        print("What is the topic of the lecture ?")

    def setLecture(self):
        print("What is the diffrence between unuversity and high school ?")

class MusicGroup:

    def __init__(self):
        print("How many songs to play ?")

    def setMusic(self):
        print("Two, Traditional!")



# Client
class You:

    def __init__(self):
        print("There are many things to do celebrate!")

    def askEventManager(self):
        print("I leave everything to the Scientific association!")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("Thank you for doing everything!")


you = You()
you.askEventManager()
