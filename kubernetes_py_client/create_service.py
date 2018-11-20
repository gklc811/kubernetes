from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')
v1 = client.CoreV1Api()


def main():
    body = client.V1Service()
    body.metadata = client.V1ObjectMeta(name="test1-service", labels={"app": "test1"})

    # Creating Port object
    port = client.V1ServicePort(protocol='TCP', target_port=5000, port=5000)

    # Creating spec
    spec = client.V1ServiceSpec(ports=[port], selector={"app": "test1"}, type="LoadBalancer",
                                external_traffic_policy="Local")
    body.spec = spec

    # creating a namespaced service
    v1.create_namespaced_service(namespace="test1", body=body)


if __name__ == '__main__':
    main()
