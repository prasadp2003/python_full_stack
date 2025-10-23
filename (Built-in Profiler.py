import cProfile
import pstats

def slow_function():
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# Profile the function
cProfile.run('slow_function()', 'profile_stats')

# Read the stats
stats = pstats.Stats('profile_stats')
stats.strip_dirs().sort_stats('time').print_stats(10)
