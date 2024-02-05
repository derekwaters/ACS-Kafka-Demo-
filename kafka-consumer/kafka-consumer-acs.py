import logging
import os
import json

from dotenv import load_dotenv
from kafka.consumer import KafkaConsumer

load_dotenv(verbose=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#def get_acs_parameters():

def main():
  print("Starting consumer", os.environ["BOOTSTRAP_SERVER"])
  consumer = KafkaConsumer( 
    bootstrap_servers=[os.environ["BOOTSTRAP_SERVER"]],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
 #   group_id=os.environ["CONSUMER_GROUP"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
  )

  consumer.subscribe([os.environ["KAFKA_TOPIC"]])

  for message in consumer:

    try:
#      kafka_message = f"""
#      Values for AAP - cluster: {message.value['alert']['clusterName']}
#      Values for AAP - namespace: {message.value['alert']['namespace']}
#      Values for AAP - deployment: {message.value['alert']['deployment']['name']}
#      """
      kafka_message = {
      "Values for AAP - cluster": {message.value['alert']['clusterName']}
      "Values for AAP - namespace": {message.value['alert']['namespace']}
      "Values for AAP - deployment": {message.value['alert']['deployment']['name']}
      }
      
      logger.info(kafka_message)
    except Exception as e:
      logger.error(e)
  

if __name__ == "__main__":
  main()
