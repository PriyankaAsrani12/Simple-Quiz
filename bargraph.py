import matplotlib.pyplot as plt
import DbHelper

def showgraph():
    query = "SELECT max(Score) FROM result GROUP BY AdminId"
    params = None
    res = DbHelper.get_all_data(query, params)
    height = []
    for i in res:
        for j in i:
            height.append(j)
    print(height)
    query1 = "SELECT Username FROM practice_user"
    params1 = None
    res1 = DbHelper.get_all_data(query1, params1)
    tl = []
    for i in res1:
        for j in i:
            tl.append(j)
    print(tl)
    left=[]
    for i in range(1,len(height)+1):
        left.append(i)
    print(left)
    plt.bar(left, height, tick_label=tl,width=0.8, color='lightblue')
    plt.xlabel('Student Name')
    plt.ylabel('Scores')
    plt.title('Highest Marks Scored till Date')
    plt.show()

