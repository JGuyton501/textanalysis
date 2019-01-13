# # print count of words in string

# test = "to be or not to be"
# t_dict = {}

# # using dict
# for a in test.split():
# 	if a in t_dict:
# 		t_dict[a] += 1
# 	else:
# 		t_dict[a] = 1

# print t_dict


# word_tracker = []
# count = []

# # using list
# for a in test.split():
# 	if a not in word_tracker:
# 		count.append(1)
# 		word_tracker.append(a)
# 	else:
# 		count[word_tracker.index(a)] += 1
# print word_tracker
# print count


# prime n to 100
limit = 100
count = 0
primes = []
for i in range(1,limit):
	for j in range(1,i+1):
		if i%j == 0:
			count += 1
	if count <= 2:
		primes.append(i)
	count = 0
print primes

