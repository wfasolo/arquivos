import templates.previsao as prevv
# A very simple Flask Hello World app for you to get started with...


from flask import Flask, render_template, redirect

app = Flask(__name__, template_folder='..')

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route("/teste")
def index():
  return  render_template('mysite/templates/index.html')

@app.route("/graf")
def grafico():
  prevv.prev()
  return  render_template('temp-plot.html')

  #redirect("https://www.pythonanywhere.com/user/wfasolo/files/home/wfasolo/temp-plot.html", code=302)


if __name__ == '__main__':
  app.run(debug=True)