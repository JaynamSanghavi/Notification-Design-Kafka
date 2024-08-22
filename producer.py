import json
from confluent_kafka import Producer

producer = Producer({"bootstrap.servers": "localhost:9092"})


EVENT_TOPICS = {
    "like": "like",
    "comment": "comment",
    "new_post": "uploaded",
    "follow": "followed"
}


def create_message():
    event_type = input("Enter event type (like, comment, new_post, follow): ").strip()
    if event_type not in EVENT_TOPICS:
        print("Invalid event type. Please try again.")
        return None

    user_id = input("Enter user ID: ").strip()
    target_user_id = input("Enter target user ID: ").strip()
    post_id = input("Enter post ID (if applicable, otherwise leave blank): ").strip()
    additional_data = input("Enter any additional data (optional, e.g., comment text): ").strip()

    message = {
        "event_type": event_type,
        "user_id": user_id,
        "target_user_id": target_user_id,
        "post_id": post_id if post_id else None,
        "additional_data": additional_data if additional_data else None
    }

    return message

def produce_message(message):
    topic = EVENT_TOPICS[message["event_type"]]
    
    message_json = json.dumps(message)
    
    producer.produce(topic, message_json)
    producer.flush()

    print(f"Message produced to topic '{topic}': {message_json}")

if __name__ == "__main__":
    while True:
        message = create_message()
        if message:
            produce_message(message)
        else:
            print("Failed to create message. Please try again.")

        cont = input("Do you want to produce another message? (yes/no): ").strip().lower()
        if cont != "yes":
            break
