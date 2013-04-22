class Material(object):

    def __init__(self, title, tags = set(), likes = 0):
        self.title = title
        self.tags = tags
        self.likes = likes

    def __repr__(self):
        return 'Material(%r, %r, %r)' % (self.title, self.likes, self.tags)

    def __str__(self):
        return self.description()

    def description(self):
        return self.title

    def like(self):
        self.likes += 1
        return self.likes

class Book(Material):

    def __init__(self, title, author, tags = set(), likes = 0):
        Material.__init__(self, title, tags, likes)
        self.author = author

    def description(self):
        return '%r, %r' % (self.author, self.title)

