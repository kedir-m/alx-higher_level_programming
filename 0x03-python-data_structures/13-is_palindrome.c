#include "lists.h"
int is_palindrome(listint_t **head)
{
  listint_t *current, *fHalf_node, *sHalf_node;
  int i, k, middle_index, no_of_node = 0;

  //if (**head == NULL || *head == NULL)
    //    return (1);
 
  current = *head;
  fHalf_node = *head;

  while (current != NULL)
    {
      current = current->next;
      no_of_node++;
    }

  if (no_of_node % 2 != 0)
    {
      middle_index = no_of_node / 2;

      for (i = 0; i < middle_index; i++)
	current = current->next;

      sHalf_node = current;
      while (middle_index > 0)
	{
	  if (fHalf_node->n != sHalf_node->n)
	    return (0);
	  fHalf_node = fHalf_node->next;
	  sHalf_node = sHalf_node->next;

	  middle_index--;
	}
    }
  else
    {
      middle_index = no_of_node / 2 + 2;
      for (k = 0; k < middle_index; k++)
	current = current->next;
      sHalf_node = current;
      middle_index -= 2;
      while (middle_index > 0)
	{
	  if (fHalf_node->n != sHalf_node->n)
	    return (0);
	  fHalf_node = fHalf_node->next;
	  sHalf_node = sHalf_node->next;
	  middle_index--;
	}
    }

  return (1);
}
