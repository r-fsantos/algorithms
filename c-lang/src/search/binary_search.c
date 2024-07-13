/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   binary_search.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfelicio <rfelicio@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/13 09:44:42 by rfelicio          #+#    #+#             */
/*   Updated: 2024/07/13 11:50:12 by rfelicio         ###   ########.fr       */
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

int			binary_search(int *haystack, int low, int high, int needle);
static	void	seed_array(int *arr, int lenght);

int	main(void)
{
	int	*array;
	int	ret;

	array = (int *) malloc(ARRAY_LENGTH * sizeof(int));
	seed_array(array, ARRAY_LENGTH);
	ret = binary_search(array, 0, ARRAY_LENGTH - 1, 0);
	printf(YELLOW "\nTesting: Binary Search Algorithm\n\n" YELLOW);
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
    Finds the index fot thre first occurrence of a needle on a haystack.

    Implements the Binary Search Algorithm. BigO: O(log n)

    Args:
        haystack: An ordered array of integers
        low: The integer index to the beggining of the array
        high: The integer index to the end of the array
        needle: The integer to be found in the haystack

    Returns:
        The first occurrence of the needle in the harstack
        or -1 if not found.
*/
int	binary_search(int *haystack, int low, int high, int needle)
{
	int	mid;

	while (high >= low)
	{
		mid = (low + high) / 2;
		if (needle == haystack[mid])
			return (mid);
		else if (needle > haystack[mid])
			low = mid + 1;
		else
			high = mid - 1;
	}
	return (-1);
}
