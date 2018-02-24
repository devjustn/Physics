# Physics Simulations 
Array of demos demonstrating a number of physics ideas

## Run simulation on browser
Point to the python file you want to run in app.js
``` javascript
fetch_code('./Fluid.py')
```

## Spin up a python server
Paste command in terminal
``` python3
python3 -m http.server
```
Demo will be in localhost:8000

## Vpython Starter Notes

### Objects

Variable named ball
``` vpython
ball = sphere(pos = vector(0,0,0), color = color.cyan, radius = ballRadius)
```

Reference ball's position attribute
``` vpython
ball.pos
```

Relative position vector - ball will have an arrow pointing towards ball_two
```
ball = sphere(pos = vector(0,0,0), color = color.cyan, radius = ballRadius)
ball_two = sphere(pos = vector(10,10,10), color = color.cyan, radius = ballRadius)
point = arrow(pos = ball.pos, axis = ball_two.pos - ball.pos, color = color.cyan ) # Arrow's beginning location - end location
```


### Loops and animation

Arrow will point to ball_two from ball as ball_two moves
```
r = vector(-3,4,0) # Destination
while ball_two.pos.x < 100:
	rate(100) # 100 calculations in 1 second
	ball_two.pos = ball_two.pos
	point.axis = ball_two.pos - ball.pos
	ball_two.pos.x = ball_two.pos.x + 1

```








