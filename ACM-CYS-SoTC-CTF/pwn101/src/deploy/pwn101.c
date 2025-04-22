#include <stdio.h>
#include <unistd.h>

int main() {
  char message[100];
  char name[100];
  
  setvbuf(stdin, 0, _IONBF, 0);
  setvbuf(stdout, 0, _IONBF, 0);
  
  printf("Here's a gift for you: %p\n", message);

  write(1, "name: ", 7);
  read(0, name, 512);
  printf("hello %s\n", name);
  
  write(1, "message: ", 9);
  read(0, message, 512);
  printf("message: %s\n", message);
  
  return 0;
} 