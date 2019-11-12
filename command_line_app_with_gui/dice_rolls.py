import random
import gooey


@gooey.Gooey(default_size=(300, 300), show_success_modal=False)
def main():
    parser = gooey.GooeyParser(description='Role some dice')
    parser.add_argument('number_of_rolls', type=int, metavar='How many rolls?', choices=range(1, 10))
    args = parser.parse_args()
    for i in range(args.number_of_rolls):
        print(f'Roll {i + 1}: {random.randint(1, 6)}')


main()
