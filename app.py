from flask import Flask, render_template, request
#import boto3 # include declaration in requirements.txt
import os

app = Flask(__name__)

access_key_id = os.environ['aws_access_key_id']
secret_access_key = os.environ['aws_secret_access_key']
table_name = os.environ['dynamo_table_name']

#dynamoDb = boto3.resource('dynamoDb', region_name='eu-central-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
#table = dynamoDb.Table(table_name)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':       
        values = getFormValues(request.form)
        values['table_name'] = table_name
        values['access_key_id'] = access_key_id
        values['secret_access_key'] = secret_access_key
        #table.put_item(Item=values)
        
        return render_template('index.html', values=values)
    else:
        return render_template('index.html')


def getFormValues(reqestFormData):
    values = { 
        'ip': reqestFormData['ip'], 
        'user': reqestFormData['user'], 
        'pass': reqestFormData['pass'], 
        'reocur': reqestFormData['reocur'] 
    }    

    return values


if __name__ == '__main__':
    app.run(debug=True) 

