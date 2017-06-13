window.onload = function() {
	var serverIP = location.host;
	var ws = new WebSocket(`ws://${serverIP}:8080`);

	ws.onmessage = function(event){
		var data = JSON.parse(event.data);
		switch(data.type){
			case 'image':
				var image = data.image;
				image = [].concat(...image.map(val => [val, val, val, 255])) // Convert to RGB (kinda)
				setImage('cameraView', image);
		}
	}

	var walk_data = {
		type: 'walk',
		steering: 0,
		speed: 0
	};

	var steer = new JustGage({
		id: 'steer',
		value: 0,
		min: -1,
		max: 1,
		gaugeColor: '#34495e',
		levelColors: ['#f39c12'],
		noGradient: true,
		hideMinMax: true,
		hideValue: true,
		refreshAnimationTime: 0.1
	});
	var l_knob = new AnalogStick(document.getElementById('lknob_container'));
	var r_knob = new AnalogStick(document.getElementById('rknob_container'));
	var info_div = document.getElementById('info');

	function runLoop(){
		window.requestAnimationFrame(runLoop);

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

			l_knob.set_axes(lX, lY);
			r_knob.set_axes(rX, rY);

			steer.refresh(steering);

			var speed = bA.pressed ? 0.2 : 0;
			if(walk_data.speed != speed || walk_data.steering != steering){
				walk_data.steering = steering;
				walk_data.speed = speed;
				ws.send(JSON.stringify(walk_data));
			}
		}
	}
	window.requestAnimationFrame(runLoop);


	function getCameraView(){
		ws.send(JSON.stringify({type: 'shoot'}));
	}

	function setImage(canvasID, image){
		var context = document.getElementById(canvasID).getContext('2d');
		var imageData = context.getImageData(0,0,200,200);
		imageData.data.forEach((val, index, arr) => arr[index] = image[index]);
		context.putImageData(imageData, 0,0);
	}

	setInterval(getCameraView, 1000);
	//setTimeout(getCameraView, 1000);
}
