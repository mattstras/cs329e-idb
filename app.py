from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/
	
@app.route('/about')
def about():
	return render_template('about.html')
	
@app.route('/politicians')
def politicians():
	return render_template('politicians.html') 

@app.route('/state')
def state():
	return render_template('state.html') 

@app.route('/positions')
def positions():
	return render_template('positions.html') 

@app.route('/alanmorales')
def alanmorales():
	return render_template('alanmorales.html')
	
@app.route('/alaska')
def alaska():
	return render_template('alaska.html') 

@app.route('/california')
def california():
	return render_template('california.html') 

@app.route('/chiefjustice')
def chiefjustice():
	return render_template('chiefjustice.html') 

@app.route('/chienchihhuang')
def chienchihhuang():
	return render_template('chienchihhuang.html')
	
@app.route('/donaldtrump')
def donaldtrump():
	return render_template('donaldtrump.html') 

@app.route('/governor')
def governor():
	return render_template('governor.html') 

@app.route('/gregabbott')
def gregabbott():
	return render_template('gregabbott.html') 

@app.route('/johnrobert')
def johnrobert():
	return render_template('johnrobert.html')
	
@app.route('/lisamurkowski')
def lisamurkowski():
	return render_template('lisamurkowski.html') 

@app.route('/massachusetts')
def massachusetts():
	return render_template('massachusetts.html') 

@app.route('/matthewlarsen')
def matthewlarsen():
	return render_template('matthewlarsen.html') 

@app.route('/matthewstrasburg')
def matthewstrasburg():
	return render_template('matthewstrasburg.html')
	
@app.route('/mayor')
def mayor():
	return render_template('mayor.html') 

@app.route('/newyork')
def newyork():
	return render_template('newyork.html') 

@app.route('/paulryan')
def paulryan():
	return render_template('paulryan.html') 

@app.route('/president')
def president():
	return render_template('president.html')
	
@app.route('/representative')
def representative():
	return render_template('representative.html') 

@app.route('/richardseifert')
def richardseifert():
	return render_template('richardseifert.html') 

@app.route('/senator')
def senator():
	return render_template('senator.html') 

@app.route('/steveadler')
def steveadler():
	return render_template('steveadler.html')
	
@app.route('/tedcruz')
def tedcruz():
	return render_template('tedcruz.html') 

@app.route('/texas')
def texas():
	return render_template('texas.html') 

@app.route('/wisconsin')
def wisconsin():
	return render_template('wisconsin.html') 

@app.route('/elizabethwarren')
def elizabethwarren():
	return render_template('elizabethwarren.html')
	
if __name__ == '__main__':
	app.run() # Run application