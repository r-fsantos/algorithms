/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   linear_search.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfelicio <rfelicio@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/17 19:57:39 by rfelicio          #+#    #+#             */
/*   Updated: 2024/07/17 20:02:44 by rfelicio         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

#define ARRAY_LENGTH 13
#define GREEN "\033[0;32m"
#define RESET "\033[0m"
#define RED "\033[0;31m"
#define BLUE "\033[0;34m"
#define YELLOW "\033[1;33m"

int			linear_search(int *haystack, int low, int high, int needle);
static	void	seed_array(int *arr, int lenght);

int	main(void)
{
	int	*array;
	int	ret;

	array = (int *) malloc(ARRAY_LENGTH * sizeof(int));
	seed_array(array, ARRAY_LENGTH);
	ret = linear_search(array, 0, ARRAY_LENGTH - 1, 0);
	printf(YELLOW "\nTesting: Linear Search Algorithm\n\n" YELLOW);
	printf(BLUE "Test 1: " RESET);
	if (ret == 0)
		printf(GREEN "OK \n" RESET);
	else
		printf(RED "NOK \n" RESET);
	free(array);
	array = NULL;
	return (0);
}

static void	seed_array(int *arr, int lenght)
{
	int	i;

	i = 0;
	while (i < lenght)
	{
		arr[i] = i;
		++i;
	}
}

/*
    Finds the index fot the first occurrence of a needle 
    inside of a haystack.

    Implements the Linear Search Algorithm. BigO: O(n)

    Args:
        haystack: An ordered array of integers
        low: The integer index to the beggining of the array
        high: The integer index to the end of the array
        needle: The integer to be found in the haystack

    Returns:
        The first occurrence of the needle in the haystack
        or -1 if not found.
*/
int	linear_search(int *haystack, int low, int high, int needle)
{
    while (high >= low)
    {
        if (needle == haystack[low])
            return low;
        low++;
    }
	return (-1);
}
