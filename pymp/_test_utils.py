PRAGMA_FOREIGN_KEYS = """PRAGMA foreign_keys = ON"""
CREATE_LEVELS_TABLE = """CREATE TABLE levels
                             (id INTEGER PRIMARY KEY NOT NULL,
                              desc TEXT NOT NULL)"""
CREATE_PEOPLE_TABLE = """CREATE TABLE people
                             (id INTEGER PRIMARY KEY NOT NULL,
                              name TEXT NOT NULL,
                              email TEXT NOT NULL,
                              level INTEGER NOT NULL,
                              manager INTEGER,
                              FOREIGN KEY(level) REFERENCES levels(id),
                              FOREIGN KEY(manager) REFERENCES people(id));"""
INSERT_PEOPLE = """INSERT INTO people VALUES (?, ?, ?, ?, ?)"""
INSERT_LEVELS = """INSERT INTO levels VALUES (?, ?)"""
LEVEL_DATA = [(1, "New Analyst"), (2, "Analyst"), (3, "Senior Analyst"),
              (4, "Consultant"), (5, "Senior Consultant"),
              (6, "Lead Consultant"), (7, "Principal Consultant"),
              (8, "Managing Principal"), (9, "Director")]
PEOPLE_DATA = [(1, 'Mick Manager', 'mick.manager@test.com', 4, 1),
               (2, 'Toby Tester', 'toby.tester@test.com', 3, 1)]
SELECT_TESTER = """SELECT * FROM people WHERE people.id == 2"""


class Person(object):
    def __init__(self, id, name, email, level, manager):
        self.id = id
        self.name = name
        self.email = email
        self.level = level
        self.manager = manager

    def __eq__(self, other):
        return isinstance(other, Person) and (
            self.id == other.id and self.name == other.name
            and self.email == other.email and self.level == other.level
            and self.manager == other.manager)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return ''.join(["{id:", str(self.id), ", name:", str(self.name),
                        ", email:", str(self.email), ", level:",
                        str(self.level), ", manager:", str(self.manager), "}"])


class Level(object):
    def __init__(self, id, desc):
        self.id = id
        self.desc = desc

    def __eq__(self, other):
        return isinstance(other, Level) and (self.id == other.id
                                             and self.desc == other.desc)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return ''.join(["{id:", str(self.id), ", desc:", str(self.desc), "}"])
