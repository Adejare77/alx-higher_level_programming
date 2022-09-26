#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a singly linked list
 * @head: pointer to the first node of the singly linked list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *current, *new, *temp;
current = *head;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (*head == NULL)
{
new->next = NULL;
*head = new;
return (new);
}
while (current && current->n < number)
{
temp = current;
current = current->next;
}
new->next = temp->next;
temp->next = new;
return (new);
}
