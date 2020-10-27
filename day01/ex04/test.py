from eval import *

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

a = Evaluator(coefs, words)

print(a.__dict__)
print(type(a))
print(a.zip_evaluate())

print(a.enumerate_evaluate())

# Evaluator.zip_evaluate(coefs, words)