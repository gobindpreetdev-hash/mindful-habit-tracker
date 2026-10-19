import random
import datetime

# 1. Core Data Structures
habits_catalog = {
    "gym": 3,
    "coding": 2,
    "reading": 1,
    "meditation": 1,
    "deep_cleaning": 3
}

self_care_tips = [
    "Drink a glass of water and look away from screens for 5 mins.",
    "Take 5 deep diaphragmatic breaths.",
    "Do a quick 10-minute light body stretch.",
    "Step outside for a brief breath of fresh air."
]

# 2. Application State Variables
today_completed = []
total_energy_spent = 0
MAX_ENERGY = 6

print("=======================================")
print("     Welcome to MindfulHabit Tracker   ")
print("=======================================")

# 3. Main Application Loop
while True:
    print("\n--- Main Menu ---")
    print("1. Log a completed habit")
    print("2. View daily status & burnout risk")
    print("3. Exit program")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        # Display available habits clearly
        print("\nAvailable habits to log:")
        for name, cost in habits_catalog.items():
            print(f"  • {name.replace('_', ' ').title()} (Energy Cost: {cost})")
            
        habit = input("\nWhat did you complete? ").lower().strip()
        
        # Validation Step A: Check if the habit exists in our catalog
        if habit not in habits_catalog:
            print(f"❌ '{habit}' is not in your habits catalog. Please try again.")
            continue
            
        habit_cost = habits_catalog[habit]
        
        # Validation Step B: Check if adding this habit causes burnout (> MAX_ENERGY)
        if total_energy_spent + habit_cost > MAX_ENERGY:
            print(f"\n⚠️  [BLOCKED] Logging '{habit}' would push you past your safe daily energy limit ({MAX_ENERGY} points)!")
            print(f"💡 Self-Care Recommendation: {random.choice(self_care_tips)}")
        else:
            # Step C: Log the habit successfully with a timestamp
            timestamp = datetime.datetime.now().strftime("%I:%M %p")
            today_completed.append({"name": habit, "cost": habit_cost, "time": timestamp})
            total_energy_spent += habit_cost
            print(f"✅ Successfully logged '{habit}' (+{habit_cost} energy points) at {timestamp}.")
            
    elif choice == "2":
        print("\n================ DAILY STATUS ================")
        print(f"Energy Spent: {total_energy_spent} / {MAX_ENERGY} points")
        
        # Step D: Dynamically calculate burnout risk safety levels
        if total_energy_spent >= 5:
            status = "🔴 Warning: Nearing Burnout! Slow down."
        elif total_energy_spent >= 3:
            status = "🟡 Moderate Activity: Balanced day so far."
        else:
            status = "🟢 Optimal: Energy levels are highly sustainable."
            
        print(f"Burnout Risk Status: {status}")
        print("----------------------------------------------")
        
        # Display list of completed items
        print("Completed Tasks Today:")
        if not today_completed:
            print("  No habits logged yet today. Get started!")
        else:
            for idx, task in enumerate(today_completed, 1):
                name_clean = task['name'].replace('_', ' ').title()
                print(f"  {idx}. [{task['time']}] {name_clean} (Cost: {task['cost']})")
        print("==============================================")
        
    elif choice == 3:
        print("\nThank you for using MindfulHabit Tracker. Take care of yourself! Goodbye.")

    else:
        print("❌ Invalid option. Please enter 1, 2, or 3.")

