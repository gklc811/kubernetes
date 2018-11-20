# from kubernetes.client.rest import ApiException
# from traceback import print_exc
# from kubernetes import client

# import create_namespace
# # import create_statefulset
# import create_service
# import create_persistent_volume
# import get_persistent_volume
# import get_routes
# # import Reloader


# def create_obj(replicas):
#     try:
#         match_labels =  {"app": "cassandra"} 

#         existing_volumes = int(get_persistent_volume.count())
        
#         if replicas > existing_volumes :
#             if create_persistent_volume.create(existing_volumes+1,replicas+1,"cassandra",match_labels):
#                 print("persistent volume created")
        
#         container_port = [
#                         client.V1ContainerPort(container_port=7000,name="intra-node"),
#                         client.V1ContainerPort(container_port=7001,name="tls-intra-node"),
#                         client.V1ContainerPort(container_port=7199,name="jmx"),
#                         client.V1ContainerPort(container_port=9042,name="cql")
#                         ]
        
#         env =  [
#                 client.V1EnvVar(name="CASSANDRA_SEEDS",value="sfst-cassandra-0.svc-cassandra.cassandra.svc.cluster.local"),
#                 client.V1EnvVar(name="MAX_HEAP_SIZE",value="256M"),
#                 client.V1EnvVar(name="HEAP_NEWSIZE",value="100M"),
#                 client.V1EnvVar(name="CASSANDRA_CLUSTER_NAME",value="Cassandra"),
#                 client.V1EnvVar(name="CASSANDRA_DC",value="DC1"),
#                 client.V1EnvVar(name="CASSANDRA_RACK",value="Rack1"),
#                 client.V1EnvVar(name="CASSANDRA_ENDPOINT_SNITCH",value="GossipingPropertyFileSnitch")
#                 ]

        
#         post_start = ['/bin/sh','-c','rm -rf /var/lib/cassandra/data/*']

#         pre_stop = ['/bin/sh','-c','/usr/bin/nodetool decommission']

#         commands  = [] 
#         sfst = create_statefulset.create_obj("cassandra","cassandra",replicas,env,container_port, commands, post_start,pre_stop)
        
#         return sfst
#     except ApiException as exc :
#         print(exc)
    
#     except:
#         print_exc()
            
#     return "app created"

    
    
# def create(sfst):
#     try:
#         if create_statefulset.create("cassandra",sfst):
#             print("cassandra created successfully")
#         return "cassandra created successfully"
#     except ApiException as exc:
#         print(exc)
    
#     except:
#         print_exc()

