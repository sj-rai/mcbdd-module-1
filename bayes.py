import numpy as np
import matplotlib.pyplot as plt

def calculate_posterior(prevalence, specificity, sensitivity=0.99):
    """
    Calculates P(Infected | Positive) using Bayes' Theorem.
    """
    prior = prevalence
    true_positive_rate = sensitivity * prior
    false_positive_rate = (1 - specificity) * (1 - prior)
    
    posterior = true_positive_rate / (true_positive_rate + false_positive_rate)
    return posterior

# 1. Setup Independent Variables
# Prevalence from 0.001% to 50% (log scale is often better for visualization here)
prevalence_range = np.linspace(0.00001, 0.50, 1000)
specificities = [0.99, 0.999, 0.9999, 0.99999]
sensitivity = 0.99

# 2. Create the Plot
plt.figure(figsize=(10, 6))

for spec in specificities:
    y_values = [calculate_posterior(p, spec, sensitivity) for p in prevalence_range]
    plt.plot(prevalence_range * 100, np.array(y_values) * 100, label=f'Specificity: {spec*100}%')

# 3. Formatting
plt.title("Probability of Infection Given a Positive Test Result", fontsize=14)
plt.xlabel("Infection Prevalence in Population (%)", fontsize=12)
plt.ylabel("Probability Fred is Actually Infected (%)", fontsize=12)
plt.legend()
plt.grid(True, which="both", ls="-", alpha=0.5)
plt.axvline(x=5, color='r', linestyle='--', alpha=0.6, label='5% Prevalence')
plt.text(5.5, 10, 'Task 1 Baseline (5%)', color='red', fontweight='bold')

plt.tight_layout()
plt.show()

# 4. Integer Check / Explanation Logic
def integer_check(total_pop, prev, spec, sens):
    infected = int(total_pop * prev)
    healthy = total_pop - infected
    
    true_pos = int(infected * sens)
    false_pos = int(healthy * (1 - spec))
    
    prob = (true_pos / (true_pos + false_pos)) * 100
    return infected, healthy, true_pos, false_pos, prob

# Example explanation for the 5% prevalence case
inf, heal, tp, fp, res = integer_check(100000, 0.05, 0.995, 0.995)
print(f"Check for 100,000 people:")
print(f"Actually Infected: {inf} | Healthy: {heal}")
print(f"Test Positive & Sick (TP): {tp} | Test Positive & Healthy (FP): {fp}")
print(f"Final Probability: {res:.2f}%")