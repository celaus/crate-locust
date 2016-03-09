
#### Build image

Build crate-locust Docker image

```bash
    docker build -t clma/crate-locust .
```

#### Use locust in master-slave setup

```bash
    docker run -d --name master -f locust.py --host=<loadbalancer> --maste
    docker run -d --name slave  -f locust.py --host=<loadbalancer> --slave --master-host=master
```