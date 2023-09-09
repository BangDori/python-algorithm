#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int final_score = 0;

static int process(int command, int param1, int param2)
{
	static int school[3][3];
	static int student[10000][3];

	int counter;

	switch (command)
	{
		case 1: return (school[param1][0]);
		case 2: return (school[param1][1]);
		case 3: return (student[param1][0]);
		case 4: return (student[param1][1]);
		case 5: student[param1][2] = param2; return (0);
	}


	if (command == 0)
	{
		for (counter = 0; counter < 3; counter++)
		{
			school[counter][0] = rand() % 1000;
			school[counter][1] = rand() % 1000;
		}

		for (counter = 0; counter < 10000; counter++)
		{
			student[counter][0] = rand() % 1000;
			student[counter][1] = rand() % 1000;
			student[counter][2] = -1;
		}

		return (0);
	}

	return (-1);
}


void get_school_position(int school_index, int* posX, int* posY)
{
	if ((0 <= school_index) && (school_index < 3))
	{
		*posX = process(1, school_index, 0);
		*posY = process(2, school_index, 0);
	}
	else
	{
		*posX = -1;
		*posY = -1;
	}

	return;
}


void get_student_position(int student_index, int* posX, int* posY)
{
	if ((0 <= student_index) && (student_index < 10000))
	{
		*posX = process(3, student_index, 0);
		*posY = process(4, student_index, 0);
	}
	else
	{
		*posX = -1;
		*posY = -1;
	}

	return;
}


void set_student_school(int student_index, int school_index)
{
	if ((0 <= student_index) && (student_index < 10000) && (0 <= school_index) && (school_index < 3))
	{
		process(5, student_index, school_index);
	}

	return;
}


float get_distance(int studentX, int studentY, int schoolX, int schoolY) {
    int deltaX = schoolX - studentX;
    int deltaY = schoolY - studentY;
    
    float distance = sqrt(deltaX * deltaX + deltaY * deltaY);
    return distance;
}


void run_contest(void)
{
    int schoolX, schoolY, studentX, studentY;
    int capacity[3] = {0, 0, 0};

    int max_distance = get_distance(0, 0, 999, 999);
    for (int i = 0; i < 10000; i++) {
        get_student_position(i, &studentX, &studentY);

        float min_distance = max_distance;
        int min_idx = 0;

        for (int j = 0; j < 3; j++) {
            if (capacity[j] >= 3500) continue;
            get_school_position(j, &schoolX, &schoolY);

            float distance = get_distance(studentX, studentY, schoolX, schoolY);
            float extra_point = max_distance / 7000 * capacity[j];
            if ((distance - extra_point) <= min_distance && capacity[j] <= capacity[min_idx]) {
                min_distance = distance;
                min_idx = j;
            }
        }

        capacity[min_idx] += 1;
        set_student_school(i, min_idx);
    }

    int score = abs(capacity[0]-capacity[1]) + abs(capacity[1]-capacity[2]) + abs(capacity[2]-capacity[0]);
    final_score += score;

    return;
}

int main(void)
{
	char* idname(void);
	int counter;

    for (int i = 0; i < 100; i++) {
        srand(i);

        for (counter = 0; counter < 10; counter++)
        {
            process(0, 0, 0);
            run_contest();
        }
    }

    printf("Final Score = %d\n", final_score);
	return -1;
}