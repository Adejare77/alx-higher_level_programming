#include <stdio.h>

/**
 * main - prints all possible different combination
 * of three digits.
 * The three digits must be different. e.g 010 and 100 are
 * considered the same
 *
 * Return: Always 0 means (success)
 */
int main(void)
{
	int i, j, l, k = 49, m = 50;

	for (i = 48; i < 58; i++)
	{
		for (j = k; j < 58; j++)
		{
			if (i != j)
			{
				for (l = m; l < 58; l++)
				{
					if (j != m)
					{
						putchar(i);
						putchar(j);
						putchar(l);
						if ((i == 55) & (k == 56) & (m == 57))
						break;
						putchar(',');
						putchar(' ');
					}
				}

				if ((i == 55) & (k == 56 & l == 57))
				break;
				m++;
			}
		k++;
		}
	}
	putchar('\n');

	return (0);
}
