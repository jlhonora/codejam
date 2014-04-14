#include <stdio.h>
#include <stdint.h>
#include <math.h>

int main(void) {
	FILE * f = fopen("input.txt", "r");
	int n_cases = 0;
	fscanf(f, "%d", &n_cases);
	printf("# Cases: %d\r\n", n_cases);
	for(int i = 0; i < n_cases; i++) {
		double r, t;
		fscanf(f, "%lf %lf", &r, &t);
		double a = 2;
		double b = (-1 + 2 * r);
		double c = -t;
		double res = (-b + pow((pow(b, 2.0) - 4.0 * a * c), 0.5)) / (2.0 * a);
		printf("Case #%d: %llu\n", i + 1, (uint64_t) floor(res));
	}
	fclose(f);
	return 0;
}
