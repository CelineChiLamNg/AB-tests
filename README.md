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

### Results
Both analytical and bootstrapping methods resulted in very similar mean and 
<br>
confidence intervals. Together with the results of the statistical tests, 
it <br>
is safe to conclude that both Promotion 1 and 3 are more effective 
campaigns <br>
compared to 2. Since average sales from Promotion 1 and 3 are not 
statistically <br>
different, any of these are recommended. <br>

## Cookie Cats Mobile Games
### Objectives
When a player installed the game Cookie Cats, the player would be randomly <br>
assigned to either gate_30 or gate_40. The dataset includes A/B test results
 of <br>
the game when the first gate in the game was moved from level 30 to 40. <br>
Apply A/B test to determine where should the Cookie Cats game locate its gate.

### Results
After calculating the confidence intervals, it is clear that the 7 day <br>
retention rates for the 2 versions of the game do not overlap, with a 95% <br>
confidence level. Also, with p-value under 0.05, we can safely conclude that
 <br>
 7 day retention is higher when the gate is located at level 30.
