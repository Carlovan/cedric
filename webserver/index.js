const WebSocket = require('ws');
const zerorpc = require('zerorpc');
const fs = require('fs');

var rpc_address = 'tcp://127.0.0.1:';
var motors_port = 22000;
var camera_port = 22001;
var nn_port     = 22002;

var motors_client = new zerorpc.Client();
motors_client.connect(rpc_address + motors_port);

var camera_client = new zerorpc.Client();
camera_client.connect(rpc_address + camera_port);

var nn_client = new zerorpc.Client();
nn_client.connect(rpc_address + nn_port);

var last_image = [];

wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function(ws){
	ws.on('message', function(msg){
		var data = JSON.parse(msg);
		if(data.type == 'walk'){
			motors_client.invoke('walk', data.speed, data.steering, (error, res, more) => {});
		}
		else if(data.type == 'shoot'){
			camera_client.invoke('shoot', (error, res, more) => {
				if(ws.readyState == ws.OPEN && res && res.length > 0){
					fs.readFile(res, function(err, content) {
						var data = {};
						data.type = 'image';
						data.image = content;
						last_image = data.image;
						if(ws.readyState == ws.OPEN)
							ws.send(JSON.stringify(data));
					});
				}
			});
		}
		else if(data.type == 'nn_steering'){
			nn_client.invoke('calculateSteering', last_image, (error, res, more) => {
				var data = {};
				data.type = 'nn_steering';
				data.steering = res;
				if(ws.readyState == ws.OPEN)
					ws.send(JSON.stringify(data));
			});
		}
	});
});
