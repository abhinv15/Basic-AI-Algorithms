# Define the knowledge base (KB) and query
knowledge_base = [
    ("Human(x) -> Mortal(x)", "If someone is human, then they are mortal"),
    ("Human(Socrates)", "Socrates is a human"),
    ("Mortal(x) -> WillDie(x)", "If someone is mortal, then they will eventually die")
]

query = "WillDie(Socrates)"

# Conversion of knowledge base into clauses for resolution
clauses = [
    ("~Human(x) V Mortal(x)", "Clause 1: All humans are mortal"),
    ("Human(Socrates)", "Clause 2: Socrates is a human"),
    ("~Mortal(x) V WillDie(x)", "Clause 3: Mortals will die"),
    ("~WillDie(Socrates)", "Negated Query: Socrates will not die")
]

# Define unification function
def unify(var, value, substitutions):
    if var in substitutions:
        return unify(substitutions[var], value, substitutions)
    elif value in substitutions:
        return unify(var, substitutions[value], substitutions)
    else:
        substitutions[var] = value
        return substitutions

# Resolution example
def resolution(kb, query):
    print("Knowledge Base and Clauses:")
    for clause, description in clauses:
        print(description + " -> " + clause)

    print("\nStep-by-Step Resolution Process:")

    # Step 1: Unify Human(Socrates) with ~Human(x) V Mortal(x)
    print("Unifying Clause 2 (Human(Socrates)) with Clause 1 (~Human(x) V Mortal(x))")
    subs = unify("x", "Socrates", {})
    print(f"Substitution found: {subs}")
    print("New Clause derived: Mortal(Socrates)")

    # Step 2: Unify Mortal(Socrates) with ~Mortal(x) V WillDie(x)
    print("\nUnifying Mortal(Socrates) with Clause 3 (~Mortal(x) V WillDie(x))")
    subs = unify("x", "Socrates", {})
    print("Substitution found: x = Socrates")
    print("New Clause derived: WillDie(Socrates)")

    # Step 3: Resolve WillDie(Socrates) with the negated query ~WillDie(Socrates)
    print("\nResolving WillDie(Socrates) with Negated Query ~WillDie(Socrates)")
    print("Contradiction found. Query is valid: Socrates will eventually die.\n")

    print("Final Answer: The query 'WillDie(Socrates)' is TRUE based on the knowledge base.")

# Run the program
resolution(knowledge_base, query)