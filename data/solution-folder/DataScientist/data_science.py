import matplotlib.pyplot as plt
import school_scores

scores = school_scores.get_all()
# have before here code alonged

# now what question did you have?
# what can you find out from this data?

years = []
AL_scores = []
MA_scores = []

print(school_scores)

# for score in scores:
# 	if score["State"]["Code"] == 'AL':
# 		AL_scores.append(score["Total"]["Math"])
# 		years.append(score["Year"])
# 	elif score["State"]["Code"] == 'MA':
# 		MA_scores.append(score["Total"]["Math"])
#
# plt.plot(years, AL_scores)
# plt.plot(years, MA_scores)
# plt.legend(['AL', 'MA'], loc='upper left')
#
# plt.xlabel('Years')
# plt.ylabel('Scores')
# plt.title('Average Math SAT scores in AL and MA')


plt.show()
