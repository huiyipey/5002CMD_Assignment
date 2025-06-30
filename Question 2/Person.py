class Person:
    def __init__(self, name, gender='', privacy='public', biography=''):
        self.name = name
        self.gender = gender
        self.privacy = privacy
        self.biography = biography

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_privacy(self):
        return self.privacy

    def get_biography(self):
        return self.biography

    def set_name(self, name):
        self.name = name

    def set_gender(self, gender):
        self.gender = gender

    def set_privacy(self, privacy):
        self.privacy = privacy

    def set_biography(self, biography):
        self.biography = biography

    def __str__(self):
        return self.name
