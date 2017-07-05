function AnalogStick(container, color) {
	this.x_axis = 0;
	this.y_axis = 0;

	this.circle = document.createElement('div');
	this.circle.style.width = '100%';
	this.circle.style.height = '100%';
	//this.circle.style.border = '1px solid #444';
	this.circle.style.borderRadius = '50%';
	this.circle.style.position = 'relative';
	this.circle.style.background = 'radial-gradient(ellipse at center, #2980b9 0%, rgba(0,0,0,0) 110%)';
	this.circle.style.boxShadow = '5px 10px 10px 0px rgba(21, 108, 165, 0.3)';
	container.appendChild(this.circle);

	this.indicator = document.createElement('div');
	this.indicator.style.width = '10%';
	this.indicator.style.height = '10%';
	this.indicator.style.borderRadius = '50%';
	this.indicator.style.transform = 'translate(-50%, -50%)';
	this.indicator.style.backgroundColor = color || '#c0392b';
	this.indicator.style.position = 'absolute';
	this.indicator.style.top = '50%';
	this.indicator.style.left = '50%';
	this.circle.appendChild(this.indicator);

	this.set_axes = function(x, y) {
		this.x_axis = Math.min(Math.max(x, -1), 1);
		this.y_axis = Math.min(Math.max(y, -1), 1);
		this.refresh();
	}

	this.refresh = function(){
		var left = 50 + 45*this.x_axis;
		var top = 50 + 45*this.y_axis;
		this.indicator.style.left = left + '%';
		this.indicator.style.top = top + '%';
	}
}
