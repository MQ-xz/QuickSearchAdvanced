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
            lines = source.split('\n')
            for line in lines:
                if q.replace('?','') in line:
                    answer_option = line.split('Answer:</b> <b>')[1].split('</b>')[0]
                    answer = line.split(answer_option)[1].split('<br>')[0].replace('</b>','')
                    answer = answer.replace('<sup>','').replace('</sup>','')
                    print(answer)
                    return answer
            break

@app.route('/', methods=['GET'])
def home():
    try:
        q = request.args.get('question')
        print(q)
        answer = finder(q)
        response = make_response(jsonify( {"anwer": answer.replace(' ','',1)}),200)

    except:
        response = make_response(jsonify( {"AppName":"QuickSearch","Version":"0.0.1"}),200)

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"]= "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)