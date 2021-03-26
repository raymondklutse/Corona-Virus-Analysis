# Corona-Virus-Analysis

## Context

Corona Virus has made waves all over the world since its appearance in December 2019. This virus has taken the lives of many people and also had a huge impact on economies world wide. Amongst these economies, the UK has been hit hard by this pandemic in terms of the lives lost and the economic strain. In this project, we analyse some data made available on [The Office for National Statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/conditionsanddiseases), to gain insights into how the pandemic is spreading and also its economic impacts.

## Getting started

1. Install the following packages
- Java 11.0.10 
- Scala 2.12.10 
- Spark 3.0.2 for Hadoop 3.2+ 
- Hadoop 3.3.0 *
- Docker Desktop 3.2.2
- Zeppelin 0.9.0 using Docker

```
docker run -p 8080:8080 --rm \ 
-v $PWD/path_to_logs:/zeppelin/logs \
-v $PWD/path_to_data:/zeppelin/seed \  
-v $PWD/path_to_notebook:/zeppelin/notebook \
-e ZEPPELIN_LOG_DIR='/zeppelin/logs' \
-e ZEPPELIN_NOTEBOOK_DIR='/zeppelin/notebook' \
--name zeppelin apache/zeppelin:0.9.0
```

2. Enter your local host IP address in your browser's address bar

3. Run notebook

PS: In case you want to use your own data, please store it in the Data directory

