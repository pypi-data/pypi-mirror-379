print("This is my code. Imported successfully!")

def noisel():
    code = """\
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Noise addition functions
def add_uniform_noise(img, low=-50, high=50):
    row, col = img.shape
    noise = np.random.uniform(low, high, (row, col))
    noisy = img + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_gaussian_noise(img, mean=0, sigma=25):
    row, col = img.shape
    noise = np.random.normal(mean, sigma, (row, col))
    noisy = img + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_rayleigh_noise(img, scale=30):
    row, col = img.shape
    noise = np.random.rayleigh(scale, (row, col))
    noisy = img + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_exponential_noise(img, scale=0.05):
    row, col = img.shape
    noise = np.random.exponential(scale, (row, col))
    noisy = img + noise*255
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_laplacian_noise(img, mean=0, scale=20):
    row, col = img.shape
    noise = np.random.laplace(mean, scale, (row, col))
    noisy = img + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(img, salt_prob=0.40, pepper_prob=0.40):
    noisy = img.copy()
    num_salt = np.ceil(salt_prob * img.size)
    num_pepper = np.ceil(pepper_prob * img.size)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in img.shape]
    noisy[coords[0], coords[1]] = 255
    coords = [np.random.randint(0, i-1, int(num_pepper)) for i in img.shape]
    noisy[coords[0], coords[1]] = 0
    return noisy

def add_gamma_noise(img, shape=2.0, scale=1.0):
    row, col = img.shape
    noise = np.random.gamma(shape, scale, (row, col))
    noisy = img + noise*10
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_poisson_noise(img):
    vals = len(np.unique(img))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(img * vals) / float(vals)
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_additive_noise(img, mean=0, sigma=20):
    noise = np.random.normal(mean, sigma, img.shape)
    noisy = img + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_multiplicative_noise(img, mean=1.0, sigma=0.05):
    noise = np.random.normal(mean, sigma, img.shape)
    noisy = img * noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

# Noise removal filter functions
def apply_mean_filter(img, kernel_size=3):
    return cv2.blur(img, (kernel_size, kernel_size))

def apply_box_filter(img, kernel_size=3):
    return cv2.boxFilter(img, -1, (kernel_size, kernel_size), normalize=True)

def apply_median_filter(img, kernel_size=3):
    return cv2.medianBlur(img, kernel_size)

def apply_gaussian_filter(img, kernel_size=3, sigma=0):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

def apply_min_filter(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(img, kernel, iterations=1)

def apply_max_filter(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)

# Function to plot histogram
def plot_histogram(img, title):
    plt.hist(img.ravel(), bins=256, range=(0, 255), density=True, alpha=0.7)
    plt.title(f"Histogram: {title}")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)

# Load image (replace with your image path)
img = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/Sun.jpg", 0)

# Check if image is loaded successfully
if img is None:
    raise FileNotFoundError("Image not found at the specified path.")

# Dictionary of noise functions
noises = {
    "Uniform": add_uniform_noise(img),
    "Gaussian": add_gaussian_noise(img),
    "Rayleigh": add_rayleigh_noise(img),
    "Exponential": add_exponential_noise(img),
    "Laplacian": add_laplacian_noise(img),
    "Salt & Pepper": add_salt_pepper_noise(img),
    "Gamma": add_gamma_noise(img),
    "Poisson": add_poisson_noise(img),
    "Additive": add_additive_noise(img),
    "Multiplicative": add_multiplicative_noise(img)
}

# Dictionary of filter functions
filters = {
    "Mean": apply_mean_filter,
    "Box": apply_box_filter,
    "Median": apply_median_filter,
    "Gaussian": apply_gaussian_filter,
    "Min": apply_min_filter,
    "Max": apply_max_filter
}

# Plot original and noisy images
plt.figure(figsize=(18, 12))
plt.subplot(3, 4, 1), plt.imshow(img, cmap='gray'), plt.title("Original"), plt.axis('off')

for i, (name, noisy_img) in enumerate(noises.items(), start=2):
    plt.subplot(3, 4, i), plt.imshow(noisy_img, cmap='gray'), plt.title(name), plt.axis('off')

plt.tight_layout()
plt.show()

# Plot histograms for original and noisy images
plt.figure(figsize=(18, 12))
plt.subplot(3, 4, 1)
plot_histogram(img, "Original")

for i, (name, noisy_img) in enumerate(noises.items(), start=2):
    plt.subplot(3, 4, i)
    plot_histogram(noisy_img, name)

plt.tight_layout()
plt.show()

# Apply filters to each noisy image and plot results
for noise_name, noisy_img in noises.items():
    plt.figure(figsize=(18, 12))
    plt.subplot(3, 4, 1), plt.imshow(noisy_img, cmap='gray'), plt.title(f"Noisy: {noise_name}"), plt.axis('off')

    for i, (filter_name, filter_func) in enumerate(filters.items(), start=2):
        # Adjust kernel size for Salt & Pepper noise with Median filter for better results
        kernel_size = 5 if noise_name == "Salt & Pepper" and filter_name == "Median" else 3
        filtered_img = filter_func(noisy_img, kernel_size)
        plt.subplot(3, 4, i), plt.imshow(filtered_img, cmap='gray'), plt.title(filter_name), plt.axis('off')

    plt.tight_layout()
    plt.show()"""
    return code

def histh():
    code = """\import cv2
import matplotlib.pyplot as plt

# ---------------- Hard-coded Histogram Specification ----------------

def compute_histogram(img):
    hist = [0]*256
    for row in img:
        for pixel in row:
            hist[pixel] += 1
    return hist

def compute_cdf(hist):
    cdf = [0]*256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + hist[i]
    # Normalize CDF to [0, 1]
    cdf_normalized = [x/cdf[-1] for x in cdf]
    return cdf_normalized

def create_mapping(src_cdf, ref_cdf):
    mapping = [0]*256
    for i in range(256):
        # Find the reference intensity with closest CDF value
        diff = [abs(src_cdf[i] - ref_cdf[j]) for j in range(256)]
        mapping[i] = diff.index(min(diff))
    return mapping

def apply_mapping(img, mapping):
    rows, cols = img.shape
    matched = [[0]*cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matched[i][j] = mapping[img[i][j]]
    return matched

# ---------------- Main ----------------

# Load grayscale images
source = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/Sun.jpg", 0)
reference =cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/sun2.jpg", 0)

# Compute histograms
source_hist = compute_histogram(source)
reference_hist = compute_histogram(reference)

# Compute CDFs
source_cdf = compute_cdf(source_hist)
reference_cdf = compute_cdf(reference_hist)

# Compute mapping
mapping = create_mapping(source_cdf, reference_cdf)

# Apply mapping
matched = apply_mapping(source, mapping)

# Convert matched to proper numpy array for plotting
import numpy as np
matched = np.array(matched, dtype='uint8')

# Plot results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1), plt.imshow(source, cmap='gray'), plt.title("Source Image"), plt.axis('off')
plt.subplot(2,3,2), plt.imshow(reference, cmap='gray'), plt.title("Reference Image"), plt.axis('off')
plt.subplot(2,3,3), plt.imshow(matched, cmap='gray'), plt.title("Matched Image"), plt.axis('off')

plt.subplot(2,3,4), plt.bar(range(256), source_hist), plt.title("Source Histogram")
plt.subplot(2,3,5), plt.bar(range(256), reference_hist), plt.title("Reference Histogram")
plt.subplot(2,3,6), plt.bar(range(256), compute_histogram(matched)), plt.title("Matched Histogram")

plt.tight_layout()
plt.show()"""
    return code 

def hist():
    code = """\
import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_matching(source, reference):
    
    # Compute histograms
    src_hist, bins = np.histogram(source.flatten(), 256, [0,256])
    ref_hist, bins = np.histogram(reference.flatten(), 256, [0,256])

    # Compute cumulative distribution function (CDF)
    src_cdf = np.cumsum(src_hist).astype(np.float32)
    src_cdf /= src_cdf[-1]  # normalize to [0,1]

    ref_cdf = np.cumsum(ref_hist).astype(np.float32)
    ref_cdf /= ref_cdf[-1]  # normalize to [0,1]

    # Create mapping
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        idx = np.argmin(np.abs(src_cdf[i] - ref_cdf))
        mapping[i] = idx

    # Apply mapping
    matched = cv2.LUT(source, mapping)
    return matched

# ---------------- Main ----------------

# Load grayscale images
source = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/Sun.jpg", 0)
reference =cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/sun2.jpg", 0)

# Histogram Matching
matched = histogram_matching(source, reference)

# Plot results
plt.figure(figsize=(12,8))

plt.subplot(2,3,1), plt.imshow(source, cmap='gray'), plt.title("Source Image"), plt.axis('off')
plt.subplot(2,3,2), plt.imshow(reference, cmap='gray'), plt.title("Reference Image"), plt.axis('off')
plt.subplot(2,3,3), plt.imshow(matched, cmap='gray'), plt.title("Matched Image"), plt.axis('off')

# Histograms
plt.subplot(2,3,4), plt.hist(source.ravel(), bins=256, range=(0,256)), plt.title("Source Histogram")
plt.subplot(2,3,5), plt.hist(reference.ravel(), bins=256, range=(0,256)), plt.title("Reference Histogram")
plt.subplot(2,3,6), plt.hist(matched.ravel(), bins=256, range=(0,256)), plt.title("Matched Histogram")

plt.tight_layout()
plt.show()
"""
    return code

def fourier():
    code = """\
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Fourier Transform ----------------
def fourier_transform(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)   # Shift zero frequency to center
    magnitude = 20*np.log(np.abs(fshift) + 1)
    phase = np.angle(fshift)
    amplitude = np.abs(fshift)
    return f, fshift, magnitude, phase, amplitude

# Distance function
def distance(u, v, M, N):
    return np.sqrt((u - M/2)**2 + (v - N/2)**2)

# ---------------- Frequency Domain Filters ----------------
def ideal_low_pass(img_shape, D0):
    M, N = img_shape
    H = np.zeros((M, N))
    for u in range(M):
        for v in range(N):
            if distance(u, v, M, N) <= D0:
                H[u, v] = 1
    return H

def ideal_high_pass(img_shape, D0):
    return 1 - ideal_low_pass(img_shape, D0)

def gaussian_low_pass(img_shape, D0):
    M, N = img_shape
    H = np.zeros((M, N))
    for u in range(M):
        for v in range(N):
            D = distance(u, v, M, N)
            H[u, v] = np.exp(-(D**2) / (2*(D0**2)))
    return H

def gaussian_high_pass(img_shape, D0):
    return 1 - gaussian_low_pass(img_shape, D0)

def butterworth_low_pass(img_shape, D0, n=2):
    M, N = img_shape
    H = np.zeros((M, N))
    for u in range(M):
        for v in range(N):
            D = distance(u, v, M, N)
            H[u, v] = 1 / (1 + (D / D0)**(2*n))
    return H

def butterworth_high_pass(img_shape, D0, n=2):
    return 1 - butterworth_low_pass(img_shape, D0, n)

# Apply filter in frequency domain
def apply_filter(img, H):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    G = fshift * H
    magnitude = 20*np.log(np.abs(G) + 1)   # Spectrum after filtering
    img_back = np.fft.ifft2(np.fft.ifftshift(G))
    img_back = np.abs(img_back)
    return img_back, magnitude

#----------- Spatial Domain Filters ----------------
def spatial_filters(img):
    results = {}

    # Low-pass filters
    results["Average Blur"] = cv2.blur(img, (5, 5))
    results["Gaussian Blur"] = cv2.GaussianBlur(img, (5, 5), 1)

    # High-pass filters
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    results["Laplacian (HPF)"] = cv2.convertScaleAbs(laplacian)

    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    results["Sobel (HPF)"] = cv2.convertScaleAbs(sobelx + sobely)

    # Sharpening filter (High-boost like)
    kernel_sharpen = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])
    results["Sharpen"] = cv2.filter2D(img, -1, kernel_sharpen)

    return results

# ---------------- MAIN ----------------
# Load two grayscale images
img1 = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/Sun.jpg", 0)
img2 = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/sun2.jpg", 0)

# Parameters
D0 = 30
n = 2

# Process both images
for idx, img in enumerate([img1, img2], start=1):
    f, fshift, magnitude, phase, amplitude = fourier_transform(img)

    # Plot Fourier components
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title(f"Original Image {idx}"), plt.axis('off')

    plt.subplot(2, 2, 2), plt.imshow(magnitude, cmap='gray')
    plt.title("Magnitude Spectrum"), plt.axis('off')

    plt.subplot(2, 2, 3), plt.imshow(phase, cmap='gray')
    plt.title("Phase Spectrum"), plt.axis('off')

    plt.subplot(2, 2, 4), plt.imshow(amplitude, cmap='gray')
    plt.title("Amplitude Spectrum"), plt.axis('off')
    plt.suptitle(f"Fourier Analysis for Image {idx}")
    plt.show()

    # ---------- Frequency Domain Filters ----------
    filters = {
        "Ideal LPF": ideal_low_pass(img.shape, D0),
        "Ideal HPF": ideal_high_pass(img.shape, D0),
        "Gaussian LPF": gaussian_low_pass(img.shape, D0),
        "Gaussian HPF": gaussian_high_pass(img.shape, D0),
        "Butterworth LPF": butterworth_low_pass(img.shape, D0, n),
        "Butterworth HPF": butterworth_high_pass(img.shape, D0, n)
    }

    plt.figure(figsize=(14, 10))
    plt.subplot(3, 3, 1), plt.imshow(img, cmap='gray')
    plt.title("Original"), plt.axis('off')

    plt.subplot(3, 3, 2), plt.imshow(magnitude, cmap='gray')
    plt.title("Original Spectrum"), plt.axis('off')

    i = 3
    for name, H in filters.items():
        filtered_img, filtered_mag = apply_filter(img, H)
        plt.subplot(3, 3, i), plt.imshow(filtered_img, cmap='gray')
        plt.title(name), plt.axis('off')
        i += 1

    plt.suptitle(f"Frequency Domain Filtering - Image {idx}")
    plt.tight_layout()
    plt.show()

    # ---------- Spatial Domain Filters ----------
    spatial_results = spatial_filters(img)
    plt.figure(figsize=(14, 10))
    plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray')
    plt.title("Original"), plt.axis('off')

    i = 2
    for name, res in spatial_results.items():
        plt.subplot(2, 3, i), plt.imshow(res, cmap='gray')
        plt.title(name), plt.axis('off')
        i += 1

    plt.suptitle(f"Spatial Domain Filtering - Image {idx}")
    plt.tight_layout()
    plt.show()
"""
    return code 