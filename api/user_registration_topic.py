from google.cloud import pubsub_v1
from google.cloud import firestore


def publish_event(event_data):
    publisher = pubsub_v1.PublisherClient()
    topic_name = 'projects/{project_id}/topics/user-registration-topic'

    # Convert event data to bytes
    data = event_data.encode('utf-8')
    future = publisher.publish(topic_name, data)

    print(f"Event published to {topic_name} with message ID: {future.result()}")


def handle_user_registration(event, context):
    """Cloud Function triggered by user registration event."""
    # Get event data from Pub/Sub message
    event_data = event['data']
    registration_details = event_data.decode('utf-8')

    # Extract event details from the message (e.g., user_id, event_id, tickets)
    user_id, event_id, tickets = registration_details.split(',')

    # Perform database operations (e.g., update registration status)
    db = firestore.Client()
    user_ref = db.collection('users').document(user_id)
    user_ref.update({
        'registration_status': 'Registered',
        'event_id': event_id,
        'tickets': tickets
    })

    # Send notification (e.g., email confirmation)
    send_email_confirmation(user_id, event_id)

    print(f"Registration for user {user_id} to event {event_id} processed.")

def send_email_confirmation(user_id, event_id):
    """Send email confirmation for the event registration."""
    # Placeholder for actual email logic (could use SendGrid, Mailgun, etc.)
    print(f"Sending email to user {user_id} for event {event_id}...")
