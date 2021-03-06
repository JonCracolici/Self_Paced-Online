#!/usr/bin/env python3

# NEIMA SCHAFI, LESSON 6 Assignment - mailroom part 4 (refactored)
donors = {
            'Leon Dechino': [200.43, 30.23, 1.50],
            'Rupert Everton': [23.99],
            'Zordon Lagasse': [400.00, 500.00, 600.00],
            'Kavinsky Mega': [23.23, 100.45],
            'Corey Camelot': [1.00, 2.00]
            }


def menu(prompt, picks):
    """Main menu function which user can select one of the options shown"""
    while True:
        selection = input(prompt)
        try:
            selection = int(selection)
        except ValueError:
            print('ERROR: Input a menu item number.')
            continue
        try:
            pick.get(selection)()
        except TypeError:
            print('ERROR: Number inputted is not a menu item.')
            continue


def send_all():
    for x in donors:
        x2 = x.split(' ', 2)
        amount = donors[x][-1]
        write_email(x, x2, amount)
    print('Sent out emails to everyone!')


def write_email(normal, split, amount):
    s = ('Dear {},\n\n\tThanks for the ${:.2f} donation.\n\n\t'
            'We will use it to bring back the spin doctors.\n\n\n\t\t'
            'Thanks,\n\t\t\tPost Malone'.format(normal, amount))
    if len(split) >= 3:  # 3 names ex: William Gates III
            with open('{}_{}_{}.txt'.format(split[0], split[1], split[2]), 'w') as f:
                f.write(s)
    else:
            with open('{}_{}.txt'.format(split[0], split[1]), 'w') as f:
                f.write(s)


def thank_you():
    """Function which tests if name inputted is in a list or not, adds the
    name if not on the list then calls donation function"""
    name = input('Please enter a full name or enter "list" for'
                    ' list of names or enter "Menu" to return to main prompt: ')
    while name.isdigit() or name == "":
        name = input('\nNot a valid name. Please enter a full name or enter'
                        '"list" for list of names or enter "Menu" to return to main prompt: ')
    if name.title() == "Menu":
        menu(prompt, pick)
    elif name.lower() == "list":
        list_names()
    elif name.title() in donors:
        donate(name.title(), 1)
    else:
        donate(name.title(), 0)

def list_names():
    """Prints list of names in alphabetical order"""
    s = []
    for x in donors:
        s.append(x)
    s.sort()
    print('\nLIST OF DONORS')
    for y in s:
        print(y)

def donate(n, t):
    """Adds donated amount to donors running amount
    then calls email function to print thank you"""
    while True:
        donation = input('Enter donation amount or enter "Menu" to return to main prompt: ')
        if donation.title() == "Menu":
            menu(prompt, pick)
        try:
            donation = float(donation)
            if t == 1:  # Case that the name exists already in donors list
                name_exists(n, donation)
                email(n, donation)
            else:  # Case that the name DOESNT exist so need to add user with donation
                name_unknown(n, donation)
                email(n, donation)
        except ValueError:
            print('ERROR: Please enter a numeric amount.')
            continue

def name_exists(name, donation):
    """Adds donation to already existing name"""
    donation = float(donation)
    donors[name].append(donation)

def name_unknown(name, donation):
    """Adds donation and name of donor to dict"""
    donation = float(donation)
    donors[name] = [donation]

def email(name, donation):
    """Writes thank you email to donor for given amount"""
    print('\nDear {}, \n\tThank you for your generous ${:.2f} donation.'
            '\n\tYou are an amazing person. Good job!'.format(name.title(), donation))


def report():
    """Prints table of donors"""
    print('{:25} | {:>15} | {:9} | {:>14}'.format('Donor Name',
            'Total Given', 'Num Gifts', 'Average Gift') + '\n' + '-'*73)
    d_total = {sum(donors[item]): item for item in donors}
    d_sort = sorted(d_total, reverse=True)  # Put in list since dict not ordered
    for amount in d_sort:
            print('{:25} | ${:>14.2f} | {:9} | ${:14.2f}'
                    .format(d_total[amount], amount, len(donors[d_total[amount]]),
                    (amount/len(donors[d_total[amount]]))))

def quit():
    raise SystemExit()


prompt = ('\nChoose an action (select number):\n 1 - Send a Thank You\n'
            ' 2 - Create a Report\n 3 - Send letters to everyone\n'
            ' 4 - Quit\n Your selection: ')
pick = {1: thank_you, 2: report, 3: send_all, 4: quit}


if __name__ == '__main__':
    menu(prompt, pick)
