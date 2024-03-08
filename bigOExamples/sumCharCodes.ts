function sum_char_codes(n: string): number {
	let sum = 0;
	// FOA: 1 - Growth vs Input
	// For a n 50% larger -> the computation of inputs (n.length) increases 50%
	// Every additional char at the string implies on another for-loop execution
	// Answer: O(n) 

	for (let i = 0; i < n.length; ++i) {
		sum += n.charCodeAt(i);
	}

	// Another loop doesn't mean O(2n), because constants are droppped.
	// For 2 basic reasons: when n scales it doesn't make a lot of difference
	// when comparing O(n) and O(n^2) outputs. And usually we aren't concerned
	// about tiny precision.
	for (let i = 0; i < n.length; ++i) {
		sum += n.charCodeAt(i);
	}


	return sum;
}


function sum_char_codes_with_matching(n: string, matching: number): number {
	let sum = 0;

	for(let i = 0; i < n.length; ++i) {
		const charCode = n.charCodeAt(i);
		
		if(charCode === matching) {
			return sum;
		}

		sum += n.charCodeAt(i);
	}

	return sum;
}

function sum_char_codes_o_n_square(n: string): number {
	let sum = 0;
	for (let i = 0; i < n.length; ++i) {
		for (let j = 0; j < n.length; ++j) {
			sum += n.charCodeAt(j);
		}
	}
	return sum;	

}


console.log(sum_char_codes("aaaa"));
console.log(sum_char_codes_with_matching("RRRRENATO", 69));
console.log(sum_char_codes("R"));
console.log(sum_char_codes("r"));
console.log(sum_char_codes_o_n_square("r"));

