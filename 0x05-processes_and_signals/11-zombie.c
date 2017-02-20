#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "sys/types.h"

/**
 *
 */
int infite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 *
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid != 0)
			printf("Zombie process created, PID: %u\n", pid);
		else
			exit(0);

	}
	infite_while();
	return (0);
}
