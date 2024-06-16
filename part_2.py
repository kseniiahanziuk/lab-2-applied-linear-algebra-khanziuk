import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def show_original():
    original_image = imread("borzyi_piesek.jpg")
    print("The size of the original piesek image(height, width): ", original_image.shape)
    plt.imshow(original_image)
    plt.axis("off")
    plt.show()
    return original_image


def black_n_white(original_image):
    image_sum = original_image.sum(axis=2)
    image_bw = image_sum / image_sum.max()
    print("\nThe size of black and white piesek image(height, width): ", image_bw.shape)
    plt.imshow(image_bw, "gray")
    plt.axis("off")
    plt.show()
    return image_bw


def cumulative_variance(image_bw):
    pca = PCA()
    pca.fit(image_bw)
    cumulative_variance = np.cumsum(pca.explained_variance_ratio_)
    components = np.argmax(cumulative_variance >= 0.95) + 1
    print("\nNumber of components that cover 95% variance: ", components)
    plt.plot(cumulative_variance)
    plt.title("Cumulative Explained Variance explained by the components")
    plt.xlabel("Principal components")
    plt.ylabel("Cumulative Explained Variance")
    plt.axvline(x=components, color='b', linestyle='--')
    plt.axhline(y=0.95, color='g', linestyle='dotted')
    plt.show()
    return components


def reconstruct_image(image_bw, components):
    pca = PCA(n_components=components)
    transform_image_bw = pca.fit_transform(image_bw)
    reconstructed_image_bw = pca.inverse_transform(transform_image_bw)
    plt.imshow(reconstructed_image_bw, cmap='gray')
    plt.title(f"\nReconstructed image with {components} components")
    plt.axis('off')
    plt.show()


def different_reconstruct(image_bw):
    components = [5, 20, 40, 50, 150, 250]
    plt.figure(figsize=(10, 8))
    for i, component in enumerate(components, 1):
        pca = PCA(n_components=component)
        transform_image_bw = pca.fit_transform(image_bw)
        reconstructed_image_bw = pca.inverse_transform(transform_image_bw)
        plt.subplot(2, 3, i)
        plt.imshow(reconstructed_image_bw, cmap='gray')
        plt.title(f"\n{component} components")
    plt.tight_layout()
    plt.show()


def main():
    original = show_original()
    image_bw = black_n_white(original)
    components = cumulative_variance(image_bw)
    reconstruct_image(image_bw, components)
    different_reconstruct(image_bw)


main()
