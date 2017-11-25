import matplotlib.pyplot as plt
import seaborn

def histograms(pos_labels, neg_labels):
    fig = plt.figure(figsize=(15, 15))

    # Duration
    ax = fig.add_subplot(331)
    ax.set_xlabel('Duration (ms)')
    ax.set_ylabel('# Observations')
    pos_labels['duration_ms'].hist(alpha=0.75, bins=30)
    ax1 = fig.add_subplot(331)
    neg_labels['duration_ms'].hist(alpha=0.75, bins=30)

    # Tempo
    ax2 = fig.add_subplot(332)
    ax2.set_xlabel('Tempo')
    ax2.set_ylabel('# Observations')
    pos_labels['tempo'].hist(alpha=0.75, bins=30)
    ax3 = fig.add_subplot(332)
    neg_labels['tempo'].hist(alpha=0.75, bins=30)

    # Instrumentalness
    ax4 = fig.add_subplot(333)
    ax4.set_xlabel('Instrumentalness')
    ax4.set_ylabel('# Observations')
    pos_labels['instrumentalness'].hist(alpha=0.75, bins=30)
    ax5 = fig.add_subplot(333)
    neg_labels['instrumentalness'].hist(alpha=0.75, bins=30)

    # Danceability
    ax6 = fig.add_subplot(334)
    ax6.set_xlabel('Danceability')
    ax6.set_ylabel('# Observations')
    pos_labels['danceability'].hist(alpha=0.75, bins=30)
    ax7 = fig.add_subplot(334)
    neg_labels['danceability'].hist(alpha=0.75, bins=30)

    # Acousticness
    ax8 = fig.add_subplot(335)
    ax8.set_xlabel('Acousticness')
    ax8.set_ylabel('# Observations')
    pos_labels['acousticness'].hist(alpha=0.75, bins=30)
    ax9 = fig.add_subplot(335)
    neg_labels['acousticness'].hist(alpha=0.75, bins=30)

    # Speechiness
    ax10 = fig.add_subplot(336)
    ax10.set_xlabel('Speechiness')
    ax10.set_ylabel('# Observations')
    pos_labels['speechiness'].hist(alpha=0.75, bins=30)
    ax11 = fig.add_subplot(336)
    neg_labels['speechiness'].hist(alpha=0.75, bins=30)

    # Valence
    ax12 = fig.add_subplot(337)
    ax12.set_xlabel('Valence')
    ax12.set_ylabel('# Observations')
    pos_labels['valence'].hist(alpha=0.75, bins=30)
    ax13 = fig.add_subplot(337)
    neg_labels['valence'].hist(alpha=0.75, bins=30)

    # Loudness
    ax14 = fig.add_subplot(338)
    ax14.set_xlabel('Loudness')
    ax14.set_ylabel('# Observations')
    pos_labels['loudness'].hist(alpha=0.75, bins=30)
    ax15 = fig.add_subplot(338)
    neg_labels['loudness'].hist(alpha=0.75, bins=30)

    # Energy
    ax16 = fig.add_subplot(339)
    ax16.set_xlabel('Energy')
    ax16.set_ylabel('# Observations')
    pos_labels['energy'].hist(alpha=0.75, bins=30)
    ax17 = fig.add_subplot(339)
    neg_labels['energy'].hist(alpha=0.75, bins=30)

    plt.show()