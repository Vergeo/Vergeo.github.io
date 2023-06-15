document.addEventListener('DOMContentLoaded', () =>{


	this.canvas = document.getElementById("canvas");
	this.ctx = this.canvas.getContext("2d");

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
				this.y -= 10;
			} else if (direction === "down" && this.y+10+this.height < canvas.height) {
				this.y += 10;
			}
		}

		shoot() {
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
			this.alive = true;
		}

		draw() {
			Gambar(this.source, this.x, this.y)
		}

		move() {
			this.x -= 7;

			if(this.x < 0 - 20){
				gameOverText.draw();
				return
			}
		}
	}


	document.addEventListener("keydown", () => {
		switch (event.code) {
			case "Space":
				MyGame.MySpaceShip.move("up");
				break;
			case "ArrowUp":
				MyGame.MySpaceShip.move("up");
				break;
			case "KeyW":
				MyGame.MySpaceShip.move("up");
				break;
			case "KeyS":
				MyGame.MySpaceShip.move("down");
				break;
			case "ArrowDown":
				MyGame.MySpaceShip.move("down");
				break;
			case "ShiftLeft":
				MyGame.MySpaceShip.move("down");
				break;
		}
	})

	document.querySelector("#canvas").addEventListener('click', function(event){
		if (!MyGame.start) startButton.checkClicked(event);
	})

	function blit(gambar, row, column){
			base_image = new Image();
			base_image.src = gambar;
			ctx.drawImage(base_image, row, column);
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
			ctx.fillText(`Score : ${MyGame.score}`, x, y);
		}
	}

	let gameOverText = {
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

	let startButton = {
		x : canvas.width/2,
		y : canvas.height/2,
		width : 10 * this.blockSize,
		height : 5 * this.blockSize,
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
	
	function checkCollision() {
		MyGame.enemies.forEach(function (enemy, i) {
			MySpaceShip.lasers.forEach(function(laser, i) {
				if (enemy.x < laser.x+laser.width &&
					enemy.x+enemy.width > laser.x &&
					enemy.y < laser.y + laser.height &&
					enemy.y + enemy.height > laser.y) {
					var index = MySpaceShip.lasers.indexOf(laser);
					MySpaceShip.lasers.splice(index, 1);

					var index_enemy = enemies.indexOf(enemy);
					enemies.splice(index_enemy, 1);
					score += 1;
					
				}
			})
		})
	}

	class TrashShooter {
		constructor() {

			this.score = 0;
			this.enemies = [];
			this.start = false;

			this.blockSize = 10;

			canvas.width = window.innerWidth-20;
			canvas.height = window.innerHeight-20;

			console.log()

			this.MySpaceShip = new SpaceShip("assets/spaceship2.png");
			console.log(this.MySpaceShip.lasers)

			this.counter = 0;
			this.many = 3;

			this.make_mainloop();
		}

		make_enemy () {
			let enemy = new Garbage(Math.floor(Math.random() * 1000 ) + canvas.width, Math.floor(Math.random() * (canvas.height-100))+50, "assets/garbage3.png", 3);
			enemies.unshift(enemy);
		}

		make_mainloop() {
			this.mainloop = setInterval(function() {
				blit("assets/background.jpg", 0, 0);
				


				scoreText.draw()
				// console.log(this.MySpaceShip.lasers)

				// this.MySpaceShip.lasers.forEach(function(laser, i) {
				// 	if (laser.x > canvas.width) {
				// 		myGame.lasers.pop();
				// 	}
				// })
				

				if (this.start){
					myGame.draw();
					myGame.drawLasers();
					myGame.moveLasers();
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

				if (this.enemies.length === 0){
					many += Math.floor(Math.random() * 3)

					for (var i=0; i < many; i++){
						make_enemy()
					}
				}

			}, 1000/60)
		}
	}

	MyGame = new TrashShooter();
	
})