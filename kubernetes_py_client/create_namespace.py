from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')
v1 = client.CoreV1Api()


def main():
    # creating a instance of class Namespace
    body = client.V1Namespace()
    # giving name for the namespace as "test1"
    body.metadata = client.V1ObjectMeta(name="test1")
    v1.create_namespace(body)


if __name__ == '__main__':
    main()
