inventory = {}
sales = []


def add_product(name, price, stock, *tags, **extra_details):
    inventory[name] = {"price": int(price), "stock": int(stock), "tags": tags}
    if inventory[name]:
        inventory[name].update(**extra_details)


def process_sale(customer_name, *items_to_buy):
    total_cost = 0
    successful_items = []
    for item in items_to_buy:
        if (inventory.get(item) is not None) and (inventory[item]["stock"] > 0):
            inventory[item]["stock"] -= 1
            total_cost += inventory[item]["price"]
            successful_items.append(item)
        else:
            print(f"{item} you're searching for is out of stock or not in inventory!!")
    
    if successful_items:
        sales.append(f"{customer_name} bought {successful_items} for Rs.{total_cost} ")
        print(sales[-1])


def get_unique_tags():
    tag = set()
    for item in inventory.values():
        tag.update(item["tags"])

    return tag


while True:
    res = int(
        input(
            " === Supermarket System === \n 1. Add a new product \n 2. Process a sale \n 3. View inventory \n 4. View unique product categories (tags) \n 5. Exit\n ========================== \n"
        )
    )
    match res:
        case 1:
            print("=" * 80)
            inp = input(
                "Enter the name, price, stock, tags and extra details separated by  comma: "
            )
            name, price, stock, *args = inp.split(",")
            add_product(name.capitalize(), price, stock, *args)
            print("=" * 80)

        case 2:
            print("=" * 80)
            uname = input(
                "Enter your name and item you want to buy separated by comma: "
            )
            name, item = uname.split(",")
            process_sale(name.strip().capitalize(), item.strip().capitalize())
            print("=" * 80)

        case 3:
            print("=" * 80)
            if not inventory:
                print("No items in inventory")
            else:
                print("Item Name    price       stock       tags            extra details")
                for key, value in inventory.items():
                    print(
                    f"{key}        {value['price']}       {value['stock']}        {value.get('tags')}         {value.get('extra_details')}"
                )
                print("-" * 80)
                
            print("=" * 80)

        case 4:
            print("=" * 80)
            print("The unique product categories are: \t")
            print(f"{get_unique_tags()}")
            print("=" * 80)

        case 5:
            break

        case _:
            print("Default input. Retry again. ")
