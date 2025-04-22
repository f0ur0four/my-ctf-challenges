#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void initialize() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

int main(int argc, char *argv[]) {
    initialize();
    while(1){
        printf("\n[1] Echo\n");
        printf("[2] Exit\n");
        printf("> ");
        char c = getchar();
        getchar();
        if(c == '1'){
            char *buf = malloc(1024);
            char echo[1024];
            printf("echo> ");
            fgets(echo, 1024, stdin);
            printf(echo);
            free(buf);
        } else {
            printf("Goodbye!\n");
            break;
        }
    }
    return 0;
}