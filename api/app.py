from flask import Flask  
import os

app = Flask(__name__)            

@app.route("/", methods=['GET'])               
def hello():                     
    return "<h1>A prototype FLASK APP for automaticpractice.com testing </h1>"


@app.route("/tests/run", methods=['GET'])               
def runAllTests():    
    os.system("behave -f allure_behave.formatter:AllureFormatter -o ./allure-results")
    return 'OK'


if __name__ == "__main__":        
    app.run() 