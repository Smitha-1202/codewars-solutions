def HQ9(code):
    if code=='H':
        return 'Hello World!'
    elif code == 'Q':
        return code
    elif code == '9':
        song = ''
        for i in range(99, 0, -1):
            current = 'bottle' if i == 1 else 'bottles'
            next_n  = 'no more bottles' if i == 1 else f'{i-1} {"bottle" if i-1 == 1 else "bottles"}'
            
            song += f'{i} {current} of beer on the wall, {i} {current} of beer.\n'
            song += f'Take one down and pass it around, {next_n} of beer on the wall.\n'
        
        song += 'No more bottles of beer on the wall, no more bottles of beer.\n'
        song += 'Go to the store and buy some more, 99 bottles of beer on the wall.'
        return song
    
    return None