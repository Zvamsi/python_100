from blind_art import logo

print(logo)
continue_='yes'
bid_record={}
while continue_=='yes':

    name=input("Enter your name:\n")
    bid=int(input("Enter your bid\n"))
    bid_record[name]=bid
    continue_=input("Enter 'yes' if there are more bids else type 'no'\n").lower()
    if continue_=='no':
        break
    print('\n'*100)
good_bid=0
good_bidder=''
for key in bid_record:
    if good_bid<bid_record[key]:
        good_bid=bid_record[key]
        good_bidder=key

print("The Good bidder is",good_bidder,'And the bid is',good_bid)