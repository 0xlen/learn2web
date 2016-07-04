import web

web.config.debug = True

urls = (
    '/', 'home',
    '/id/(\d+)', 'user',
    '/render/(.*)', 'rander',
)

template = web.template.render("static/")


class home:
    def GET(self):
        return "Hello web.py"


class user:
    def GET(self, id):
        return "The index is " + id + " ."

class rander:
    def GET(self, name):
        return template.print_name(name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
