import click
import just_count.square

@click.command()
@click.argument("base")

def main(base):
    print(f"The square of {base} is {just_count.square.square(float(base))}")

if __name__ == '__main__':
    main()