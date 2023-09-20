#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

/* A user-defined struct relating to a person */
struct Person {
    char *firstName;
    char *lastName;
    char *emailAddress;
    char *phone;
};

/* Counts the number of rows in the file */
int rowCounter(FILE *file) {
    int count = 0;
    char ch;
    // While there are rows increase count 
    while ((ch = fgetc(file)) != EOF) {
        if (ch == '\n') {
            count++;
        }
    }
    rewind(file);
    return count;
}


/* Method for finding the position of a firstName in the firstName array */
int findFirstNamePosition(struct Person *p, int numRows, const char *targetFirstName) {
    // If the targetFirstName is in this position it will return the position
    for (int i = 0; i < numRows; i++) {
        if (strcmp(p[i].firstName, targetFirstName) == 0) {
            return i;
        }
    }
    return -1;
}

/* Method for finding the position of a lastName in the lastName array*/
int findLastNamePosition(struct Person *p, int numRows, const char *targetLastName) {
    // If the targetFirstName is in this position it will return the position
    for (int i = 0; i < numRows; i++) {
        if (strcmp(p[i].lastName, targetLastName) == 0) {
            return i;
        }
    }
    return -1;
}

/* Method for finding the position of a phone in the phone array*/
int findPhonePosition(struct Person *p, int numRows, const char *targetPhone) {
    // If the targetFirstName is in this position it will return the position    
    for (int i = 0; i < numRows; i++) {
        if (strcmp(p[i].phone, targetPhone) == 0) {
            return i;
        }
    }
    return -1;
}

/* Method for finding the position of a EmailAddress in the EmailAddress array*/
int findEmailAddressPosition(struct Person *p, int numRows, const char *targetEmailAddress) {
    // If the targetFirstName is in this position it will return the position
    for (int i = 0; i < numRows; i++) {
        if (strcmp(p[i].emailAddress, targetEmailAddress) == 0) {
            return i;
        }
    }
    return -1;
}

/* The main method */
int main(int argc, char **argv) {
    // sets i to int and buffer to char[10]
    int i;
    char buffer[10];

    // Opens the the test_data.txt file, if it can not be found it will print out an error
    FILE *f = fopen("test_data.txt", "r");
    if (f == NULL) {
        printf("ERROR: Failed to open the file");
        return 1;
    }

    // Gets the number of rows in the txt file
    int numRows = rowCounter(f);

    // Assigns memory to the struct Person
    struct Person* p = (struct Person*) malloc(numRows * sizeof(struct Person));


    // Assigns memory to the positions in the Person arrays then inputs the data from the
    // text file into the arrays.
    for(i = 0; i < numRows; i++) {
        p[i].firstName = malloc(20 * sizeof(char));
        p[i].lastName = malloc(40 * sizeof(char));
        p[i].emailAddress = malloc(40 * sizeof(char));
        p[i].phone = malloc(20 * sizeof(char));
        fscanf(f, "%s %s %s %s", p[i].firstName, p[i].lastName, p[i].phone, p[i].emailAddress);
    }

    // Reads from the user input
    int command = 10;
    while(command != 0){
        printf("-------------------------------------------------------------------------------------\n");
        printf("Enter One of the Following Commands to Search Followed by Search Term you Require.\n");
        printf("* 1 - To Search By First Name\n");
        printf("* 2 - To Search By Last Name\n");
        printf("* 3 - To Search By Phone Number\n");
        printf("* 4 - To Search By Email Address\n");
        printf("* 0 - To Close The Program");
        printf("\n");
	   
       // Reads the users initial input, wanting either 0, 1 ,2 ,3 ,4 or 5
        char* val = malloc(100*sizeof(val[0]));
    	fgets(buffer, sizeof(buffer), stdin);
	    command = atoi(buffer);

        // If the input is 0 closes the program
        if (command == 0) {
            printf("Program Closed\n");
            return 0;
        }

        // Reads the users second input used for searching the search term
        printf("Enter Search Term: ");
	    fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0'; 
	    strcpy(val, buffer);
        int position;

    switch(command){

        // If "1" is inputted it checks if the first name matches
        case 1:
            position = -1;
            printf("Looking for first name: %s\n", val);
            position = findFirstNamePosition(p, numRows, val);
            if (position == -1) {
                printf("The first name, %s, can not be found in the database \n", val);
            } else {
                printf("First name: %s\n", p[position].firstName);
                printf("Last name: %s\n", p[position].lastName);
                printf("Email address: %s\n", p[position].emailAddress);
                printf("Phone number: %s\n", p[position].phone);
            }
            break;
        
        // If "2" is inputted it checks if the last name matches
        case 2:
            position = -1;
            printf("Looking for the last name: %s\n", val);
            position = findLastNamePosition(p, numRows, val);
            if (position == -1) {
                printf("The last name, %s, can not be found in the database \n", val);
            } else {
                printf("First name: %s\n", p[position].firstName);
                printf("Last name: %s\n", p[position].lastName);
                printf("Email address: %s\n", p[position].emailAddress);
                printf("Phone number: %s\n", p[position].phone);   
            }
            break;
        
        // If "3" is inputted it checks if the phone number matches
        case 3:
            position = -1;
            printf("Looking for the phone number: %s\n", val);
            position = findPhonePosition(p, numRows, val);
            if (position == -1) {
                printf("The phone number, %s, can not be found in the database \n", val);
            } else {
                printf("First name: %s\n", p[position].firstName);
                printf("Last name: %s\n", p[position].lastName);
                printf("Email address: %s\n", p[position].emailAddress);
                printf("Phone number: %s\n", p[position].phone);   
            }
            break;
        
        // If "4" is inputted it checks if the email address matches
        case 4:
            position = -1;
            printf("Looking for the email address: %s\n", val);
            position = findEmailAddressPosition(p, numRows, val);
            if (position == -1) {
                printf("The email, %s, can not be found in the database \n", val);
            } else {
                printf("First name: %s\n", p[position].firstName);
                printf("Last name: %s\n", p[position].lastName);
                printf("Email address: %s\n", p[position].emailAddress);
                printf("Phone number: %s\n", p[position].phone);   
            }
        default:
            printf("Please enter a valid input\n");
            break;
        }

        // Frees val memory
        free(val);
    }
    
    // Freeing memory
    for (int i = 0; i < numRows; i++) {
        free(p[i].firstName);
        free(p[i].lastName);
        free(p[i].emailAddress);
        free(p[i].phone);
    }

    // Freeing memory and closes the file
    free(p);
    fclose(f);

    return 0;
}

