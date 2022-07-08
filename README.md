# HR-analysis

# Test data
In our Test data by using (import missingno) library we have plotted null values. We have noticed that there are null values in education and previous_year_rating.
 ![1](https://user-images.githubusercontent.com/50281621/177892813-1cd8058f-ab7f-4421-9d89-bf3741ad7aba.png)

# Train data
In the same way, we have identified null values in train dataset. As we can the columns that have lines in the below plot represents missing values. Therefore, we have missing values education and previous_year_rating 
![2](https://user-images.githubusercontent.com/50281621/177892818-9e2729fa-1d81-438c-8e9d-4611c076a1f0.png)

# HISTOGRAM:

1.	In the above histogram plot for train dataset, employees who have met KPI are above 80% less compared to who have met 
2.	We have more employees with 30-40 years of age
3.	 We have Employees with average training score in between 45 – 60
4.	Employees who received awards are very few
5.	Very few employees are promoted
6.	We have more than 25000 employees with 0-9 years in service
7.	We have more than 17500 employees with 3 rating
![3](https://user-images.githubusercontent.com/50281621/177892834-2e184e0c-d435-471e-abd7-c8e4a6b31efe.png)

# HEATMAP
![4](https://user-images.githubusercontent.com/50281621/177892849-c1b77e9e-cec3-4506-8fa7-4bc2408d7a9b.png)

Age ~ length_of_service  are low correlated each other
KPI_met > 80% ~ previous_year_rating are slightly correlated

# EXPLORARTORY ANALYSIS

# DEPARTMENT
 ![5](https://user-images.githubusercontent.com/50281621/177892855-80cd5ed3-ffc5-41d1-b752-2b4dddef1f23.png)

The above is bar plot for department column in the train dataset, we have distinct groups in department. As we can see, there are more employees in sales and marketing and very few employees in legal department and second highest are in operations department.


# GENDERGAP
 ![6](https://user-images.githubusercontent.com/50281621/177892897-d04a5930-08a9-4fa7-adbb-fc6e5f0bd57a.png)

The above pie chart explains gender gap between male and female. In our dataset we gave a greater number of male (more than double the number) compared to female employees which we can graphically see the same as above.
 


# COMAPARISION OF MALE AND FEMALE IN THEIR LEVEL OF EDUCATION
 ![7](https://user-images.githubusercontent.com/50281621/177892911-22389e97-6ceb-4168-9ecc-87395864b00c.png)

The bar chart shows level of education of different employees from different educational background such as Bachelor’s, masters and above, below secondary. In our dataset there are many employees with bachelor's degree and very few with below secondary education. 

# COMAPARISION OF MALE AND FEMALE W.R.T PROMOTION
 ![8](https://user-images.githubusercontent.com/50281621/177892916-2067bf5e-996f-4ea7-858a-67737f72a3bb.png)

The above chart depicts the comparision between male and female with respect to promotion. From the above chart we can see that the ratio of promotion is approximately same for both males and females.

# AGE OF EMPLOYEES
![9](https://user-images.githubusercontent.com/50281621/177892926-ec6bd168-4604-4f61-b217-c243577608cd.png)

The above distribution plot represents Age of Employees. From the plot we can see that there are employees mostly from all the age groups above 20. But we have more than 80% of employees ranging between 25-35.

# PREVIOUS YEAR RATING OF THE EMPLOYEES
![10](https://user-images.githubusercontent.com/50281621/177892933-b44671fe-682b-41ca-b558-45f00eda4f84.png)

The above graph represents the distribution of previous year rating of the employees. More than 17500 employees have been rated 3 out of 5. We can see there are also respectable number of employees more than 11000 have 5 out of 5.

# EMPLOYEE AWARDS
 ![11](https://user-images.githubusercontent.com/50281621/177892942-75b5037d-6613-4617-b515-455925999a17.png)

The above graph represents the percentage of employees who won awards. All the employees have been  awarded based on their performance, except 2.32% have not received any award.

# PROMOTED AND NON-PROMOTED EMPLOYEES
![12](https://user-images.githubusercontent.com/50281621/177892948-f30d4865-8eec-442b-badd-8d9c64773dfc.png)

The above plot shows the gap in promoted and non-promoted employees. 0 represents that there is no promotion and 1 represents there is a promotion. We can also see a long gap between both.

# DEPENDENCY OF TRAINING SCORE IN PROMOTION:
 ![13](https://user-images.githubusercontent.com/50281621/177892970-54abf4f2-a9af-4584-aa9f-ab973135ec4f.png)

The above plot depicts the dependency of training score in promotion. Employees who have above 90% on training have more chances of promotion and who scored less than 90% have very less chance of promotion.

# DEPENDENCY OF REGIONS IN DETERMINING PROMOTION:
 ![14](https://user-images.githubusercontent.com/50281621/177892979-9446584a-cbfe-48b5-a5e8-3efec63e4c50.png)

The above plot represents the dependency of regions in determining the promotion. The region_4 has remarkably high chances of promotion compared to all other regions.

# DEPENDENCY OF AWARDS IN DETERMINING PROMOTION:
![15](https://user-images.githubusercontent.com/50281621/177892986-f4be6eb9-d388-436d-ad7a-ac6c26c9aaff.png)

Awards won by an employee can play a significant role when it comes to promotion. There are a greater number of employees who are not promoted because they did not receive any awards as we can see employees who are promoted received awards before. 

# DEPENDENCY OF PREVIOUS YEAR RATINGS IN DETERMINING PROMOTION:
 ![16](https://user-images.githubusercontent.com/50281621/177892994-f5ce1d73-f435-4833-91b9-3d5afe9b1cf7.png)


The above plot shows the dependency of previous year rating in determining promotion. From our train data as we can observe that employees who have rating 5/5 have high chances of promotion.

# DEPENDENCY OF DEPARTMENTS IN DETERMINING PROMOTION:
![17](https://user-images.githubusercontent.com/50281621/177892999-9022026f-e30e-411e-b4e8-14c1d2285bc9.png)

Promotions can be analyzed within departments as above. The above plot shows the dependency of departments in determning the promotion. In the technology, Analytics and operations and procurement departments have high chances of promotion.

# DEPENDENCY OF LENGTH OF SERVICE IN PROMOTION:
 ![18](https://user-images.githubusercontent.com/50281621/177893004-c3e0f07d-4b94-455a-8d9b-9f316c4477d2.png)

The experience of an employee in an organization is the major attribute to be considered for the promotion. The above plot shows the dependency of length of service in determining the promotion. As the service increases the chance of getting promotion also increases.

# DEPENDENCY OF GENDER IN DETERMINING PROMOTION:
![19](https://user-images.githubusercontent.com/50281621/177893013-33dd5e5c-2b25-492b-a30b-080932fd5fbb.png)

The above plot shows the dependency of gender in determining the promotion. We can see that graph remains same in both the cases. So, we can conclude that the gender is not at all a barrier in determining the promotion.
	
# DATA PREPROCESSING

In our train and test dataset we have null value in education and previous year rating

![20](https://user-images.githubusercontent.com/50281621/177892478-3f7f76e8-5452-4fa9-adf4-db93bc646827.png)

![21](https://user-images.githubusercontent.com/50281621/177892483-c3d31947-3005-4e48-b7e8-0f0f07fd4427.png)

![22](https://user-images.githubusercontent.com/50281621/177892486-e71d8bcb-4c6f-44c5-b189-3cd654427d4d.png)

Using mode function, we replaced null values in education with ‘0’ and previous year rating with ‘1’ For both test and train dataset
Random Forest Classifier:
Training Accuracy: 0.9998130235341045

XGB Classifier:
Training Accuracy: 0.912582269644994

LGBM Classifier:
Training Accuracy: 0.9600992221779019

Extra Trees Classifier:
Training Accuracy: 0.9998130235341045
