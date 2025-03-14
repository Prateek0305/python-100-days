<html>
<body>
    <h1>Reeborg's World Challenges</h1>
    <h2>Hurdle Challenges</h2>
    <h3>Hurdle 1</h3>
    <p>Fixed number of evenly spaced hurdles. The logic is to move forward and jump over obstacles using a loop. Since the number of hurdles is known, we use a for loop to iterate through all jumps.</p>
    <h3>Hurdle 2</h3>
    <p>Unknown number of evenly spaced hurdles. The approach is similar to Hurdle 1, but since we don't know the number of hurdles in advance, we use a while loop that runs until the goal is reached.</p> 
    <h3>Hurdle 3</h3>
    <p>Hurdles have varying heights. We need to check the height of each hurdle and adjust our jump accordingly. This requires a flexible jump function that can handle different obstacle heights dynamically.</p>
    <h3>Hurdle 4</h3>
    <p>Hurdles are randomly spaced. We need to check if the path is clear before moving. If a hurdle is encountered, we jump; otherwise, we keep moving forward. This requires an additional condition to check if there’s an obstacle in front.</p>
    <h2>Maze Challenge</h2>
    <p>The maze has walls blocking direct movement. The strategy used is the right-hand rule, where we always try to keep the right side free. If there’s space to the right, we turn and move; if not, we move forward; otherwise, we turn left to find a path.</p>
</body>
</html>
