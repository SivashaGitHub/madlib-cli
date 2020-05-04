from textwrap import dedent

def read_template(path):
    with open(path) as file:
        template = file.read()
        return (template)
        #print(template)

def parse_template(template):

    stripped =""
    parts =[]
    capturing = False
    current_part = ""

    for char in template:
        if char == "{":
            stripped += char
            capturing = True
            current_part =""
        elif char == "}":
            stripped +=char
            capturing = False
            parts.append(current_part)
        elif capturing:
            current_part += char
        else: 
            stripped += char

    return (stripped,tuple(parts))

def collect_input(parts):
    responses = []
    for part in parts:
        response = input(f"Enter a {part}")
        responses.append(response)
    return responses

def merge(stripped_template, response):
    return stripped_template.format(*response)

def save_madlib(merged,path):
    with open(path, "w") as f:
        f.write(merged)

def main(path):
    print ("Madlib CLI Game!!")
    template = read_template(path)
    stripped, parts = parse_template(template)
    responses = collect_input(parts)
    merged = merge(stripped,responses)
    print(merged)
    out_path = path.replace(".txt","completed.txt")

    save_madlib(merged,out_path)

if __name__ == "__main__":
    path ="files/template2.txt"
    main(path)
