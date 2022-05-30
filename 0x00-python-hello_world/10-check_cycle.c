#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks a list for a loop
 *
 * @list: list to be checked
 * Return: 1 if there is loop or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list || !list->next)
		return (0);

	slow = fast = list;
	slow = slow->next;
	fast = fast->next->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
