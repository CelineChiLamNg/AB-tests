# A/B Testing - double datasets
**May 2024**<br>
**Celine Ng**<br>

## Project Description
This project aims to analyze both datasets, [Fast Food Marketing Campaign](https://www.kaggle.com/datasets/chebotinaa/fast-food-marketing-campaign-ab-test)
<br>and [Cookie Cats Mobile Games](https://www.kaggle.com/datasets/mursideyarkin/mobile-games-ab-testing-cookie-cats) 
<br> with A/B testing.

## Fast Food Marketing Campaign
Looker Studio Dashboard: https://lookerstudio.google.com/s/kyJoFQec1tU
### Objectives
The fast-food chain tested out 3 promotions in several store and <br>
the data records sales in the initial 4 weeks of the new promotion. <br>
Apply A/B test to understand which of the 3 campaigns is the most effective.

### Approach & Methodology
1. Data Cleaning: Check for duplicates and missing values.
2. Exploratory Data Analysis (EDA): Data distribution in general and by 
   promotion. Plotting shows target population for all promotions are 
   similar, as features like MarketID, Market Size, and Age of Store are 
   similar across all 3 promotions. Average values for Sales In Thousands 
   vary slightly through the weeks for all promotions, with Promotion 2 
   registering the least sales and Promotion 1 the highest during the whole 
   time. Promotion 1 and 3 had overlapping confidence interval during the 
   period.
3. Metrics: Average Sales by Promotion (Identify which of the 3 promotions 
   has the highest average sales.)
4. Statistical Analysis: To compare means of Promotion 1, 2 and 3, to minimize type 1 error, <br>
instead of t-tests, ANOVA test is used to detect if there is any difference 
   between the 3 groups.
Then for post-hoc test, Tukey HSD will find out which specific groups' means
 differ. Both analytical and bootstrapping methods were used to calculate 
   confidence interval.

### Results
Both analytical and bootstrapping methods resulted in very similar mean and 
<br>
confidence intervals. Together with the results of the statistical tests, 
it <br>
is safe to conclude that both Promotion 1 and 3 are more effective 
campaigns <br>
compared to 2. Since average sales from Promotion 1 and 3 are not 
statistically <br>
different, any of these are recommended.


### Challenges & Learnings 
Defining the metric for A/B testing was the most challenging part because 
the feature Sales In Thousands distribution was not normal. Which means 
average might not be the best statistical metric, or at least a secondary 
metric, like total sum of Sales, can be helpful to add credibility to the 
findings.

## Cookie Cats Mobile Games
### Objectives
When a player installed the game Cookie Cats, the player would be randomly <br>
assigned to either gate_30 or gate_40. The dataset includes A/B test results
 of <br>
the game when the first gate in the game was moved from level 30 to 40. <br>
Apply A/B test to determine where should the Cookie Cats game locate its gate.

### Approach & Methodology
1. Data Cleaning: Check for duplicates and missing values.
2. Exploratory Data Analysis (EDA): Data distribution in general and by 
   Gate Level. Similar to Fast Food Marketing project, plot to understand 
   whether features relationships with different gate levels, to 
   then decide on target metric. The average number of game rounds played, 
   and both retention rates were similar for both gate levels. The 
   difference between gates lie on the standard deviation of game rounds 
   played (gate 30 2x as much as gate 40).
3. Metrics: Identify if version gate_30 indeed does have a higher 7 days 
   retention rate. Even though total game rounds showed the largest 
   difference between gates on standard deviation, the mean was very 
   similar, concluding that this feature does not have enough sensitivity 
   for our A/B testing.
4. Statistical Analysis: Chi-square test will be applied to verify if 
   retention rate is different between the 2 versions. Then confidence 
   interval was also plotted to confirm the hypothesis testing.

### Results
After calculating the confidence intervals, it is clear that the 7 day <br>
retention rates for the 2 versions of the game do not overlap, with a 95% <br>
confidence level. Also, with p-value under 0.05, we can safely conclude that
 <br>
 7 day retention is higher when the gate is located at level 30.<br>

**Additional Business Insights**<br>
While hypothesis test confirmed that gate 30 is the better choice, looking 
into the 7-day retention rate value itself (between 18-19%), 
the decreasing retention over time (1 day, 7 day), and total sum game 
rounds heavily skewed to the right tells us the Cookie Cats Mobile Game 
might have a long-term player retention problem. <br>
The issue is initially improved by moving the gate to level 30 (day 1-7), 
but not so much in a longer period of time (14 days). 

### Challenges & Learnings
During data exploration, it was found that total game rounds mean was 
similar between gates, but not its standard deviation. Gate 30 has a lot 
more outliers, which could reduce the reliability of our findings, as the 
sampling population were not the same.
In the next iteration try remove/cap extreme outliers from total number of 
game rounds for both gates, and reanalyze hypothesis testing results.