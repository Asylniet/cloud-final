from google.cloud import retail_v2
from google.oauth2 import service_account


# Initialize the Recommendations AI client
def get_recommendations(user_id, event_category):
    # Create a client to interact with the Recommendations AI API
    client = retail_v2.PredictionServiceClient()

    # Construct the request for the recommendation
    request = retail_v2.PredictRequest(
        placement="projects/{project_id}/locations/global/catalogs/default_catalog/placements/event-recommendation",
        user_event={
            "visitor_id": user_id,
            "event_type": "view",  # Can also be 'purchase', 'register', etc.
            "event_detail": {
                "event_category": event_category
            }
        }
    )

    # Fetch recommendations from the model
    response = client.predict(request=request)

    recommended_events = []
    for recommendation in response.results:
        recommended_events.append({
            'event_id': recommendation.id,
            'event_title': recommendation.title,
            'event_description': recommendation.description,
            'event_date': recommendation.date,
        })

    return recommended_events


# Example usage
user_id = "12345"
event_category = "music"
recommended_events = get_recommendations(user_id, event_category)
print("Recommended events:", recommended_events)
