#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* A user-defined struct relating to a person */
struct S{
    
    char *firstName;
    char *lastName;
    char *emailAddress;
    int *phone;
};

static int i, j;
static int count;

/* This method is trying to sort an array of pointers based
   On the alphabetical order of their first names */
void sfn(struct S** ss){
    for(i = 0; i < count; i++)
        for (j = 0; j < count; j++)
            if (ss[i]->firstName > ss[j]->firstName)
                ss[i] = ss[j];
                ss[j] = ss[i];
} 

/* This method is trying to determine if there is a matching first name 
   Returning 1 if there is a match and 0 if there isn't a match */
int ffn(struct S** ss, char* s){
    while(++i < count)
        if (strcmp(ss[i]->firstName, s) == 0)
            return 1;
    return 0;
}

/* This function sorts the array struct S, pointers in ascending order based on their alphabetical order
   of last name */
void sln(struct S** ss){
    for(i = 0; i < count; i++) 
        for (j = 0; j < count; j++)
            if (ss[i]->lastName > ss[j]->lastName)
                ss[i] = ss[j];
                ss[j] = ss[i];
}

/* Checking if there is a matching last name is in the array */
int fln(struct S** ss, char* s){
    while(++i < count){
        if (strcmp(ss[i]->lastName, s) == 0)
            return 1;
    }
    return 0;
}

/* I think it is meant to sort the array of pointers to 'struct S (ss)'
   Based on their alphabetical order using bubble sort
   Fixed an error with  ss[j] = s */
void sem(struct S** ss) {
    for (i = 0; i < count; i++) {
        for (j = 0; j < count; j++) {
            if (ss[i]->emailAddress > ss[j]->emailAddress) {
                struct S *s = ss[i];
                ss[i] = ss[j];
                ss[j] = s;
            }
        }
    }
}

/* Meant to check if there is a matching email (s) in an array of 
   Struct S pointers (ss). Returning 1 if found, and 0 if not found */
int fem(struct S** ss, char* s){
    while(++i < count){
        if (strcmp(ss[i]->emailAddress, s) == 0)
            return 1;
    }
    return 0;
}


/* Sort an array by their phone number */
void sph(struct S** ss){
    for(; i < count; i++) {
        for (; j < count; j++) {
            if (ss[i]->phone > ss[j]->phone) {
                struct S *s = ss[i];
                ss[i] = ss[j];
                ss[j] = s;
            }
        }
    }
}

/* Check if there is a matching phone number */
int fph(struct S** ss, int s){
    //count = len(ss);
    int i = 0;
    while (i < count) {
        if (*(ss[i]->phone) == s) {
            return 1;
        }
        i++;
    }
    return 0;
}

/* Main Method */
int main(int argc, char ** argv) {

    /* defines i as int, defines count  = int 0, defines buffer a char array of size 10 */
    int i;
    int count = 0;
    char buffer[10];

    /* The allocated memory can hold 100 pointers of  struct S */
    struct S** ss = (struct S**) malloc(100*sizeof(struct S**));

    /*  Allocates memory for a single instance of struct s*/
    struct S* s = malloc(sizeof(*s));

    /* Opens a file, and returns a pointer 'f' to refer to the read-only opened file */
    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        printf("ERROR: Failed to open the file");
        return 1;
    }

    /* Iterates 50 times */
    for(i = 0; i < 50; i++){

        /* Memory is allocated for Struct S* s,firstName, lastName, emailAddress and phone with 80* size of memory */
        struct S* s = malloc(sizeof(struct S));
        s->firstName = malloc(80 * sizeof(char));
        s->lastName = malloc(80 * sizeof(char));
        s->emailAddress = malloc(80 * sizeof(char));
        s->phone = malloc(sizeof(int));

    /* Is used to read data from the file and store it in the respective struct member */
	fscanf(f, "%s %s %d %s", &s->firstName, &s->lastName, &s->phone, &s->emailAddress);
	
    /* creates an array of struct pointers */
	ss[count] = s;
        count += 1;
    {
        int command = 10;
    	while(command != 0){
		char* val = malloc(100*sizeof(val[0]));
    		gets(buffer);
		command = atoi(buffer);
		gets(buffer);
		strcpy(val, buffer);
		switch(command){

            /* Looks for email, sorts the array of emails, checks to see if it can be found */
			case 1:
			printf("looking for email %s\n", val);
			sem(ss);
			printf("found it? %d\n", fem(ss, val));
			break;

            /* Looks for first name, sorts the array of first names, checks to see if it can be found */
			case 2:
			printf("looking for first name %s\n", val);
			sfn(ss);
			printf("found it? %d\n", ffn(ss, val));
			break;

            /* looks for last name, sorts the array of last names, checks to see if it can be found */
			case 3:
			printf("looking for last name %s\n", val);
			sln(ss);
			printf("found it? %d\n", fln(ss, val));
			break;

            /* Looks for email, sorts the array of phone numbers, checks to see if it can be found */
			case 4:
			printf("looking for phone number %s\n", val);
			sph(ss);
			printf("found it? %d\n", fph(ss, atoi(val)));
			default:
			break;
			}
		}
	}

    /* Freeing memory */
    free(s->firstName);
    free(s->lastName);
    free(s->emailAddress);
    free(s->phone);
    for (i = 0; i < count; i++) {
    free(ss[i]);
}
}
    /* Deallocate memory for s and ss */
    free(ss);
    free(s);

    /* Closes the file */
    fclose(f);
}
