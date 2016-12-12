
from flask import Blueprint, render_template, request
from bson import json_util
from app import mongo
mod_main = Blueprint('main', __name__)

@mod_main.route('/', methods=['GET','POST'])
def index():
   ''' Renders the App index page.
   :return:
   '''
   db = mongo.db.arkep

   if request.method == 'GET':
       return render_template('index.html')
   elif request.method == 'POST':
       data = request.form.to_dict()
       db.insert(data)
       return json_util.dumbs(data)
   else:
       return 'Bad request'

@mod_main.route('/<string:id>', methods=['GET'])
def get_doc(id):

   #Return a mongo document with the specified id.
   #return MongoDb Cursor

   db = mongo.db.arkep

   if request.method == 'GET':
        doc = db.find({"_id":Object (id)})
        return "You requested a document with ID" + id
   else:
        return 'Bad request'
