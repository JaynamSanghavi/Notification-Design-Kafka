from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({
    "bootstrap.servers": "localhost:9092"
})

topics = [
    NewTopic("like", num_partitions=3, replication_factor=1),
    NewTopic("comment", num_partitions=3, replication_factor=1),
    NewTopic("shared", num_partitions=3, replication_factor=1),
    NewTopic("followed", num_partitions=3, replication_factor=1),
    NewTopic("uploaded", num_partitions=3, replication_factor=1),
]


def create_topics(admin_client, topics):
    fs = admin_client.create_topics(topics)
    for topic, f in fs.items():
        try:
            f.result()
            print(f"Topic {topic} created")
        except Exception as e:
            print(f"Failed to create topic {topic}: {e}")

def list_topic_partitions(admin_client, topics):
    metadata = admin_client.list_topics(timeout=10)
    for topic in topics:
        partitions = metadata.topics[topic].partitions
        print(f"Topic '{topic}' has partitions: {list(partitions.keys())}")

if __name__ == "__main__":
    create_topics(admin_client, topics)
    list_topic_partitions(admin_client, ["like", "comment", "shared", "followed", "uploaded"])
