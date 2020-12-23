#include <stdio.h>
#include <string.h>

int find_min_day(char* filename){
    FILE* fp;
    fp = fopen(filename, "r");
    char reading[100000];
    fgets(reading, sizeof(reading), fp);
    

}