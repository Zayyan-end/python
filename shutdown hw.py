def shutdown(system_name, user_confirmed, battery_level):
    if not user_confirmed:
        print(f"Shutdown cancelled. {system_name} shutdown not confirmed.")
    elif battery_level > 80:
        print(f"{system_name} has sufficient battery. Shutdown postponed.")
    else:
        print(f"{system_name} is shutting down...")

shutdown("My Laptop", user_confirmed=True, battery_level=50)

