#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - singly linked list
 * @list: list ptr
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list, *second = list;

	while (second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
		{
			return (1);
		}
	}
	return (0);
}
