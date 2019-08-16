import sqlite3

from faker import Faker
from slugify import slugify

fake = Faker()

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

for i in range(20):
	name = fake.name()
	slug = slugify(name)
	is_online = fake.boolean(chance_of_getting_true=50);
	avatar = "https://randomuser.me/api/portraits/men/" + str(i) + '.jpg'
	cur.execute('INSERT INTO users (name, avatar, slug, is_online) VALUES (?, ?, ?, ?)', (name, avatar, slug, is_online))
	conn.commit()
	print("done");

conn.close()