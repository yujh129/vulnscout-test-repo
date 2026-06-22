/**
 * Buffer utilities — fixed for VulnScout testing.
 */
#include <cstring>
#include <cstdio>

void copy_data(char *input) {
    char buffer[64];
    // Safe: use strncpy with bounds checking
    strncpy(buffer, input, sizeof(buffer) - 1);
    buffer[sizeof(buffer) - 1] = '\0';
}

void format_string(char *user, char *ip) {
    char log[256];
    // Safe: use snprintf to prevent buffer overflow
    snprintf(log, sizeof(log), "User: %s from IP: %s", user, ip);
}

void read_input() {
    char buf[128];
    // Safe: use fgets instead of gets()
    fgets(buf, sizeof(buf), stdin);
}

int add(int a, int b) {
    // Safe
    return a + b;
}