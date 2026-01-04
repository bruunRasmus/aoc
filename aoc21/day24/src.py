monad_instructions = open("input.txt").read().strip().splitlines()
monad_instructions = [l.split(" ") for l in monad_instructions]
monad_instructions = [(m[0],(m[1:])) for m in monad_instructions]

def run_monad(number):
    i = 0
    variables = {"w":0,"x":0,"y":0,"z":0}
    for ins,vals in monad_instructions:
        if ins == "inp":
            variables[vals[0]] = int(number[i])
            i+=1
        if ins == "add":
            a,b = vals
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] + b
        if ins == "mul":
            a,b = vals
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] * b
        if ins == "div":
            a,b = vals
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] // b
        if ins == "mod":
            a,b = vals
            b = variables[b] if b in variables else int(b)
            variables[a] = variables[a] % b
        if ins == "eql":
            a,b = vals
            b = variables[b] if b in variables else int(b)
            variables[a] = int(variables[a] == b)

    return variables["z"]

#found by pen and paper
hi = "69914999975369" 
lo = "14911675311114"

print(run_monad(hi))
print(run_monad(lo))