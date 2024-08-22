from confluent_kafka import Consumer, KafkaError

consumer = Consumer({
    "bootstrap.servers": "localhost:9092",
    "group.id": "notification-consumer-group",
    "auto.offset.reset": "earliest"
})

consumer.subscribe(["like", "comment", "uploaded", "followed"])

def handle_message(message):
    event = message.value()
    topic = message.topic()

    if topic == "like":
        handle_like_event(event)
    elif topic == "comment":
        handle_comment_event(event)
    elif topic == "uploaded":
        handle_new_post_event(event)
    elif topic == "followed":
        handle_follow_event(event)
    else:
        print(f"Unknown topic: {topic}")

def handle_like_event(event):
    print(f"Handling 'like' event: {event}")

def handle_comment_event(event):
    print(f"Handling 'comment' event: {event}")

def handle_new_post_event(event):
    print(f"Handling 'new_post' event: {event}")

def handle_follow_event(event):
    print(f"Handling 'follow' event: {event}")

if __name__ == "__main__":
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            handle_message(msg)

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
