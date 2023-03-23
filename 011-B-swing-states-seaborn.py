import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

swing_states = pd.read_csv('011 - 2008_swing_states.csv')

sns.set()

plt.hist(swing_states['dem_share'])
plt.title('Swing States')
plt.xlabel('Percent of Obama Votes')
plt.ylabel('Counties')
plt.savefig('011-A - 2008_swing_states.png', bbox_inches='tight')




