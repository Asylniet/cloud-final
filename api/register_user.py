import functions_framework
from google.cloud import firestore


@functions_framework.http
def register_user(request):
    data = request.get_json()

    # Handle user registration
    user_id = firestore.Client().collection('users').add(data)

    return f'User {user_id.id} registered successfully', 200
