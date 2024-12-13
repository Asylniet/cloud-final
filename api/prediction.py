from google.cloud.aiplatform.gapic import PredictionServiceClient

def predict_event_registration(user_data):
    # Client to interact with AI Platform's prediction service
    client = PredictionServiceClient()

    # Define the model endpoint
    endpoint = "projects/{project_id}/locations/{location}/endpoints/{endpoint_id}"

    # Prepare the input data for prediction
    instances = [{
        'user_id': user_data['user_id'],
        'age': user_data['age'],
        'location': user_data['location'],
        'past_events': user_data['past_events']
    }]

    # Request prediction from the AI model
    response = client.predict(endpoint=endpoint, instances=instances)

    # Extract the prediction result (likelihood of registration)
    registration_probability = response.predictions[0]

    return registration_probability


# Example usage
user_data = {
    'user_id': '12345',
    'age': 30,
    'location': 'New York',
    'past_events': ['concert', 'workshop']
}

registration_probability = predict_event_registration(user_data)
print(f"Prediction for event registration: {registration_probability}")
