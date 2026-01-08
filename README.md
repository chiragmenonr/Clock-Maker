# Clock Display (Python Turtle)

## Description

This project is a Python program that uses the built-in **`turtle`** graphics module to create a visual **analog clock**. The program asks the user to input an hour and a minute, then draws a clock face and positions the hour and minute hands to match the entered time.

The drawing process is animated, allowing the viewer to see the clock being constructed step by step.

---

## Program Behavior

* Prompts the user for an **hour** and **minute**
* Draws a circular clock face
* Adds 12 tick marks to represent the hours
* Calculates correct angles for both clock hands
* Draws the minute hand first, followed by the hour hand
* Hides the turtle after the drawing is complete

---

## Visualization

The animation below shows the clock face being drawn first, followed by a transition to the minute hand and then the hour hand based on user input:

https://github.com/user-attachments/assets/d65e2c4c-ebee-41ce-8fa4-fc4c61398dde

---

## Angle Logic

* Each minute corresponds to **6 degrees** of rotation (360° ÷ 60)
* Each hour corresponds to **30 degrees**, with an additional adjustment based on the minutes

This allows the hour hand to move smoothly between hour markers instead of jumping directly from one number to the next.

---

## Requirements

* Python 3.x
* Python’s built-in `turtle` module

---

## Running the Program

1. Make sure Python is installed.
2. Save the file as `clock_display.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python clock_display.py
   ```
5. Enter an hour and minute when prompted to see the clock displayed.

---

## Concepts Demonstrated

* Turtle graphics and animation
* Loops and rotation
* User input handling
* Geometric reasoning with angles
* Screen and turtle control
