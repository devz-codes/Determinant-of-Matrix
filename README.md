# Determinant-of-Matrix
Python Code to Calculate the Determinant of a Square Matrix

The Determinant of A Square Matrix can be calculated by reducing the matrix to a upper triangular form and them multiplying the diagonal elements.

Let there be a 3x3 Matrix :- 

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad1\quad0 \\5\quad4\quad3\\2\quad1\quad3\end{bmatrix}">

<img src="https://render.githubusercontent.com/render/math?math=By\quad\R2->R2-5*R1">

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad1\quad0 \\0\quad-1\quad3\\2\quad1\quad3\end{bmatrix}">

<img src="https://render.githubusercontent.com/render/math?math=By\quad\R3->R3-2*R1">

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad1\quad0 \\0\quad-1\quad3\\0\quad-1\quad3\end{bmatrix}">

<img src="https://render.githubusercontent.com/render/math?math=By\quad\R3->R3-R2">

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad1\quad0 \\0\quad-1\quad3\\0\quad0\quad0\end{bmatrix}">

As the matrix is now in upper triangular form, 

<img src="https://render.githubusercontent.com/render/math?math=Determinant = 1*-1*0=0">

If any of the diagonal elements are zero, then the rows have to be swapped.. For eg, in the below matrix :- 

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad0\quad10 \\5\quad0\quad3\\2\quad1\quad3\end{bmatrix}">


<img src="https://render.githubusercontent.com/render/math?math=By\quad\R2->R2-5*R1">


<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad0\quad10 \\0\quad0\quad-47\\2\quad1\quad3\end{bmatrix}">


<img src="https://render.githubusercontent.com/render/math?math=By\quad\R3->R3-2*R1">

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad0\quad10 \\0\quad0\quad-47\\0\quad1\quad-17\end{bmatrix}">

As for the second row, the diagonal element is 0, by swapping R2 with R3

<img src="https://render.githubusercontent.com/render/math?math=\begin{bmatrix}\1\quad0\quad10 \\0\quad1\quad-17\\0\quad0\quad-47\end{bmatrix}">

By swapping the rows, the sign of the final product would change from + to -. If the rows are further swapped, then the sign of the product would change to + from -

As the matrix is in upper triangular form, 

<img src="https://render.githubusercontent.com/render/math?math=Determinant = -1*(1 * 1 * -47)=47">


