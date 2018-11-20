from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')
v1 = client.CoreV1Api()


def create(namespace_name,service_name,container_port,commands,replicas):
    # creating a instance of class Namespace
    body = client.V1ReplicationController()

    # giving name for the namespace as given in the function call
    body.metadata = client.V1ObjectMeta(name=str(service_name)+"-controller")
    
    port_obj = []

    # Creating Port object
    for ports in container_port:
        port = client.V1ContainerPort(container_port=ports["port"],name=ports["name"])
        port_obj.append(port)

    #containers
    container_obj= client.V1Container(name=service_name,image="registry.gokul.com:5000/gokul/" + str(namespace_name) ,command=commands,
    ports=port_obj, resources=client.V1ResourceRequirements(requests={"cpu":"100m"}))

    #pod spec
    pod_spec = client.V1PodSpec(containers=[container_obj])

    #spec template 
    template = client.V1PodTemplateSpec(client.V1ObjectMeta(labels={"app":service_name}),spec=pod_spec)

    #replication specs
    body.spec = client.V1ReplicationControllerSpec(replicas=replicas,selector={"app":service_name},template=template)

    v1.create_namespaced_replication_controller(namespace=namespace_name,body=body)

    return "replication controller created"
