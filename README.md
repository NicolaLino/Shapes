### Shapes


My little brother is recently learning about shapes and colors at school, and he asked me to evaluate his progress, so I created an annotation game for him, and I need your help with this. There are 100 different records representing geometric shapes with different colors, which are Circles or Squares. His answers were added to a text file in the following format:

                                                Shape Type;Number;Color;Measure
                                                
Shape Type: Circle or Square.

Number: An identifier number for each shape.

Color: The shape color (Red, Green or Blue)

Measure: For circles, it’s the radius and for squares it’s the side length.


 # To give a hand, you should do the following using Python:
 
1. Create a class for each shape (Class for Circle & Class for Square), which extend a parent class called Shape (see below).
2. Add the needed attributes for each created class and override calc_area function (radius or side) to calculate the area of each shape.
3. Read data from an input file. The file contains data with the above format (assume that the data in the correct format). 
4. Create an object for each record (each reeded line from data file) based on its type and save them in an appropriate data structure.
5. Create a menu that has 3 options as follows (you should write a function for each option):

    a. Print colors frequency for each Shape.
    
    b. Print the average area for each type. The program must raise an error ‘{ShapeType} Average Below 
    100’ if any average is below 100. And handle it outside the function.
    
    c. Find and print details of shapes with min and max area for each type.
