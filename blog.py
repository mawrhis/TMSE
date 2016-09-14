import web
import model #will work with database
import random

urls = (
	'/', 'Index',
	'/(\d+)', 'Comics',
	'/static/', 'static',
	)

t_globals ={
	'datestr' : web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)


class Index:
	def GET(self):
		post = model.get_latest_post()
		post_id = int(post.id)
		current_post = "/%d" %post_id
		raise web.seeother(current_post)

class Comics:
	def GET(self,id):
		post = model.get_post(int(id))
		random_post = random.randint(1,73)
		return render.comics(post, random_post)


'''
class Comics: #vezmi id od komiksu co je prave zobrazen a pricti/odecti jednicku
	def GET(self, id):
		refering_url = web.ctx.path.get()
		print refering_url
		if refering_url == 'index' :#if current page is index
			latest_post = model.get_latest_post_id(int(id))#go to latest post -1
			post = latest_post - 1 + '.png'
			return render.comics(post)
		else: # go to current post -1
			print "not implemented"

	# def GET_previous(self, id):
	# current_post = 
'''

'''
class Previous: #vezmi id od komiksu co je prave zobrazen a odecti jednicku
	def GET(self, id)
	current_post = 
'''

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()