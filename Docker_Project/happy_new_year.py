import turtle
import random
import math
import time

# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Happy New Year 2025!")

# Particle class for fireworks
class Particle(turtle.Turtle):
    def __init__(self, x, y, color, angle, speed):
        super().__init__()
        self.shape("circle")
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.direction = math.radians(angle)
        self.speed_value = speed
        self.gravity = 0.2
        self.lifetime = 50

    def move(self):
        # Update position based on angle and speed
        self.setx(self.xcor() + math.cos(self.direction) * self.speed_value)
        self.sety(self.ycor() + math.sin(self.direction) * self.speed_value - self.gravity)
        self.speed_value *= 0.98  # Simulate air resistance
        self.lifetime -= 1

# Firework class
class Firework:
    def __init__(self, x, y):
        self.particles = []
        self.color = random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
        for angle in range(0, 360, 10):
            speed = random.uniform(3, 7)
            particle = Particle(x, y, self.color, angle, speed)
            self.particles.append(particle)

    def update(self):
        for particle in self.particles:
            if particle.lifetime > 0:
                particle.move()
            else:
                particle.hideturtle()  # Hide particles once their lifetime ends

# Display text
def display_text():
    text = turtle.Turtle()
    text.hideturtle()
    text.color("white")
    text.penup()
    text.goto(0, 200)
    text.write("Happy New Year 2025!", align="center", font=("Arial", 36, "bold"))

# Firework animation loop
def firework_show():
    fireworks = []
    for _ in range(15):  # Number of fireworks
        x = random.randint(-300, 300)
        y = random.randint(0, 300)
        fireworks.append(Firework(x, y))
        time.sleep(0.5)  # Delay between each firework

    for _ in range(50):  # Animation frames
        screen.update()
        for firework in fireworks:
            firework.update()

# Run the celebration
screen.tracer(0)  # Turn off automatic updates for smooth animation
display_text()
firework_show()
screen.update()

# Keep the screen open
screen.mainloop()
