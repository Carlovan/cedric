const WebSocket = require('ws');
const zerorpc = require('zerorpc');
const fs = require('fs');

var rpc_address = 'tcp://127.0.0.1:';
var motors_port = 22000;
var camera_port = 22001;

var motors_client = new zerorpc.Client();
motors_client.connect(rpc_address + motors_port);

var camera_client = new zerorpc.Client();
camera_client.connect(rpc_address + camera_port);

wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function(ws){
	ws.on('message', function(msg){
		var data = JSON.parse(msg);
		if(data.type == 'walk'){
			process.stdout.write(`${data.steering.toFixed(2)}  \t${data.speed}      \r`);
			motors_client.invoke('walk', data.speed, data.steering, (error, res, more) => {console.log(res)});
		}
		else if(data.type == 'shoot'){
			camera_client.invoke('shoot', (error, res, more) => {
				if(res && res.length > 0){
					fs.readFile(res, function(err, content) {
						var data = {};
						data.type = 'image';
						data.image = content;
						ws.send(JSON.stringify(data));
					});
				}
			});
		}
	});
});
