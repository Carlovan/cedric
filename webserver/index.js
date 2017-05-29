const WebSocket = require('ws');

wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function(ws){
	ws.on('message', function(msg){
		var data = JSON.parse(msg);
		process.stdout.write(`${data.x}    ${data.y}    ${data.button}          \r`);
	});

	ws.send('ok');
});
