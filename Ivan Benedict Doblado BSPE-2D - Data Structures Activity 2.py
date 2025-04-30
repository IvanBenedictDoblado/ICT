{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "baa3264c-ac8c-4037-a24e-27f97d1d9118",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1st Matrix:\n",
      "[[ 1 16  3]\n",
      " [ 9  2  4]]\n",
      "\n",
      "2nd Matrix:\n",
      "[[2 0 2]\n",
      " [0 4 8]]\n",
      "\n",
      "3rd Matrix (matrix1 + matrix2):\n",
      "[[ 3 16  5]\n",
      " [ 9  6 12]]\n",
      "\n",
      "4th Matrix (matrix1 * 2):\n",
      "[[ 2 32  6]\n",
      " [18  4  8]]\n",
      "\n",
      "5th Matrix (Transpose of Matrix2):\n",
      "[[2 0]\n",
      " [0 4]\n",
      " [2 8]]\n",
      "\n",
      "6th Matrix (matrix3 x matrix5):\n",
      "[[ 16 104]\n",
      " [ 42 120]]\n",
      "\n",
      "Sum of elements in 3rd Matrix: 51\n",
      "\n",
      "7th Matrix (Zero Matrix 2x3):\n",
      "[[0 0 0]\n",
      " [0 0 0]]\n"
     ]
    }
   ],
   "source": [
    "LetterisNumber = {'a':1,'b':2,'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,\n",
    "    'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':19, 's':19,\n",
    "    't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26\n",
    "}\n",
    "\n",
    "def convert_letters_to_numbers(letters):\n",
    "    return [LetterisNumber[char.lower()] for char in letters]\n",
    "\n",
    "initials = \"APC\"\n",
    "second_letters = \"IBD\"\n",
    "row1 = convert_letters_to_numbers(initials)\n",
    "row2 = convert_letters_to_numbers(second_letters)\n",
    "matrix1 = np.array([row1, row2])\n",
    "\n",
    "matrix2 = np.array([[2, 0, 2], [0, 4, 8]])\n",
    "\n",
    "print(\"1st Matrix:\")\n",
    "print(matrix1)\n",
    "\n",
    "print(\"\\n2nd Matrix:\")\n",
    "print(matrix2)\n",
    "\n",
    "matrix3 = matrix1 + matrix2\n",
    "print(\"\\n3rd Matrix (matrix1 + matrix2):\")\n",
    "print(matrix3)\n",
    "\n",
    "matrix4 = matrix1 * 2\n",
    "print(\"\\n4th Matrix (matrix1 * 2):\")\n",
    "print(matrix4)\n",
    "\n",
    "matrix5 = matrix2.T\n",
    "print(\"\\n5th Matrix (Transpose of Matrix2):\")\n",
    "print(matrix5)\n",
    "\n",
    "matrix6 = np.dot(matrix3, matrix5)\n",
    "\n",
    "print(\"\\n6th Matrix (matrix3 x matrix5):\")\n",
    "print(matrix6)\n",
    "\n",
    "sum_matrix3 = np.sum(matrix3)\n",
    "print(\"\\nSum of elements in 3rd Matrix:\", sum_matrix3)\n",
    "\n",
    "matrix7 = np.zeros((2,3), dtype=int)\n",
    "print(\"\\n7th Matrix (Zero Matrix 2x3):\")\n",
    "print(matrix7)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d44cad58-7ce7-46bb-a5de-7c326d2663b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
