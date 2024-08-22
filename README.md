# Kafka-Based Notification System

## Overview

This project implements a Kafka-based notification system designed for social media platforms. It handles various user events like likes, comments, new posts, and follows, efficiently routing these notifications to dedicated Kafka topics. The system is built using Python and leverages Kafka for distributed messaging.

## Features

- **Event Handling:** Supports events such as `like`, `comment`, `new_post`, and `follow`.
- **Topic Segregation:** Each event type is routed to its specific Kafka topic (`like`, `comment`, `uploaded`, `followed`).
- **Customizable Messages:** The producer creates event messages with details like `user_id`, `target_user_id`, `post_id`, and more.
- **Randomized Event Generation:** The producer can generate random events, simulating real-world usage.

## Project Structure

- **admin.py**: Script to create Kafka topics and manage Kafka cluster settings.
- **producer.py**: Kafka producer script that generates event messages and sends them to the appropriate Kafka topics.
- **consumer.py**: Kafka consumer script that listens to specific topics and processes incoming messages.

## Prerequisites

- **Python 3.7+**
- **Kafka**: A running Kafka instance is required. You can set up Kafka locally or use a managed service like Confluent Cloud.
- **Python Packages**: Install the required Python packages using `pip`.

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/JaynamSanghavi/Notification-Design-Kafka.git
   cd Notification-Design-Kafka
   ```

2. **Install Dependencies:**

   Install the required Python packages:

   ```bash
   
   pip install -r requirements.txt
   ```

3. **Start Kafka:**

   Ensure that Kafka is running on your local machine or remote server. By default, the Kafka bootstrap server is set to `localhost:9092`.

4. **Create Kafka Topics:**

   Run the `admin.py` script to create necessary Kafka topics:

   ```bash
   python admin.py
   ```

5. **Run the Kafka Producer:**

   To produce events, run the `producer.py` script. It will generate random event messages and send them to the appropriate Kafka topics.

   ```bash
   python producer.py
   ```

6. **Run the Kafka Consumer:**

   To consume messages from a specific topic, run the `consumer.py` script.

   ```bash
   python consumer.py
   ```

## Next Steps

- **Queue Implementation:** The next phase involves adding queues at the consumer end for different types of notifications (e.g., email, in-app, SMS).

## Contributing

Feel free to fork this project, open issues, or submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, please reach out via LinkedIn or open an issue on GitHub.