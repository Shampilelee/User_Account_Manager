
# I Gat A Simple Game Here, I Want To Try It Out ?

customer = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five'
}



result = ''

while True:
    user_in = input("\n'exit' to Stop \nenter :> ")
    if user_in == 'exit':
        exit()

    for gh in user_in:
        result += customer.get(gh, '!') + ' '
    print(result)

