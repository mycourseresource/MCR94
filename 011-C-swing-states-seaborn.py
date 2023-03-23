import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


swing_states = pd.read_csv('011 - 2008_swing_states.csv')

sns.set_theme()

sns.swarmplot(x='state', y='dem_share', data=swing_states)


plt.hist(swing_states['dem_share'], bins=20)
plt.title('Swing States')
plt.xlabel('States')
plt.ylabel('Percentage')
plt.savefig('011-C - 2008_swing_states.png', bbox_inches='tight')




