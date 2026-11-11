# Python Turtle House Challenge

## Your mission

Your team is opening a tiny neighborhood! Design a colorful house with Python turtle graphics, give it a name, and introduce it to the class. Build it with **exactly two functions** that your team writes.

- **Group size:** 2–3 students.
- **Suggested time:** 45–60 minutes.
- **Practice:** functions, parameters, loops, colors, and positioning.
- **Program file:** `turtle_house.py`, directly in the repository root.

## Choose your team roles

| Role | Responsibility |
| --- | --- |
| Driver | Type the code and run the program. |
| Navigator | Read the instructions and suggest the next step. |
| Designer and tester | Choose the look and check the drawing. |

Switch roles after each building stage so everyone gets a turn coding. In a group of two, share the designer and tester role.

## Plan your house together

Pick a theme: a candy cottage, a space house, a beach bungalow, or your own idea. Keep the first version simple: one square and one triangle.

Discuss and record your house name, theme, wall color, and roof color in comments at the top of your Python file. Include every group member's name.

## Your building rules

1. Define exactly two functions: `draw_house(size, color)` and `draw_roof(size, color)`. Do not add a main function.
2. Use a `for` loop in each function. The `size` parameter controls side length; `color` controls the fill color.
3. Each shape starts facing right. Each function returns the turtle to its starting position and direction.
4. Use the same size for the square and triangle so the roof fits.
5. Add a short comment above each function explaining what it draws.
6. Use different colors for the walls and roof.

Everyone should be able to explain a function call and how changing an argument changes the drawing.

## Build your house step by step

### 1 — Set up your drawing

Open `turtle_house.py`. Import `turtle`, choose a background color, and set a comfortable drawing speed. Run locally on a computer with a graphics window. See the [README](README.md) for VS Code setup.

### 2 — Build the walls

Define `draw_house(size, color)`. Set the color, begin filling, and use a loop to draw four equal sides with a 90-degree left turn after each side. End the fill. Test this function before continuing. Switch team roles.

### 3 — Build the roof

Define `draw_roof(size, color)`. Set the color and use a filled triangle with three equal sides and a 120-degree left turn after each side. Test it on its own. Switch team roles again.

**Think about it:** Why does the turtle turn 120 degrees for a triangle even though each inside angle is 60 degrees?

### 4 — Put the pieces together

Below your function definitions:

1. Lift the pen, move to **(-100, -100)**, face right with `turtle.setheading(0)`, and lower the pen.
2. Call your house function with a side length of **150** and your wall color.
3. Lift the pen and move to **(-100, 50)**, the top-left corner of the square.
4. Face right, lower the pen, and call your roof function with a side length of **150** and your roof color.

**Checkpoint:** The roof base should sit directly on the top edge of the square. There should be no diagonal line connecting the two starting positions.

### 5 — Add your team personality

Choose one small extra: a house name with `turtle.write()`, a sun with `turtle.circle()`, or a door drawn with movement commands. Put these extra commands below the function definitions; do not define another function.

Finish with `turtle.hideturtle()` and `turtle.done()` so the finished drawing stays visible.

## Quick command guide

These are individual command reminders, not a complete solution.

| Command | Purpose |
| --- | --- |
| `turtle.forward(150)` | Move forward 150 steps. |
| `turtle.left(90)` | Turn left 90 degrees. |
| `turtle.penup()` | Move without drawing. |
| `turtle.pendown()` | Draw while moving again. |
| `turtle.goto(-100, 50)` | Move to a particular x and y position. |
| `turtle.setheading(0)` | Face right. |
| `turtle.color("coral")` | Set the drawing and fill color. |
| `turtle.begin_fill()` | Start a filled shape. |
| `turtle.end_fill()` | Finish filling the shape. |

## Test your work

- [ ] The program runs without errors.
- [ ] There are exactly two function definitions, each with a loop.
- [ ] The house is a filled square and the roof is a filled triangle.
- [ ] The two shapes line up and use different colors.
- [ ] There are no unwanted connecting lines.
- [ ] Your team added one creative detail.
- [ ] Each function ends at its starting position, facing right.
- [ ] Every team member can explain the program.

**Debug together:** If a line appears where it should not, check the pen state before moving. If a shape points the wrong way, check the heading and turns. Fix one issue, then run again.

## Share your creation

Give a one-minute house tour: introduce the theme, explain one function, and share one bug your team fixed. Each member should contribute to the explanation.

Submit one shared repository link and one screenshot through Blackboard Ultra as directed. Your repository must contain:

- Your completed `turtle_house.py` with all group members' names.
- A completed `AI-Use-Report.md`, including when no AI was used and each member's contribution.
- The course instructions and configuration files supplied in this starter.

Read and follow [AI-Use-Policy.md](AI-Use-Policy.md). AI may explain concepts and provide small hints; your group must write and understand its own program.

## Bonus challenge

Reuse the same two functions to draw a smaller neighboring house. Change the size and colors without editing either function definition. Plan a new starting point and calculate the roof position from the new house size.
