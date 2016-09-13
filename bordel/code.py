import web
render = web.template.render('templates/')
db = web.database(dbn='mysql', user='root', pw='password', db='dbname')

urls = (
    '/', 'index',
    '/add', 'add'

    )

class index:
    def GET(self):
        todos = db.select('todo')
        return render.index(todos)

if __name__== "__main__":
    app = web.application(urls, globals())
    app.run()

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')