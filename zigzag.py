import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main programme loop
        print(' ' * indent, end= '')
        print('********')
        time.sleep(0.1) # Pause for 0.10 seconds.

        if indentIncreasing:
        # Increase the number of spaces:
            indent = indent + 1 
            if indent == 20:
                # Change direction:
                indentIncreasing = False
        else:
            # Dexrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()