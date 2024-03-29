def do_create(self, arg):
    """Create a new instance of a class"""
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    class_name = args[0]

    if class_name not in self.classes:
        print("** class doesn't exist **")
        return

    args = " ".join(args[1:])
    args = args.split(",")

    kwargs = {}
    for arg in args:
        key, value = arg.split("=")
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace("_", " ")
        elif "." in value:
            value = float(value)
        else:
            try:
                value = int(value)
            except ValueError:
                continue
        kwargs[key] = value

    new_instance = self.classes[class_name](**kwargs)
    new_instance.save()
    print(new_instance.id)