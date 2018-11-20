from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')
v1 = client.CoreV1Api()


def count():
    # creating a instance of class Namespace
    pv = v1.list_persistent_volume()

    return (len(getattr(pv, 'items', '')))
