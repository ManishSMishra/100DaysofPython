
with open('Day24\Input\\Names\invited_names.txt') as f:
    lines=f.readlines()


for line in lines:
    with open('Day24\Input\Letters\starting_letter.txt','r') as inputs:
            with open(f"Day24\Output\ReadyToSend\letter_for_{line.strip()}", "w") as output:
                for input in inputs:
                    if "[name]" in input:
                        output.write(input.replace("[name]",line.strip()))
                    else:
                        output.write(input)