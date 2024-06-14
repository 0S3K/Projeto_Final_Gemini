import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

texto = (input("Informe o texto: "))
tokens = word_tokenize(texto)
print("Número de tokens:", len(tokens))
print("Tokens:", tokens)
import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict



nltk.download('punkt')

texto = input("Informe o texto: ")
tokens = list(texto)  # Inicializa os tokens como uma lista de caracteres
print("Tokens iniciais:", tokens)


# # print()

# # def get_stats(tokens):
# #     pairs = defaultdict(int)
# #     for i in range(len(tokens) - 1):
# #         pairs[tuple(tokens[i:i+2])] += 1
# #     return pairs

# # def merge_tokens(best_pair, tokens):
# #     new_tokens = []
# #     i = 0
# #     while i < len(tokens):
# #         try:
# #             j = tokens.index(best_pair[0], i)
# #             new_tokens.extend(tokens[i:j])
# #             i = j
# #         except ValueError:
# #             new_tokens.extend(tokens[i:])
# #             break
# #         if tokens[i:i+2] == list(best_pair):
# #             new_tokens.append(''.join(tokens[i:i+2]))
# #             i += 2
# #         else:
# #             new_tokens.append(tokens[i])
# #             i += 1
# #     return new_tokens

# # num_merges = 6
# # for i in range(num_merges):
# #     pairs = get_stats(tokens)
# #     most_frequent_pair = max(pairs, key=pairs.get)
# #     tokens = merge_tokens(most_frequent_pair, tokens)
# #     print(f"Passo {i + 1}:")
# #     print("Pares:", list(map(tuple, [tokens[i:i+2] for i in range(len(tokens) - 1)])))
# #     print(f"Novo token mais frequente: {most_frequent_pair}")
# #     print("Tokens:", tokens)
# #     print()

# # print("Token final:", tokens[0])

# from collections import defaultdict

# texto = input("Informe o texto: ")
# tokens = list(texto)  # Inicializa os tokens como uma lista de caracteres
# print("Tokens iniciais:", tokens)
# print()

# def get_stats(tokens):
#     pairs = defaultdict(int)
#     for i in range(len(tokens) - 1):
#         pairs[tuple(tokens[i:i+2])] += 1
#     return pairs

# def merge_tokens(best_pair, tokens):
#     new_tokens = []
#     i = 0
#     while i < len(tokens):
#         try:
#             j = tokens.index(best_pair[0], i)
#             new_tokens.extend(tokens[i:j])
#             i = j
#         except ValueError:
#             new_tokens.extend(tokens[i:])
#             break
#         if tokens[i:i+2] == list(best_pair):
#             new_tokens.append(''.join(tokens[i:i+2]))
#             i += 2
#         else:
#             new_tokens.append(tokens[i])
#             i += 1
#     return new_tokens

# num_merges = 6
# for i in range(num_merges):
#     pairs = get_stats(tokens)
#     most_frequent_pair = max(pairs, key=pairs.get)
#     tokens = merge_tokens(most_frequent_pair, tokens)
#     print(f"Passo {i + 1}:")
#     print("Pares:", list(map(tuple, [tokens[i:i+2] for i in range(len(tokens) - 1)])))
#     print(f"Novo token mais frequente: {most_frequent_pair}")
#     print("Tokens:", tokens)
#     print()

# print("Token final:", tokens[0])



# from collections import defaultdict

# def bpe(texto):
#     tokens = list(texto)
#     vocab = defaultdict(int)

#     print("Tokens iniciais:", tokens)
#     print()

#     while len(tokens) > 1:  # Continue until only one token remains
#         # Count pairs
#         for i in range(len(tokens) - 1):
#             pair = (tokens[i], tokens[i + 1])
#             vocab[pair] += 1

#         # Find most frequent pair
#         most_frequent_pair = max(vocab, key=vocab.get)

#         # Merge the most frequent pair
#         new_tokens = []
#         i = 0
#         while i < len(tokens):
#             if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == most_frequent_pair:
#                 new_tokens.append(tokens[i] + tokens[i + 1])
#                 i += 2
#             else:
#                 new_tokens.append(tokens[i])
#                 i += 1

#         tokens = new_tokens
#         vocab = defaultdict(int)  # Reset the vocabulary for the next iteration

#         print("Tokens:", tokens)
#         print()

#     return tokens[0]

# texto = input("Informe o texto: ")
# encoded_texto = bpe(texto)
# print("Texto codificado (BPE):", encoded_texto)
