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
		double b = (2.0 * r - 1.0);
		double c = -t;
		double res = (-b + pow((4 * pow(r, 2.0) - 4 * r + 1 + (8.0 * t)), 0.5));
		printf("Case #%d: %llu\n", i + 1, (uint64_t) floor(res / 4.0));
	}
	fclose(f);
	return 0;
}
