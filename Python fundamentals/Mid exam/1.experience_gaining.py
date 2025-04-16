def main():
    experience_needed = float(input())
    total_battles = int(input())

    collected_experience = 0
    for battle in range(1, total_battles + 1):
        experience_gained_per_battle = float(input())

        if battle % 3 == 0:
            experience_gained_per_battle *= 1.15
        if battle % 5 == 0:
            experience_gained_per_battle *= 0.90
        if battle % 15 == 0:
            experience_gained_per_battle *= 1.05

        collected_experience += experience_gained_per_battle

        if collected_experience >= experience_needed:
            print(f"Player successfully collected his needed experience for {battle} battles.")
            return

    remaining_experience = experience_needed - collected_experience
    print(f"Player was not able to collect the needed experience, {remaining_experience:.2f} more needed.")


if __name__ == "__main__":
    main()
