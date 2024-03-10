class Cercle {
    constructor({
      x,
      y,
      radius,
      color,
      approchRadius,
      approchSpeed,
      velocity,
      number = 1,
    }) {
      this.x = x;
      this.y = y;
      this.radius = radius;
      this.color = color;
      this.approchRadius = approchRadius;
      this.approchSpeed = approchSpeed;
      this.velocity = velocity;
      this.number = number;
    }
  
    drawNumber() {
      if (this.number < 10) {
        const x = this.x - FONT_SIZE / 4;
        const y = this.y + FONT_SIZE / 2;
        c.fillStyle = "white";
        c.font = `${FONT_SIZE}px Arial`;
        c.fillText(this.number, x, y);
      } else {
        this.number = 1;
        COMBO = 1;
      }
    }
  
    drawMainCercle() {
      c.strokeStyle = BORDER_COLOR;
      c.lineWidth = BORDER_WIDTH;
      c.save();
      c.beginPath();
      c.fillStyle = this.color;
      c.arc(this.x, this.y, this.radius, 0, Math.PI * 2, false);
      c.fill();
      c.restore();
      c.stroke();
    }
  
    drawArroundCercle() {
      c.strokeStyle = this.color;
      c.lineWidth = BORDER_WIDTH;
      c.save();
      c.beginPath();
      c.fillStyle = "transparent";
      c.arc(
        this.x,
        this.y,
        this.radius + this.approchRadius,
        0,
        Math.PI * 2,
        false
      );
      c.fill();
      c.restore();
      c.stroke();
    }
  
    update() {
      if (c.globalAlpha < 1) {
        c.globalAlpha += (APPROCH_SPEED / APPROCH_RADIUS) * 1.6;
      }
      this.drawMainCercle();
      this.drawArroundCercle();
      this.drawNumber();
      // this.x += this.velocity.x;
      // this.y += this.velocity.y;
    }
  }