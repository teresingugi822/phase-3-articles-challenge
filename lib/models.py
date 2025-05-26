from db import CURSOR, CONN

class Author:
    def __init__(self, name):
        self.name = name

    def save(self):
        CURSOR.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
        CONN.commit()

    @classmethod
    def find_by_name(cls, name):
        row = CURSOR.execute("SELECT * FROM authors WHERE name = ?", (name,)).fetchone()
        if row:
            author = cls(row[1])
            author.id = row[0]
            return author
        return None

    def articles(self):
        rows = CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,)).fetchall()
        return [Article(row[1], row[2], row[3], row[4]) for row in rows]

    def magazines(self):
        rows = CURSOR.execute(
            """SELECT DISTINCT m.* FROM magazines m
               JOIN articles a ON m.id = a.magazine_id
               WHERE a.author_id = ?""",
            (self.id,)
        ).fetchall()
        return [Magazine(row[1], row[2]) for row in rows]


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def save(self):
        CURSOR.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
        CONN.commit()

    @classmethod
    def all(cls):
        rows = CURSOR.execute("SELECT * FROM magazines").fetchall()
        return [cls(row[1], row[2]) for row in rows]

    def contributors(self):
        return list({article.author for article in Article.all_articles if article.magazine == self})

    def article_titles(self):
        return [article.title for article in Article.all_articles if article.magazine == self]

class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        # Check for duplicate title by same author
        for article in Article.all_articles:
            if article.author == author and article.title == title:
                raise ValueError("Duplicate article title for this author.")  # ✅ use ValueError
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    def save(self):
        CURSOR.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (self.title, self.content, self.author_id, self.magazine_id)
        )
        CONN.commit()

    @classmethod
    def all(cls):
        rows = CURSOR.execute("SELECT * FROM articles").fetchall()
        return [cls(row[1], row[2], row[3], row[4]) for row in rows]
