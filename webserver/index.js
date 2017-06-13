const WebSocket = require('ws');
const zerorpc = require('zerorpc');

var motors_port = 22000;

var rpc_client = new zerorpc.Client()
rpc_client.connect('tcp://127.0.0.1:' + motors_port);

wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function(ws){
	ws.on('message', function(msg){
		var data = JSON.parse(msg);
		process.stdout.write(`${data.steering.toFixed(2)}  \t${data.speed}      \r`);
		rpc_client.invoke('walk', data.speed, data.steering, (error, res, more) => {});
	});

	ws.send('ok');
});
