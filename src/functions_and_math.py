# Title: Unmasking the actual figures
# Author: Doug Hart
# Date Created: 4/21/2020
# Last Updated: 4/21/2020


'''~~~~~~~~~~~~~~~~~~~~~~~Part 1: establishing feasability range~~~~~~~~~~~~~~~~~~~~~~~'''
def findrange(currentnum):
    '''
    calculates range of possibilities under different assumptions
    of proportion of actual cases identied through testing

    currentnum: current official number of cases identied via testing
    '''
    possible = []
    for i in range(5,96):
        possible.append(((100/i)*currentnum)/1000000)
    return possible
possible = findrange(645936)

#Creating graph of possible infection numbers 
fig, ax=plt.subplots(figsize = (10, 8))
ax.plot(possible, scalex=True)
# gdp=ax.scatter(x = df18['ratio'], y = (df18['state_gdp']/1000))
ax.set_xlabel('Percentage of Cases Documented',fontsize = 18)
ax.set_ylabel('Total Cases in Millions',fontsize = 18)
ax.set_title('Potential Covid-19 Cases in the U.S.',fontsize = 22, pad = 8)
# ax.set_xlim([0,95])
# ax.xticks(np.arange(5, 95, step=20))
# set_xticks
# plt.set_xticks(np.arange(5, 95, step=20))
plt.xticks(np.arange(5, 95, step=15))


'''~~~~~~~~~~~~~~~~~~~~~~~~~~Part 2: estimating via simulation~~~~~~~~~~~~~~~~~~~~~~~~~'''

def letsfindout(n=1000000):
    '''
    simulates n number of infected individuals and returns proportion of those with 
    pre-existing conditions who exhibit symptoms to total, n. Assumes assymptotic 
    trait overrides pre-existing conditions or age. 
    metrics represent:
    nums[0]:no symptoms present, 25-30%
    nums[1]:over 50, 34%
    nums[2]:diabetic, or obese 39%
    nums[3]:chronic lung disease, 13%
    '''
    patients = []
    for i in range(n):
        nums = np.random.randint(1,101,4)
        patients.append([nums[0], nums[1], nums[2], nums[3]])
    count = 0
    for i in patients:
        if i[0] > 30 and i[1] > 66 or i[0] > 30 and i[2] > 61 or i[0] > 30 and i[3] > 87:
            count += 1
    return (count/n)

testedratio = letsfindout(1000000)  # = 0.455769

# to generate figure from proportion estimate
sim_est = (100/testedratio)*currentnum # = 1421201.32

# calculating percentage of total population, roughly
(sim_est/331000000)*100 # = 0.4294%
