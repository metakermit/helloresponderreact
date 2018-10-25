import responder

api = responder.API()

api.add_route("/", static=True)

@api.route("/admin")
async def greet_world(req, resp):
    resp.content = api.template('admin.html')

def start():
    api.run(address="0.0.0.0")

if __name__ == '__main__':
    start()
