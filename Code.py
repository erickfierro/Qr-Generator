# Import library
import qrcode

'''
Version is an integer between 1 and 40, version 1 is a 21x21 matrix
ERROR_CORRECT_L Approximately 7% or less errors can be corrected
ERROR_CORRECT_M (default) Approximately 15% or less errors can be corrected
ERROR_CORRECT_Q Approximately 25% or less errors can be corrected
ERROR_CORRECT_H Approximately 30% or less errors can be corrected
'''
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add String to pass to qr code
qr.add_data('https://github.com/erickfierro')

qr.make(fit=True)

# Add the background color and primary color
img = qr.make_image(fill_color='black', back_color='white')

# Save image in actual folder
img.save('Qr.png')
