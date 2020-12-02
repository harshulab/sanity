from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient as MC, DESCENDING
import flask
from pprint import pprint
from flask import request, jsonify
from datetime import datetime, timedelta
from traceback import print_exc

conn = MC()

db = "comp_portal"
coll_complaints = conn[db]['saved_complains']
coll_logins = conn[db]['user_login_data']
app = flask.Flask(__name__)
app.config["DEBUG"] = True


#
#
#
# known bugs- multiple users can register, unique username
def check_logged_in(login_id, max_time=24):
    try:
        dt_last_login = datetime.strptime(coll_logins.find_one({'login_id': login_id})['datetime_login'],
                                          "%Y-%m-%d %H:%M:%S.%f")
        if timedelta(hours=max_time) <= datetime.now() - dt_last_login:
            return False
        else:
            return True
    except TypeError:
        return None


@app.route('/register_user', methods=['GET', 'POST'])
def get_register():
    req_data = request.args
    pprint(req_data)
    try:
        coll_logins.insert_one({"login_id": req_data['login_id'], 'password': req_data['password'],
                                'datetime_login': datetime.now().__str__()})
        resp_ = {'response': 200}
    except KeyError:
        resp_ = {'response': 400, "error": "request is not having keys- " + set(["login_id", 'password']).difference(
            req_data.keys()).__str__()}
    except DuplicateKeyError:
        resp_ = {'response': 400, "error": 'username already exists'}
    except Exception as e:
        resp_ = {'response': 400, "error": str(e)}
    return jsonify(resp_)


@app.route('/login', methods=['GET', 'POST'])
def get_login():
    req_data = request.args
    pprint(req_data)
    try:
        data_user = coll_logins.find_one({"login_id": req_data['login_id']})
        if data_user is None:
            resp_ = {'response': 200, "login_match": False, "error": 'USER MUST REGISTER'}
        else:
            if req_data['password'] == data_user['password']:
                session_ = check_logged_in(req_data['login_id'])
                if session_ is False or session_ is not None:
                    coll_logins.update({"login_id": req_data['login_id']},
                                       {'$set': {'datetime_login': datetime.now().__str__()}})
                    resp_ = {'response': 200, "login_match": True}
                else:
                    resp_ = {'response': 200, "login_match": True, 'data': 'user_already_logged_in'}
            else:
                resp_ = {'response': 200, "login_match": False}

    except KeyError:
        print_exc()
        resp_ = {'response': 400, "error": "request is not having keys- " + set(["login_id", "password"]).difference(
            req_data.keys()).__str__()}

    except Exception as e:
        print_exc()
        resp_ = {'response': 400, "login_match": False, "error": str(e)}
    return jsonify(resp_)


@app.route('/read_all_complain', methods=['GET', 'POST'])
def get_read_complains():
    req_data = request.args
    pprint(req_data)
    try:
        session_ = check_logged_in(req_data['login_id'])
        if session_ is None:
            return jsonify({'response': 200, 'data': 'YOU NEED TO REGISTER FIRST'})
        elif session_ is False:
            return jsonify({'response': 200, 'data': 'USER MUST RE-LOGIN'})
        else:
            all_complains = list(coll_complaints.find({"department": req_data['department']},
                                                      {'_id': 0}).sort('datetime', DESCENDING).limit(100))
            if all_complains.__len__() >= 1:
                resp_ = {'response': 200, "all_complains": all_complains}
            else:
                resp_ = {'response': 200, "all_complains": []}

    except KeyError:
        print_exc()
        resp_ = {'response': 400, "error": "request is not having keys- " + set(["department"]).difference(
            req_data.keys()).__str__()}

    except Exception as e:
        print_exc()
        resp_ = {'response': 400, "all_complains": [], "error": str(e)}
    return jsonify(resp_)


@app.route('/home', methods=['GET'])
def home_routine():
    return 'this is project server'


@app.route('/write_complain', methods=['GET', 'POST'])
def get_write_complains():
    req_data = request.args

    try:
        coll_complaints.insert_one({"username": req_data['username'],
                                    "department": req_data['department'],
                                    "datetime": datetime.now().__str__(),
                                    "complain_text": req_data['complain_text'],
                                    "phone_number": req_data['phone_number'],
                                    "address": req_data['address']})

        resp_ = {'response': 200}
    except KeyError:
        resp_ = {'response': 400, "error": "request is not having keys- " + {"username", "department", "complain_text",
                                                                             "phone_number", "address"}.difference(
            req_data.keys()).__str__()}
    except Exception as e:
        print_exc()
        resp_ = {'response': 400, "error": str(e)}

    return jsonify(resp_)

def foo (chutia):
    print('cskdkhvbsdibv')
    print('duffer')
class avnoor:
    def __init__(self):
        pass
    def __enter__(self):
        print('sckhb')
    def __exit__(self):
        print('DESTRUCTOR ')
if __name__ == '__main__':
    with avnoor as p:
        p = avnoor()
    print('sdckhib')
    # app.run(host="0.0.0.0", port=4090, )

