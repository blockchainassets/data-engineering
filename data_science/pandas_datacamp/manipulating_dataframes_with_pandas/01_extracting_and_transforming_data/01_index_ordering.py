'''

Index ordering
In this exercise, the DataFrame election is provided for you. It contains the 2012 US election results for the state of Pennsylvania with county names as row indices. Your job is to select 'Bedford' county and the'winner' column. Which method is the preferred way?

Feel free to explore the DataFrame in the IPython Shell.

Instructions

Possible Answers
election['Bedford', 'winner']
election['Bedford']['winner']
election['eggs']['Bedford']
election.loc['Bedford', 'winner']
election.iloc['Bedford', 'winner']

'''

election.loc['Bedford', 'winner']
