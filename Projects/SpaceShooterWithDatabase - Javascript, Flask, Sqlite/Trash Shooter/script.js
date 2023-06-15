document.addEventListener('DOMContentLoaded', () =>{

	let canvas = document.getElementById("canvas");
	let ctx = canvas.getContext("2d");

	let score = 0;
	let enemies = []
	let start = false;

	const blockSize = 10

	// resize screen
	canvas.width = window.innerWidth-20;
	canvas.height = window.innerHeight-20;

	// function draw()
	function Gambar(gambar,row,column){
		let base_image = new Image();
		base_image.src = gambar;
		ctx.drawImage(base_image, row, column);
	}

	class SpaceShip {
		constructor(source) {
			this.x = 40;
			this.y = canvas.height/2;
			this.source = source;
			this.width = 100;
			this.height = 93;
			this.lasers = [];
			
		}

		draw() {
			Gambar(this.source, this.x, this.y);
		}

		move(direction) {
			if (direction === "up" && this.y-10 > 0) {
				this.y -= 7;
			} else if (direction === "down" && this.y+10+this.height < canvas.height) {
				this.y += 7;
			}
		}

		shoot() {
			let sound = new Audio("assets/shoot.wav")
			sound.play();
			let laser = new Laser(this.x + this.width + 10, this.y + this.height/2, "assets/laser.png");
			this.lasers.unshift(laser);
			
			// console.log(this.lasers);
		}

		drawLasers() {
			this.lasers.forEach(function(laser, i) {
				laser.draw();
			})
		}

		moveLasers() {
			this.lasers.forEach(function(laser, i) {
				laser.move();
			})
		}


	}

	let scoreText = {
		font : "37px Courier",
		color : "Lavender",
		align : "left",
		baseline : "top",

		draw : function () {
			const x = 0;
			const y = 0;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Score : ${score}`, x, y);
		}
	}

	const gameOverText = {
		font : "60px Courier",
		color : "White",
		align : "center",
		baseline : "middle",

		draw : function () {
			clearInterval(mainloop);
			const x = canvas.width/2;
			const y = canvas.height/2;
			ctx.font = this.font;
			ctx.fillStyle = this.color;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText(`Game Over`, x, y);
		}
	}

	const startButton = {
		x : canvas.width/2,
		y : canvas.height/2,
		width : 10 * blockSize,
		height : 5 * blockSize,
		color : "White",
		textColor : "Black",
		font : "32px Courier",
		align : "center",
		baseline : "middle",

		draw : function (){
			ctx.fillStyle = this.color;
			ctx.fillRect(this.x - this.width/2, this.y - this.height/2, this.width, this.height);

			ctx.fillStyle = this.textColor;
			ctx.font = this.font;
			ctx.textAlign = this.align;
			ctx.textBaseline = this.baseline;
			ctx.fillText('Start', this.x, this.y);
		},

		checkClicked : function (event){
			if ((event.offsetX >= this.x- this.width/2) && (event.offsetY >= this.y- this.height/2) && (event.offsetX <= (this.x+this.width/2)) && (event.offsetY <= (this.y+this.height/2))) start = true;
		}

	}

	class Laser {
		constructor(x, y, source) {
			this.x = x;
			this.y = y;
			this.source = source;
			this.width = 41;
			this.height = 6;
		}

		draw() {
			Gambar(this.source, this.x, this.y);
		}

		move() {
			this.x += 10;

		}
	}

	class Garbage {
		constructor(x, y, source, hp) {
			this.x = x;
			this.y = y;
			this.source = source;
			this.width = 50;
			this.height = 50;
			this.hp = hp;
			this.maxhp = hp
			this.alive = true;
		}

		draw() {
			Gambar(this.source, this.x, this.y)
			// let base_image = new Image();
			// base_image.src = this.source;
			// ctx.drawImage(base_image.rotate(90), row, column);
			ctx.fillStyle = "Red";
			ctx.fillRect(this.x, this.y+52, 50, 5);
			ctx.fillStyle = "Green";
			ctx.fillRect(this.x, this.y+52, this.hp/this.maxhp*50, 5);
		}

		move() {
			this.x -= 7;

			if(this.x < 0 - 20){
				gameOverText.draw();
				let sound = new Audio("assets/gameover.wav")
				sound.play();
				return
			}
		}
	}

	!function(a){var f=function(){var n={forEach:function(n,e){var t;for(t in n)n.hasOwnProperty(t)&&e(n[t],t)}},e=n.forEach;n.getTranspose=function(n){var t={};return e(n,function(n,e){t[n]=e}),t},n.indexOf=function(n,e){if(n.indexOf)return n.indexOf(e);var t,o=n.length;for(t=0;t<o;t++)if(n[t]===e)return t;return-1};var o=n.indexOf;return n.pushUnique=function(n,e){return-1===o(n,e)&&(n.push(e),!0)},n.removeValue=function(n,e){var t=o(n,e);if(-1!==t)return n.splice(t,1)[0]},n.documentOn=function(n,e){a.addEventListener?a.addEventListener(n,e,!1):document.attachEvent&&document.attachEvent("on"+n,e)},n.requestAnimationFrame=a.requestAnimationFrame||a.webkitRequestAnimationFrame||a.mozRequestAnimationFrame||function(n){a.setTimeout(n,1e3/60)},n.noop=function(){},n}(),n={ZERO:48,ONE:49,TWO:50,THREE:51,FOUR:52,FIVE:53,SIX:54,SEVEN:55,EIGHT:56,NINE:57,A:65,B:66,C:67,D:68,E:69,F:70,G:71,H:72,I:73,J:74,K:75,L:76,M:77,N:78,O:79,P:80,Q:81,R:82,S:83,T:84,U:85,V:86,W:87,X:88,Y:89,Z:90,ENTER:13,SHIFT:16,ESC:27,SPACE:32,LEFT:37,UP:38,RIGHT:39,DOWN:40,BACKSPACE:8,DELETE:46,TAB:9,TILDE:192},p=f.getTranspose(n),e=[],t=function(){"use strict";function n(n){this.keyCode=n,this.cachedKeypressEvent=null}function t(n,e,t,o){t?n[e]=t:n[e](o)}return n.prototype._downHandler=f.noop,n.prototype._upHandler=f.noop,n.prototype._pressHandler=f.noop,n.prototype.isDown=function(){return-1!==f.indexOf(e,this.keyCode)},n.prototype.down=function(n){t(this,"_downHandler",n,this.cachedKeypressEvent)},n.prototype.up=function(n,e){t(this,"_upHandler",n,e)},n.prototype.press=function(n,e){this.cachedKeypressEvent=e,t(this,"_pressHandler",n,e)},n.prototype.unbindDown=function(){this._downHandler=f.noop},n.prototype.unbindUp=function(){this._upHandler=f.noop},n.prototype.unbindPress=function(){this._pressHandler=f.noop},n}(),o=function(i){"use strict";var c={};c.Key=t;var o=!1,r=Date.now?Date.now:function(){return+new Date},u=r();return c.tick=function(){var n,e=i.length;for(n=0;n<e;n++){var t=i[n],o=p[t];o&&c[o].down()}},c.run=function(n){o=!0;var e=r(),t=e-u;f.requestAnimationFrame.call(a,function(){o&&(c.run(n),n(t,e))}),u=e},c.stop=function(){o=!1},f.forEach(n,function(n,e){c[e]=new t(n)}),f.documentOn("keydown",function(n){var e=n.keyCode,t=p[e],o=f.pushUnique(i,e),r=c[t];if(r){var u=r.cachedKeypressEvent||{};(u.ctrlKey||u.shiftKey||u.metaKey)&&(o=!0),o&&r.press(null,n)}}),f.documentOn("keyup",function(n){var e=f.removeValue(i,n.keyCode),t=p[e];t&&c[t].up(null,n)}),f.documentOn("blur",function(n){f.forEach(i,function(n){var e=p[n];e&&c[e].up()}),i.length=0}),c}(e);"object"==typeof module&&"object"==typeof module.exports?module.exports=o:"function"==typeof define&&define.amd?define(function(){return o}):a.kd=o}(window);


	kd.W.down(function () {
		MySpaceShip.move("up");
	});
	kd.S.down(function () {
		MySpaceShip.move("down");
	});

	kd.run(function () {
		kd.tick();
	});

	document.querySelector("#canvas").addEventListener('click', function(event){
		if (!start) startButton.checkClicked(event);
	})

	let MySpaceShip = new SpaceShip("assets/spaceship2.png");

	assets = []
	// assets[Math.floor(Math.random()*assets.length)]

	function make_enemy () {
		let enemy = new Garbage(Math.floor(Math.random() * 1000 ) + canvas.width, Math.floor(Math.random() * (canvas.height-100))+50, "assets/garbage3.png", Math.floor(Math.random() * 2)+1);
		enemies.unshift(enemy);
	}

	let counter = 0;

	function checkCollision() {
		enemies.forEach(function (enemy, i) {
			MySpaceShip.lasers.forEach(function(laser, i) {
				if (enemy.x < laser.x+laser.width &&
					enemy.x+enemy.width > laser.x &&
					enemy.y < laser.y + laser.height &&
					enemy.y + enemy.height > laser.y) {
					var index = MySpaceShip.lasers.indexOf(laser);
					MySpaceShip.lasers.splice(index, 1);

					var index_enemy = enemies.indexOf(enemy);
					enemies[index_enemy].hp -= 1
					// let sound = new Audio("assets/hit2.wav")
					// sound.play();
					// console.log(enemies[index_enemy].hp)
					if (enemies[index_enemy].hp === 0){
						let sound = new Audio("assets/die.wav")
						sound.play();
						enemies.splice(index_enemy, 1);
						score += 1;
					}
						
				}
			})
		})
	}

	let many = 3;

	let mainloop = setInterval(function() {
		Gambar("assets/background.jpg", 0, 0);
		


		scoreText.draw()

		MySpaceShip.lasers.forEach(function(laser, i) {
			if (laser.x > canvas.width) {
				MySpaceShip.lasers.pop();
			}
		})
		

		if (start){
			MySpaceShip.draw();
			MySpaceShip.drawLasers();
			MySpaceShip.moveLasers();
			counter += 1;
			if (counter === 10) {
				MySpaceShip.shoot();
				counter = 0;
			}
			enemies.forEach(function(enemy, i) {
				enemy.draw();
				enemy.move();
			})						
		} else {
			startButton.draw()
		}


		checkCollision();

		if (enemies.length === 0){
			many += Math.floor(Math.random() * 3)

			for (var i=0; i < many; i++){
				make_enemy()
			}
		}

	}, 1000/60)
})