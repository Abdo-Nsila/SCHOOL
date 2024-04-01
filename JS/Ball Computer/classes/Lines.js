class Lines {
  constructor() {
    this.lines = [];
  }

  update() {
    // Check if the ball touches the circle
    if (ball.touches(circle)) {
      // Create a new line from the touch point to the center of the ball
      const line = new Line(ball.touchPoint, ball.center);
      this.lines.push(line);
    }
  }

  draw() {
    // Draw all the lines
    this.lines.forEach((line) => {
      line.draw();
    });
  }
}

class Line {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  draw() {
    // Use a drawing library or canvas API to draw the line
    ctx.strokeStyle = `hsl(${hsl}, 100%, 50%)`;
    ctx.lineWidth = BORDER_WIDTH;
    ctx.beginPath();
    ctx.moveTo(this.start.x, this.start.y);
    ctx.lineTo(ball.x, ball.y);
    // ctx.lineTo(this.end.x, this.end.y);
    ctx.stroke();
  }
}
