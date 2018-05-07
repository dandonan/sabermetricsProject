# CoHRE
## Comparative Home Run Effect

## Sabermetrics Final Project
## Daniel Yedidovich

### To Run
Open the main.html file in a web browser.

### Introduction
Park Effects show how each park affects the probability of different events happening during a game. This can be helpful to compare the performance of teams and individual players between parks and get a more accurate comparison point for the performance of each player and team between parks. However, what Park Effect lacks is a way to see more individual effects on performance at each park.

What CoHRE introduces is a way to see if different parks have different Park Effects (specifically for home runs) for different players. So for instance we can look at Nolan Arenado and we can find that at Oriole Park, he has a CoHRE score of 0.75, meaning at Oriole Park he on average scores 25% less home runs than at a generic park while at Comerica Park, he has a CoHRE score of 1.875.

CoHRE can be a tool for in-depth analysis of different players to discover where they perform best and understand why different parks may have different effects on different players.

### The Stat
CoHRE is calculated using Retrosheet. From events, we pull all homeruns at each park each player has performed, and calculate what their average home run per game ratio is. Then we go park-by-park and calculate the CoHRE by dividing their average home run rate to their home run rate at an individual park. To try and make this statistic more accurate, this is averaged over a 4-year period (2010-2013) with higher weights for more recent years (0.25 for 2010, 0.5 for 2011, 0.75 for 2012, and 1 for 2013).  

### Limitations
CoHRE is a very data-intensive stat to run. Originally I was going to run a similar statistic for every Park Effect, but quickly ran into issues when trying to parse through all the data. Just running CoHRE took over 14 hours using both my laptop and desktop together so I decided to scrap the rest of the park effects and focus solely on home runs. While I assume my algorithm was not as optimized as it could be, this does show how data-intensive individualized Park Effects are to calculate, which could make it difficult for this to be a useful statistic.

As well, home runs may not be the best statistic for this kind of individual comparisons. Home runs are fairly rare events, especially when you try to box them out between every park and every player in a season. A particularly good game can heavily tip weight towards one park over others. While this is partially mitigated by averaging this out over several years, this statistic has more use as a thought-experiment starter (seeing if there is a reason for one player to over/underperform at a certain park) than as an accurate data point.
