from kubernetes import client, config
from simplejson import dumps

config.load_kube_config(config_file='./config')

v1 = client.CoreV1Api()


def get_routemap() -> dict:
    routemap = dict()
    namespace_obj = v1.list_namespace()
    for namespace_item in getattr(namespace_obj, 'items', ''):
        namespace = getattr(getattr(namespace_item, 'metadata', ''), 'name', '')
        endpoints = v1.list_namespaced_endpoints(namespace)
        endpoints_obj = getattr(endpoints, 'items', '')[0] if (getattr(endpoints, 'items', '')) else ''
        endpoints_obj = getattr(endpoints_obj, 'subsets', '')[0] if (getattr(endpoints_obj, 'subsets', '')) else ''
        servers = set()
        addresses = getattr(endpoints_obj, 'addresses', '')
        if addresses:
            for node in addresses:
                servers.add(node.node_name)
        servers = list(servers)
        if servers and namespace != 'default':
            service_port = v1.list_namespaced_service(namespace).items[0].spec.ports[0].node_port
            routemap.update({namespace: {'service_port': service_port, 'server': servers}})
    returnobj = {'routemap': routemap}
    return dumps(returnobj)


confjson = get_routemap()
print(confjson)
