# Exercise 2

This will result in an undefined behavior. The reason is that we have a defined a pointer line and initialized it to a null pointer or 0, which means it points to nothing in memory. Then you attempt to copy the string to the location where line points, but since line is an uninitialized pointer, there is no valid memory area to copy the string to.

If we wanted to avoid such undefined behavior we would need to allocate memory for line before copying the string into it, for example using malloc to dynamically allocate memory, or some other way.
