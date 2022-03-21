from flask import Flask


app=Flask(__name__)



@app.route('/')
def homeppage():
     return('Hello GCPCET-AI')

if (__name__=="__main__"):
     app.run()
          