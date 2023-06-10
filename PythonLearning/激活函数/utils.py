import matplotlib.pyplot as plt


def show_img(x, y_pois,titles):
    fig = plt.figure()
    # axes = []
    for i,y in enumerate(y_pois):
        ax = fig.add_subplot(3,2,i+1)
        ax.plot(x,y,color = 'blue')
        ax.grid()
        ax.set_title(titles[i])
        ax.spines['right'].set_color('none') 
        ax.spines['top'].set_color('none') 
        ax.spines['bottom'].set_position(('data',0))
        ax.spines['left'].set_position(('data',0))
    plt.show()