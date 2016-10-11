def words(phrase):
	count_dict = {}
	for l in phrase.split():
		if l.isdigit():
			count_dict.setdefault(int(l),0)
			count_dict[int(l)] += 1
		else:
			count_dict.setdefault(l,0)
			count_dict[l] += 1

	return count_dict
