import web
from web import form

web.config.debug = True

# config
template = web.template.render('static/')
db       = web.database(dbn="mysql", db="cscamp", user="cscamp", pw="cscamp")
table    = 'messages'

urls = (
    '/', 'messages',
    '/add', 'add',
)

class messages:
    def GET(self):
        return template.index(db.select(table))
class add:
    def GET(self):
        return template.add_message();

    def POST(self):

        messages_form = form.Form(
            form.Textbox('user'),
            form.Textbox('title'),
            form.Textarea('content'),
        )

        form_obj = messages_form()
        if form_obj.validates():
            db.insert(table, **form_obj.d)
            return 'add success'
        else:
            return 'no input'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
