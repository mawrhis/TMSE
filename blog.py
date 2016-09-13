import web
import model #will work with database

urls = (
	'/', 'Index',
	'/comics/(\d+)', 'Comics'
	'/static/', 'static'
	)

t_globals ={
	'datestr' : web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)


class Index:
	def GET(self):
		latest_post = model.get_latest_post()
		return render.index(latest_post)



'''
class Comics: #vezmi id od komiksu co je prave zobrazen a pricti/odecti jednicku
	def GET_next(self, id):
	current_post = 

	def GET_previous(self, id):
	current_post = 
'''

'''
class Previous: #vezmi id od komiksu co je prave zobrazen a odecti jednicku
	def GET(self, id)
	current_post = 
'''

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()