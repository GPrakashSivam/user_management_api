from datetime import datetime
from django.http import JsonResponse
from rest_framework.views import APIView
from pymongo.errors import DuplicateKeyError
from bson.objectid import ObjectId
from user_management_project.settings import MONGO_DB
from .schemas import UserSchema

class UserCreateView(APIView):
    """
    View to handle creation of Users
    Method: POST
    """
    def post(self, request):
        try:
            # parse and validate the incoming JSON request data
            data = request.data
            user = UserSchema(**data) # Validate using Pydantic Schema
            user_data = user.model_dump()  # Convert Pydantic model to dictionary

            # Convert dob (if present) to datetime.datetime
            if 'dob' in user_data:
                user_data['dob'] = datetime.combine(user_data['dob'], datetime.min.time())

            #Insert new User into Mongo DB
            result = MONGO_DB['users'].insert_one(user_data)
            return JsonResponse({"message": "User created successfully.", 
                                "user_id": str(result.inserted_id)}, status=201)
        except DuplicateKeyError:
            return JsonResponse({"error": "User with this email already exists."}, status=400)
        except Exception as ex:
            return JsonResponse({"error": str(ex)}, status=400)

class UserDetailView(APIView):
    """
    View to handle retrieving, updating, and deleting a user by ID.
    Methods: GET, PUT, DELETE
    """
    def get(self, request, user_id):
        """
        Retrieve a user by MongoDB's ObjectId.
        """
        try:
            # find user_id based on _id and exclude _id in the reponse
            user = MONGO_DB['users'].find_one({"_id": ObjectId(user_id)}, {"_id": 0}) 
            if user:
                return JsonResponse(user, status=200)
            
            return JsonResponse({"error": "User not found."}, status=404)
        except Exception as ex:
            return JsonResponse({"error": str(ex)}, status=400)
    
    def put(self, request, user_id):
        """
        Update user details by ID.
        """
        try:
            # Parse the incoming data and filter out None values
            data = request.data
            updated_data = {key: value for key, value in data.items() if value is not None}

            # Update a document in Mongo DB
            result = MONGO_DB['users'].update_one({"_id": ObjectId(user_id)}, {"$set": updated_data})
            if result.matched_count:
                return JsonResponse({"message": "User updated sucessfully."}, status=200)
            
            return JsonResponse({"error": "User not found."}, status=404)
        
        except Exception as ex:
            return JsonResponse({"error": str(ex)}, status=400)
    
    def delete(self, request, user_id):
        """
        Delete a user by ID.
        """
        try:
            # Remove the document from MongoDB
            result = MONGO_DB['users'].delete_one({"_id": ObjectId(user_id)})
            if result.deleted_count:
                return JsonResponse({"message": "User deleted sucessfully."}, status=200)
            
            return JsonResponse({"error": "User not found."},status=404)
        
        except Exception as ex:
            return JsonResponse({"error": str(ex)}, status=400)
