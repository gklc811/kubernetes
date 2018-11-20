from os import path
import yaml
from kubernetes import client, config
from pprint import pprint

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')


def main():
    with open(path.join(path.dirname(__file__), "zdeployment.yml")) as f:
        dep = yaml.load(f)
        k8s_beta = client.ExtensionsV1beta1Api()
        pprint(dep)
        resp = k8s_beta.create_namespaced_deployment(
            body=dep, namespace="test-service-a")
        print("Deployment created. status='%s'" % str(resp.status))


if __name__ == '__main__':
    main()
