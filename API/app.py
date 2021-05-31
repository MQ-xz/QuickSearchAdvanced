import flask
from flask import request,jsonify,make_response
import requests
from googlesearch import search 


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def finder(q):
    for site in search(q):
        if 'geeksforgeeks' in site:
            source = requests.get(site).text
            try:
                lines = source.split('\n')
                for line in lines:
                    if  '..' in q:
                        q = q.split('..')[0]
                    if q.replace('?','') in line:
                        answer_option = line.split('Answer:</b> <b>')[1].split('</b>')[0]
                        answer = line.split(answer_option)[1].split('<br>')[0].replace('</b>','')
                        answer = answer.replace('<sup>','').replace('</sup>','')
            except:
                locate_q = source.split(q.replace('?',''))[1]
                answer_option =  locate_q.split('<p>Answer ')[1].split('</p><br>')[0]
                answer = locate_q.split('<p>Answer ')[0].split(answer_option)[1].split('<br>')[0]
            return answer

@app.route('/', methods=['GET'])
def home():
    try:
        q = request.args.get('question')
        answer = finder(q)
        response = make_response(jsonify( {"answer": answer.replace(' ','',1)}),200)

    except:
        response = make_response(jsonify( {"AppName":"Quick Search Advanced","Version":"1.0.2"}),200)

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]= "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)