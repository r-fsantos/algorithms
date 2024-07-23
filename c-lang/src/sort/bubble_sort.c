/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bubble_sort.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rfelicio <rfelicio@student.42sp.org.br>    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/22 22:11:29 by rfelicio          #+#    #+#             */
/*   Updated: 2024/07/23 09:46:29 by rfelicio         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

#define ARRAY_LENGTH 7
#define GREEN "\033[0;32m"
#define RESET "\033[0m"
#define RED "\033[0;31m"
#define BLUE "\033[0;34m"
#define YELLOW "\033[1;33m"

void	bubble_sort(int *arr, int size);
void	print_array(int *arr, int size);
int		arrays_are_equal(int *fst, int *snd, int size);

// TODO: add command-line input handling
int	main(void)
{
	int	arr[] = {9, 3, 7, 4, 69, 420, 42};
	int	bkp[] = {9, 3, 7, 4, 69, 420, 42};
	int	exp[] = {3, 4, 7, 9, 42, 69, 420};
	int	ret;

	bubble_sort(arr, ARRAY_LENGTH);
	ret = arrays_are_equal(arr, exp, ARRAY_LENGTH);
	printf(YELLOW "\nTesting: Bubble Sort Algorithm\n\n" YELLOW);
	printf("");
	printf(BLUE "Test if array is sorted: " RESET);
	if (ret == 1)
		printf(GREEN "OK \n" RESET);
	else
		printf(RED "NOK \n" RESET);
	printf("before: ");
	print_array(bkp, ARRAY_LENGTH);
	printf("after:  ");
	print_array(arr, ARRAY_LENGTH);
	return (0);
}

void	bubble_sort(int *arr, int size)
{
	int	i;
	int	j;
	int	tmp;

	i = 0;
	while (i < size)
	{
		j = 0;
		while (j < size - 1 - i)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
			j++;
		}
		i++;
	}
}

int	arrays_are_equal(int *fst, int *snd, int size)
{
	int	i;

	i = -1;
	while (++i < size)
		if (fst[i] != snd[i])
			return (0);
	return (1);
}

void	print_array(int *arr, int size)
{
	int	i;

	i = -1;
	while (++i < size)
		printf("%d ", arr[i]);
	printf("\n");
}
