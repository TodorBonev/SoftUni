percent_loaded = int(input())

def loading_bar(percent):
    output = "0% [..........]\nStill loading..."
    if 10 <= percent < 100:
        output = (f"{percent_loaded}% "
                  + "["
                  + f"{'%' * (percent // 10)}"
                  + f"{'.' * ((100 - percent) // 10)}"
                  + f"]\n"
                  + "Still loading..."
                  )
    elif percent_loaded == 100:
        output = (f"{percent_loaded}% "
                  + "Complete!\n"
                  + "["
                  + f"{'%' * (percent // 10)}"
                  + f"{'.' * ((100 - percent) // 10)}"
                  + "]"
                  )
    return output

print(loading_bar(percent_loaded))