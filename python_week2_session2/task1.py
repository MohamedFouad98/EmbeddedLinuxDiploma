def generate_gpio_init_function(ddra_value):
    ddra_binary = ''.join(map(str, ddra_value))
    init_function = f"""
void gpio_init(){{
    // Initialize GPIO pins here
    DDRA = 0b{ddra_binary};  // Set DDRA value
}}
"""

    return init_function

def main():
    pin_count = 8
    ddra_value = []

    for pin in range(pin_count):
        value = int(input(f"Enter value (0 or 1) for Pin {pin}: "))
        value = 1 if value > 1 else value
        ddra_value.append(value)
    ddra_value.reverse()
    init_code = generate_gpio_init_function(ddra_value)

    with open("gpio_init.c", "w") as file:
        file.write(init_code)

if __name__ == "__main__":
    main()
