#include "lists.h"


/**
 * check_cycle - checks a list for a loop
 *
 * @list: list to be checked
 * Return: 1 if there is loop or 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *sloth = list;
	listin_t *ant = list;

	if (!list)
		return (0);

	
	while (sloth && ant && ant->next)
	{
		sloth = sloth->next;
		ant = ant->next;
		if (sloth == ant)
			return (1);
	}
	return (0);
}
