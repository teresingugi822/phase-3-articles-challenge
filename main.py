from lib.models import Author, Magazine, Article

author = Author("Teresa")
magazine = Magazine("Tech Weekly", "Technology")
article = Article(author, magazine, "The Power of Python")

print("=== Article Info ===")
print(f"Title: {article.title}")
print(f"Author: {article.author.name}")
print(f"Magazine: {article.magazine.name}")
