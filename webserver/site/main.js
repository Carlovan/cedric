var serverIP = location.host;

var ws = new WebSocket(`ws://${serverIP}:8080`);

function runLoop(){
	var stateDiv = document.getElementById('stateDiv');
	window.requestAnimationFrame(runLoop);

	var gamepads = navigator.getGamepads();
	var sleft = '50%';
	var stop = '50%';
	var ssize = '50px';
	var sbgcolor = '#c0392b';

	if(gamepads.length == 0 || !gamepads[0]){
		stateDiv.innerHTML = 'No gamepad connected';
	}
	else{
		var gp = gamepads[0];

		var ax0 = gp.axes[2];
		var ax1 = gp.axes[3];
		sleft = `calc(50% + ${ax0 * 380}px)`;
		stop = `calc(50% + ${ax1 * 380}px)`;

		var bA = gp.buttons[6];
		ssize = `${bA.pressed ? 70 : ssize}px`;
		sbgcolor = bA.pressed ? '#2ecc71' : sbgcolor;

		var data = {
			'x': ax0,
			'y': ax1,
			'button': bA.pressed
		};
		if(ws.readyState == ws.OPEN)
			ws.send(JSON.stringify(data));
	}
	stateDiv.style.left = sleft;
	stateDiv.style.top  = stop;
	stateDiv.style.height = ssize;
	stateDiv.style.width = ssize;
	stateDiv.style.backgroundColor = sbgcolor;
}
window.requestAnimationFrame(runLoop);
