from facebook_scraper import get_posts
import sqlite3 as sl

class Scraper():
	def scrapedata(self,page):
		posts = get_posts(page, pages=3)
		con = sl.connect('./app/posts.db')
		with con:
		    con.execute("""CREATE TABLE IF NOT EXISTS POSTS
		    	(id INTEGER NOT NULL PRIMARY KEY, page TEXT,contenu TEXT,likes INTEGER,comments INTEGER,shares INTEGER); """)
		data = []
		for post in posts:
			values=(post['post_id'], page, post['text'], post['likes'], post['comments'], post['shares'])
			with con:
				con.execute('REPLACE INTO POSTS (id, page, contenu, likes, comments, shares) values(?, ?, ?, ?, ?, ?)', values)
			item = {'post_id': post['post_id'],
				'text':post['text'],
				'likes': post['likes'],
				'comments': post['comments'],
				'shares': post['shares']
				}
			data.append(item)
		return data
