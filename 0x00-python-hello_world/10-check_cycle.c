#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - singly linked list
 * @list: integer
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_s *first = list, *second = list;

	while (first && first->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}
