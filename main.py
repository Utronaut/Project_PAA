import random
import time
import matplotlib.pyplot as plt

def generate_array(n, max_value, seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def is_unique(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return False
        seen.add(num)
    return True

def check_uniqueness(arr):
    start_time = time.time()
    result = is_unique(arr)
    end_time = time.time()
    return result, end_time - start_time

def run_experiment(n, max_value, num_trials):
    worst_case = 0
    total_time = 0
    
    for _ in range(num_trials):
        arr = generate_array(n, max_value, random.randint(1, 1000))
        _, execution_time = check_uniqueness(arr)
        worst_case = max(worst_case, execution_time)
        total_time += execution_time
    
    average_case = total_time / num_trials
    return worst_case, average_case

# Assuming the last 3 digits of your stambuk are 123
stambuk_last_3 = 123
max_value = 250 - stambuk_last_3

n_values = [100, 150, 200, 250, 300, 350, 400, 500]
num_trials = 100

worst_cases = []
average_cases = []

with open('worst_avg.txt', 'w') as f:
    for n in n_values:
        worst_case, average_case = run_experiment(n, max_value, num_trials)
        worst_cases.append(worst_case)
        average_cases.append(average_case)
        
        f.write(f"n = {n}:\n")
        f.write(f"Worst case: {worst_case:.6f} seconds\n")
        f.write(f"Average case: {average_case:.6f} seconds\n\n")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(n_values, worst_cases, label='Worst Case', marker='o')
plt.plot(n_values, average_cases, label='Average Case', marker='s')
plt.xlabel('Array Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Worst Case vs Average Case Execution Time')
plt.legend()
plt.grid(True)
plt.savefig('execution_time_plot.pdf')
plt.savefig('execution_time_plot.jpg')

print("Experiment completed. Results saved in worst_avg.txt and plots saved as PDF and JPG.")