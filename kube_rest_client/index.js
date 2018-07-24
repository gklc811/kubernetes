var Client = require('node-kubernetes-client');

var client = new Client({
    host:  '192.168.56.61',
    protocol: 'https',
    version: 'v1beta2',
    token: ''
});
