import argparse
from engine import get_answer
from config import HELP_MESSAGE


def parse_args():
    parser = argparse.ArgumentParser(
        description="Чат-бот на ключевых словах для университета Синергия"
    )
    parser.add_argument(
        "--once",
        help="Один запрос и выход. Пример: --once \"Какие документы по практике?\"",
        default=None,
    )
    return parser.parse_args()


def interactive_mode():
    print(HELP_MESSAGE)
    while True:
        user_input = input("> ").strip()
        if not user_input:
            continue
        if user_input.lower() in {"exit", "quit"}:
            break
        print(get_answer(user_input))


def main():
    args = parse_args()

    if args.once:
        print(get_answer(args.once))
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
