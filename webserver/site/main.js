var serverIP = '192.168.1.190';

var ws = new WebSocket(`ws://${serverIP}:8080`);

function runLoop(){
	var stateDiv = document.getElementById('stateDiv');
	window.requestAnimationFrame(runLoop);

	var gamepads = navigator.getGamepads();
	if(gamepads.length == 0)
		stateDiv.innerHTML = 'No gamepad connected';
	else{
		var gp = gamepads[0];

		var ax0 = gp.axes[2];
		var ax1 = gp.axes[3];
		var sleft = `calc(50% + ${ax0 * 380}px)`;
		var stop = `calc(50% + ${ax1 * 380}px)`;

		var bA = gp.buttons[6];
		var ssize = `${bA.pressed ? 70 : 50}px`;
		var sbgcolor = bA.pressed ? '#2ecc71' : '#c0392b';

		stateDiv.style.left = sleft;
		stateDiv.style.top  = stop;
		stateDiv.style.height = ssize;
		stateDiv.style.width = ssize;
		stateDiv.style.backgroundColor = sbgcolor;

		var data = {
			'x': ax0,
			'y': ax1,
			'button': bA.pressed
		};
		if(ws.readyState == ws.OPEN)
			ws.send(JSON.stringify(data));
	}
}
window.requestAnimationFrame(runLoop);
