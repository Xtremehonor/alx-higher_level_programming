#include "lists.h"

/**
 * check_cycle - Checks for a cycle 
 * in a linked list using Floyd's algorithm
 * @list: Pointer to the head of the linked list
 * Return: 1 if a cycle is found, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tortoise = list;
	hare = list;

	while (hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			tortoise = list;
			while (tortoise != hare)
			{
				tortoise = tortoise->next;
				hare = hare->next;
			}
			return (1);
		}
	}

	return (0);
}
