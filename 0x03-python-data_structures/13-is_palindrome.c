#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - prints all elements of a listint_t list
 * @head: pointer to head of list
 * Return: node
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	return (palind(head, *head));
}

/*
 * palind - palindrome
 * @head: head of the list
 * @last: last of list
 */
int palind(listint_t **head, listint_t *last)
{
	if (palind(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
