from flask_restful import reqparse, Resource

from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field is required"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field is required"
    )

    def post(self):
        data = self.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message': 'Username taken. Try another username'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User registered successfully'}, 201





# another = User.find_by_id(1)
# print(another.username)