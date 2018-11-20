from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper
# utility. If no argument provided, the config will be loaded from
# default location.
config.load_kube_config(config_file='./config')
v1 = client.CoreV1Api()


def create(existing_volumes,create_volumes,namespace_name,labels):
    for i in range (existing_volumes,create_volumes):

        # creating a instance of class Namespace
        body = client.V1PersistentVolume()
        
        labels['type']="local"
        # giving name for the namespace as given in the function call
        body.metadata = client.V1ObjectMeta(name="cassandra-data-"+str(i),namespace=namespace_name,labels=labels)

        host_path = client.V1HostPathVolumeSource(path="/tmp/data/cassandra-data-"+str(i))

        #creating volume Spec
        spec = client.V1PersistentVolumeSpec(access_modes=["ReadWriteOnce"], capacity={"storage": "5Gi"}, host_path=host_path, persistent_volume_reclaim_policy="Delete")

        body.spec = spec

        v1.create_persistent_volume(body=body)

    return "persistent volume created"

