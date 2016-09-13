import web, datetime

db = web.database(dbn='mysql', db='dbname', user='root', passwd='password')


def get_latest_post():
	lines = list(db.select('posts', order='id DESC'))
	print  lines[0].post_image
	return  lines[0].post_image
