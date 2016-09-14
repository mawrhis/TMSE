import web, datetime

db = web.database(dbn='mysql', db='dbname', user='root', passwd='password')


def get_latest_post():
	try:
		return db.select('posts', order='id DESC', limit=1)[0]
	except IndexError:
		return None

def get_post(id):
	try:
		return db.select('posts', order='id DESC', where='id=$id', vars=locals())[0]
	except IndexError:
		return None

'''
def get_second_latest_post():
	lines = list(db.select('posts', order='id DESC'))
	print  lines[0].id
	latest =  lines[0].id
	second_latest_id = latest - 1
	second_latest = list(db.select('posts', order='id DESC'))
	second_latest_post = second_latest[1].post_image
'''
'''
get_latest_post()
print list(db.select('posts', order='id DESC', limit=1))
'''