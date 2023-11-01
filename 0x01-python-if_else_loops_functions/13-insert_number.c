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
	listint_t *node, *current;

	if (!head)
		return (NULL);
	
	node = malloc(sizeof(listint_t));
	if (!node)
		return (NULL);
	node->n = number;
	node->next = NULL;

	if (!*head || number < (*head)->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}
	
	while(!*head)
	{
		if (*(head)->next->n > number)
		{
			node->next = *(head)->next;
			node->n = number;
			*(head)->next = node;
			return (node); 
		}
		*(head) = head->next;
	}
	return (NULL);
}
