from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn


def histograms(pos_labels, neg_labels, pos_name, neg_name):
    fig = plt.figure(figsize=(15, 15))

    # Duration
    ax = fig.add_subplot(331)
    ax.set_xlabel("Duration (ms)")
    ax.set_ylabel("# Observations")
    pos_labels["duration_ms"].hist(alpha=0.7, bins=25, color="crimson")
    ax1 = fig.add_subplot(331)
    neg_labels["duration_ms"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Tempo
    ax2 = fig.add_subplot(332)
    ax2.set_xlabel("Tempo")
    ax2.set_ylabel("# Observations")
    pos_labels["tempo"].hist(alpha=0.7, bins=25, color="crimson")
    ax3 = fig.add_subplot(332)
    neg_labels["tempo"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Instrumentalness
    ax4 = fig.add_subplot(333)
    ax4.set_xlabel("Instrumentalness")
    ax4.set_ylabel("# Observations")
    pos_labels["instrumentalness"].hist(alpha=0.7, bins=25, color="crimson")
    ax5 = fig.add_subplot(333)
    neg_labels["instrumentalness"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Danceability
    ax6 = fig.add_subplot(334)
    ax6.set_xlabel("Danceability")
    ax6.set_ylabel("# Observations")
    pos_labels["danceability"].hist(alpha=0.7, bins=25, color="crimson")
    ax7 = fig.add_subplot(334)
    neg_labels["danceability"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Acousticness
    ax8 = fig.add_subplot(335)
    ax8.set_xlabel("Acousticness")
    ax8.set_ylabel("# Observations")
    pos_labels["acousticness"].hist(alpha=0.7, bins=25, color="crimson")
    ax9 = fig.add_subplot(335)
    neg_labels["acousticness"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Speechiness
    ax10 = fig.add_subplot(336)
    ax10.set_xlabel("Speechiness")
    ax10.set_ylabel("# Observations")
    pos_labels["speechiness"].hist(alpha=0.7, bins=25, color="crimson")
    ax11 = fig.add_subplot(336)
    neg_labels["speechiness"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Valence
    ax12 = fig.add_subplot(337)
    ax12.set_xlabel("Valence")
    ax12.set_ylabel("# Observations")
    pos_labels["valence"].hist(alpha=0.7, bins=25, color="crimson")
    ax13 = fig.add_subplot(337)
    neg_labels["valence"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Loudness
    ax14 = fig.add_subplot(338)
    ax14.set_xlabel("Loudness")
    ax14.set_ylabel("# Observations")
    pos_labels["loudness"].hist(alpha=0.7, bins=25, color="crimson")
    ax15 = fig.add_subplot(338)
    neg_labels["loudness"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    # Energy
    ax16 = fig.add_subplot(339)
    ax16.set_xlabel("Energy")
    ax16.set_ylabel("# Observations")
    pos_labels["energy"].hist(alpha=0.7, bins=25, color="crimson")
    ax17 = fig.add_subplot(339)
    neg_labels["energy"].hist(alpha=0.7, bins=25, color="turquoise")
    c_patch = mpatches.Patch(color="crimson", label=pos_name)
    h_patch = mpatches.Patch(color="turquoise", label=neg_name)
    plt.legend(handles=[c_patch, h_patch])

    plt.show()


def correlation_matrix(df):

    # format data
    correlations = df.drop(["class"], axis=1).corr()
    names = list(df.drop(["class"], axis=1).columns.values)

    # add figure
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111)

    # set correlation matrix params
    cax = ax.matshow(correlations, cmap="coolwarm", vmin=-1, vmax=1)
    fig.colorbar(cax)
    ticks = np.arange(0, 13, 1)

    # set tick values
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(names)
    ax.set_yticklabels(names)
    plt.xticks(rotation=30)

    plt.show()


def plot_confusion_matrix(y_test, y_pred):
    def font_color(value):
        if value < 100:
            return "black"
        else:
            return "white"

    cm = confusion_matrix(y_test, y_pred)

    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    res = ax.imshow(
        cm, cmap=plt.cm.binary, interpolation="nearest", vmin=0, vmax=300
    )

    # add color bar
    plt.colorbar(res)

    # annotate confusion entries
    width = len(cm)
    height = len(cm[0])

    for x in xrange(width):
        for y in xrange(height):
            ax.annotate(
                str(cm[x][y]),
                xy=(y, x),
                horizontalalignment="center",
                verticalalignment="center",
                color=font_color(cm[x][y]),
            )
