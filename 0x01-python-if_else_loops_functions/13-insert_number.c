#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * *insert_node - code
 * @number: integer
 * @head: points to the node
 *
 * Return: new node
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	int i = 0;
	listint_t *node;

	node = malloc(sizeof(listint_t));
	while(!head)
	{
		if (head->next->n > number)
		{
			node->next = head->next;
			node->n = number;
			head->next = node;
			return (node); 
		}
		head = head->next;	
	}
	return (NULL);
}
