import re
from flask import Flask, jsonify, request, render_template
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import sys


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = "static/"
db = SQLAlchemy(app)

# Method for upload file to local folder
@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        content = file.read()
        
        
    return render_template('content.html', content=content) 

class QuestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    required_lvl = db.Column(db.Integer, nullable = False)
    
    def __init__(self, new_quest_id, new_quest_name, new_quest_description, new_quest_required_lvl):
        self.id = new_quest_id
        self.name = new_quest_name
        self.description = new_quest_description
        self.required_lvl = new_quest_required_lvl
    
    def __repr__(self):
        return 'Quest {0}: {1}: {2}: {3}:'.format(self.id, self.name, self.description, self.required_lvl)
    
db.create_all()


quest_put_args = reqparse.RequestParser()
quest_put_args.add_argument("name", type = str, help = "Name of the quest is required", required = True)
quest_put_args.add_argument("description", type = str, help = "descriptionription of the quest", required = True)
quest_put_args.add_argument("required_lvl", type = int, help = "required_lvl quest", required = True)

quest_update_args = reqparse.RequestParser()
quest_update_args.add_argument("name", type = str, help = "Name of the quest is required")
quest_update_args.add_argument("description", type = str, help = "descriptionription of the quest")
quest_update_args.add_argument("required_lvl", type = int, help = "required_lvl quest")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'description': fields.String,
    'required_lvl': fields.Integer
}

class Quest_Implementation(Resource):
    #GET REQUESTS
    #ger request for python
    @marshal_with(resource_fields)
    def get(self, quest_id):
        result = QuestModel.query.filter_by(id=quest_id).first()
        if not result:
            abort(404, message="could not found quest with that id")
        return result
    
    #get request for unity
    @app.route('/list') #key for C# script
    def get_data():
        get_result = QuestModel.query.all()
        print(get_result)
        return jsonify([str(result) for result in get_result])
    #PUT, POST REQUEST 
    #put request for python
    @marshal_with(resource_fields)
    def put(self, quest_id):
        args = quest_put_args.parse_args()
        result = QuestModel.query.filter_by(id=quest_id).first()
        if result:
            abort(409, message="Quest id taken...")
            
        quest = QuestModel(id = quest_id, name = args['name'], description = args['description'], required_lvl = args['required_lvl'])
        db.session.add(quest)
        db.session.commit()
        return quest, 201
    
    #post request for unity
    @app.route('/list_add', methods=['POST']) #key for C# script
    def insert_new_quest():
        print("before JSON")
        data = request.get_json()
        print(data)
        print("im here")
        sys.stdout.flush()
        new_quest_id = data['questID']
        new_quest_name = data['questName']
        new_quest_description = data['questDesc']
        new_quest_required_lvl = data['questReqLvl']
        new_quest = QuestModel(new_quest_id, new_quest_name, new_quest_description, new_quest_required_lvl)
        db.session.add(new_quest)
        db.session.commit()
        return "OK"
    
    @marshal_with(resource_fields)
    def patch(self, quest_id):
        args = quest_update_args.parse_args()
        result = QuestModel.query.filter_by(id=quest_id).first()
        if not result:
            abort(404, message="Video doesn't exist, cannot update")
        
        if args["name"]:
            result.name = args["name"]
        if args["description"]:
            result.description = args["description"]
        if args["required_lvl"]:
            result.required_lvl = args["required_lvl"]
            
        # db.session.add(result)
        db.session.commit()
        
        return result
        
    
api.add_resource(Quest_Implementation, "/quest/<int:quest_id>")


def init_app():
    return app


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug = True)