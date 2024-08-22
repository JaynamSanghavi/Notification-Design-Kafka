import json
import random
import uuid
from confluent_kafka import Producer
from datetime import datetime


producer = Producer({"bootstrap.servers": "localhost:9092"})


EVENT_TOPICS = {
    "like": "like",
    "comment": "comment",
    "new_post": "uploaded",
    "follow": "followed"
}


def create_random_message():
    event_type = random.choice(list(EVENT_TOPICS.keys()))
    user_id = str(uuid.uuid4())
    target_user_id = str(uuid.uuid4())
    post_id = str(uuid.uuid4()) if event_type in ["like", "comment", "new_post"] else None
    additional_data = "Random comment text" if event_type == "comment" else None

    message = {
        "event_type": event_type,
        "user_id": user_id,
        "target_user_id": target_user_id,
        "post_id": post_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "additional_data": additional_data
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
        message = create_random_message()
        if message:
            produce_message(message)
