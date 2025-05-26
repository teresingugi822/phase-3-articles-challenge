from db.create_tables import create_tables
from db.seed import seed_data

def setup():
    create_tables()
    seed_data()

if __name__ == '__main__':
    setup()
