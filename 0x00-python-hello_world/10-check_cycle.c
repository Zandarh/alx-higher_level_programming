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
	listint_t *sloth, *ant;

	if (!list || !list->next)
		return (0);

	slot = ant = list;
	slot = sloth->next;
	ant = ant->next-next;
	while (sloth && ant && ant->next)
	{
		if (sloth == ant)
			return (1);
		sloth = sloth->next;
		ant = ant->next;
	}
	return (0);

