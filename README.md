# ACS-Kafka-Demo-
This is the Git repo describing the various steps to interconnect ACS and a Kafka broker (AMQ Streams in that case).

The idea behind this demo is to integrate ACS to AMQ Streams to provide event driven capabilities for:
- a higher order orchestrator (like a SOAR - could be Splunk SOAR, IBM QRadar, etc...)
- an automation engine (like AAP)
- any other endpoint that may want to do something based on a policy violation coming from ACS.

This specific demo is around GitOps. It is presented in the figure below.

![Browser](https://github.com/SimonDelord/ACS-Kafka-Demo-/blob/main/images/ACS-Kafka-Demo.png)
