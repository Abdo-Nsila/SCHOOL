class Enemy {
    constructor(x, y, radius, color, velocity) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.color = color;
      this.velocity = velocity;
    }
  
    draw() {
      c.beginPath();
      c.fillStyle = this.color;
      c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
      c.fill();
    }
  
    update() {
      this.draw();
      this.x += this.velocity.x;
      this.y += this.velocity.y;
    }
  }