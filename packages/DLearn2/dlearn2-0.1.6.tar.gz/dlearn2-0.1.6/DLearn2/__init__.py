print("DLearn2 Imported successfully!")

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

def histl():
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

def histh():
    code = """\
import cv2
import matplotlib.pyplot as plt

# ---------------- Hard-coded Histogram Specification ----------------

def compute_histogram(img):
    #Compute histogram manually
    hist = [0]*256
    for row in img:
        for pixel in row:
            hist[pixel] += 1
    return hist

def compute_cdf(hist):
    #Compute cumulative distribution function manually
    cdf = [0]*256
    cdf[0] = hist[0]
    for i in range(1, 256):
        cdf[i] = cdf[i-1] + hist[i]
    # Normalize CDF to [0, 1]
    cdf_normalized = [x/cdf[-1] for x in cdf]
    return cdf_normalized

def create_mapping(src_cdf, ref_cdf):
    #Create intensity mapping from source to reference CDF
    mapping = [0]*256
    for i in range(256):
        # Find the reference intensity with closest CDF value
        diff = [abs(src_cdf[i] - ref_cdf[j]) for j in range(256)]
        mapping[i] = diff.index(min(diff))
    return mapping

def apply_mapping(img, mapping):
    #Apply intensity mapping manually
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
plt.show()
"""
    return code 


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

def noiseh():
    code = """\
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------- Noise Models ----------------
def add_uniform_noise(img, low=-50, high=50):
    r, c = img.shape
    noise = np.random.uniform(low, high, (r, c))
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_gaussian_noise(img, mean=0, sigma=25):
    r, c = img.shape
    noise = np.random.normal(mean, sigma, (r, c))
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_rayleigh_noise(img, scale=30):
    r, c = img.shape
    noise = np.random.rayleigh(scale, (r, c))
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_exponential_noise(img, scale=0.05):
    r, c = img.shape
    noise = np.random.exponential(scale, (r, c))
    noisy = img.astype(np.float32) + noise * 255.0
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_laplacian_noise(img, mean=0, scale=20):
    r, c = img.shape
    noise = np.random.laplace(mean, scale, (r, c))
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(img, salt_prob=0.02, pepper_prob=0.02):
    noisy = img.copy()
    r, c = img.shape
    num_salt = int(np.ceil(salt_prob * img.size))
    num_pepper = int(np.ceil(pepper_prob * img.size))
    # Salt
    coords = [np.random.randint(0, i, num_salt) for i in img.shape]
    noisy[coords[0], coords[1]] = 255
    # Pepper
    coords = [np.random.randint(0, i, num_pepper) for i in img.shape]
    noisy[coords[0], coords[1]] = 0
    return noisy

def add_gamma_noise(img, shape=2.0, scale=1.0):
    r, c = img.shape
    noise = np.random.gamma(shape, scale, (r, c))
    noisy = img.astype(np.float32) + noise * 10.0
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_poisson_noise(img):
    # Simple Poisson model: scale intensities, draw Poisson, rescale
    img_float = img.astype(np.float32) / 255.0
    peak = 30.0  # photon scale (adjustable)
    lam = img_float * peak
    noisy = np.random.poisson(lam).astype(np.float32) / peak
    noisy = np.clip(noisy * 255.0, 0, 255).astype(np.uint8)
    return noisy

def add_additive_noise(img, mean=0, sigma=20):
    r, c = img.shape
    noise = np.random.normal(mean, sigma, (r, c))
    noisy = img.astype(np.float32) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_multiplicative_noise(img, mean=1.0, sigma=0.05):
    r, c = img.shape
    noise = np.random.normal(mean, sigma, (r, c))
    noisy = img.astype(np.float32) * noise
    return np.clip(noisy, 0, 255).astype(np.uint8)

# ---------------- Hardcoded Filters (spatial domain) ----------------

def pad_reflect(img, pad):
    return np.pad(img, pad, mode='reflect')

def convolve2d(img, kernel):
    k = kernel.shape[0]
    pad = k // 2
    padded = pad_reflect(img, pad)
    out = np.zeros_like(img, dtype=np.float32)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+k, j:j+k]
            out[i, j] = np.sum(region * kernel)
    return np.clip(out, 0, 255)

def apply_mean_filter(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size*kernel_size)
    out = convolve2d(img, kernel)
    return out.astype(np.uint8)

def apply_box_filter(img, kernel_size=3):
    return apply_mean_filter(img, kernel_size)  # same as mean

def apply_median_filter(img, kernel_size=3):
    pad = kernel_size // 2
    padded = pad_reflect(img, pad)
    out = np.zeros_like(img, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+kernel_size, j:j+kernel_size].ravel()
            out[i, j] = np.median(region)
    return out

def gaussian_kernel(kernel_size=3, sigma=1.0):
    pad = kernel_size // 2
    ax = np.arange(-pad, pad+1, dtype=np.float32)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2.0 * sigma**2))
    kernel /= np.sum(kernel)
    return kernel

def apply_gaussian_filter(img, kernel_size=3, sigma=1.0):
    kernel = gaussian_kernel(kernel_size, sigma)
    out = convolve2d(img, kernel)
    return out.astype(np.uint8)

def apply_min_filter(img, kernel_size=3):
    pad = kernel_size // 2
    padded = pad_reflect(img, pad)
    out = np.zeros_like(img, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+kernel_size, j:j+kernel_size]
            out[i, j] = np.min(region)
    return out

def apply_max_filter(img, kernel_size=3):
    pad = kernel_size // 2
    padded = pad_reflect(img, pad)
    out = np.zeros_like(img, dtype=np.uint8)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            region = padded[i:i+kernel_size, j:j+kernel_size]
            out[i, j] = np.max(region)
    return out

# ---------------- Utility: histogram plotting ----------------
def plot_histogram(img, title=None):
    plt.hist(img.ravel(), bins=256, range=(0, 255), density=True, color='gray')
    if title: plt.title(title)

# ---------------- Main / Demo ----------------

# Load image (use a moderate-size image for performance)
img = cv2.imread("/content/drive/MyDrive/Semester_9/Computer_Vision/CA 2 portions/Sun.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Image not found at the path.")

# Resize a bit for speed if large
max_size = 512
h, w = img.shape
if max(h, w) > max_size:
    scale = max_size / max(h, w)
    img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_AREA)

# Generate noisy images (all requested types)
noises = {
    "Uniform": add_uniform_noise(img),
    "Gaussian": add_gaussian_noise(img),
    "Rayleigh": add_rayleigh_noise(img),
    "Exponential": add_exponential_noise(img),
    "Laplacian": add_laplacian_noise(img),
    "Salt & Pepper": add_salt_pepper_noise(img, salt_prob=0.02, pepper_prob=0.02),
    "Gamma": add_gamma_noise(img),
    "Poisson": add_poisson_noise(img),
    "Additive": add_additive_noise(img),
    "Multiplicative": add_multiplicative_noise(img)
}

# Filters to apply (hardcoded implementations)
filter_funcs = [
    ("Mean", apply_mean_filter),
    ("Median", apply_median_filter),
    ("Gaussian", apply_gaussian_filter),
    ("Min", apply_min_filter),
    ("Max", apply_max_filter)
]

# Show original + all noisy images
n = len(noises) + 1
cols = 4
rows = math.ceil(n / cols)
plt.figure(figsize=(4*cols, 3*rows))
plt.subplot(rows, cols, 1)
plt.imshow(img, cmap='gray'); plt.title("Original"); plt.axis('off')
for i, (name, noisy) in enumerate(noises.items(), start=2):
    plt.subplot(rows, cols, i)
    plt.imshow(noisy, cmap='gray'); plt.title(name); plt.axis('off')
plt.tight_layout()
plt.show()

# Plot histograms for original + noisy images (optional)
plt.figure(figsize=(4*cols, 3*rows))
plt.subplot(rows, cols, 1); plot_histogram(img, "Original Histogram")
for i, (name, noisy) in enumerate(noises.items(), start=2):
    plt.subplot(rows, cols, i); plot_histogram(noisy, f"{name} Hist")
plt.tight_layout()
plt.show()

# Apply filters (hard-coded) to every noisy image and display
for noise_name, noisy_img in noises.items():
    # pick kernel sizes: larger median for salt & pepper
    k_med = 5 if noise_name == "Salt & Pepper" else 3
    k = 5 if noise_name in ["Poisson", "Multiplicative"] else 3

    # apply
    mean_f = apply_mean_filter(noisy_img, kernel_size=k)
    median_f = apply_median_filter(noisy_img, kernel_size=k_med)
    gauss_f = apply_gaussian_filter(noisy_img, kernel_size=k, sigma=1.0)
    min_f = apply_min_filter(noisy_img, kernel_size=3)
    max_f = apply_max_filter(noisy_img, kernel_size=3)

    # show
    plt.figure(figsize=(15,6))
    plt.subplot(1,6,1), plt.imshow(noisy_img, cmap='gray'), plt.title(f"Noisy: {noise_name}"), plt.axis('off')
    plt.subplot(1,6,2), plt.imshow(mean_f, cmap='gray'), plt.title("Mean"), plt.axis('off')
    plt.subplot(1,6,3), plt.imshow(median_f, cmap='gray'), plt.title("Median"), plt.axis('off')
    plt.subplot(1,6,4), plt.imshow(gauss_f, cmap='gray'), plt.title("Gaussian"), plt.axis('off')
    plt.subplot(1,6,5), plt.imshow(min_f, cmap='gray'), plt.title("Min"), plt.axis('off')
    plt.subplot(1,6,6), plt.imshow(max_f, cmap='gray'), plt.title("Max"), plt.axis('off')
    plt.suptitle(f"Filtering results for: {noise_name}")
    plt.tight_layout()
    plt.show()
"""
    return code


def highboost():
    code = """\
# Unsharp Masking & High-Boost Filtering for Grayscale (OpenCV)
# Uses only: cv2, numpy

import cv2
import numpy as np

def unsharp_mask(gray, sigma=1.5, amount=1.5, threshold=0):
    
    #gray: uint8 grayscale image
    #sigma: Gaussian blur sigma
    #amount: strength of sharpening (typical 0.5–2.0)
    #threshold: only sharpen edges with |mask| >= threshold (0–255)
    
    gray_f = gray.astype(np.float32)
    # Gaussian blur
    blurred = cv2.GaussianBlur(gray_f, ksize=(0,0), sigmaX=sigma, sigmaY=sigma, borderType=cv2.BORDER_REPLICATE)
    # High-frequency mask
    mask = gray_f - blurred

    if threshold > 0:
        # Apply threshold to mask (soft gating)
        mabs = np.abs(mask)
        gate = (mabs >= threshold).astype(np.float32)
        mask = mask * gate

    # Add scaled mask back
    sharp = gray_f + amount * mask
    sharp = np.clip(sharp, 0, 255).astype(np.uint8)
    return sharp

def high_boost(gray, sigma=1.5, k=2.0):
    #gray: uint8 grayscale image
    #sigma: Gaussian blur sigma
    #k: high-boost factor (>1). k=1 reduces to original; larger = stronger boost.
    #Formula: output = original + k * (original - blurred)
    gray_f = gray.astype(np.float32)
    blurred = cv2.GaussianBlur(gray_f, ksize=(0,0), sigmaX=sigma, sigmaY=sigma, borderType=cv2.BORDER_REPLICATE)
    hb = gray_f + k * (gray_f - blurred)
    hb = np.clip(hb, 0, 255).astype(np.uint8)
    return hb

if __name__ == "__main__":
    # Load grayscale image
    img = cv2.imread("input.png", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("grey.png", img)
    # Unsharp mask examples
    usm_soft  = unsharp_mask(img, sigma=1.0, amount=1.0, threshold=0)
    usm_crisp = unsharp_mask(img, sigma=1.5, amount=1.8, threshold=3)

    # High-boost examples
    hb_mild = high_boost(img, sigma=1.0, k=1.2)
    hb_strong = high_boost(img, sigma=1.5, k=2.5)

    # Save results
    cv2.imwrite("unsharp_soft.png", usm_soft)
    cv2.imwrite("unsharp_crisp.png", usm_crisp)
    cv2.imwrite("highboost_mild.png", hb_mild)
    cv2.imwrite("highboost_strong.png", hb_strong)"""
    return code

def cnnimage():
    code = """\
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Image parameters
img_width, img_height = 150, 150
batch_size = 32

# Data augmentation and preprocessing
train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2 # Use 20% of training data for validation
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Load training data
train_generator = train_datagen.flow_from_directory(
    '/content/drive/MyDrive/PSG/SEMESTER_9/Deep_Learning/skin_dataset/Skin_Data/',
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary',
    subset='training'
)

# Load validation data
validation_generator = train_datagen.flow_from_directory(
    '/content/drive/MyDrive/PSG/SEMESTER_9/Deep_Learning/skin_dataset/Skin_Data/',
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary',
    subset='validation'
)

# Load testing data
test_generator = test_datagen.flow_from_directory(
    '/content/drive/MyDrive/PSG/SEMESTER_9/Deep_Learning/skin_dataset/Skin_Data/',
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary',
    shuffle=False # Keep data in order for evaluation
)

# Build the CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid') # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Train the model
epochs = 10

history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

# Evaluate the model on the test set
loss, accuracy = model.evaluate(test_generator)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# Plot training history (optional)
import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()"""
    return code

def cnncsv():
    code = """\
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Reshape data for CNN (add a channel dimension)
X_train_reshaped = X_train_scaled[:, :, np.newaxis]
X_test_reshaped = X_test_scaled[:, :, np.newaxis]

# Build the CNN model
model = Sequential([
    Conv1D(filters=32, kernel_size=2, activation='relu', input_shape=(X_train_reshaped.shape[1], 1)),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(10, activation='relu'),
    Dense(3, activation='softmax') # 3 classes in Iris dataset
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(X_train_reshaped, y_train, epochs=50, validation_data=(X_test_reshaped, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test_reshaped, y_test)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# Optional: Plot training history
import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.show()

plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label = 'val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

"""
    return code 

def cnndataset():
    code = """\
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset from CSV
# -----------------------------
# Example: dataset.csv where last column is the target
data = pd.read_csv("dataset.csv")   # <--- put your csv file here

# Separate features (X) and target (y)
X = data.iloc[:, :-1].values   # all columns except last
y = data.iloc[:, -1].values    # last column as labels

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# Feature scaling
# -----------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -----------------------------
# Reshape for CNN (Conv1D expects 3D input: samples, timesteps, channels)
# -----------------------------
X_train_reshaped = X_train_scaled[:, :, np.newaxis]
X_test_reshaped = X_test_scaled[:, :, np.newaxis]

# -----------------------------
# Build CNN model
# -----------------------------
num_classes = len(np.unique(y))  # detect number of classes automatically

model = Sequential([
    Conv1D(filters=32, kernel_size=2, activation='relu',
           input_shape=(X_train_reshaped.shape[1], 1)),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# -----------------------------
# Train model
# -----------------------------
history = model.fit(
    X_train_reshaped, y_train,
    epochs=50,
    validation_data=(X_test_reshaped, y_test),
    verbose=1
)

# -----------------------------
# Evaluate
# -----------------------------
loss, accuracy = model.evaluate(X_test_reshaped, y_test)
print(f"\nTest Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

# -----------------------------
# Plot history
# -----------------------------
plt.plot(history.history['accuracy'], label='train_accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.show()

plt.plot(history.history['loss'], label='train_loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
"""
    return code 

def convolution():
    code = """\
        print("Convolution in deep learning is a fundamental operation used to extract features from input data, typically images. It involves sliding a small filter (or kernel) over the input data and computing a dot product between the filter and the local region of the input it's currently covering. This process generates a feature map that highlights specific patterns or characteristics in the data, such as edges, corners, or textures. By using multiple filters, a convolutional layer can learn to detect a variety of features at different levels of abstraction.")
print("\nPooling, often used after convolutional layers, is a technique for reducing the spatial dimensions (width and height) of the feature maps while retaining the most important information. The most common types are max pooling and average pooling. Max pooling takes the maximum value within a defined window, effectively keeping the most prominent feature in that region. Average pooling takes the average value. Pooling helps to reduce the number of parameters and computations in the network, making it more computationally efficient and helping to prevent overfitting by providing a form of translation invariance.")
import numpy as np
import matplotlib.pyplot as plt
def convolve2d(image, kernel):
    
    image_height, image_width = image.shape
    kernel_height, kernel_width = kernel.shape
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1

    output = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):
            # Extract the local region
            image_region = image[i:i + kernel_height, j:j + kernel_width]
            # Perform element-wise multiplication and summation
            output[i, j] = np.sum(image_region * kernel)

    return output

# Define a sample input image and kernel
input_image = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]])

convolution_kernel = np.array([[1, 0],
                             [0, -1]])

# Perform convolution
output_image = convolve2d(input_image, convolution_kernel)

# Print the results
print("Input Image:")
print(input_image)
print("\nConvolution Kernel:")
print(convolution_kernel)
print("\nOutput Image after Convolution:")
print(output_image)

def max_pooling2d(input_matrix, pool_size, stride):
    
    #Performs 2D max pooling on an input matrix.

    #Args:
       # input_matrix: A 2D NumPy array representing the input matrix.
      #  pool_size: A tuple (pool_height, pool_width) representing the size of the pooling window.
     #   stride: A tuple (stride_height, stride_width) representing the step size for the pooling window.

    #Returns:
    #    A 2D NumPy array representing the output after max pooling.
    
    input_height, input_width = input_matrix.shape
    pool_height, pool_width = pool_size
    stride_height, stride_width = stride

    # Calculate output dimensions
    output_height = (input_height - pool_height) // stride_height + 1
    output_width = (input_width - pool_width) // stride_width + 1

    output_matrix = np.zeros((output_height, output_width))

    # Perform max pooling
    for i in range(output_height):
        for j in range(output_width):
            # Extract the region
            row_start = i * stride_height
            row_end = row_start + pool_height
            col_start = j * stride_width
            col_end = col_start + pool_width
            input_region = input_matrix[row_start:row_end, col_start:col_end]

            # Apply max pooling
            output_matrix[i, j] = np.max(input_region)

    return output_matrix

# Define a sample input matrix and parameters
input_matrix_pooling = np.array([[1, 2, 3, 4, 5],
                                 [6, 7, 8, 9, 10],
                                 [11, 12, 13, 14, 15],
                                 [16, 17, 18, 19, 20],
                                 [21, 22, 23, 24, 25]])

pool_size = (2, 2)
stride = (2, 2)

# Perform max pooling
output_matrix_pooling = max_pooling2d(input_matrix_pooling, pool_size, stride)

# Print the results
print("Input Matrix for Pooling:")
print(input_matrix_pooling)
print("\nPool Size:", pool_size)
print("Stride:", stride)
print("\nOutput Matrix after Max Pooling:")
print(output_matrix_pooling)

# 1. Define a new sample input image
input_image_combined = np.array([[1, 1, 2, 4],
                                 [5, 6, 7, 8],
                                 [3, 2, 1, 0],
                                 [1, 2, 3, 4]])

# 2. Define a convolution kernel
convolution_kernel_combined = np.array([[1, 0],
                                      [0, 1]])

# 3. Apply the previously defined convolve2d function
convolved_output = convolve2d(input_image_combined, convolution_kernel_combined)

# 4. Define the pool_size and stride for the pooling operation
pool_size_combined = (2, 2)
stride_combined = (2, 2)

# 5. Apply the previously defined max_pooling2d function
pooled_output = max_pooling2d(convolved_output, pool_size_combined, stride_combined)

# 6. Print the results
print("Original Input Image:")
print(input_image_combined)
print("\nConvolution Kernel:")
print(convolution_kernel_combined)
print("\nOutput after Convolution:")
print(convolved_output)
print("\nOutput after Pooling:")
print(pooled_output)


## Summary:

### Data Analysis Key Findings

# *   The process successfully implemented Python functions for 2D convolution and 2D max pooling using NumPy.
# *   The `convolve2d` function correctly computes the convolution of an input image with a kernel, handling the output dimensions without padding.
# *   The `max_pooling2d` function effectively reduces the spatial dimensions of an input matrix by taking the maximum value within defined pooling windows with a specified stride.
# *   A simple example demonstrated the typical sequential application of convolution followed by max pooling on a sample input matrix, showing the output after each operation.

### Insights or Next Steps

# *   The implemented functions provide a basic foundation for understanding the core operations of convolutional neural networks.
# *   Further steps could involve adding padding options to the convolution function, implementing other pooling types (e.g., average pooling), and integrating these functions into a simple layered structure to mimic a basic CNN architecture.
        """
    return code 

def all():
    code = """\
    noiseh()
    noisel()
    cnnimage()
    cnndataset()
    cnncsv()
    histh()
    histl()
    fourier()
    convolution()
    convolutionl()
    highboost()
    cnnboth()
    harmonic()"""
    return code 


def histn():
    code = """\
import cv2
import matplotlib.pyplot as plt
import numpy as np

# ---------------- Histogram Specification (same logic) ----------------

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
    cdf_normalized = [x/cdf[-1] for x in cdf]
    return cdf_normalized

def create_mapping(src_cdf, ref_cdf):
    mapping = [0]*256
    for i in range(256):
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

source = cv2.imread("/Users/nayeeemx/Downloads/download (1).jpeg", 0)
reference = cv2.imread("/Users/nayeeemx/Downloads/download (1).jpeg", 0)

source_hist = compute_histogram(source)
reference_hist = compute_histogram(reference)
source_cdf = compute_cdf(source_hist)
reference_cdf = compute_cdf(reference_hist)
mapping = create_mapping(source_cdf, reference_cdf)
matched = np.array(apply_mapping(source, mapping), dtype='uint8')

# ---------------- Unique Plotting ----------------

plt.figure(figsize=(10,12))

# Images (keep same but rearranged order)
plt.subplot(3,2,1), plt.imshow(source, cmap='gray')
plt.title("Original Source"), plt.axis('off')

plt.subplot(3,2,2), plt.imshow(reference, cmap='gray')
plt.title("Reference Image"), plt.axis('off')

plt.subplot(3,2,3), plt.imshow(matched, cmap='gray')
plt.title("Histogram Matched"), plt.axis('off')

# Histograms as **line plots** with styles
plt.subplot(3,2,4)
plt.plot(source_hist, color='red', linestyle='-', marker='', alpha=0.7)
plt.grid(True, linestyle='--', alpha=0.4)
plt.title("Source Histogram (Line Plot)")

plt.subplot(3,2,5)
plt.plot(reference_hist, color='blue', linestyle='--', linewidth=2)
plt.fill_between(range(256), reference_hist, color='lightblue', alpha=0.3)
plt.title("Reference Histogram (Filled Line)")

plt.subplot(3,2,6)
matched_hist = compute_histogram(matched)
plt.plot(matched_hist, color='green', linestyle='-.', marker='o', markersize=3, alpha=0.6)
plt.title("Matched Histogram (Markers)")

plt.tight_layout()
plt.show()
"""
    return code 



def noisen():
    code = """\
        import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# ---------------- Noise Generators ----------------
def uniform_noise(image, low=-40, high=40):
    rows, cols = image.shape
    noise = np.random.uniform(low, high, (rows, cols))
    result = image.astype(np.float32) + noise
    return np.clip(result, 0, 255).astype(np.uint8)

def gaussian_noise(image, mu=0, sigma=20):
    rows, cols = image.shape
    noise = np.random.normal(mu, sigma, (rows, cols))
    result = image.astype(np.float32) + noise
    return np.clip(result, 0, 255).astype(np.uint8)

def rayleigh_noise(image, scale=25):
    rows, cols = image.shape
    noise = np.random.rayleigh(scale, (rows, cols))
    result = image.astype(np.float32) + noise
    return np.clip(result, 0, 255).astype(np.uint8)

def exponential_noise(image, scale=0.08):
    rows, cols = image.shape
    noise = np.random.exponential(scale, (rows, cols))
    result = image.astype(np.float32) + noise * 255
    return np.clip(result, 0, 255).astype(np.uint8)

def laplacian_noise(image, loc=0, scale=15):
    rows, cols = image.shape
    noise = np.random.laplace(loc, scale, (rows, cols))
    result = image.astype(np.float32) + noise
    return np.clip(result, 0, 255).astype(np.uint8)

def salt_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    noisy = image.copy()
    total_pixels = image.size
    num_salt = int(salt_prob * total_pixels)
    num_pepper = int(pepper_prob * total_pixels)
    
    coords_salt = [np.random.randint(0, i, num_salt) for i in image.shape]
    noisy[coords_salt[0], coords_salt[1]] = 255
    
    coords_pepper = [np.random.randint(0, i, num_pepper) for i in image.shape]
    noisy[coords_pepper[0], coords_pepper[1]] = 0
    
    return noisy

def gamma_noise(image, shape=2.2, scale=1.2):
    rows, cols = image.shape
    noise = np.random.gamma(shape, scale, (rows, cols))
    result = image.astype(np.float32) + noise * 8
    return np.clip(result, 0, 255).astype(np.uint8)

def poisson_noise(image):
    normalized = image.astype(np.float32) / 255.0
    lam = normalized * 40
    noisy = np.random.poisson(lam).astype(np.float32) / 40
    return np.clip(noisy * 255, 0, 255).astype(np.uint8)

def additive_noise(image, mean=0, sigma=15):
    rows, cols = image.shape
    noise = np.random.normal(mean, sigma, (rows, cols))
    result = image.astype(np.float32) + noise
    return np.clip(result, 0, 255).astype(np.uint8)

def multiplicative_noise(image, mean=1.0, sigma=0.1):
    rows, cols = image.shape
    noise = np.random.normal(mean, sigma, (rows, cols))
    result = image.astype(np.float32) * noise
    return np.clip(result, 0, 255).astype(np.uint8)

# ---------------- Filtering Functions ----------------
def reflect_pad(image, pad):
    return np.pad(image, pad, mode="reflect")

def custom_convolution(image, kernel):
    k = kernel.shape[0]
    pad = k // 2
    padded = reflect_pad(image, pad)
    output = np.zeros_like(image, dtype=np.float32)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+k, j:j+k]
            output[i, j] = np.sum(region * kernel)
    
    return np.clip(output, 0, 255)

def mean_filter(image, size=3):
    kernel = np.ones((size, size), dtype=np.float32) / (size * size)
    return custom_convolution(image, kernel).astype(np.uint8)

def median_filter(image, size=3):
    pad = size // 2
    padded = reflect_pad(image, pad)
    out = np.zeros_like(image, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region = padded[i:i+size, j:j+size]
            out[i, j] = np.median(region)
    return out

def gaussian_kernel(size=3, sigma=1.0):
    axis = np.arange(-(size//2), size//2 + 1)
    xx, yy = np.meshgrid(axis, axis)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / np.sum(kernel)

def gaussian_filter(image, size=3, sigma=1.0):
    kernel = gaussian_kernel(size, sigma)
    return custom_convolution(image, kernel).astype(np.uint8)

def min_filter(image, size=3):
    pad = size // 2
    padded = reflect_pad(image, pad)
    out = np.zeros_like(image, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            out[i, j] = np.min(padded[i:i+size, j:j+size])
    return out

def max_filter(image, size=3):
    pad = size // 2
    padded = reflect_pad(image, pad)
    out = np.zeros_like(image, dtype=np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            out[i, j] = np.max(padded[i:i+size, j:j+size])
    return out

# ---------------- Histogram Plot ----------------
def display_histogram(image, title="Histogram"):
    plt.hist(image.ravel(), bins=256, range=(0, 255), color="gray")
    plt.title(title)

# ---------------- Main Execution ----------------
# Load grayscale image
img = cv2.imread("/Users/nayeeemx/Downloads/download (1).jpeg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("Could not load the image.")

# Resize for consistency
max_side = 512
h, w = img.shape
if max(h, w) > max_side:
    scale = max_side / max(h, w)
    img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_AREA)

# Generate noisy versions
noisy_versions = {
    "Uniform": uniform_noise(img),
    "Gaussian": gaussian_noise(img),
    "Rayleigh": rayleigh_noise(img),
    "Exponential": exponential_noise(img),
    "Laplacian": laplacian_noise(img),
    "Salt-Pepper": salt_pepper_noise(img, 0.02, 0.02),
    "Gamma": gamma_noise(img),
    "Poisson": poisson_noise(img),
    "Additive": additive_noise(img),
    "Multiplicative": multiplicative_noise(img),
}

# Show original and noisy images
cols = 4
rows = math.ceil((len(noisy_versions) + 1) / cols)
plt.figure(figsize=(4*cols, 3*rows))
plt.subplot(rows, cols, 1)
plt.imshow(img, cmap="gray"); plt.title("Original"); plt.axis("off")
for i, (name, noisy) in enumerate(noisy_versions.items(), start=2):
    plt.subplot(rows, cols, i)
    plt.imshow(noisy, cmap="gray"); plt.title(name); plt.axis("off")
plt.tight_layout()
plt.show()

# Show histograms
plt.figure(figsize=(4*cols, 3*rows))
plt.subplot(rows, cols, 1); display_histogram(img, "Original Hist")
for i, (name, noisy) in enumerate(noisy_versions.items(), start=2):
    plt.subplot(rows, cols, i); display_histogram(noisy, f"{name} Hist")
plt.tight_layout()
plt.show()

# Apply filters on each noisy image
for n_name, n_img in noisy_versions.items():
    k_median = 5 if n_name == "Salt-Pepper" else 3
    k = 5 if n_name in ["Poisson", "Multiplicative"] else 3
    
    mean_out = mean_filter(n_img, size=k)
    median_out = median_filter(n_img, size=k_median)
    gauss_out = gaussian_filter(n_img, size=k, sigma=1.0)
    min_out = min_filter(n_img, size=3)
    max_out = max_filter(n_img, size=3)
    
    plt.figure(figsize=(15,6))
    plt.subplot(1,6,1), plt.imshow(n_img, cmap="gray"), plt.title(f"Noisy: {n_name}"), plt.axis("off")
    plt.subplot(1,6,2), plt.imshow(mean_out, cmap="gray"), plt.title("Mean"), plt.axis("off")
    plt.subplot(1,6,3), plt.imshow(median_out, cmap="gray"), plt.title("Median"), plt.axis("off")
    plt.subplot(1,6,4), plt.imshow(gauss_out, cmap="gray"), plt.title("Gaussian"), plt.axis("off")
    plt.subplot(1,6,5), plt.imshow(min_out, cmap="gray"), plt.title("Min"), plt.axis("off")
    plt.subplot(1,6,6), plt.imshow(max_out, cmap="gray"), plt.title("Max"), plt.axis("off")
    plt.suptitle(f"Filtering Results - {n_name}")
    plt.tight_layout()
    plt.show()

    """
    return code 


def convolutionl():
    code = """\
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Example using Keras
# Create a simple sequential model
model = keras.Sequential([
    # Add a Convolutional layer
    layers.Conv2D(filters=1, kernel_size=(2, 2), activation='relu', input_shape=(4, 4, 1)),
    # Add a MaxPooling layer
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
])

# Input data (needs to be 4D for Keras Conv2D: batch_size, height, width, channels)
input_data_keras = np.array([[1, 1, 2, 4],
                             [5, 6, 7, 8],
                             [3, 2, 1, 0],
                             [1, 2, 3, 4]])
input_data_keras = input_data_keras.reshape(1, 4, 4, 1) # Reshape for Keras

# Get the output after convolution and pooling
output_keras = model.predict(input_data_keras)

print("\nInput data for Keras:")
print(input_data_keras.reshape(4, 4)) # Print in original shape for clarity
print("\nOutput after Keras Conv2D and MaxPooling:")
print(output_keras.reshape(output_keras.shape[1], output_keras.shape[2])) # Reshape to 2D for clarity   """
    return code 

def convolutionn():
    code = """\
import numpy as np
import cv2
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt

# ---------------- Model ----------------
# Simple CNN with Conv2D + MaxPooling
model = keras.Sequential([
    layers.Conv2D(filters=1, kernel_size=(3, 3), activation='relu', input_shape=(None, None, 1)),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2))
])

# ---------------- Image Preprocessing ----------------
# Load image (grayscale)
img = cv2.imread("your_image.jpg", cv2.IMREAD_GRAYSCALE)

# Normalize to 0–1 (Keras prefers float32)
img = img.astype("float32") / 255.0

# Reshape for Keras: (batch, height, width, channels)
input_img = img.reshape(1, img.shape[0], img.shape[1], 1)

# ---------------- Forward Pass ----------------
output = model.predict(input_img)

# ---------------- Results ----------------
print("\nInput shape:", input_img.shape)   # e.g. (1, 256, 256, 1)
print("Output shape after Conv2D+Pooling:", output.shape)

# Visualize
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap="gray")
plt.title("Input Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(output[0, :, :, 0], cmap="gray")
plt.title("After Conv+Pooling")
plt.axis("off")

plt.show()
    """
    return code 



def cnnboth():
    code = """\
        import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.losses import BinaryCrossentropy, CategoricalCrossentropy

img_width, img_height = 150, 150
batch_size = 32

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Determine the number of classes
# Assuming the directory structure is /dataset/class1, /dataset/class2, etc.
import os
data_dir = '/content/drive/MyDrive/Sem 9/DL/skin dataset/Skin_Data/'
num_classes = len(os.listdir(data_dir))

if num_classes == 2:
    class_mode = 'binary'
    loss_function = BinaryCrossentropy()
    activation_function = 'sigmoid'
    output_units = 1
else:
    class_mode = 'categorical'
    loss_function = CategoricalCrossentropy()
    activation_function = 'softmax'
    output_units = num_classes


train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=class_mode,
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=class_mode,
    subset='validation'
)

test_generator = test_datagen.flow_from_directory(
    data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode=class_mode,
    shuffle=False
)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_width, img_height, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(output_units, activation=activation_function) # Output layer for binary or multiclass classification
])

model.compile(optimizer='adam',
              loss=loss_function,
              metrics=['accuracy'])

epochs = 10

history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator
)

loss, accuracy = model.evaluate(test_generator)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
"""
    return code 

def harmonic():
    code = """\
    import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

image = cv2.imread('/home/cslinux/Downloads/image.jpg',cv2.IMREAD_GRAYSCALE)
plt.imshow(image,cmap="gray")
plt.show()


salt_image = image.copy()
height, width = image.shape
num_salt = 500# number of pixels of salt
salt_coords = [np.random.randint(0,height,num_salt) ,
               np.random.randint(0,height,num_salt)]

salt_image[salt_coords[0], salt_coords[1]] = 255

plt.imshow(salt_image,cmap="gray")
plt.show()


#kernal for performin g mean

k=3
padding = k//2
denoised_harmonic_image = np.zeros((height+padding, width+padding))

print(denoised_harmonic_image.shape)

print(salt_image,type(salt_image))
for r in range(1,height):
    for c in range(1,width):
        window = salt_image[r:r+k,c:c+k]
        #print(window, type(window))
        nonzero = window[window>0]
        #print(nonzero)
        e=10**-6
        sumofrecp = np.sum(1.0/(nonzero+e))
        harmonic_mean = (k*k)/(sumofrecp)
        #print(harmonic_mean)
        denoised_harmonic_image[r, c] = harmonic_mean

np.clip(denoised_harmonic_image,0,255)

plt.imshow(denoised_harmonic_image,cmap="gray")
plt.show()

# equalized_img = cv2.equalizeHist(denoised_harmonic_image)
# plt.imshow(equalized_img,cmap="gray")
# plt.show()    """
    return code