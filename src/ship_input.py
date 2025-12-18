def coordinates(coord):
    #print(coord)
    if len(coord) < 2 or len(coord) > 3:
        print("You need to enter 2 or 3 symbols to continue")
        return None
    
    row_letter = coord[0].upper()
    column_number = coord[1:]
    #print(row_letter, column_number)
    allowed_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if row_letter not in allowed_letters:
        print("Make sure your letter is A,B,C,D,E,F,G,H,I,J")
        return None
    
    if not column_number.isdigit() or  int(column_number) < 1 or int(column_number) > 10:
        print("Make sure your number is 1,2,3,4,5,6,7,8,9,10")
        return None
    
    row_index = ord(row_letter) - ord('A')
    column_index = int(column_number) - 1

    return row_index, column_index
    



    