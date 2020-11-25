from flask import Flask, render_template, send_from_directory, request, redirect
import csv
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html') 

'''

@app.route('/blog')
def blog():
    return 'Hello, Pranay!!! These blogs are your thoughts!!!'     

@app.route('/blog/2/tech')
def blog2():
    return 'Hello, Pranay!!! Technology is engaging after a point.Right!!!' 


@app.route('/about.html')
def about():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('about.html')  

@app.route('/')
def my_home():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template("index.html")  

@app.route('/works.html')
def works():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('works.html')  


@app.route('/work.html')
def work():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('work.html')      

@app.route('/contact.html')
def contact():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('contact.html')      


@app.route('/components.html')
def componenets():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('components.html')  ''' 


@app.route('/<string:page_name>')
def html_page(page_name):
    #return 'Hello, Pranay!!! How are you?!'
    return render_template(page_name)      



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method =='POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('thankyou.html')
		except:
			return "did not save to database"	
	else:
	    return "sth went wrong"	

def write_to_file(data):
	with open('database.txt', mode ='a') as database:
		email = data["email"]
		subject =data["subject"]
		message =data["message"]
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open('database.csv', newline='', mode ='a') as database2:
		email = data["email"]
		subject =data["subject"]
		message =data["message"]
		csv_writer = csv.writer(database2, delimiter =',', quotechar ='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])		

	

''', quoting=csv.QUOTE_MINIMAL

@app.route('/home.html')
def home():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('index.html') 

'''          

'''  
  return render_template('index.html')

@app.route('/about.html')
def about():
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('about.html')    

@app.route('/<username>')
def hello_world(username=None):
    #return 'Hello, Pranay!!! How are you?!'
    return render_template('index.html', name =username)        

# @app.route('/favicon.ico')
# def about():
#     #return 'Hello, Pranay!!! How are you?!'
#     return render_image('favicon.ico')              

'''