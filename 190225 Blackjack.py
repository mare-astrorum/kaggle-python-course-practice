def total_of_hand(hand):
    """
    Count the total of a blackjack hand.
    """
    total = 0
    # start counting from 0
    
    hand.sort(key='A'.__eq__)
    # sort the list, so that all 'A's are at the end
    
    for card in hand:
    # assign values to non-numeric cards
        if card == 'K':
            total += 10
        elif card == 'J':
            total += 10
        elif card == 'Q':
            total += 10
        elif card != 'A':
        # assign values to numeric cards
            total += int(card)
        elif card == 'A':
        # sort out 'A's values
            test_total = total + 10
            if test_total <= 21:
                total += 10
            else:
                total += 1
        
    return total




def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    total_1 = total_of_hand(hand_1)
    total_2 = total_of_hand(hand_2)

    if total_1 <= 21:
        if total_1 > total_2 or total_2 > 21:
            return True
        else:
            return False
    else:
        return False

        
#print(int('4'))
#print(int('K'))


hand_1 = ['A', '4', 'A', 'A', 'Q', '3']
hand_2 = ['3', '4']
blackjack_hand_greater_than(hand_1, hand_2)
#q3.check()