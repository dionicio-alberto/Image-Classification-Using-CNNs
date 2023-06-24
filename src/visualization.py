import random
import matplotlib.pyplot as plt


def explorer(names: list,animal: str):
    """Plotting images (3x3)

    Args:
        names (list): list of PosixPath elements
        animal (str): Cat or Dog
    """
    fig, axs = plt.subplots(3,3, figsize=(20,10))
    fig.suptitle(f'{animal}', fontsize=22, weight='bold')
    
    for ax in axs.flat:
        image = str(random.choice(names))
        img_read = plt.imread(image)
        ax.imshow(img_read)
        ax.axis('off')
        ax.set_title(f'{animal} '+image[-8:-4])
    plt.show()