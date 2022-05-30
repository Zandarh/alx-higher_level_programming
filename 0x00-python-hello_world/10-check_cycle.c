#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks a list for a loop
 *
 * @list: list to be checked
 * Return: 1 if there is loop or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *sloth, *ant;

	if (!list || !list->next)
		return (0);

	sloth = ant = list;
	sloth = sloth->next;
	while (sloth && ant && ant->next)
	{
		if (sloth == ant)
			return (1);
		sloth = sloth->next;
		ant = ant->next->next;
	}
	return (0);
}
