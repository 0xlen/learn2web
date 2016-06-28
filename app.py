import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return 'hello web'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
