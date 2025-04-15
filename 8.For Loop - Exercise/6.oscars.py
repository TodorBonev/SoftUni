actor_name = input()
academy_points = float(input())


if 2.0 <= academy_points <= 450.5:
    
    n = int(input())

    
    if 1 <= n <= 20:
        
        total_points = academy_points

        
        for i in range(n):
            
            reviewer_name = input()
            reviewer_points = float(input())

            
            if 1.0 <= reviewer_points <= 50.0:
                
                points = len(reviewer_name) * reviewer_points / 2

                
                total_points += points

                
                if total_points > 1250.5:
                    
                    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
                    break
            else:
                
                print("Invalid points!")
                break
        else:
           
            print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
    else:
        
        print("Invalid number of reviewers!")
else:
    
    print("Invalid points!")