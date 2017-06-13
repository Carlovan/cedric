const WebSocket = require('ws');
const zerorpc = require('zerorpc');

var rpc_address = 'ipc:///tmp/';
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
			motors_client.invoke('walk', data.speed, data.steering, (error, res, more) => {});
		}
		else if(data.type == 'shoot'){
			try {
				camera_client.invoke('shoot', (error, res, more) => {
					try{
						var data = {};
						data.type = 'image';
						data.width = res[0].length;
						data.height = data.length;
						data.image = [].concat(...res); // Flatten the array
						ws.send(JSON.stringify(data));
					}catch(er){}
				});
			}
			catch(err){}
		}
	});
});
