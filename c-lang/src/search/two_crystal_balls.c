/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   two_crystal_balls.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfelicio <rfelicio@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/21 17:54:31 by rfelicio          #+#    #+#             */
/*   Updated: 2024/07/21 18:58:33 by rfelicio         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ARRAY_LENGTH 10000
#define GREEN "\033[0;32m"
#define RESET "\033[0m"
#define RED "\033[0;31m"
#define BLUE "\033[0;34m"
#define YELLOW "\033[1;33m"

void	*balloc(int length, unsigned long size_of);
void	set_true_from(int idx, int *at_ptr, int ptr_length);

/*
Given the following problem:

Given two crystal balls that will break if dropped from high enough
distance, determine the exact spot in which it will break in the most
optimized way.

Solution: Iterates over the array with a well-established jump amount,
given by the square root of the size of the array. Once a true value is
found, then the index go back of a jump amount and go forward until a new
counter hits the jump amount or the array size.

It's a middle term solution between linear search and binary search
algorithms. It's running time is O(qrt(n)).

Args:
	breaks: An array of booleans

Returns:
	The first occurrence of true or -1 if not found.
*/
int	two_crystal_balls(int *arr, int arr_length)
{
	int	jmp_amount;
	int	i;
	int	j;

	jmp_amount = (int) sqrt(arr_length);
	i = jmp_amount;
	while (i < arr_length)
	{
		if (arr[i] == 1)
			break;
		i += jmp_amount;
	}
	i -= jmp_amount;
	j = 0;
	while (j < jmp_amount && i < arr_length)
	{
		if (arr[i] == 1)
			return (i);
		i++;
		j++;
	}
	return (-1);
}

int	main(void)
{
	int	*breaks;
	int	random_idx;
	int	ret;

	breaks = (int *)balloc(ARRAY_LENGTH, sizeof(int));
	random_idx = rand() % (ARRAY_LENGTH + 1);
	set_true_from(random_idx, breaks, ARRAY_LENGTH);
	ret = two_crystal_balls(breaks, ARRAY_LENGTH);
	printf(YELLOW "\nTesting: Two Crystal Balls Colision Algorithm\n\n" YELLOW);
	printf(BLUE "Test it should return  %d:" RESET, random_idx);
	if (ret == random_idx)
		printf(GREEN "OK \n" RESET);
	else
		printf(RED "NOK \n" RESET);
	return (0);
}

void	*balloc(int length, unsigned long size_of)
{
	int	*ptr;
	int	i;

	i = -1;
	ptr = (void *)malloc(length * sizeof(size_of));
	while (++i < length)
		ptr[i] = 0;
	return (ptr);
}

void	set_true_from(int idx, int *at_ptr, int ptr_length)
{
	while (idx < ptr_length)
		at_ptr[idx++] = 1;
}
