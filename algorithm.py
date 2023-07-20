# import numpy as np
# import scipy.fftpack as fftpack
# import matplotlib.pyplot as plt

# # Parameters for the EIT simulation
# num_pixels = 100  # Number of pixels in the image
# num_measurements = 180  # Number of measurements/projections

# # Generate an example object (conductivity distribution)
# object_image = np.zeros((num_pixels, num_pixels))
# object_image[40:60, 40:60] = 1.0  # A square-shaped object with higher conductivity

# # Generate projection angles
# theta = np.linspace(0, 180, num_measurements, endpoint=False)

# # Perform EIT simulation
# sinogram = np.zeros((num_measurements, num_pixels))
# for i, angle in enumerate(theta):
#     projection = object_image.sum(axis=0)  # Simplified projection, sum along rows
#     sinogram[i] = np.roll(projection, -int(np.floor(angle * num_pixels / 180)))

# # Perform the inverse Radon transform (backprojection)
# reconstructed_image = np.zeros_like(object_image)
# for i, angle in enumerate(theta):
#     projection = sinogram[i]
#     rotated_projection = np.roll(projection, int(np.floor(angle * num_pixels / 180)))
#     reconstructed_image += rotated_projection.reshape(-1, 1)

# # Display the results
# plt.figure(figsize=(10, 8))

# plt.subplot(221)
# plt.imshow(object_image, cmap='inferno', extent=[0, num_pixels, 0, num_pixels])
# plt.title('True Object')
# plt.colorbar()

# plt.subplot(222)
# plt.imshow(sinogram, cmap='inferno', aspect='auto', extent=[0, num_pixels, 0, 180])
# plt.title('Sinogram')
# plt.xlabel('Pixel Position')
# plt.ylabel('Projection Angle (degrees)')
# plt.colorbar()

# plt.subplot(223)
# plt.imshow(reconstructed_image, cmap='inferno', extent=[0, num_pixels, 0, num_pixels])
# plt.title('Reconstructed Image')

# plt.colorbar()

# plt.show()



# import numpy as np
# import scipy.fftpack as fftpack
# import scipy.ndimage as ndimage
# import matplotlib.pyplot as plt

# # Parameters for the EIT simulation
# num_pixels = 100  # Number of pixels in the image
# num_measurements = 180  # Number of measurements/projections

# # Generate an example object (conductivity distribution)
# object_image = np.zeros((num_pixels, num_pixels))
# object_image[40:60, 40:60] = 1.0  # A square-shaped object with higher conductivity

# # Generate projection angles
# theta = np.linspace(0, 180, num_measurements, endpoint=False)

# # Compute the Fourier series of the object image
# object_fourier_coeffs = fftpack.fft2(object_image)

# # Compute the Radon transform of the Fourier coefficients
# sinogram = np.zeros((num_measurements, num_pixels))
# for i, angle in enumerate(theta):
#     rotated_coeffs = ndimage.rotate(object_fourier_coeffs, angle, reshape=False)
#     sinogram[i] = np.sum(rotated_coeffs.real, axis=0)

# # Perform the inverse Radon transform (backprojection) on the sinogram
# reconstructed_image = np.zeros_like(object_image)
# for i, angle in enumerate(theta):
#     rotated_projection = np.roll(sinogram[i], int(np.floor(angle * num_pixels / 180)))
#     rotated_coeffs = np.outer(rotated_projection, np.ones(num_pixels))
#     rotated_image = fftpack.ifft2(rotated_coeffs)
#     reconstructed_image += rotated_image.real

# # Display the results
# plt.figure(figsize=(10, 8))

# plt.subplot(221)
# plt.imshow(object_image, cmap='inferno', extent=[0, num_pixels, 0, num_pixels])
# plt.title('True Object')
# plt.colorbar()

# plt.subplot(222)
# plt.imshow(sinogram, cmap='inferno', aspect='auto', extent=[0, num_pixels, 0, 180])
# plt.title('Sinogram')
# plt.xlabel('Pixel Position')
# plt.ylabel('Projection Angle (degrees)')
# plt.colorbar()

# plt.subplot(223)
# plt.imshow(reconstructed_image, cmap='inferno', extent=[0, num_pixels, 0, num_pixels])
# plt.title('Reconstructed Image')
# plt.colorbar()

# plt.show()

