# Exercise 3

There are some problems and potential wrongs in this programming snippet, i will list it below.

1. Buffer Overflow
The text string is defined as a character array with a size of 5 characters. If the user enters a string longer than 4 characters (plus the null terminator), this will lead to a buffer overflow, potentially overwriting memory beyond the boundaries of the text array, resulting in unpredictable behavior.

2. Unbounded input
cin >> text allows the user to input text without restricting it to a maximum length of 4 characters, giving the user the opportunity to input a string that is to long for the text array.

3. Infinite loop
Of the user does not enter the letter e in the input, the (while (*pointer != search_for)) loop will never terminate, causing the program to enter an infinite loop.

4. Missing Null Terminator
After the loop has terminated, the text array will not contain a null terminator. This can cause issues if you intend to treat text as a C-string later in the program.
