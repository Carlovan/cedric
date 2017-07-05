function ascii(c) {
	return c.charCodeAt(0);
}

var gross;

window.onload = function() {
	var serverIP = location.host;
	var ws = new WebSocket(`ws://${serverIP}:8080`);

	ws.onmessage = function(event){
		var data = JSON.parse(event.data);
		switch(data.type){
			case 'image':
				var image = data.image.data;
				image = [].concat(...image.map(function(val){
					return [val, val, val, 255];
				})); // Convert to RGB (kinda)
				//console.log(image[0]);
				setImage('cameraView', image);
				break;
			case 'nn_steering':
				setNeuralNetSteering(data.steering);
				break;
		}
	}

	var walk_data = {
		type: 'walk',
		steering: 0,
		speed: 0
	};

	var steer = document.getElementById('steer_indicator');
	var l_knob = new AnalogStick(document.getElementById('lknob_container'));
	var r_knob = new AnalogStick(document.getElementById('rknob_container'));
	var info_div = document.getElementById('info');

	function runLoop(){
		//window.requestAnimationFrame(runLoop);

		var gamepads = navigator.getGamepads();

		if(gamepads.length == 0 || !gamepads[0]){
			info_div.innerHTML = 'No gamepad connected';
		}
		else{
			info_div.innerHTML = '';
			var gp = gamepads[0];

			var rX = gp.axes[2];
			var rY = gp.axes[3];
			var lX = gp.axes[0];
			var lY = gp.axes[1];

			var bA = gp.buttons[6];

			// Calculate the steering value
			var steering = Math.min(1, Math.max(-1, rX + lX/5 ));
			steering = Math.round(steering * 100) / 100;
			//steering *= 0.95;

			l_knob.set_axes(lX, lY);
			r_knob.set_axes(rX, rY);

			steer.value = steering;

			var speed = bA.pressed ? 0.1 : 0;
			if(walk_data.speed != speed || walk_data.steering != steering){
				walk_data.steering = steering;
				walk_data.speed = speed;
				ws.send(JSON.stringify(walk_data));
			}
		}
	}
	//window.requestAnimationFrame(runLoop);
	setInterval(runLoop, 10);


	function getCameraView(){
		ws.send(JSON.stringify({type: 'shoot'}));
	}

	function setImage(canvasID, image){
		var context = document.getElementById(canvasID).getContext('2d');
		var imageData = context.getImageData(0,0,100,100);
		imageData.data.forEach((val, index, arr) => arr[index] = image[index]);
		context.putImageData(imageData, 0,0);
	}
	setInterval(getCameraView, 700);
	//setTimeout(getCameraView, 1000);

	function getNeuralNetSteering(){
		ws.send(JSON.stringify({type: 'nn_steering'}))
	}
	function setNeuralNetSteering(value){
		document.getElementById('nn_steer_indicator').value = value;
	}
	setInterval(getNeuralNetSteering, 500);
}
