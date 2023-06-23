#include <stdio.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8000
int startServer(int PORT, int IPA){ 
    int sfd;
    if ((sfd = socket(AF_INET,SOCK_STREAM,0))<0) {
        perror("Socket creation failed"); 
        exit(EXIT_FAILURE);
    };
    
}
int main() { 
    printf("hello"); 
    return 0;
}
