# Remove comments from a C file

This script is written to remove comments from a given C file.

Example:

```
// Remove comments from main.c file
// main.c contents:
int main()
{
   // printf() displays the string inside quotation
   printf("Hello, World!");
   printf("foo"); /* More comments
And more comments
*/ return 0;
}
```

Expected output:

```
int main()
{
   printf("Hello, World!");
   return 0;
}
```
