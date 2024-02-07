This repo contains the code for the webhook and producer microservice.
As part of the setup of this component, the variables are:
- the bootstrap server (for the kafka environment)
- the topic name 
- the url for the webhook (default is simply /webhook).

For the url component, I use Flask and if I keep the default and expose it on port 8001 for the following cluster - rosa-f54xw.wvqh.p1.openshiftapps.com
when I create a route for this environment the url is at http://acs-webhook-kafka.apps.rosa-f54xw.wvqh.p1.openshiftapps.com/webhook

The following three screen captures show how to deploy the container onto OpenShift.
Do not forget to:
 - create a route (in this example I disable the secure part of it) and add the /webhook for the url.
 - point to the proper port for the service creation (default is 8001 - this is configurable in the .env file)

![Browser](https://github.com/SimonDelord/ACS-Kafka-Demo-/blob/main/images/acs-webhook-screenshot-1.png)

![Browser](https://github.com/SimonDelord/ACS-Kafka-Demo-/blob/main/images/acs-webhook-screenshot-2.png)

![Browser](https://github.com/SimonDelord/ACS-Kafka-Demo-/blob/main/images/acs-webhook-screenshot-3.png)
