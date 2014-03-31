@app.route('/helloworld')
def search():
    return "Hello World"

@app.route('/hello/<name>')
def search_candidate(name):
  return "Hello " + str(name)
