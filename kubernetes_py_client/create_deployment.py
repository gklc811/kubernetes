from kubernetes import client, config
from traceback import print_exc
from pprint import pprint

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.

config.load_kube_config(config_file='./config')
v2 = client.ExtensionsV1beta1Api()


def main():
    try:
        # creating a instance of class deployment
        dep = client.ExtensionsV1beta1Deployment()

        # giving name for the name as "test1"
        dep.metadata = client.V1ObjectMeta(name="dpl-test1")

        # creating a instance for container class and specifying the details
        container = client.V1Container(name="test1", ports=[client.V1ContainerPort(container_port=5000)],
                                       image="gklc811/test1")

        # creating template for container
        template = client.V1PodTemplateSpec(metadata=client.V1ObjectMeta(labels={"app": "test1", 'tier': 'backend'}),
                                            spec=client.V1PodSpec(containers=[container],
                                                                  node_selector={'tier': 'backend'}))

        # Create the deployment spec
        spec = client.V1DeploymentSpec(replicas=3, selector=client.V1LabelSelector(match_labels={"app": "test1"}),
                                       template=template)
        print("\n\n\n")

        # adding a spec instance to deployment spec details
        dep.spec = spec

        # creating  a deployment with namespace
        v2.create_namespaced_deployment(namespace="test1", body=dep)

    except:
        print_exc()


if __name__ == '__main__':
    main()
